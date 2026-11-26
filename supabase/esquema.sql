-- Simulador CENS · registro de usuarios, sesiones, encuesta e informe semanal
-- Pegar completo en Supabase → SQL Editor → Run. Después cambiar la clave de administrador (última línea).
create extension if not exists pgcrypto;

create table if not exists usuarios (
  id uuid primary key default gen_random_uuid(),
  email text unique not null,
  pais text not null,
  provincia text not null,
  pin_hash text not null,               -- bcrypt del hash que manda el navegador (nunca la clave en claro)
  creado timestamptz not null default now()
);
create table if not exists sesiones (
  id bigserial primary key,
  usuario uuid not null references usuarios(id) on delete cascade,
  inicio timestamptz not null default now(),
  fantoma text,
  vr boolean default false
);
create table if not exists encuestas (
  id bigserial primary key,
  usuario uuid references usuarios(id) on delete set null,
  calificacion int check (calificacion between 1 and 5),
  mejoraria text,
  necesita text,
  creado timestamptz not null default now()
);
create table if not exists intentos (email text primary key, fallos int not null default 0, bloqueo timestamptz);
create table if not exists ajustes (clave text primary key, valor text not null);

-- Nadie lee las tablas directamente: sólo por las funciones de abajo
alter table usuarios enable row level security;
alter table sesiones enable row level security;
alter table encuestas enable row level security;
alter table intentos enable row level security;
alter table ajustes enable row level security;

create or replace function registrar(p_email text, p_pais text, p_provincia text, p_pin text)
returns uuid language plpgsql security definer set search_path = public as $$
declare uid uuid;
begin
  if p_email !~* '^[^@\s]+@[^@\s]+\.[^@\s]+$' then raise exception 'Mail inválido'; end if;
  if exists (select 1 from usuarios where email = lower(trim(p_email))) then raise exception 'Ese mail ya está registrado: ingresá con tu clave'; end if;
  insert into usuarios(email, pais, provincia, pin_hash)
  values (lower(trim(p_email)), left(p_pais, 60), left(p_provincia, 80), crypt(p_pin, gen_salt('bf')))
  returning id into uid;
  return uid;
end $$;

create or replace function ingresar(p_email text, p_pin text)
returns uuid language plpgsql security definer set search_path = public as $$
declare u usuarios; i intentos; e text := lower(trim(p_email));
begin
  select * into i from intentos where email = e;
  if i.bloqueo is not null and i.bloqueo > now() then raise exception 'Demasiados intentos: probá de nuevo en 15 minutos'; end if;
  select * into u from usuarios where email = e;
  if u.id is null or u.pin_hash <> crypt(p_pin, u.pin_hash) then
    insert into intentos(email, fallos) values (e, 1)
      on conflict (email) do update set fallos = intentos.fallos + 1,
        bloqueo = case when intentos.fallos + 1 >= 5 then now() + interval '15 minutes' else null end;
    return null;
  end if;
  delete from intentos where email = e;
  return u.id;
end $$;

create or replace function registrar_sesion(p_usuario uuid, p_fantoma text, p_vr boolean)
returns void language sql security definer set search_path = public as $$
  insert into sesiones(usuario, fantoma, vr) select p_usuario, left(p_fantoma, 30), p_vr where exists (select 1 from usuarios where id = p_usuario);
$$;

create or replace function enviar_encuesta(p_usuario uuid, p_calificacion int, p_mejoraria text, p_necesita text)
returns void language sql security definer set search_path = public as $$
  insert into encuestas(usuario, calificacion, mejoraria, necesita) values (p_usuario, p_calificacion, left(p_mejoraria, 2000), left(p_necesita, 2000));
$$;

-- Informe: nuevos registrados, de dónde son, cuántas veces usaron, encuestas (sólo con la clave de administrador)
create or replace function informe(p_clave text, p_dias int default 7)
returns json language plpgsql security definer set search_path = public as $$
declare r json; desde timestamptz := now() - make_interval(days => p_dias);
begin
  if not exists (select 1 from ajustes where clave = 'admin' and valor = p_clave) then raise exception 'Clave de administrador incorrecta'; end if;
  select json_build_object(
    'periodo_dias', p_dias,
    'nuevos', (select count(*) from usuarios where creado >= desde),
    'nuevos_por_lugar', (select coalesce(json_agg(x order by x.n desc), '[]') from (select pais, provincia, count(*) n from usuarios where creado >= desde group by 1, 2) x),
    'usuarios_totales', (select count(*) from usuarios),
    'sesiones', (select count(*) from sesiones where inicio >= desde),
    'usuarios_activos', (select count(distinct usuario) from sesiones where inicio >= desde),
    'sesiones_por_lugar', (select coalesce(json_agg(x order by x.n desc), '[]') from (select u.pais, u.provincia, count(*) n from sesiones s join usuarios u on u.id = s.usuario where s.inicio >= desde group by 1, 2) x),
    'sesiones_por_fantoma', (select coalesce(json_agg(x order by x.n desc), '[]') from (select coalesce(fantoma, '?') fantoma, count(*) n, sum(case when vr then 1 else 0 end) en_vr from sesiones where inicio >= desde group by 1) x),
    'encuestas', (select coalesce(json_agg(x order by x.creado desc), '[]') from (select calificacion, mejoraria, necesita, creado from encuestas where creado >= desde) x),
    'calificacion_promedio', (select round(avg(calificacion)::numeric, 2) from encuestas where creado >= desde)
  ) into r;
  return r;
end $$;

revoke all on function registrar, ingresar, registrar_sesion, enviar_encuesta, informe from public;
grant execute on function registrar, ingresar, registrar_sesion, enviar_encuesta, informe to anon;

-- CAMBIAR esta clave por una propia (es la que pide el informe semanal)
insert into ajustes(clave, valor) values ('admin', 'CAMBIAR-ESTA-CLAVE') on conflict (clave) do update set valor = excluded.valor;
