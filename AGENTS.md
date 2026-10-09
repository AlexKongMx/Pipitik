# PIPITIK — Project operating rules

## Deployments

- DO NOT PUSH TO MAIN. Alex's instruction of October 8, 2026 supersedes earlier deployment authorization.
- Work on a preview branch and publish a Netlify Deploy Preview through a draft pull request. Share the preview URL for review.
- Do not push, merge, or deploy to production until Alex explicitly says this version is ready for push to main. A request to edit the site is not that approval.
- Keep `main` unchanged throughout review.

## Project management

- Board: https://trello.com/b/m2b9JcBy (ID `6ac813bc9a4c0457a1ed923f`).
- All Trello reads and writes go through n8n. Do not invoke the native Trello connector in ChatGPT/Work: Alex wants compact text results without card widgets.
- Writes: n8n workflow `381LOBZppJtL4dFQ`, Grok Trello Bridge. Read its current definition/input schema before execution. Actions include `create_card`, `update_card`, `move_card`, `create_list`.
- Scoped reads: n8n workflow `7VMkfPbSekWYjcSs`, Alex OS — Trello Compact Context. Execute through authenticated MCP in manual mode and retrieve only the `Compact Context` node. Leave this read workflow unpublished.
- The board's first list contains the operating rules. Keep the preview review card current with its URL and open decisions.
- The one-time board creation workflow `siilI4LWBbrLRNEF` has its creation node disabled after success; do not run it again.

## Current creative decisions

- Homepage cover: Alex now wants text over the photograph, aligned right on desktop and mobile. Preserve the full portrait framing and keep faces clear. Removing the screen-right team member is pending: both requested image edits were rejected. Keep the original photo until a usable retouch is provided; do not evade the rejected request through Fal.ai or another model.
- Hulk project: keep the real shopping-mall installation photo.
- First Light Cycle appearance: wide promotional stand photo. Second appearance: preserve the close photo.
- Featured projects: Hulk, Mufasa, Pinocho, The Last of Us, Robin, Tron. Exactly six, no duplicate projects.
- AI hero direction: believable promotional installations in cinemas, shopping malls, and conventions. Preserve the actual sculpture design. These are proposals; do not describe invented venues as confirmed installation history.
- Alien: wait for Alex's location confirmation from Lalo before changing its hero.
- Team portraits are approved; preserve them.
- Robin AI generation was blocked; retain the real Bellas Artes photograph. Do not retry or evade the rejected image request.
