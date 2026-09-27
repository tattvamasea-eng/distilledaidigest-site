# D·A·D Newsletter — Standing Production Preferences

> **PRECEDENCE — read this file first, every issue.** These are Ram's current, durable instructions and they **override any conflicting instruction** in the `dad-newsletter` skill's SKILL.md and in the project's inline "Production Process" / CLAUDE.md / "Website HTML Standard" wherever they disagree. Known conflicts to resolve in favor of THIS file: (a) **The Stack has SIX layers, not five**; (b) **skip the Word doc by default**; (c) **the Beehiiv teaser uses the per-section link structure and sign-off defined below** (older docs don't mention it); (d) **push the website live BEFORE publishing Beehiiv** (older docs say website is post-publish); (e) **the bullets section is titled "The Governance Angle," not "Quick Hits"**; (f) **there is a mandatory HTML review gate before anything is committed/pushed** (see below); (g) **production/deploy mechanics** — thumbnail filename has NO hyphen, deploy via `scripts/deploy.sh`, the four section anchors are standard, and the template is the most recent shipped issue (see "Production & deploy mechanics" below). When something here contradicts an older instruction, follow this file and note the conflict; do not blend them.

Durable instructions from Ram. Apply to every issue unless he overrides in the moment.

## Deliverables
- **Skip the Word doc (.docx) by default.** Issues #29 onward do not need it. `make_docx.js` lives only in the skill folder, not on the Mac. Only build it if Ram explicitly asks for a given issue.
- Standard deliverables: full website `issue-NN.html` (written to the repo on the Mac), 1200×630 thumbnail PNG, Beehiiv teaser draft (Ram publishes it himself).
- **Save all text outputs to the Mini autonomously — do not rely on manual saving.** Write every text deliverable (`issue-NN.html`, the updated `index.html` / `archive.html`, and any spec or preferences update) straight into the repo on the Mac via the Filesystem MCP, as part of the task. Never leave them as chat text for Ram to save by hand: manual saving is what let files drift (a newer version once lived only in a chat while the Mac copy stayed stale). Filesystem quirk: reads time out often but writes succeed — use `write_file` with the complete file, not `edit_file` (it corrupts Unicode: em dashes, arrows, middots). **Known exception:** the 1200×630 thumbnail is a binary PNG and the current Filesystem MCP writes text only, so the PNG still needs a manual move into `assets/` until a binary-write path exists — call this out each issue rather than assuming it saved.

