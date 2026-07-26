# D·A·D Newsletter — Issue Standards (v1.0)

*Established from the consistency fix applied to Issues #24 and #25 (July 2026). These standards apply to all future issues.*

---

## 1. CSS & Design Tokens

### Color Palette (exact values)
| Token | Value | Usage |
|-------|-------|-------|
| `--navy` | `#1C2F50` | Hero background, section headers |
| `--navy-dark` | `#111e33` | Site navigation bar |
| `--navy-mid` | `#243a60` | Hover states, secondary fills |
| `--gold` | `#C9A84C` | Accent, badges, emphasis, borders |
| `--gold-light` | `#e2c06e` | Hover/light accent |
| `--gold-pale` | `#f5ecd4` | Subtle backgrounds |
| `--cream` | `#FAF7F2` | Page background |
| `--white` | `#ffffff` | Text on dark backgrounds |
| `--ink` | `#1a1a2e` | Body text |
| `--ink-soft` | `#3a3a52` | Secondary text |
| `--rule` | `#d6cfc4` | Dividers, borders |

### Font Stack
- **Body copy:** `'Source Serif 4', Georgia, serif` — 17px, line-height 1.75
- **Headings (hero, titles):** `'Playfair Display', serif` — weights 700–900
- **Meta/nav/badges:** `'JetBrains Mono', monospace` — sizes 0.7–0.75rem
- **Code blocks:** `'JetBrains Mono', monospace` (inline in mono elements)

### Hero Section
- Background: `var(--navy)` with radial gradient overlay (gold at 8% opacity)
- Bottom border: `3px solid var(--gold)`
- Title: `Playfair Display`, 900 weight, `clamp(2.2rem, 5vw, 3.6rem)`, italic gold `<em>`
- Badge: `JetBrains Mono`, gold border `1px solid rgba(201,168,76,0.4)`
- Hook: max-width 680px, italic, gold bold emphasis via `<strong>`

---

## 2. Page Structure (mandatory order)

```
<nav class="site-nav">           → Navigation bar (sticky, navy-dark)
<header class="hero">            → Issue badge, title, date, hook
<nav class="toc-strip">          → Table of contents (links to each section)
<div class="page-wrap">          → Main content wrapper
  <article id="story1">         → Story 1 (section-header + story-body + callout)
  <article id="story2">         → Story 2
  <article id="story3">         → Story 3
  <article id="story4">         → Story 4
  <article id="story5">         → Story 5
  <section id="quickhits">      → Quick Hits (5 items, bullet style)
  <section id="cio">            → CIO Corner (4 paragraphs + callout)
  <section id="stack">          → The Stack (Energy/Chips/Cloud/Models/Apps)
  <section id="agent101">       → Agent 101 (new concept each issue)
  <section class="closing-section"> → Closing ornament + text + byline
</div>
<footer class="site-footer">    → Footer with links
```

### Story Structure (each story)
```
<article id="storyN">
  <div class="section-header">
    <div class="section-number">NN</div>
    <div class="section-title-block">
      <div class="section-label">CATEGORY</div>
      <h2 class="section-title">Story Title</h2>
    </div>
  </div>
  <div class="story-body">
    <p><strong>Bold hook sentence.</strong> Body text...</p>
    <p>More paragraphs...</p>
  </div>
  <div class="callout">
    <div class="callout-label">The Signal / The Implication / The Risk</div>
    <p>Callout content...</p>
  </div>
</article>
```

### Callout labels (consistent set)
- `The Signal` — for a new development worth watching
- `The Implication` — for the second-order effect
- `The Risk` — for a warning or downside
- `The Opportunity` — for a positive strategic angle
- `The Bottom Line` — for a summary verdict

### Quick Hits Structure
```
<section id="quickhits">
  <div class="section-header">...</div>
  <ul class="quick-hits-list">
    <li><span class="qh-bullet">▶</span><span class="qh-text"><strong>Bold headline</strong> body text</span></li>
    ... (exactly 5 items)
  </ul>
</section>
```

### CIO Corner
- 4 paragraphs minimum
- Each paragraph opens with a bold thesis sentence
- Ends with a `callout` box (label: "The Action")

### The Stack
- Entry per layer: Energy, Chips, Cloud, Models, Applications
- Each entry: `stack-card` with `stack-layer` label + body text
- Cross-layer synthesis paragraph at the end

