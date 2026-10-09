# Launch checklist

## Launch blockers
- [x] `site.siteUrl` set to https://sreenirgithub.github.io/localrepo (GitHub Pages address); preview tags generated.
- [x] Phone number +91 8197152412 confirmed by owner.
- [x] YouTube error 153: fixed. When the page is opened as a local file, the video opens on YouTube; owner confirmed. On-page playback still to be confirmed once hosted over https.
- [ ] Front-room photos (middle and back photos and videos are added; front has only the YouTube video).
- [x] Review dates removed from all reviews (owner decision).
- [ ] Hosting: GitHub Pages chosen. Enable it in repo Settings → Pages (deploy from `main`, root folder), then run the post-launch checks below.

## Missing information (omitted from the site)
- Electricity rate per unit (owner chose to leave out)

## Tests actually run
- Page generated; no placeholder text such as "[Enter ...]" present.
- Gallery: 10 photos and 2 videos load with no 404s or broken images; no horizontal scroll at 390 px and 1280 px.
- In-page anchors resolve; no horizontal scroll at 390 px and 1280 px; no JavaScript errors.
- WhatsApp, call and directions links are generated with the expected URLs.

## Manually verified by owner (desktop and phone)
- WhatsApp, Call owner and Get directions buttons; middle and back room videos; sideways photo strips; layout and readability.

## Still needs manual checking
- Screen-reader and contrast review; keyboard tab order (focus styles are in place).
- WhatsApp link preview (needs the deployed URL).

## Post-launch checks (after Pages is enabled)
- Site loads at https://sreenirgithub.github.io/localrepo/ over https; all photos and videos load.
- Front-room YouTube video plays inside the page.
- WhatsApp link preview shows the picture (paste the link into a WhatsApp chat; previews are cached).
