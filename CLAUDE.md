# D·A·D Newsletter — Production Workflow (CLAUDE.md)

This repo publishes the **Distilled AI Digest (D·A·D)** weekly enterprise-AI newsletter.
This file is the operating contract. Claude follows it every issue.

## The one human gate
The ONLY steps requiring Ram are: (1) approving the 5 story topics + 5 Quick Hits
+ title, and (2) publishing the Beehiiv draft. Everything else Claude does.

## Two-message rhythm
- **Message 1:** Claude scopes the week, scans Gmail, researches, and presents
  **10 story candidates + 3 title options.** Then STOPS.
- **Message 2:** Ram picks 5 stories + 5 Quick Hits + 1 title.
- Claude then runs the rest to a deployed site + a Beehiiv draft, no further questions
  unless a blocking error or an unverifiable load-bearing fact forces a flag.

## Pipeline (after selection)
1. **VERIFY — mandatory, non-skippable (see scripts/verify.md).** Re-check EVERY
   figure/name/date/quote/product-claim in THIS session via web_search/web_fetch.
   Cut or flag anything unverifiable. Produce a verification ledger. NEVER write a
   number from memory or from cleared tool results. (Issue #19 proved why: drafting
   from memory produced fabrications in 4 of 5 stories.)
2. **WRITE** issues/issue-N.html from templates/issue-template.html. Fill the
   {{TOKENS}}. Do NOT alter the CSS or section order. Fixed order:
   5 stories (3-4 paras + named callout) -> Quick Hits (5) -> CIO Corner
   (4 paras + callout) -> The Stack (Energy/Chips/Cloud/Models/Apps) ->
   Agent 101 (NEW concept) -> Closing. issue-19.html is the worked reference.
3. **ASSETS:** thumbnail (scripts/make_thumbnail.py, Issue #17 visual template),
   Word .docx, Beehiiv teaser, X thread text + stat cards.
4. **UPDATE SITE:** scripts/update_site.py edits index.html (featured-card swap)
   and archive.html (insert card at top of grid).
5. **DEPLOY:** scripts/deploy.sh — git add/commit/push, .DS_Store cleanup,
   wait for Netlify, verify live 200.
6. **BEEHIIV (manual publish):** Claude builds the draft via Chrome injection
   (ProseMirror); Ram reviews and publishes. Website must be live FIRST (the
   teaser CTA links to the Netlify issue URL).
7. **X (manual post):** Claude generates thread + stat cards; Ram posts.

## Hard guardrails (always)
- Byline = **"The Distilled AI Digest Team."** NEVER the personal name "Ram."
- American spelling: Organization/Organize, never Organis-.
- Never guess Anthropic model versions/pricing — web_search first.
- issue-N.html is ALWAYS the full standalone issue; Beehiiv is the teaser only.
- Use templates/issue-template.html — never reinvent or reconstruct the design.
- Agent 101 concept must be NEW each issue. Used so far: Harness(#13),
  Eval Gate(#14), Agent IAM(#15), Persistent Agents(#16), Orchestration(#17),
  Context Window(#18), Model Routing & Fallback(#19).
- After file writes, run `git add -A && git status` before commit. .DS_Store is git-ignored.

## File structures (confirmed Issue #19)
- **index.html:** single "Latest Issue" featured-card (~lines 49-63). Update = swap
  thumbnail src+alt, issue-badge #N, issue-date, featured-title, featured-excerpt,
  and the btn-primary "Read issue #N →" link.
- **archive.html:** archive-grid newest-first. Update = INSERT a new archive-card at
  the top of the grid (before the previous issue's "<!-- Issue N -->" card).

## Filesystem access
Claude has confirmed read/write access to this repo via Filesystem tools
(/Users/AI-Projects ...). Claude edits files directly; Ram runs git push, or Claude
runs it via bash if the repo is reachable. Do NOT claim filesystem access is
unavailable — test with Filesystem:list_allowed_directories first.

## Scheduling note
A cron/launchd job CANNOT run the AI steps (research/verify/write/Beehiiv) — those
need a live Claude session. A scheduled job can only run the deterministic scripts
on an already-written issue. The practical weekly trigger is Ram sending Message 1.
See scripts/weekly-reminder.md for the optional Sunday reminder setup.