### Agent 101
- New concept each issue (never repeated)
- Structure: `agent-eyebrow` ("This Week's Concept") → `agent-title` → `agent-body` (3-4 paragraphs)
- Must end with an italic *procurement question* or *actionable question* paragraph

### Closing Section
- Ornament: `&middot; &middot; &middot;`
- 1-2 paragraph closing reflection
- Byline: `— The Distilled AI Digest Team` (NEVER a personal name)
- "We'll see you next week with more signal, less noise."

---

## 3. Content Rules

### Hard Rules
- **Byline:** Always "The Distilled AI Digest Team." Never "Ram" or any personal name.
- **Spelling:** American English only. "Organization" not "Organisation." "Labor" not "Labour."
- **Model names/versions:** Never guess. Web-search to verify if uncertain.
- **Pricing/figures:** Always verify against source. Flag if unverifiable.

### Story Guidelines
- Each story: 3-4 paragraphs of body + 1 callout box
- First paragraph: bold thesis sentence followed by exposition
- Each paragraph: bold sub-headline at start (`<strong>...</strong>`)
- Quotes: Use `&ldquo;` and `&rdquo;` for smart quotes
- Em-dashes: Use `&mdash;` with spaces on both sides

### Quick Hits Rules
- Exactly 5 items
- Each item: bold headline + 1-2 sentence body
- No nested bold inside body text
- Use `▶` as bullet (Unicode, accessible)

### Issue Dating
- Format: `Month Day–Day, Year` (e.g., `July 12–18, 2026`)
- Consistent across hero badge, footer, and meta tags

---

## 4. TOC Strip

Generated from each story's short slug + Quick Hits + CIO + Stack + Agent 101.
```
<nav class="toc-strip">
  <a href="#story1" class="toc-item">Short Slug</a>
  <span class="toc-sep">&middot;</span>
  <a href="#story2" class="toc-item">Short Slug</a>
  ...
  <a href="#quickhits" class="toc-item">Quick Hits</a>
  <span class="toc-sep">&middot;</span>
  <a href="#cio" class="toc-item">CIO Corner</a>
  <span class="toc-sep">&middot;</span>
  <a href="#stack" class="toc-item">The Stack</a>
  <span class="toc-sep">&middot;</span>
  <a href="#agent101" class="toc-item">Agent 101</a>
</nav>
```

---

## 5. SEO & Meta

- `<title>`: `Issue #N — The Week [Title] | Distilled AI Digest`
- `<meta name="description">`: 1-sentence hook from the hero
- Open Graph tags: `og:title`, `og:description`, `og:image` (thumbnail)
- Twitter Card: `summary_large_image`

---

## 6. Agent 101 Concept Archive

| Issue | Concept | First Used |
|-------|---------|------------|
| #13 | Harness | — |
| #14 | Eval Gate | — |
| #15 | Agent IAM | — |
| #16 | Persistent Agents | — |
| #17 | Orchestration | — |
| #18 | Context Window | — |
| #19 | Model Routing & Fallback | — |
| #20 | (fill from issue) | — |
| #21 | (fill from issue) | — |
| #22 | (fill from issue) | — |
| #23 | (fill from issue) | — |
| #24 | AI Identity and Access Management (AI IAM) | July 7–11 |
| #25 | (fill from issue) | July 12–18 |

*Each issue introduces a new Agent 101 concept. Never reuse.*

---

## 7. Thumbnail Spec

- **Dimensions:** 1200×630px
- **Format:** PNG
- **Template:** Per Issue #15 brand spec (gold/navy palette, Playfair Display)
- **File name:** `thumbnail_issueN.png`
- **Path:** `Assets/thumbnail_issueN.png`

---

## 8. Verification Checklist (before deploy)

- [ ] Byline is "The Distilled AI Digest Team" — not a personal name
- [ ] American spelling throughout (no "organis-", "labour", etc.)
- [ ] All 5 stories present, each with 3-4 paragraphs + callout
- [ ] Quick Hits: exactly 5 items
- [ ] CIO Corner: 4 paragraphs + callout
- [ ] The Stack: all 5 layers covered
- [ ] Agent 101: new concept, not reused
- [ ] Closing: correct byline, ornament, "see you next week"
- [ ] TOC strip links match all sections
- [ ] Hero badge: correct issue number, date range, slug
- [ ] Issue date consistent across badge, footer, meta tags
- [ ] All figures verified against source (no guesswork)
- [ ] Thumbnail generated and deployed
- [ ] HTML validates (no unclosed tags)
- [ ] Beehiiv teaser generated (separate file)