// Builds contact buttons at load and enables click-to-play YouTube videos.
(function () {
  var c = window.__C;
  var num = c.cc + c.p;
  var links = [
    ["btn btn-wa", "https://wa.me/" + num + "?text=" + encodeURIComponent(c.m), "Contact on WhatsApp"],
    ["btn btn-call", "tel:+" + num, "Call owner"],
    ["btn btn-ghost", c.g, "Get directions"],
  ];
  document.querySelectorAll("[data-contact]").forEach(function (box) {
    links.forEach(function (l) {
      var a = document.createElement("a");
      a.className = l[0];
      a.href = l[1];
      a.textContent = l[2];
      if (l[1].indexOf("http") === 0) { a.target = "_blank"; a.rel = "noopener"; }
      box.appendChild(a);
    });
  });
  document.querySelectorAll("[data-yt]").forEach(function (b) {
    b.addEventListener("click", function () {
      // YouTube refuses embeds with no web origin (error 153), e.g. a page opened from a local file.
      if (location.protocol === "file:") {
        window.open("https://www.youtube.com/watch?v=" + b.dataset.yt, "_blank", "noopener");
        return;
      }
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + b.dataset.yt + "?autoplay=1";
      f.title = "Room video";
      f.allow = "autoplay; encrypted-media; fullscreen";
      f.allowFullscreen = true;
      f.referrerPolicy = "strict-origin-when-cross-origin";
      f.className = "video";
      b.replaceWith(f);
    });
  });
})();
