/* Simulador CENS · acceso (registro único + ingreso con clave de 4 dígitos) y encuesta de calificación.
   Datos en Supabase (ver supabase/esquema.sql). Si SUPA_URL o SUPA_KEY están vacíos, no pide nada.
   La clave nunca viaja en claro: el navegador manda SHA-256(mail + clave) y la base guarda su bcrypt. */
(() => {
  const SUPA_URL = 'https://zktoqxwokmuekmywatad.supabase.co';
  const SUPA_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InprdG9xeHdva211ZWtteXdhdGFkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODc3NzA1NjgsImV4cCI6MjEwMzM0NjU2OH0.lQdhCZPBvWdFA94pWUZ5IkGGKOwlgk6QXthD6yQgEUc';   // clave pública anon (sólo ejecuta las funciones cens_*)
  if (!SUPA_URL || !SUPA_KEY) return;

  const LS_MAIL = 'cens_mail', SS_UID = 'cens_uid', LS_N = 'cens_n', LS_ENC = 'cens_enc';
  const PAISES = ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Ecuador', 'El Salvador', 'España', 'Estados Unidos', 'Guatemala', 'Honduras', 'México', 'Nicaragua', 'Panamá', 'Paraguay', 'Perú', 'Portugal', 'Puerto Rico', 'República Dominicana', 'Uruguay', 'Venezuela', 'Otro'];
  const PROV_AR = ['Buenos Aires', 'CABA', 'Catamarca', 'Chaco', 'Chubut', 'Córdoba', 'Corrientes', 'Entre Ríos', 'Formosa', 'Jujuy', 'La Pampa', 'La Rioja', 'Mendoza', 'Misiones', 'Neuquén', 'Río Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucumán'];

  async function rpc(fn, args) {
    const r = await fetch(`${SUPA_URL}/rest/v1/rpc/${fn}`, { method: 'POST', headers: { apikey: SUPA_KEY, Authorization: `Bearer ${SUPA_KEY}`, 'Content-Type': 'application/json' }, body: JSON.stringify(args) });
    const t = await r.text(); let d = null; try { d = t ? JSON.parse(t) : null; } catch (e) { d = t; }
    if (!r.ok) throw new Error((d && d.message) || 'Error de conexión');
    return d;
  }
  async function pinHash(mail, pin) {
    const b = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(mail.trim().toLowerCase() + ':' + pin + ':cens'));
    return [...new Uint8Array(b)].map(x => x.toString(16).padStart(2, '0')).join('');
  }
  const fantoma = () => (location.pathname.endsWith('basico.html') ? 'basico' : (new URLSearchParams(location.search).get('fantoma') || 'generico'));

  const css = `
  #censAcc{position:fixed;inset:0;z-index:9999;background:rgba(6,10,14,.92);display:flex;align-items:center;justify-content:center;font-family:system-ui,sans-serif;color:#e8eef3}
  #censAcc .box{width:min(420px,92vw);background:#121a22;border:1px solid #2b3946;border-radius:14px;padding:22px 22px 18px;box-shadow:0 10px 40px rgba(0,0,0,.5)}
  #censAcc h2{margin:0 0 4px;font-size:19px} #censAcc p{margin:0 0 14px;font-size:13px;opacity:.8}
  #censAcc label{display:block;font-size:12px;margin:10px 0 4px;opacity:.85}
  #censAcc input,#censAcc select,#censAcc textarea{width:100%;box-sizing:border-box;padding:9px 10px;border-radius:8px;border:1px solid #33475a;background:#0b1117;color:#e8eef3;font-size:15px}
  #censAcc textarea{min-height:64px;font-size:13px}
  #censAcc .pin{letter-spacing:10px;font-size:22px;text-align:center}
  #censAcc button{margin-top:14px;width:100%;padding:10px;border:0;border-radius:8px;background:#3fbf9b;color:#04120d;font-weight:700;font-size:15px;cursor:pointer}
  #censAcc button.sec{background:transparent;color:#9fd8c6;border:1px solid #2f5b4f;margin-top:8px;font-weight:500}
  #censAcc .err{color:#ff9c8f;font-size:12.5px;min-height:16px;margin-top:8px}
  #censAcc .stars{display:flex;gap:6px;justify-content:center;font-size:30px;cursor:pointer;margin:6px 0}
  #censAcc .stars span{opacity:.3} #censAcc .stars span.on{opacity:1}`;
  const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
  const ov = document.createElement('div'); ov.id = 'censAcc';
  const show = html => { ov.innerHTML = `<div class="box">${html}</div>`; if (!ov.isConnected) document.body.appendChild(ov); ov.style.display = 'flex'; };
  const hide = () => { ov.style.display = 'none'; };
  const $ = s => ov.querySelector(s);
  const onlyDigits = el => el.addEventListener('input', () => { el.value = el.value.replace(/\D/g, '').slice(0, 4); });

  function vistaIngreso(msg = '') {
    const mail = localStorage.getItem(LS_MAIL) || '';
    show(`<h2>EndoNasal 3DSim</h2><p>Ingresá con tu mail y tu clave de 4 dígitos.</p>
      <label>Mail</label><input id="aMail" type="email" autocomplete="email" value="${mail.replace(/"/g, '')}">
      <label>Clave (4 dígitos)</label><input id="aPin" class="pin" type="password" inputmode="numeric" autocomplete="current-password" maxlength="4">
      <div class="err" id="aErr">${msg}</div>
      <button id="aGo">Ingresar</button><button class="sec" id="aReg">Es mi primera vez: registrarme</button>`);
    onlyDigits($('#aPin')); (mail ? $('#aPin') : $('#aMail')).focus();
    $('#aPin').addEventListener('keydown', e => { if (e.key === 'Enter') $('#aGo').click(); });
    $('#aReg').onclick = () => vistaRegistro();
    $('#aGo').onclick = async () => {
      const m = $('#aMail').value.trim(), p = $('#aPin').value;
      if (!m || p.length !== 4) { $('#aErr').textContent = 'Completá el mail y los 4 dígitos.'; return; }
      $('#aGo').disabled = true; $('#aErr').textContent = '';
      try {
        const uid = await rpc('cens_ingresar', { p_email: m, p_pin: await pinHash(m, p) });
        if (!uid) { $('#aErr').textContent = 'Mail o clave incorrectos.'; $('#aGo').disabled = false; return; }
        entrar(uid, m);
      } catch (e) { $('#aErr').textContent = e.message; $('#aGo').disabled = false; }
    };
  }
  function vistaRegistro() {
    show(`<h2>Registro (una sola vez)</h2><p>Después entrás siempre con tu mail y tu clave.</p>
      <label>Mail</label><input id="rMail" type="email" autocomplete="email" value="${(localStorage.getItem(LS_MAIL) || '').replace(/"/g, '')}">
      <label>País</label><select id="rPais">${PAISES.map(p => `<option${p === 'Argentina' ? ' selected' : ''}>${p}</option>`).join('')}</select>
      <label>Provincia / estado</label><span id="rProvBox"></span>
      <label>Elegí una clave de 4 dígitos</label><input id="rPin" class="pin" type="password" inputmode="numeric" maxlength="4">
      <label>Repetila</label><input id="rPin2" class="pin" type="password" inputmode="numeric" maxlength="4">
      <div class="err" id="rErr"></div>
      <button id="rGo">Registrarme</button><button class="sec" id="rBack">Ya tengo cuenta</button>`);
    const prov = () => { $('#rProvBox').innerHTML = $('#rPais').value === 'Argentina' ? `<select id="rProv">${PROV_AR.map(p => `<option>${p}</option>`).join('')}</select>` : '<input id="rProv" type="text" maxlength="80">'; };
    prov(); $('#rPais').onchange = prov; onlyDigits($('#rPin')); onlyDigits($('#rPin2'));
    $('#rBack').onclick = () => vistaIngreso();
    $('#rGo').onclick = async () => {
      const m = $('#rMail').value.trim(), pa = $('#rPais').value, pr = $('#rProv').value.trim(), p = $('#rPin').value;
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(m)) { $('#rErr').textContent = 'Revisá el mail.'; return; }
      if (!pr) { $('#rErr').textContent = 'Completá la provincia o estado.'; return; }
      if (p.length !== 4 || p !== $('#rPin2').value) { $('#rErr').textContent = 'La clave tiene que tener 4 dígitos y coincidir.'; return; }
      $('#rGo').disabled = true; $('#rErr').textContent = '';
      try { const uid = await rpc('cens_registrar', { p_email: m, p_pais: pa, p_provincia: pr, p_pin: await pinHash(m, p) }); entrar(uid, m); }
      catch (e) { $('#rErr').textContent = e.message; $('#rGo').disabled = false; }
    };
  }
  function entrar(uid, mail) {
    localStorage.setItem(LS_MAIL, mail.trim().toLowerCase()); sessionStorage.setItem(SS_UID, uid);
    rpc('cens_registrar_sesion', { p_usuario: uid, p_fantoma: fantoma(), p_vr: false }).catch(() => { });
    const n = (+localStorage.getItem(LS_N) || 0) + 1; localStorage.setItem(LS_N, n);
    hide();
    if (n === 3 && !localStorage.getItem(LS_ENC)) setTimeout(() => vistaEncuesta(true), 20 * 60 * 1000);   // pedir opinión en la 3.ª sesión, a los 20 minutos
  }
  function vistaEncuesta(auto) {
    let cal = 0;
    show(`<h2>¿Qué te pareció el simulador?</h2><p>${auto ? 'Nos ayuda mucho para mejorarlo (1 minuto).' : 'Tu opinión nos ayuda a mejorarlo.'}</p>
      <label>Calificación</label><div class="stars" id="eSt">${[1, 2, 3, 4, 5].map(i => `<span data-v="${i}">★</span>`).join('')}</div>
      <label>¿Qué mejorarías?</label><textarea id="eMej" maxlength="2000"></textarea>
      <label>¿Qué necesitás que agreguemos (cirugías, anatomía, instrumentos)?</label><textarea id="eNec" maxlength="2000"></textarea>
      <div class="err" id="eErr"></div><button id="eGo">Enviar</button><button class="sec" id="eNo">Ahora no</button>`);
    ov.querySelectorAll('#eSt span').forEach(s => s.onclick = () => { cal = +s.dataset.v; ov.querySelectorAll('#eSt span').forEach(x => x.classList.toggle('on', +x.dataset.v <= cal)); });
    $('#eNo').onclick = hide;
    $('#eGo').onclick = async () => {
      if (!cal) { $('#eErr').textContent = 'Elegí de 1 a 5 estrellas.'; return; }
      $('#eGo').disabled = true;
      try { await rpc('cens_enviar_encuesta', { p_usuario: sessionStorage.getItem(SS_UID), p_calificacion: cal, p_mejoraria: $('#eMej').value, p_necesita: $('#eNec').value });
        localStorage.setItem(LS_ENC, '1'); show('<h2>¡Gracias!</h2><p>Recibimos tu opinión.</p><button id="eOk">Volver al simulador</button>'); $('#eOk').onclick = hide; }
      catch (e) { $('#eErr').textContent = e.message; $('#eGo').disabled = false; }
    };
  }
  // VR: registra que la sesión pasó a realidad virtual
  window.censAccesoVR = () => { const uid = sessionStorage.getItem(SS_UID); if (uid) rpc('cens_registrar_sesion', { p_usuario: uid, p_fantoma: fantoma(), p_vr: true }).catch(() => { }); };
  window.censEncuesta = () => vistaEncuesta(false);
  const start = () => {
    const btn = document.createElement('button'); btn.textContent = '★ Calificar y sugerir'; btn.title = 'Contanos qué mejorarías';
    btn.style.cssText = 'position:fixed;right:12px;bottom:12px;z-index:50;padding:7px 12px;border-radius:16px;border:1px solid #2f5b4f;background:#0f1a17;color:#9fd8c6;font-size:12.5px;cursor:pointer';
    btn.onclick = () => vistaEncuesta(false); document.body.appendChild(btn);
    if (sessionStorage.getItem(SS_UID)) return;   // misma pestaña ya ingresada (recarga o cambio de fantoma)
    vistaIngreso();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