## The Stack — SIX layers, not five (from issue #32 on)
Order, top of supply chain to end use:
**Energy → Chips → Cloud → Models → Harness → Applications**
- The **Harness** layer sits **between Models and Applications**: the agent runtime/scaffold that wraps a raw model into an agent — the perceive-plan-act loop, context/memory management, tool-call brokering, orchestration. (Precedent: issue #28 used this 6-card layout; #29 and #31 mistakenly dropped to 5.)
- Suggested emoji to match house style: ⚡ Energy · 💾 Chips · ☁ Cloud · 🧠 Models · 🔧 Harness · 📱 Applications.

## Research (Step 3, before the story-selection pause)
- Gmail scan + web search as always, **plus always consult leading analyst/consulting sources for the top-10 slate**: Gartner, Forrester, HBR, McKinsey, BCG, Bain, Deloitte, IDC, Accenture, PwC and similar. Work at least one such data-backed source naturally into the issue.
- **Always refer to distilledaidigest.com for past issues** — the live site is the reference for the latest published state, section structure, and what has already been covered. Mirror the most recent published issue's HTML and anchor structure.

## Agent 101 (permanent section)
- The concept must not repeat **any** Agent 101 concept used in **all past issues since the section was introduced** — check the full run every time (see `claude/agent101-history.md`), not just the last few issues. Update `agent101-history.md` with the new concept after every issue.

## Section naming
- Keep the CIO section named **"CIO Corner"** — not "CTO Corner" or "CIO/CTO Corner." Its content (procurement, vendor contracts, governance, operating-model, risk) is CIO territory, and the single crisp name has brand continuity across the run. Widen the audience in the subtitle if ever needed, not the section name.
- **The bullets section is titled "The Governance Angle"** — NOT "Quick Hits." This applies to the section heading in the **full website issue** (the `<h2>` in `issue-NN.html`) as well as the teaser label. (From issue #34 on; older issues used "Quick Hits.") Also update any in-issue cross-reference to read "(see The Governance Angle)."

## Perspective lenses — reader views (from issue #36 on)
Additive to the Website HTML Standard's story structure; it does not replace the default text.

- **Default view is "Leader"** — the existing story prose, written for IT and business leaders. This is the canonical text and never changes based on view. If anything below fails, the reader sees this.
- **Each of the 5 stories gets TWO collapsible lens add-ons**, written every issue:
  - **"In simple terms"** (renamed from "Plain English" on issue #36; the URL value stays `?lens=plain`) — 2–3 sentences: what the story means for someone new to AI, no jargon.
  - **"Under the Hood"** — 2–3 sentences: the technical mechanism, for engineers.
  - Lenses apply to the **5 stories only.** Not CIO Corner, not The Stack, not The Governance Angle.
- **The "Perspective" dropdown** sits at the top of `issue-NN.html`. Options: **Leader (default) / In simple terms / Engineer.**
  - Changing it shows/hides the matching add-ons under each story. The default Leader prose stays visible in all three views; the lens add-ons open or close around it.
  - **No-JavaScript fallback:** with the script disabled or broken, the page renders the full Leader view and the lens add-ons stay collapsed (or visible as plain text) — nothing breaks, no 404, no blank story.
  - **Deep-link parameter:** `?lens=plain` and `?lens=engineer` open the page pre-set to that view; no param = Leader. Existing `#story-N` anchors must still work alongside it (e.g. `...issue-36.html?lens=engineer#story-3`).
  - **Remember choice:** persist the reader's selection in browser storage (localStorage) wrapped in try/catch, with a safe fallback to Leader when storage is unavailable (private windows, cleared data).
- **Agent 101 gets NO lens** — it stays the one shared section. Instead it follows a fixed four-paragraph structure so it serves every reader at once:
  1. **Everyday analogy first** — explain the concept with zero AI terms.
  2. **Name and define** — introduce the real term; expand every acronym on first use.
  3. **Why it matters** — the enterprise consequence, in leader language.
  4. **One technical line** — the mechanism for engineers, one to two sentences.
- **"In simple terms" view shows a pointer:** when the reader selects In simple terms, surface a small "New to agents? Start with Agent 101 →" link near the top, anchored to the Agent 101 section.

## Perspective lenses — pilot and kill switch
- **Pilot for issues #36–#38 (3 issues).** Track how often readers change the dropdown (a view-switch event on the site). If no site analytics exist, a lightweight free counter (e.g. GoatCounter) is enough to capture the event.
- **Decision rule:** if fewer than ~10% of readers ever switch views across the pilot, drop the feature and revert to plain Leader-only issues. (The 10% threshold is a working guess, not a benchmark — revisit once real numbers land.)
- The **Beehiiv teaser is unchanged** for the pilot. The `?lens=` param is available for manual/future use but is not required in teaser links yet.

## Two mandatory pauses (do not skip either)
1. **Story-selection pause** — after Gmail + web + analyst research, present 10 candidate stories + 3 title options + a proposed (non-repeated) Agent 101 concept. Ram picks 5 stories and 1 title before writing begins.
2. **HTML review gate** — after the full `issue-NN.html` is written and the thumbnail generated, **PAUSE and present the finished issue to Ram for approval before anything is committed, pushed, or staged for Beehiiv.** Nothing moves toward publish until Ram says "approved." He reviews, requests edits, the issue is revised, and only on his explicit approval does the git push (and then Beehiiv) proceed.
   - **Review format:** in-chat rendered preview — deliver the full `issue-NN.html` as a rendered file card in the conversation (Ram's chosen default). Do not require a local browser preview unless he asks.

## Beehiiv teaser structure (from issue #34 on)
The Beehiiv post is the teaser only; the website HTML is the full issue. In the teaser body, **every section gets its own "read more" link back to the full issue on the site** so each section drives a click-through:
- **After each of the 5 stories:** a `Read the full story →` link. Point it at the story anchor on the site page (`.../issues/issue-NN.html#story-1` … `#story-5`; the story `<article>`s carry `id="story-1"`…`"story-5"`).
- **A teaser line + link for each remaining section** — one or two sentences of tease followed by the link below. Section labels and link text in the teaser:
  - **The Governance section:** label it **"The Governance Angle"** (not "Quick Hits"); link reads **"Read the Angle →"**. Anchor: `#governance`.
  - **CIO Corner:** link reads **"Read the CIO Angle →"**. Anchor: `#cio`.
  - **The Stack:** label it **"The 6-Layer Stack"**; link reads **"Read the Stack Impact →"**. Anchor: `#stack`.
  - **Agent 101:** link reads **"Learn about <this issue's Agent 101 concept> →"** — the concept name changes every week (e.g. issue #34 = "Learn about The Sandbox →"). Do not hard-code "The Sandbox"; use whatever that issue's Agent 101 topic is. Anchor: `#agent101`.
- The four section anchors above are standard in the HTML from issue #35 on (see "Production & deploy mechanics"), so section links deep-link rather than landing on the base URL.
- After the section links, add a final `Read the complete issue →` link.
- **Close the teaser with the standard D·A·D sign-off** (do not let it end abruptly on the CTA): a one-line week-signal wrap sentence, then "See you next week — still watching, still distilling.", then a bold "— The Distilled AI Digest Team". This mirrors the closing of the full website issue.
- Use absolute `https://www.distilledaidigest.com/issues/issue-NN.html` URLs so links work in email.

## Publish order (from issue #34 on)
- Gate on the HTML review pause above FIRST. Then: **push the website live, then publish Beehiiv.** Because every teaser section links to the live site page and its `#story-N` anchors, the site must be deployed before the email goes out — otherwise readers hit 404s. Sequence: (1) Ram approves the HTML; (2) deploy via `scripts/deploy.sh` → Netlify deploy of `issue-NN.html` + updated `index.html`/`archive.html`; (3) verify the page and anchors load; (4) then publish the Beehiiv email. This reverses the older "website update = post-publish" step.

## Production & deploy mechanics (locked from the issue #35 run, 2026-09-20)
These override the `dad-newsletter` SKILL.md wherever they disagree.
- **Thumbnail filename has NO hyphen:** `assets/thumbnail_issueNN.png` (e.g. `thumbnail_issue36.png`). The SKILL.md's hyphenated `thumbnail_issue-NN.png` is wrong — it breaks the deploy precondition and the homepage/archive `<img>` cards. (The PNG is binary; per Deliverables it still needs a manual move into `assets/`.)
- **Thumbnail generator needs a venv (PEP 668 / Homebrew Python):** `pip install pillow` fails with `externally-managed-environment`; `--user` / `--break-system-packages` are not the house method. From the repo root: `python3 -m venv .venv && source .venv/bin/activate && pip install pillow`, run `scripts/make_thumbnail_dad17.py --issue NN … --out assets/thumbnail_issueNN.png`, then `deactivate`. `.venv/` stays git-ignored.
- **Deploy through `scripts/deploy.sh`, not hand-written git:** `cd ~/Documents/GitHub/distilledaidigest-site && ./scripts/deploy.sh NN "Full Title"`. First run on a fresh clone/session needs `chmod +x scripts/deploy.sh` once. deploy.sh runs guardrail checks (fails on a "— Ram" byline, warns on British spelling), preconditions (issue HTML + thumbnail present, index/archive both link the issue), then `git add -A`, commit, push to `main`, and live-poll. The push runs on the Mac; Claude writes the files and hands over the command, never pushes.
- **deploy.sh live-check false-negative (301) — FIX PENDING, apply before #36 deploys:** deploy.sh polls the apex URL with `curl -sI` (no redirect follow); the apex 301-redirects to `www`, so every check prints 301 and it ends on a false "⚠️ Not 200 yet" even when the page is live (seen on #35). Fix: poll `https://www.distilledaidigest.com/issues/issue-NN.html` and follow redirects — `curl -sIL "$URL" | grep -i '^HTTP' | tail -1 | awk '{print $2}'`. Until patched, verify manually with that command — a final `200` means live; the script's 301 warning is cosmetic.
- **Section anchors are standard from #35 on:** in addition to `id="story-1"`…`"story-5"`, the four non-story sections carry `id="governance"`, `id="cio"`, `id="stack"`, `id="agent101"` so the Beehiiv teaser's section links deep-link instead of dead-ending. (Supersedes the older "add anchors if/when they exist" note; #34 had story anchors only.)
- **Beehiiv injection recipe (confirmed #35):** needs a connected Chrome (Claude-in-Chrome extension, Ram signed in, Chrome open) — the built-in browser pane returned HTTP 400 on this surface and is not reliable; if no browser is reachable, hand Ram the teaser HTML to paste. Editor DOM: `textarea[0]` = title, `textarea[1]` = subtitle, one `.ProseMirror` body. Set title/subtitle via the React native setter. Inject the teaser body as base64 decoded in-page (avoids em-dash/arrow/apostrophe corruption): decode to a string, then `.ProseMirror` `focus()` → `execCommand('selectAll')` → `execCommand('insertHTML', false, html)` → dispatch an `input` event (bubbles). Verify: read back both textarea values, count links (should be 10: 5 stories + governance/cio/stack/agent101 + complete-issue), confirm "Synced". Never publish and never upload the thumbnail on Ram's behalf — he uploads the thumbnail, sets the kebab-case slug under Web → Post URL, confirms the Email checkbox, reviews, and publishes, only after the site is live.
- **Repo write path when the Filesystem connector fails (found #36, 2026-09-27):** in cloud sessions linked to the Mini, every `Filesystem` tool call can fail with "invalid outputSchema … draft-07 … supports JSON Schema 2020-12 only". Cause: the Filesystem server (versions from 2025.11.25 on) publishes its output schemas as JSON Schema draft-07, and the remote-devices bridge only accepts 2020-12, so the call is rejected before it runs. Nothing on the Mac is broken. Workaround used: `device_request_folder_access` on the repo folder, then `device_bash` to write and edit files in place. Do not blind-retry Filesystem writes.
- **Title format:** house format is **"The Week …"** (e.g. "The Week Spending Raced Its Own Safety Case"), under ~8 words.
- **CSS/structure template = the most recent shipped issue** (as of now, `issues/issue-35.html`, which carries the four section anchors), keeping the six-card Stack. Roll the template forward each week.

## Sourcing discipline
- Treat AI-agent-supplied leads (e.g. from Bram/Grok) as unverified until checked against a primary source. This session alone caught: a "$31K loss" that was a garbled ¥31,000, a nonexistent "Agent Armor" product, an SB 53 author error, and a mis-framed Marvell "$12.2B spend." Verify every figure, name, date, and attribution before it goes in.

## Publishing
- Never publish the Beehiiv email or push git without Ram's explicit go. Deploy is via `scripts/deploy.sh` (which pushes); Ram runs it (or clicks publish) himself.
