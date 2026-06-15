# D·A·D Newsletter — Automation Runbook

This is the single source of truth for producing a Distilled AI Digest issue.
When Ram says "build issue N" (or the weekly trigger fires), follow this exactly.
The work runs through Claude in a session using the Filesystem, web_search, bash,
and Claude-in-Chrome tools — NOT through a standalone daemon.

## Confirmed environment (do not re-litigate)
- Filesystem WRITE access to the Mac repo IS available. Test once with
  Filesystem:list_allowed_directories (allowed: /Users/AI-Projects,
  /Users/AI-Projects/Documents). Never claim it's unavailable without testing.
- Repo: /Users/AI-Projects/Documents/GitHub/distilledaidigest-site
- Netlify auto-deploys on push to main (~60s). Site: distilledaidigest.com
- Beehiiv is on the Launch (free) tier → NO API. Draft is built via
  Claude-in-Chrome ProseMirror injection (browser picker prompt is unavoidable).

## The two human gates (everything else is automated)
1. TOPIC + TITLE APPROVAL — present 10 story candidates + 3 titles, PAUSE.
2. BEEHIIV PUBLISH — Claude builds the draft; Ram reviews and clicks publish.

## Pipeline

### Step 1 — Scope
Confirm issue number (last published + 1) and the Sun–Sat date range.

### Step 2 — Gmail scan
Gmail:search_threads, pageSize 30:
  after:YYYY/MM/DD before:YYYY/MM/DD (AI OR artificial intelligence) (newsletter OR digest OR weekly)

### Step 3 — Web research
Per-candidate targeted searches (topic + org + month/year). Pull Tier-2 analyst
sources (Gartner, Forrester, McKinsey, IDC, Deloitte) for CIO Corner weight.

### Step 4 — Present candidates → GATE 1
10 story candidates (each with a one-line enterprise angle) + 3 title options.
PAUSE for Ram to pick 5 stories, 5 Quick Hits, and 1 title.

### Step 5 — VERIFICATION (MANDATORY, NON-SKIPPABLE)
See verification-checklist.md. Re-verify EVERY figure/name/date/quote/product
claim IN THIS SESSION against a live source before writing. Confirm each story
falls inside the target week (Issue #19 caught a 3-week-stale story). Cut or
explicitly flag anything unverifiable. Produce a short verification ledger.
RULE: never write a number from memory or from cleared tool results.

### Step 6 — Write issue-N.html
Fill dad-automation/templates/issue-template.html. Replace all {{TOKENS}}.
Structure (fixed order): 5 stories (3-4 paras + named callout each) → Quick
Hits (5) → CIO Corner (4 paras + callout) → The Stack (5 cards: Energy/Chips/
Cloud/Models/Applications) → Agent 101 (NEW concept) → Closing.
Write directly to issues/issue-N.html via Filesystem:write_file.
Agent 101 used so far: Harness(#13), Eval Gate(#14), Agent IAM(#15),
Persistent Agents(#16), Orchestration(#17), Context Window(#18),
Model Routing & Fallback(#19). NEVER repeat.

### Step 7 — Thumbnail
Run thumbnail generator (Pillow) in the bash container, 1200x630, Issue #17
template (gold border bars, left accent, gold issue badge top-right, 3-line
white/gold/white title, gold divider, outlined tag pills, muted date).
Save to container, then write bytes to assets/thumbnail_issueN.png on the Mac.
(Issue #10 = "Deca·1" → thumbnail_deca1.png.)

### Step 8 — Word doc
Node + docx in container → AI_Newsletter_Digest_IssueN_<Month><Year>.docx.
Navy/gold branding, callouts as shaded tables. Validate before sharing.

### Step 9 — Update index.html + archive.html (direct Filesystem edits)
index.html: SINGLE "Latest Issue" featured-card (~lines 49-63). Swap 5 fields:
  thumbnail img src+alt, issue-badge #N, issue-date, featured-title,
  featured-excerpt, and btn-primary "Read issue #N →" link.
archive.html: INSERT a new <article class="archive-card"> at the TOP of
  .archive-grid (right before the previous "<!-- Issue N -->" card). Match
  markup exactly: archive-thumb img, issue-badge, issue-date, archive-title,
  archive-excerpt, read-link to issues/issue-N.html.
Use Filesystem:edit_file with exact-match oldText (dryRun first to preview).

### Step 10 — Commit, push, verify
Ensure .DS_Store is in .gitignore. Then (Ram runs, or Claude via bash if repo
reachable):
  cd <repo> && git add -A && git status
  git commit -m "Add Issue #N: <TITLE>" && git push origin main
Wait ~60s; verify: curl -sI https://distilledaidigest.com/issues/issue-N.html
  → expect HTTP/2 200.

### Step 11 — Beehiiv teaser draft (Claude-in-Chrome)
Build teaser: intro + Story 1 in FULL + Stories 2-5 teased (2 sentences each)
+ Quick Hits + CTA button → https://distilledaidigest.com/issues/issue-N.html.
Method: navigate to app.beehiiv.com/posts → Start writing → Blank draft →
set title via type, subtitle via type, body via document.querySelector
('.ProseMirror').focus() + execCommand('insertHTML', false, html).
STOP at draft. Do NOT advance Audience/Email/Web or publish. → GATE 2.
WEBSITE MUST BE LIVE (200) BEFORE Beehiiv publishes — the CTA links to it.

### Step 12 — X thread (manual post)
Generate 5-tweet thread text + 5 stat cards (Pillow, 800x420, navy/gold, no
lines/dividers). Thumbnail on tweet 1 (manual drag-drop). Ram posts.

## Hard guardrails (ALWAYS)
- Byline = brand only: "The Distilled AI Digest Team." NEVER "Ram."
- American spelling: Organization/Organize, never Organis-.
- Never guess Anthropic model versions/pricing — web_search first.
- issue-N.html is ALWAYS the full standalone issue; Beehiiv is teaser only.
- Verification gate is non-skippable. Correctness over speed.
- Read this runbook + the template before writing; never reconstruct the design.

## Trigger
Manual, by choice. The weekly run starts when Ram sends "build issue N for the
week SUN to SAT". Claude has no scheduler and cannot self-trigger. At the start
of a run, read this RUNBOOK first, then compute the issue number (highest
issues/issue-N.html + 1) and confirm the Sun–Sat date range.
