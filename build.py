#!/usr/bin/env python3
"""Generate index.html from content/content.json. Usage: python3 build.py"""
import json, html, pathlib

root = pathlib.Path(__file__).parent
c = json.loads((root / "content" / "content.json").read_text(encoding="utf-8"))
e = html.escape


def kv(items):
    return "".join(f"<div><dt>{e(i['label'])}</dt><dd>{e(i['text'])}</dd></div>" for i in items)


def group(g):
    out = [f'<article class="card"><h3>{e(g["title"])}</h3>']
    if g.get("note"):
        out.append(f'<p class="muted">{e(g["note"])}</p>')
    photos = g.get("photos", [])
    if photos:
        out.append('<div class="photos">')
        for p in photos:
            out.append(f'<img src="assets/photos/{e(p["file"])}" alt="{e(p["alt"])}" loading="lazy" width="{p["width"]}" height="{p["height"]}">')
        out.append("</div>")
    if g.get("videoFile"):
        v = g["videoFile"]
        out.append(f'<video class="video" controls preload="none" playsinline poster="assets/photos/{e(v["poster"])}" src="assets/photos/{e(v["src"])}"></video>')
    if g.get("youtubeId"):
        out.append(f'<button class="btn btn-ghost yt" data-yt="{e(g["youtubeId"])}" type="button">▶ Play video</button>'
                   f'<p class="small"><a href="{e(g["videoUrl"])}" target="_blank" rel="noopener">Open on YouTube</a></p>')
    elif g.get("videoUrl"):
        out.append(f'<a class="btn btn-ghost" href="{e(g["videoUrl"])}" target="_blank" rel="noopener">▶ Watch video</a>')
    out.append("</article>")
    return "".join(out)


rv = json.loads((root / "content" / "reviews.json").read_text(encoding="utf-8"))
def review(r):
    stars = "★" * r["stars"]
    body = "".join(f"<p>{e(x)}</p>" for x in r["text"].split("\n"))
    reply = ""
    if r.get("reply"):
        reply = f'<div class="reply"><strong>Reply from the owner</strong> <span class="muted">· {e(r["reply"]["date"])}</span><p>{e(r["reply"]["text"])}</p></div>'
    return (f'<article class="card review"><header><span class="avatar" aria-hidden="true">{e(r["name"][0].upper())}</span>'
            f'<div><strong>{e(r["name"])}</strong><div class="muted">{e(r["meta"])}</div></div></header>'
            f'<p class="stars"><span aria-label="{r["stars"]} out of 5 stars">{stars}</span> <span class="muted">{e(r["date"])}</span></p>{body}{reply}</article>')
reviews_html = ""
if rv["reviews"]:
    reviews_html = f'<h3>What tenants say</h3><p class="muted">Reviews from {e(rv["source"])}</p><div class="grid">' + "".join(review(r) for r in rv["reviews"]) + "</div>"

faq = "".join(f"<details><summary>{e(f['q'])}</summary><p>{e(f['a'])}</p></details>" for f in c["faq"])
s = c["site"]
ct = c["contact"]

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(s['name'])} – Single rooms for rent</title>
<meta name="description" content="{e(s['description'])}">
<meta property="og:title" content="{e(s['name'])}">
<meta property="og:description" content="{e(s['description'])}">
<meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <a class="brand" href="#top">{e(s['name'])}</a>
  <nav aria-label="Main"><ul>
    <li><a href="#rooms">Rooms</a></li><li><a href="#rent">Rent</a></li><li><a href="#terms">Terms</a></li><li><a href="#faq">FAQ</a></li><li><a href="#contact">Contact</a></li>
  </ul></nav>
</header>
<div class="hero-wrap"><section class="hero" id="top">
  <h1>{e(s['name'])}</h1>
  <p class="lead">{e(s['tagline'])}</p>
  <ul class="chips">{''.join(f'<li>{e(h)}</li>' for h in c['overview']['highlights'])}</ul>
  <div class="actions" data-contact></div>
</section></div>
<main id="main">
<section id="overview"><h2>{e(c['overview']['heading'])}</h2>{''.join(f'<p>{e(p)}</p>' for p in c['overview']['paragraphs'])}</section>

<section id="rooms"><h2>{e(c['rooms']['heading'])}</h2><p>{e(c['rooms']['intro'])}</p>
<div class="grid">{''.join(group(g) for g in c['rooms']['groups'])}</div></section>

<section id="rent"><h2>{e(c['rent']['heading'])}</h2>
<p class="big">{e(c['rent']['headline'])}</p><p>{e(c['rent']['sub'])}</p><dl class="kv">{kv(c['rent']['items'])}</dl></section>

<section id="deposit"><h2>{e(c['deposit']['heading'])}</h2>
<p class="big">{e(c['deposit']['headline'])}</p><dl class="kv">{kv(c['deposit']['items'])}</dl></section>

<section id="facilities"><h2>{e(c['facilities']['heading'])}</h2>
<ul class="ticks">{''.join(f'<li>{e(i)}</li>' for i in c['facilities']['items'])}</ul><p>{e(c['facilities']['wifi'])}</p></section>

<section id="shared"><h2>{e(c['shared']['heading'])}</h2><dl class="kv">{kv(c['shared']['items'])}</dl></section>

<section id="terms"><h2>{e(c['terms']['heading'])}</h2><dl class="kv">{kv(c['terms']['items'])}</dl></section>

<section id="cleaning"><h2>{e(c['cleaning']['heading'])}</h2><p>{e(c['cleaning']['text'])}</p>{reviews_html}</section>

<section id="faq"><h2>Frequently asked questions</h2>{faq}</section>

<section id="contact"><h2>{e(c['location']['heading'])}</h2>
<p><strong>Nearest bus stop:</strong> {e(c['location']['busStop'])}</p>
<div class="actions" data-contact></div>
<noscript><p class="notice">Please enable JavaScript to see the contact buttons.</p></noscript>
</section>
</main>
<footer class="foot"><p>© {e(s['name'])}</p></footer>
<script>window.__C={{cc:{json.dumps(ct['countryCode'])},p:{json.dumps(ct['phone'])},m:{json.dumps(ct['whatsappMessage'])},g:{json.dumps(ct['mapsUrl'])}}};</script>
<script src="app.js" defer></script>
</body>
</html>
"""
(root / "index.html").write_text(page, encoding="utf-8")
print("index.html written")
