# Linga Bhairavi Apartment – rental website

A lightweight static website (plain HTML + CSS, ~30 lines of JavaScript, no frameworks, no trackers).
Share the link on WhatsApp and use it as the Google Ads destination.

## Files
| Path | Purpose |
|---|---|
| `content/content.json` | All property text, rent, terms, FAQ, contact and video links |
| `content/reviews.json` | Customer reviews (text copied from Google reviews) |
| `assets/photos/` | Room photos (add files here) |
| `assets/reviews/` | Original review screenshots (backup, not shown on the site) |
| `build.py` | Generates `index.html` from the content files |
| `style.css`, `app.js` | Layout and the small amount of behaviour |
| `docs/OWNERS_GUIDE.md` | How to update content and media |
| `docs/LAUNCH_CHECKLIST.md` | Missing information, blockers and test results |

## Preview locally
```
python3 build.py
python3 -m http.server 8000
```
Open http://localhost:8000

## Deploy (free HTTPS)
See `docs/OWNERS_GUIDE.md`. Nothing is deployed until you approve.
