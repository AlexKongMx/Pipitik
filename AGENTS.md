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

## Project galleries

- Use the curated selection in galleries.mjs. Aim for 2–3 views of the finished piece and 6–9 process photos where good source material exists. Prefer fewer strong images over duplicates or weak frames.
- Keep compact thumbnails and open the larger image in the gallery viewer, with previous/next arrows and keyboard navigation.
- Keep previous and next project links with thumbnails at the end of every project page.

## Current creative decisions

- Homepage cover: use Alex's supplied panoramic image from October 9, public/assets/studio-cover-alex-wide.jpg (2048×877). Preserve its exact image bytes. Fill the hero edge to edge with no black bars; use object-fit:cover when viewport height requires a shallow crop. Keep the hero beneath the header and above the fold on desktop. Large right-aligned text fills the clear wall below/right of the fist, clear of faces. Only CSS shading for legibility. Do not reuse the rejected montage or run ops/prepare-cover.py. Preview only.
- Hulk project: keep the real shopping-mall installation photo.
- First Light Cycle appearance: wide promotional stand photo. Second appearance: preserve the close photo.
- Featured projects: Hulk, Mufasa, Pinocho, The Last of Us, Robin, Tron. Exactly six, no duplicate projects.
- AI hero direction: believable promotional installations in cinemas, shopping malls, and conventions. Preserve the actual sculpture design. These are proposals; do not describe invented venues as confirmed installation history.
- Alien: wait for Alex's location confirmation from Lalo before changing its hero.
- Team portraits are approved; preserve them.
- Robin and Spider-Man use Alex’s supplied hero images from October 9. Próximus César uses the approved-direction AI recreation based on the actual location references.
- Catalog now includes Checoneta, Diorama de mamut and Rancor. Preserve the six featured projects unless Alex changes that selection.
