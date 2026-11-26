-- Simulador CENS · registro (tablas y funciones con prefijo cens_, conviven con otros proyectos en la misma base)
-- Simulador CENS · registro de usuarios, sesiones, encuesta e informe semanal
-- Pegar completo en Supabase → SQL Editor → Run. Después cambiar la clave de administrador (última línea).
create extension if not exists pgcrypto with schema extensions;

create table if not exists cens_usuarios (
  id uuid primary key default gen_random_uuid(),
  email text unique not null,
  pais text not null,
  provincia text not null,
  pin_hash text not null,               -- bcrypt del hash que manda el navegador (nunca la clave en claro)
  creado timestamptz not null default now()
);
create table if not exists cens_sesiones (
  id bigserial primary key,
  usuario uuid not null references cens_usuarios(id) on delete cascade,
  inicio timestamptz not null default now(),
  fantoma text,
  vr boolean default false
);
create table if not exists cens_encuestas (
  id bigserial primary key,
  usuario uuid references cens_usuarios(id) on delete set null,
  calificacion int check (calificacion between 1 and 5),
  mejoraria text,
  necesita text,
  creado timestamptz not null default now()
);
create table if not exists cens_intentos (email text primary key, fallos int not null default 0, bloqueo timestamptz);
create table if not exists cens_ajustes (clave text primary key, valor text not null);

-- Nadie lee las tablas directamente: sólo por las funciones de abajo
alter table cens_usuarios enable row level security;
alter table cens_sesiones enable row level security;
alter table cens_encuestas enable row level security;
alter table cens_intentos enable row level security;
alter table cens_ajustes enable row level security;

create or replace function cens_registrar(p_email text, p_pais text, p_provincia text, p_pin text)
returns uuid language plpgsql security definer set search_path = public, extensions as $$
declare uid uuid;
begin
  if p_email !~* '^[^@\s]+@[^@\s]+\.[^@\s]+$' then raise exception 'Mail inválido'; end if;
  if exists (select 1 from cens_usuarios where email = lower(trim(p_email))) then raise exception 'Ese mail ya está registrado: ingresá con tu clave'; end if;
  insert into cens_usuarios(email, pais, provincia, pin_hash)
  values (lower(trim(p_email)), left(p_pais, 60), left(p_provincia, 80), crypt(p_pin, gen_salt('bf')))
  returning id into uid;
  return uid;
end $$;

create or replace function cens_ingresar(p_email text, p_pin text)
returns uuid language plpgsql security definer set search_path = public, extensions as $$
declare u cens_usuarios; i cens_intentos; e text := lower(trim(p_email));
begin
  select * into i from cens_intentos where email = e;
  if i.bloqueo is not null and i.bloqueo > now() then raise exception 'Demasiados intentos: probá de nuevo en 15 minutos'; end if;
  select * into u from cens_usuarios where email = e;
  if u.id is null or u.pin_hash <> crypt(p_pin, u.pin_hash) then
    insert into cens_intentos(email, fallos) values (e, 1)
      on conflict (email) do update set fallos = cens_intentos.fallos + 1,
        bloqueo = case when cens_intentos.fallos + 1 >= 5 then now() + interval '15 minutes' else null end;
    return null;
  end if;
  delete from cens_intentos where email = e;
  return u.id;
end $$;

create or replace function cens_registrar_sesion(p_usuario uuid, p_fantoma text, p_vr boolean)
returns void language sql security definer set search_path = public, extensions as $$
  insert into cens_sesiones(usuario, fantoma, vr) select p_usuario, left(p_fantoma, 30), p_vr where exists (select 1 from cens_usuarios where id = p_usuario);
$$;

create or replace function cens_enviar_encuesta(p_usuario uuid, p_calificacion int, p_mejoraria text, p_necesita text)
returns void language sql security definer set search_path = public, extensions as $$
  insert into cens_encuestas(usuario, calificacion, mejoraria, necesita) values (p_usuario, p_calificacion, left(p_mejoraria, 2000), left(p_necesita, 2000));
$$;

-- Informe: nuevos registrados, de dónde son, cuántas veces usaron, encuestas (sólo con la clave de administrador)
create or replace function cens_informe(p_clave text, p_dias int default 7)
returns json language plpgsql security definer set search_path = public, extensions as $$
declare r json; desde timestamptz := now() - make_interval(days => p_dias);
begin
  if not exists (select 1 from cens_ajustes where clave = 'admin' and valor = p_clave) then raise exception 'Clave de administrador incorrecta'; end if;
  select json_build_object(
    'periodo_dias', p_dias,
    'nuevos', (select count(*) from cens_usuarios where creado >= desde),
    'nuevos_por_lugar', (select coalesce(json_agg(x order by x.n desc), '[]') from (select pais, provincia, count(*) n from cens_usuarios where creado >= desde group by 1, 2) x),
    'usuarios_totales', (select count(*) from cens_usuarios),
    'sesiones', (select count(*) from cens_sesiones where inicio >= desde),
    'usuarios_activos', (select count(distinct usuario) from cens_sesiones where inicio >= desde),
    'sesiones_por_lugar', (select coalesce(json_agg(x order by x.n desc), '[]') from (select u.pais, u.provincia, count(*) n from cens_sesiones s join cens_usuarios u on u.id = s.usuario where s.inicio >= desde group by 1, 2) x),
    'sesiones_por_fantoma', (select coalesce(json_agg(x order by x.n desc), '[]') from (select coalesce(fantoma, '?') fantoma, count(*) n, sum(case when vr then 1 else 0 end) en_vr from cens_sesiones where inicio >= desde group by 1) x),
    'encuestas', (select coalesce(json_agg(x order by x.creado desc), '[]') from (select calificacion, mejoraria, necesita, creado from cens_encuestas where creado >= desde) x),
    'calificacion_promedio', (select round(avg(calificacion)::numeric, 2) from cens_encuestas where creado >= desde)
  ) into r;
  return r;
end $$;

revoke all on function cens_registrar, cens_ingresar, cens_registrar_sesion, cens_enviar_encuesta, cens_informe from public, authenticated;
grant execute on function cens_registrar, cens_ingresar, cens_registrar_sesion, cens_enviar_encuesta, cens_informe to anon;

-- CAMBIAR esta clave por una propia (es la que pide el informe semanal)
insert into cens_ajustes(clave, valor) values ('admin', 'CAMBIAR-ESTA-CLAVE') on conflict (clave) do update set valor = excluded.valor;
