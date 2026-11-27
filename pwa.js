/* EndoNasal 3DSim — instalar la app en el escritorio (o en la pantalla de inicio).
   Chrome / Edge / navegador del Quest: botón que abre el diálogo de instalación.
   Safari (Mac): Archivo → Agregar al Dock. iPhone / iPad: Compartir → Agregar a inicio. */
(() => {
  if ('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js').catch(() => {});
  const standalone = matchMedia('(display-mode: standalone)').matches || navigator.standalone;
  if (standalone) return;
  let deferred = null;
  const ua = navigator.userAgent, iOS = /iPhone|iPad|iPod/.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  const safari = /Safari/.test(ua) && !/Chrome|Chromium|CriOS|Edg|OPR|Firefox|FxiOS/.test(ua);
  const btn = document.createElement('button');
  btn.textContent = '⬇ Instalar en el escritorio'; btn.title = 'Instalar EndoNasal 3DSim como app con su ícono';
  btn.style.cssText = 'position:fixed;right:12px;bottom:50px;z-index:50;padding:7px 12px;border-radius:16px;border:1px solid #2f5b4f;background:#0f1a17;color:#9fd8c6;font-size:12.5px;cursor:pointer;display:none';
  const help = msg => {
    const o = document.createElement('div');
    o.style.cssText = 'position:fixed;inset:0;z-index:10000;background:rgba(6,10,14,.85);display:flex;align-items:center;justify-content:center;font-family:system-ui,sans-serif';
    o.innerHTML = `<div style="max-width:380px;margin:16px;background:#111a20;border:1px solid #2f5b4f;border-radius:14px;padding:18px 20px;color:#e8eef3;font-size:14px;line-height:1.5">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px"><img src="icons/icon-192.png" width="40" height="40" style="border-radius:9px"><b style="font-size:16px">Instalar EndoNasal 3DSim</b></div>
      ${msg}<div style="text-align:right;margin-top:14px"><button style="padding:7px 16px;border-radius:10px;border:0;background:#4fd1a5;color:#08130f;font-weight:600;cursor:pointer">Entendido</button></div></div>`;
    o.querySelector('button').onclick = () => o.remove(); o.onclick = e => { if (e.target === o) o.remove(); };
    document.body.appendChild(o);
  };
  btn.onclick = async () => {
    if (deferred) { deferred.prompt(); const r = await deferred.userChoice; deferred = null; if (r.outcome === 'accepted') btn.remove(); return; }
    if (iOS) help('Tocá el botón <b>Compartir</b> (el cuadrado con la flecha) y elegí <b>“Agregar a inicio”</b>. El ícono queda en la pantalla y la app abre a pantalla completa.');
    else if (safari) help('En la barra de menú de Safari elegí <b>Archivo → Agregar al Dock…</b> y confirmá. El ícono queda en el Dock y en Aplicaciones, y la app abre en su propia ventana.');
    else help('Este navegador no permite instalar apps. Abrí esta página en <b>Google Chrome</b> o <b>Microsoft Edge</b> y tocá de nuevo este botón (o el ícono de instalar ⊕ en la barra de direcciones).');
  };
  addEventListener('beforeinstallprompt', e => { e.preventDefault(); deferred = e; btn.style.display = 'block'; });
  addEventListener('appinstalled', () => btn.remove());
  const add = () => { document.body.appendChild(btn); if (iOS || safari || /Firefox/.test(ua)) btn.style.display = 'block'; };
  document.body ? add() : addEventListener('DOMContentLoaded', add);
})();
