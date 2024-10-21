const assets = [
    "/",
    "static/css/style.css",
    "static/js/app.js",
    "static/images/logo.png",
    "static/images/favicon.jpg",
    "static/icons/icon-128x128.png",
    "static/icons/icon-192x192.png",
    "static/icons/icon-384x384.png",
    "static/icons/icon-512x512.png"
  ];

const CATALOGUE_ASSETS = "catalogue-assets";

self.addEventListener("install", (installEvt) => {
  installEvt.waitUntil(
    caches
      .open(CATALOGUE_ASSETS)
      .then((cache) => {
        console.log(cache)
        cache.addAll(assets);
      })
      .then(self.skipWaiting())
      .catch((e) => {
        console.log(e);
      })
  );
});

self.addEventListener("activate", function (evt) {
  evt.waitUntil(
    caches
      .keys()
      .then((keyList) => {
        return Promise.all(
          keyList.map((key) => {
            if (key === CATALOGUE_ASSETS) {
              console.log("Removed old cache from", key);
              return caches.delete(key);
            }
          })
        );
      })
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", function (evt) {
  evt.respondWith(
    fetch(evt.request).catch(() => {
      return caches.open(CATALOGUE_ASSETS).then((cache) => {
        return cache.match(evt.request);
      });
    })
  );
})