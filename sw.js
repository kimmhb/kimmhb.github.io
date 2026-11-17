/* =========================================================
   김현보 수학 — 서비스 워커 (앱 설치 + 폰 알림)
   index.html 과 같은 폴더(저장소 맨 위)에 두세요. 고칠 필요 없습니다.
   ========================================================= */
importScripts(
  'https://www.gstatic.com/firebasejs/10.12.2/firebase-app-compat.js',
  'https://www.gstatic.com/firebasejs/10.12.2/firebase-messaging-compat.js'
);

// index.html 의 FIREBASE_CONFIG 와 같은 값
firebase.initializeApp({
  apiKey: 'AIzaSyAf7Oez1X8lja7uTIsGs_PRda4aMjWYcqA',
  authDomain: 'kimmhb.firebaseapp.com',
  projectId: 'kimmhb',
  storageBucket: 'kimmhb.firebasestorage.app',
  messagingSenderId: '760747546538',
  appId: '1:760747546538:web:266db9e9daab37a8467dd3',
});
// 앱이 닫혀 있을 때 온 알림은 Firebase가 알아서 띄우고, 누르면 해당 글로 이동합니다.
firebase.messaging();

const CACHE = 'kimmath-v4';

self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (e) => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k !== CACHE) await caches.delete(k);
    await self.clients.claim();
  })());
});

// 화면(index.html)은 항상 최신 것을 먼저 받고, 인터넷이 끊겼을 때만 저장해 둔 것을 보여 줍니다.
self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET' || req.mode !== 'navigate' || new URL(req.url).origin !== location.origin) return;
  e.respondWith((async () => {
    try {
      const res = await fetch(req);
      // 정상으로 받은 첫 화면만 저장합니다 (오류 화면을 저장해 두지 않도록).
      const path = new URL(req.url).pathname, root = new URL('./', location.href).pathname;
      if (res.ok && (path === root || path === root + 'index.html')) {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put('./', copy));
      }
      return res;
    } catch {
      return (await caches.match('./')) || Response.error();
    }
  })());
});
