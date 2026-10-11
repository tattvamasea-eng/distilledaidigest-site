# D·A·D Newsletter — Standing Production Preferences

> **PRECEDENCE — read this file first, every issue.** These are Ram's current, durable instructions and they **override any conflicting instruction** in the `dad-newsletter` skill's SKILL.md and in the project's inline "Production Process" / CLAUDE.md / "Website HTML Standard" wherever they disagree. Known conflicts to resolve in favor of THIS file: (a) **The Stack has SIX layers, not five**; (b) **skip the Word doc by default**; (c) **the Beehiiv teaser uses the per-section link structure and sign-off defined below** (older docs don't mention it); (d) **push the website live BEFORE publishing Beehiiv** (older docs say website is post-publish); (e) **the bullets section is titled "The Governance Angle," not "Quick Hits"**; (f) **there is a mandatory HTML review gate before anything is committed/pushed** (see below); (g) **production/deploy mechanics** — thumbnail filename has NO hyphen, deploy via `scripts/deploy.sh`, the four section anchors are standard, and the template is the most recent shipped issue (see "Production & deploy mechanics" below); (h) **from #38, Ram's takes and Ram's own CIO Corner are collected at the story-selection pause** (see "Human voice" below). When something here contradicts an older instruction, follow this file and note the conflict; do not blend them.

Durable instructions from Ram. Apply to every issue unless he overrides in the moment.

