// EndoNasal 3DSim: service worker mínimo para que la app se pueda instalar.
// Siempre busca la versión más nueva en internet; sólo si no hay conexión muestra la última guardada.
const CACHE = 'endonasal-v3';
self.addEventListener('install', e => { self.skipWaiting(); });
self.addEventListener('activate', e => { e.waitUntil(self.clients.claim()); });
self.addEventListener('fetch', e => {
  const r = e.request;
  if (r.method !== 'GET' || new URL(r.url).origin !== location.origin) return;
  const page = r.mode === 'navigate' || /\.(html|js|webmanifest)$/.test(new URL(r.url).pathname);
  if (!page) return;
  e.respondWith(fetch(r).then(res => { const c = res.clone(); caches.open(CACHE).then(k => k.put(r, c)); return res; })
    .catch(() => caches.match(r).then(m => m || caches.match('./index.html'))));
});
