# D·A·D — Mandatory Verification Pass (verify.md)

**Runs AFTER topic/title approval, BEFORE writing. NON-SKIPPABLE.**
Ram confirmed (Issue #19): correctness over speed, permanently.

## The rule
Do not write any figure, valuation, %, count, parameter size, benchmark, name,
date, quote, or product claim that has NOT been verified with a tool call in THIS
session. If a fact can't be verified, cut it or flag it explicitly as unverified.
Never reconstruct a number from memory or from cleared search results.

## Per-story checklist (all 5 stories + Quick Hits)
- [ ] **Recency:** event falls inside the issue's target week. Flag/cut anything stale.
      (Issue #19 caught a story 3 weeks out of window with fabricated details.)
- [ ] **Figures:** every number confirmed via web_search/web_fetch this session.
- [ ] **Names/titles:** people, companies, products, job titles correct.
- [ ] **Dates:** specific dates/times confirmed, not inferred.
- [ ] **Quotes:** verified verbatim, <15 words, one quote per source max.
- [ ] **Sources:** >=1 reputable/primary source per load-bearing claim; note conflicts.
- [ ] **No duplication** of a prior issue's specific stat unless an intentional follow-up.

## Output
A short verification ledger (story -> status -> corrections) before writing begins.

## Known failure mode to avoid
In Issue #19, the first draft was written from memory after research results were
cleared from context. Result: a fabricated story (wrong week + invented features),
a backwards valuation (OpenAI mislabeled ~$1T), and unverifiable stats. The fix is
this pass — re-search before writing, every time.