## Deliverables
- **Skip the Word doc (.docx) by default.** Issues #29 onward do not need it. `make_docx.js` lives only in the skill folder, not on the Mac. Only build it if Ram explicitly asks for a given issue.
- Standard deliverables: full website `issue-NN.html` (written to the repo on the Mac), 1200×630 thumbnail PNG, Beehiiv teaser draft (Ram publishes it himself).
- **Save all text outputs to the Mini autonomously — do not rely on manual saving.** Write every text deliverable (`issue-NN.html`, the updated `index.html` / `archive.html`, and any spec or preferences update) straight into the repo on the Mac via the Filesystem MCP, as part of the task. Never leave them as chat text for Ram to save by hand: manual saving is what let files drift (a newer version once lived only in a chat while the Mac copy stayed stale). Filesystem quirk: reads time out often but writes succeed — use `write_file` with the complete file, not `edit_file` (it corrupts Unicode: em dashes, arrows, middots). **Known exception:** the 1200×630 thumbnail is a binary PNG and the current Filesystem MCP writes text only, so the PNG still needs a manual move into `assets/` until a binary-write path exists — call this out each issue rather than assuming it saved.
- **Write-path order (from #36):** (1) Filesystem MCP. (2) If every Filesystem call fails (see the draft-07 outputSchema note under Production & deploy mechanics), call `device_request_folder_access` on the repo folder, then use `device_bash` to write and edit files in place (Python read-modify-write keeps em dashes and arrows intact); `device_commit_files` should also carry the thumbnail PNG into `assets/` — untested as of #36. (3) Last resort: one all-or-nothing installer script (every edit checked before any write, refuses to re-run) that Ram runs once. Never hand Ram whole files to paste.

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
- **Counter was not live for #36–#37 (installed with #38 — see "Working rules (from #38)"):** the issue pages fire `goatcounter.count({path:'lens-switch-<view>', event:true})` on every dropdown change, but no GoatCounter script is on the site, so nothing was recorded for #36 or #37. Add the site-wide GoatCounter snippet before #38 ships (the last pilot issue), or the pilot ends with no data for the 10% decision.
- **Lens implementation = copy from `issues/issue-36.html` verbatim** (lens CSS block, the `lens-bar` markup, the end-of-body script): `<details class="lens lens-plain">` / `<details class="lens lens-engineer">` after each story callout; the `js` class set on `<html>` in `<head>`; view stored in `data-lens`; localStorage key `dad-lens`; `?lens=plain|engineer`. Labels: dropdown "In simple terms", summaries "In simple terms" / "Under the Hood". Test four states before the review gate: JS off, default, `?lens=engineer#story-3`, `?lens=plain`.
- **Decision rule:** if fewer than ~10% of readers ever switch views across the pilot, drop the feature and revert to plain Leader-only issues. (The 10% threshold is a working guess, not a benchmark — revisit once real numbers land.)
- The **Beehiiv teaser is unchanged** for the pilot. The `?lens=` param is available for manual/future use but is not required in teaser links yet.

## Two mandatory pauses (do not skip either)
1. **Story-selection pause** — after Gmail + web + analyst research, present 10 candidate stories + 3 title options + a proposed (non-repeated) Agent 101 concept. Ram picks 5 stories and 1 title before writing begins. **From #38 on, this pause also collects Ram's take on each picked story and his CIO Corner notes (see "Human voice" below) — writing does not start without them.**
2. **HTML review gate** — after the full `issue-NN.html` is written and the thumbnail generated, **PAUSE and present the finished issue to Ram for approval before anything is committed, pushed, or staged for Beehiiv.** Nothing moves toward publish until Ram says "approved." He reviews, requests edits, the issue is revised, and only on his explicit approval does the git push (and then Beehiiv) proceed.
   - **Review format:** in-chat rendered preview — deliver the full `issue-NN.html` as a rendered file card in the conversation (Ram's chosen default). Do not require a local browser preview unless he asks.

## Human voice — Ram's take and Ram's CIO Corner (from issue #38 on)
Decided 2026-10-04 after #37. The aim is copy that carries a practitioner's judgment, not AI prose made to sound warmer.

- **Step A — Ram's take, before writing.** As soon as Ram picks his 5 stories and title, ask in the same turn for **one or two rough sentences per picked story**: what he actually thinks, something a client or colleague said that week (anonymized), or where he disagrees with the consensus. Rough notes or dictation are fine.
  - Write each story **around his thesis** — his take sets the angle, the lead-in and the callout. Research supplies the evidence; it does not replace his position.
  - **Do not start writing until the takes arrive**, unless Ram explicitly says "skip takes" for that issue. If he gives takes for only some stories, write those around his thesis and say which stories have none.
  - **Never invent** an anecdote, a client remark, or an opinion and present it as his. Use only what he supplies; keep clients and employer unnamed.
- **Step B — CIO Corner is Ram's own section.** Ask for it at the same pause: about **150 rough words**, typed or dictated, in his own voice.
  - Claude **only tidies**: grammar, order, length, and fitting the 4-paragraphs-plus-callout shape. No new arguments, no added data points unless he asks; if a claim needs a source, flag it back to him instead of quietly adding one.
  - **First person** ("I", "what I am seeing"). **No byline for now** — it runs unsigned, with the subtitle prefixed "From the editor's desk:". The `deploy.sh` guard against a "— Ram" byline stays until Ram decides otherwise.
  - If Ram has not supplied the notes, **stop and ask**. Do not write CIO Corner for him. The only fallback is his explicit "write it yourself this week".
- **At the HTML review gate**, state which stories were written from his takes and confirm CIO Corner is his words, tidied — so nothing AI-authored is passed off as his.
- Not adopted yet (revisit later): taking scored positions and a "what we got wrong" line, a reader question per issue, varying story length, a how-it-is-made footer.

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
- **deploy.sh live-check — FIXED (#36):** now polls `https://www.distilledaidigest.com/...` with `curl -sIL` and follows redirects; #36 printed `check 1: 200 ✅ LIVE`. A "⚠️ Not 200 yet" now means a real problem — verify with `curl -sIL https://www.distilledaidigest.com/issues/issue-NN.html | grep -i '^HTTP' | tail -1`.
- **deploy.sh must stay executable:** editing and re-saving `scripts/deploy.sh` dropped its execute bit (git mode 100755 → 100644), so #36's first run failed with `zsh: permission denied`. After any edit to the script, check `git diff --summary scripts/deploy.sh` shows no mode change; fix with `chmod +x scripts/deploy.sh` (or run `bash scripts/deploy.sh NN "Title"`).
- **Section anchors are standard from #35 on:** in addition to `id="story-1"`…`"story-5"`, the four non-story sections carry `id="governance"`, `id="cio"`, `id="stack"`, `id="agent101"` so the Beehiiv teaser's section links deep-link instead of dead-ending. (Supersedes the older "add anchors if/when they exist" note; #34 had story anchors only.)
- **Beehiiv injection recipe (confirmed #35):** needs a connected Chrome (Claude-in-Chrome extension, Ram signed in, Chrome open) — the built-in browser pane returned HTTP 400 on this surface and is not reliable; if no browser is reachable, hand Ram the teaser HTML to paste. Editor DOM: `textarea[0]` = title, `textarea[1]` = subtitle, one `.ProseMirror` body. Set the subtitle via the React native setter; for the **title, click the field, select all and type it with real keystrokes**. On #36 the native setter showed the title but it did not persist; it reverted to "New post" on reload. Start a new post via the sidebar "+" → "Blank draft post", because "Start writing" opens the template library. After injecting, **reload the editor and re-read title, subtitle and link count** — "Synced" alone is not proof. Inject the teaser body as base64 decoded in-page (avoids em-dash/arrow/apostrophe corruption): decode to a string, then `.ProseMirror` `focus()` → `execCommand('selectAll')` → `execCommand('insertHTML', false, html)` → dispatch an `input` event (bubbles). Verify: read back both textarea values, count links (should be 10: 5 stories + governance/cio/stack/agent101 + complete-issue), confirm "Synced". Never publish and never upload the thumbnail on Ram's behalf — he uploads the thumbnail, sets the kebab-case slug under Web → Post URL, confirms the Email checkbox, reviews, and publishes, only after the site is live.
- **Repo write path when the Filesystem connector fails (found #36, 2026-09-27):** in cloud sessions linked to the Mini, every `Filesystem` tool call can fail with "invalid outputSchema … draft-07 … supports JSON Schema 2020-12 only". Cause: the Filesystem server (versions from 2025.11.25 on) publishes its output schemas as JSON Schema draft-07, and the remote-devices bridge only accepts 2020-12, so the call is rejected before it runs. Nothing on the Mac is broken. Workaround used: `device_request_folder_access` on the repo folder, then `device_bash` to write and edit files in place. Do not blind-retry Filesystem writes.
- **Title format:** house format is **"The Week …"** (e.g. "The Week Spending Raced Its Own Safety Case"), under ~8 words.
- **CSS/structure template = the most recent shipped issue** (as of now, `issues/issue-38.html`, which also carries the Sources block and the GoatCounter script, and which carries the four section anchors and the lens markup), keeping the six-card Stack. Roll the template forward each week.

## Working rules (from #36)
- **A mid-issue change from Ram applies to the current issue immediately** — make it in the issue and in this file in the same turn. Do not ask whether it applies "from next issue".
- **Reconcile `claude/agent101-history.md` at session start** against the newest `issues/issue-NN.html` and log any missing issue before proposing a concept (#35 "The Token Bill" was missing when #36 started).
- **Title options at the story-selection pause must already follow the "The Week …" format** (under ~8 words); #36's first three options did not.
- **The repo copy of this file is the golden source.** The copy attached to the claude.ai Project can lag behind; when they differ, follow the repo and refresh the Project copy.

## Working rules (from #37)
- **Never run plain `git status` / `git diff` from the linked-session shell.** It leaves an empty `.git/index.lock` that the shell cannot delete without a delete-permission prompt, and that lock blocks `deploy.sh`. Use `GIT_OPTIONAL_LOCKS=0 git status` (read-only) and confirm `.git/index.lock` does not exist before handing over.
- **Thumbnail from the linked-session shell renders in Liberation fonts, not Georgia/Arial** (the shell is a Linux VM; the Mac's `.venv` and system fonts are not used). It writes straight to `assets/thumbnail_issueNN.png`, so no manual move is needed, but for an exact font match with earlier issues re-run `scripts/make_thumbnail_dad17.py` on the Mac itself.
- **`device_commit_files` can report "written" without updating the file** when the same staged path is committed twice (#37: the revised Story 1 did not land on the second commit). Copy the revision to a new staged filename before re-committing, and always compare `md5sum` of the workspace copy and the repo copy before handing over.
- **Beehiiv title (#37):** inject body and subtitle first, then triple-click the title text itself, confirm `document.activeElement` is the "Add a title" textarea with the old text selected, and only then type. A click at coordinates measured before the body was inserted missed the field and the title stayed "New post". Reload and re-read all three fields before reporting.
- **Issue date range runs Sunday to Saturday** (#36 = Sep 20–26, #37 = Sep 27–Oct 3); state it that way at the story-selection pause.
- **Write path that worked on #37:** build `issue-NN.html` in the cloud workspace, test the four lens states there, then `device_commit_files` into `issues/`; edit `index.html` / `archive.html` / `agent101-history.md` in place with a Python read-modify-write that asserts every match before writing. `scripts/update_site.py` is stale (it expects a `featured-excerpt` class the homepage no longer has) — do not use it.
- **Check prior coverage before the story-selection pause:** grep past issues in the repo for each candidate's product and company names, and say in the candidate list where a topic was already covered (#37: Grok Bot was #29, Muse was #36), so the angle is new and cross-referenced rather than repeated.
- **The Project copy of this file cannot be refreshed by file transfer** (the bridge refuses the repo file as hardlinked); it has to be re-written through the Projects tool with the full text. Do it whenever this file changes.

## Sourcing discipline
- Treat AI-agent-supplied leads (e.g. from Bram/Grok) as unverified until checked against a primary source. This session alone caught: a "$31K loss" that was a garbled ¥31,000, a nonexistent "Agent Armor" product, an SB 53 author error, and a mis-framed Marvell "$12.2B spend." Verify every figure, name, date, and attribution before it goes in.

## Publishing
- Never publish the Beehiiv email or push git without Ram's explicit go. Deploy is via `scripts/deploy.sh` (which pushes); Ram runs it (or clicks publish) himself.

## Working rules (from #38)
- **No past calendar dates in body copy.** Write "this week", "recently", "last month". Future, action-relevant dates stay (e.g. "November 12"). The week range stays in the hero line, the Stack heading and the closing.
- **CIO Corner framing.** It is the set of questions a CIO reading the issue should be asking, in Ram's first-person voice, not a hot take and never a pitch ("where my team comes in" is out). One lens per issue, rotating through Ram's four: workforce; customer and sponsor objectives; regulatory and compliance; technology adoption (the lever for the other three). #38 used regulatory and compliance. The last paragraph's lead-in is **"Put on the Radar:"** (not "The check for Monday").
- **Sources section in every issue.** After the closing, add the collapsed `<details class="sources" id="sources">` block ("Sources for this issue"), grouped by story, Governance Angle and Stack. Link only pages actually opened and read; write "as reported by" when the original (e.g. a paywalled FT piece) was not read. The Beehiiv teaser is unchanged.
- **Do the source check before the review gate, not after.** Opening every source to link it caught six errors in the #38 draft that came from the research brief (a "private preview" claim, deal terms, who a letter was addressed to). Re-verify each research-phase fact against the opened page at write time.
- **Outlets Ram does not want cited: Al Jazeera, Associated Press, NPR.** Find another outlet for the same story (TechCrunch and BetaNews are fine).
- **GoatCounter is installed.** `<script data-goatcounter="https://bramforgelabs.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>` sits before `</body>` on `index.html`, `archive.html` and issues #36–#38; new issues inherit it from the template. Recording starts with the #38 deploy, so #36 and #37 have no lens-switch data. Open decision: whether to extend the lens pilot past #38 (Claude suggested through #40; Ram has not decided).
- **Voice chats cannot write Project docs.** Decisions made in a voice chat must be saved at the start of the next text session (recover them with conversation search), before any other work.
- **`device_commit_files` staged path must be under `/mnt/user-data/outputs/`.** Use a new filename for every revision (`issue-NN-r2.html`, `-r3` …) with `force`, then compare `md5sum` of the build and the repo copy.
- **Anthropic usage policy as a source:** `anthropic.com/legal/aup` is the primary text (eleven high-risk areas; qualified human review plus disclosure). Press coverage of the October 2026 update mostly covered the cruelty clause only.
