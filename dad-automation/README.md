# D·A·D Automation

Build tooling for the Distilled AI Digest weekly issue. Not served by Netlify
(it lives outside the published HTML); it's the playbook + locked template.

## Files
- `RUNBOOK.md` — the complete step-by-step process. Claude reads this FIRST
  at the start of every weekly run.
- `verification-checklist.md` — the mandatory, non-skippable fact-check gate.
- `templates/issue-template.html` — the LOCKED design, frozen from the verified
  Issue #19. Never reconstruct the design; fill this template's {{TOKENS}}.

## Weekly run (manual trigger, two human gates)
1. Send Claude:  `build issue N for the week SUN to SAT`
   (First, point it at this folder: "read dad-automation/RUNBOOK.md first.")
2. Approve the 10 stories + title.            ← GATE 1
3. Claude verifies every fact in-session, writes issue-N.html from the locked
   template, builds the thumbnail + Word doc, updates index.html + archive.html,
   commits, pushes, confirms the live 200, and builds the Beehiiv draft.
4. Review and publish the Beehiiv draft.      ← GATE 2
5. Post the X thread (text + stat cards Claude generated).

## Not automated (by design / by constraint)
- Triggering the run — manual by choice. Claude has no scheduler.
- Beehiiv publish — your call; Launch tier also blocks the API.
- The Chrome browser-picker prompt and occasional SSO click.

## Guardrails
Byline = "The Distilled AI Digest Team" (never "Ram"). American spelling.
Verify every fact in-session. issue-N.html is the full issue; Beehiiv is the
teaser. Agent 101 concept never repeats (see RUNBOOK for the used list).
