# D·A·D Newsletter — Standing Production Preferences

**PRECEDENCE — read this file first, every issue.** These are Ram's current, durable instructions and they override any conflicting instruction in the dad-newsletter skill's SKILL.md and in the project's inline "Production Process" / CLAUDE.md / "Website HTML Standard" wherever they disagree. Known conflicts to resolve in favor of THIS file: (a) The Stack has SIX layers, not five; (b) skip the Word doc by default; (c) the Beehiiv teaser uses the per-section link structure and sign-off defined below (older docs don't mention it); (d) push the website live BEFORE publishing Beehiiv (older docs say website is post-publish); (e) the bullets section is titled "The Governance Angle," not "Quick Hits." When something here contradicts an older instruction, follow this file and note the conflict; do not blend them.

Durable instructions from Ram. Apply to every issue unless he overrides in the moment.

## Deliverables
Skip the Word doc (.docx) by default. Issues #29 onward do not need it. `make_docx.js` lives only in the skill folder, not on the Mac. Only build it if Ram explicitly asks for a given issue.
Standard deliverables: full website `issue-NN.html` (written to the repo on the Mac), 1200×630 thumbnail PNG, Beehiiv teaser draft (Ram publishes it himself).

## The Stack — SIX layers, not five (from issue #32 on)

Order, top of supply chain to end use: **Energy → Chips → Cloud → Models → Harness → Applications**

The Harness layer sits between Models and Applications: the agent runtime/scaffold that wraps a raw model into an agent — the perceive-plan-act loop, context/memory management, tool-call brokering, orchestration. (Precedent: issue #28 used this 6-card layout; #29 and #31 mistakenly dropped to 5.)
Suggested emoji to match house style: ⚡ Energy · 💾 Chips · ☁ Cloud · 🧠 Models · 🔧 Harness · 📱 Applications.

## Research (Step 3, before the story-selection pause)
Gmail scan + web search as always, plus always consult leading analyst/consulting sources for the top-10 slate: Gartner, Forrester, HBR, McKinsey, BCG, Bain, Deloitte, IDC, Accenture, PwC and similar. Work at least one such data-backed source naturally into the issue.

## Agent 101 (permanent section)
The concept must not repeat any Agent 101 concept used in all past issues since the section was introduced — check the full run every time (see `claude/agent101-history.md`), not just the last few issues. Update `agent101-history.md` with the new concept after every issue.

## Section naming
Keep the CIO section named **"CIO Corner"** — not "CTO Corner" or "CIO/CTO Corner." Its content (procurement, vendor contracts, governance, operating-model, risk) is CIO territory, and the single crisp name has brand continuity across the run. Widen the audience in the subtitle if ever needed, not the section name.
The bullets section is titled **"The Governance Angle"** — NOT "Quick Hits." This applies to the section heading in the full website issue (the `<h2>` in `issue-NN.html`) as well as the teaser label. (From issue #34 on; older issues used "Quick Hits.") Also update any in-issue cross-reference to read "(see The Governance Angle)."

## Beehiiv teaser structure (from issue #34 on)

The Beehiiv post is the teaser only; the website HTML is the full issue. In the teaser body, every section gets its own "read more" link back to the full issue on the site so each section drives a click-through:

- After each of the 5 stories: a **Read the full story →** link. Point it at the story anchor on the site page (`.../issues/issue-NN.html#story-1` … `#story-5`; the story `<article>`s carry `id="story-1"`…`"story-5"`).
- A teaser line + link for each remaining section — one or two sentences of tease followed by the link below. Section labels and link text in the teaser:
  - The Governance section: label it **"The Governance Angle"** (not "Quick Hits"); link reads **"Read the Angle →"**.
  - CIO Corner: link reads **"Read the CIO Angle →"**.
  - The Stack: label it **"The 6-Layer Stack"**; link reads **"Read the Stack Impact →"**.
  - Agent 101: link reads **"Learn about <this issue's Agent 101 concept> →"** — the concept name changes every week (e.g. issue #34 = "Learn about The Sandbox →"). Do not hard-code "The Sandbox"; use whatever that issue's Agent 101 topic is.
- Section links point to the full issue URL (add section anchors to the HTML if/when they exist; base URL is fine otherwise).
- After the section links, add a final **Read the complete issue →** link.
- Close the teaser with the standard D·A·D sign-off (do not let it end abruptly on the CTA): a one-line week-signal wrap sentence, then "See you next week — still watching, still distilling.", then a bold "— The Distilled AI Digest Team". This mirrors the closing of the full website issue.
- Use absolute `https://www.distilledaidigest.com/issues/issue-NN.html` URLs so links work in email.

## Publish order (from issue #34 on)
Push the website live **FIRST**, then publish Beehiiv. Because every teaser section links to the live site page and its `#story-N` anchors, the site must be deployed before the email goes out — otherwise readers hit 404s. Sequence: (1) git push → Netlify deploy of `issue-NN.html` + updated `index.html`/`archive.html`; (2) verify the page and anchors load; (3) then publish the Beehiiv email. This reverses the older "website update = post-publish" step.

## Workflow pause
After Gmail + web + analyst research, **PAUSE** with 10 candidate stories + 3 title options + a proposed (non-repeated) Agent 101 concept. Ram picks 5 stories and 1 title before writing begins.

## Sourcing discipline
Treat AI-agent-supplied leads (e.g. from Bram/Grok) as unverified until checked against a primary source. This session alone caught: a "$31K loss" that was a garbled ¥31,000, a nonexistent "Agent Armor" product, an SB 53 author error, and a mis-framed Marvell "$12.2B spend." Verify every figure, name, date, and attribution before it goes in.

## Publishing
Never publish the Beehiiv email or push git without Ram's explicit go. Provide git commands; he runs them (or clicks publish) himself.
