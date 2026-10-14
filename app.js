// Builds contact buttons at load and enables click-to-play YouTube videos.
(function () {
  // Highlight the menu link for the section currently on screen.
  var navLinks = document.querySelectorAll("nav a[href^='#']");
  var secs = document.querySelectorAll("main section[data-nav]");
  var ticking = false;
  function mark() {
    ticking = false;
    var cur = "";
    secs.forEach(function (s) { if (s.getBoundingClientRect().top <= 120) cur = s.dataset.nav; });
    if (window.innerHeight + window.scrollY >= document.body.scrollHeight - 4) cur = "contact";
    navLinks.forEach(function (a) {
      var on = a.getAttribute("href") === "#" + cur;
      a.classList.toggle("active", on);
      if (on) a.setAttribute("aria-current", "true"); else a.removeAttribute("aria-current");
    });
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(mark); } }, { passive: true });
  mark();

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
      f.src = "https://www.youtube-nocookie.com/embed/" + b.dataset.yt + "?autoplay=1&rel=0&playsinline=1&origin=" + encodeURIComponent(location.origin);
      f.title = "Room video";
      f.allow = "autoplay; encrypted-media; fullscreen";
      f.allowFullscreen = true;
      f.referrerPolicy = "strict-origin-when-cross-origin";
      f.className = "video";
      b.replaceWith(f);
    });
  });
})();
