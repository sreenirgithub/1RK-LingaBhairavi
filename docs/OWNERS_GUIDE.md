# Owner's guide

After any change below, run `python3 build.py`, check the site locally, then commit and push. The site updates only when you redeploy; there is no automatic sync from OneDrive or Google Docs.

## Change rent, deposit, rules, FAQ, links
Edit `content/content.json` (plain text between quotes, keep the commas and quotes) and rebuild.
- Rent: `rent.headline` and `rent.sub`
- Deposit and deduction: `deposit`
- Rules: `terms`
- Phone / WhatsApp message / map link: `contact`

## Change reviews
Edit `content/reviews.json`. Copy review text exactly. Add a `reply` block for an owner reply. Relative dates such as "9 weeks ago" go stale; replace them with real dates when you can.

## Add or replace photos
1. Download the photo from OneDrive and save it in `assets/photos/` (JPEG, about 1600 px wide, under 400 KB).
2. In `content/content.json`, add to the matching group's `photos` list:
   `{"file": "front-1.jpg", "alt": "Front room with bed and cupboard", "width": 1600, "height": 1200}`
3. Rebuild. Only label a photo front/middle/back if it truly is.

OneDrive share links are not permanent image links, so photos must be copied into the repo.

## Change videos
Replace `videoUrl` (and `youtubeId` for YouTube) in the group. OneDrive videos open in a new tab; YouTube videos play on click.

## Hosting and safety
- Recommended: GitHub Pages or Cloudflare Pages (both free with HTTPS; verify current limits before launch). A custom domain is an extra cost.
- Protect the GitHub account: unique password, two-factor authentication, no shared logins.
- Protect the `main` branch (require a pull request to change it) so edits are deliberate.
- Backups and rollback: every change is a git commit. To undo, revert the commit and redeploy.

## Phone number privacy (static option)
The number is not written as plain text on the page, and the buttons are created by a small script. This only deters simple scrapers. Anyone loading the page can obtain the number, and no static approach can guarantee it is never collected. A server-side check would be stronger but needs a backend, which you chose not to use.
