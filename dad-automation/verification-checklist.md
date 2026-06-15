# D·A·D Verification Checklist (NON-SKIPPABLE)

Runs AFTER topic/title approval, BEFORE writing. Issue #19 proved why: writing
from memory/cleared results produced fabrications in 4 of 5 stories — a
wrong-week story with invented features (Cursor: fake subagents/Dell/benchmark),
a backwards valuation (OpenAI mislabeled ~$1T; actual target $730–850B), and
unverifiable stats. Verification caught all of it. This gate is permanent.

## The rule
Do not write any figure, $, %, count, valuation, parameter size, benchmark,
name, title, date, quote, or product claim that has not been verified with a
tool call IN THE CURRENT SESSION. If it can't be verified, cut it or flag it
explicitly as unverified. Never reconstruct a number from memory.

## Per-story (all 5 + Quick Hits)
- [ ] RECENCY: event falls inside the target week. Flag/cut anything stale.
- [ ] FIGURES: every number confirmed via web_search/web_fetch this session.
- [ ] NAMES/TITLES: people, companies, products, job titles correct.
- [ ] DATES: specific dates/times confirmed, not inferred.
- [ ] QUOTES: verified verbatim; under 15 words; one quote per source max.
- [ ] SOURCE QUALITY: ≥1 primary/reputable source per load-bearing claim.
- [ ] NO DUP: not repeating a prior issue's specific stat unless a deliberate
      follow-up (and labeled as such).

## Output
A verification ledger: story → status → corrections. Append to the run notes.
Writing begins only after the ledger is complete.

## Lesson banked from Issue #19
- OpenAI IPO target was $730–850B, NOT ~$1T. (~$1T was Anthropic's expected debut.)
- Cursor Composer 2.5 launched May 18 (Issue #18's window) — verify launch dates.
- "Silent self-nerf" / "30-day retention" for Fable 5 were unverifiable — cut.
- Always confirm the event week before committing a story to the lineup.
