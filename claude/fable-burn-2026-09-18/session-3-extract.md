# Session 3 — Architecture extract: Artie G2–G4 (Claude Fable 5.1)

**Cap:** ~$15–20 · **Source ack:** `~/.hermes/shared-memory/acks/2026-09-17-sutra-artie-phase0.md`  
**G1 already landed:** local skills git snapshot `28241e5` (visibility only; no remote)

Copy below the line into Claude Fable 5.1.

---

## Task
Turn Sutra’s Artie **AMEND** verdicts into **landable, minimal patches** cheaper seats (Asi/Asmi) can apply — no new cluster, no routes.json.

## Deliverables (write under `~/.hermes/shared-memory/drafts/fable-burn-2026-09-18/`)

### G2 — Trace → skill-change verdict (fold D349 / board #54)
- One-page schema: after a skill change, emit a single line: `keep | revert-candidate | inconclusive` + evidence pointer  
- **Candidate only** — never auto-revert; RSI Soft AMEND stays counsel-only  
- Show where it hooks existing `nightly-evals` / `evaluator-optimizer-gate` without a new cron

### G3 — Cost alert line (fold weekly-measurement-report)
- Exact prompt/script addition: per-provider budget threshold + alert  
- Alert only — **never** auto-disable a route  
- NO-OP health (already covered by provider-health-probe / NVIDIA / tool-repair watchdogs)

### G4 — Skill Review prune rule
- One paragraph to add to existing Sunday Skill Review cron prompt:  
  “value obvious + cost justified, else it does not get built”  
- Propose-only kill list; **Ram approves** any kill  
- No new agent / coach bot

## Explicit REJECT (do not reopen)
Hermes Coach · Slack surface · $60 Hetzner clone · roster copy · Phoenix/Datadog · auto-revert skills

## Also flag (do not expand into epic)
`sutra-messages-router` duplicate slug[:25] swallow — one-line Asi bug note only

## Done means
Three small patch drafts + why-receipt (why this fold, alternatives not chosen, uncertainty labeled). No `routes.json` edits.
