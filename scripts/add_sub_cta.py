#!/usr/bin/env python3
"""Add subscribe CTAs to weekly issue pages (plan: claude/subscribe-cta-plan.md).
CTA 1 after Story 1, CTA 2 after Story 5, CTA 3 band after the closing (before Sources).
Idempotent: skips any page that already contains class="sub-cta".
Usage: python3 scripts/add_sub_cta.py [--write] issues/issue-41.html ...
"""
import re, sys

URL = "https://newsletter.distilledaidigest.com/subscribe"
CSS = """
  /* Subscribe CTA (sub-cta) */
  .sub-cta { font-family:Arial,sans-serif; box-sizing:border-box; }
  .sub-cta-inline { display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:10px 16px; background:#fff; border:1px solid #e3dccb; border-left:4px solid #C9A84C; padding:12px 16px; margin:22px 0; font-size:15px; color:#333; line-height:1.5; }
  .sub-cta-inline p { margin:0; padding:0; flex:1 1 260px; font-size:15px; color:#333; }
  .sub-cta a.sub-btn { display:inline-block; background:#C9A84C; color:#1A2A4A; font-weight:bold; text-decoration:none; padding:10px 20px; border-radius:4px; font-size:14px; white-space:nowrap; border:0; }
  .sub-cta a.sub-btn:hover { background:#e0bc64; color:#1A2A4A; }
  .sub-cta-band { background:#1A2A4A; color:#fff; text-align:center; padding:44px 24px; margin:30px 0 12px; border-radius:4px; }
  .sub-cta-band h2 { font-family:Georgia,serif; font-size:26px; line-height:1.25; color:#fff; margin:0 0 12px; padding:0; border:0; }
  .sub-cta-band h2 em { color:#C9A84C; font-style:italic; }
  .sub-cta-band p { color:#F5F0E8; font-size:15px; margin:0 auto 22px; max-width:560px; }
"""
CTA1 = f'\n<div class="sub-cta sub-cta-inline"><p>Reading this on the site? Get every issue in your inbox on Sunday, free.</p><a class="sub-btn" href="{URL}">Subscribe Free &rarr;</a></div>\n'
CTA2 = f'\n<div class="sub-cta sub-cta-inline"><p>Those are the week&rsquo;s five. Get next week&rsquo;s in your inbox on Sunday, free.</p><a class="sub-btn" href="{URL}">Subscribe Free &rarr;</a></div>\n'
CTA3 = f'\n<div class="sub-cta sub-cta-band"><h2>Stay <em>one issue</em> ahead.</h2><p>Every Sunday, the five AI developments that actually matter &mdash; with the strategic context to act on them. Free, always.</p><a class="sub-btn" href="{URL}">Subscribe Free &rarr;</a></div>\n'

STORY = re.compile(r'<article\b[^>]*>|<div class="story(?:-card)?"[^>]*>')

def block_end(s, start):
    """Index just after the element that opens at `start` (balanced on its tag name)."""
    tag = re.match(r'<(\w+)', s[start:]).group(1)
    depth, pos = 0, start
    for m in re.compile(rf'<(/?){tag}\b[^>]*>').finditer(s, start):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return m.end()
    raise ValueError(f'unbalanced <{tag}>')

def apply(s):
    if 'sub-cta' in s:
        return None, 'already has sub-cta'
    stories = [m for m in STORY.finditer(s)]
    if len(stories) != 5:
        raise ValueError(f'{len(stories)} story blocks, expected 5')
    if s.count('</style>') != 1:
        raise ValueError('expected exactly one </style>')
    p1 = stories[1].start()
    cm = re.search(r'<!--(?:(?!-->).)*-->\s*$', s[:p1], re.S)
    if cm and p1 - cm.start() < 200:
        p1 = cm.start()  # keep the 'STORY 2' comment attached to its story
    p2 = block_end(s, stories[4].start())
    src = re.search(r'(?:<!-- SOURCES -->\s*)?<details class="sources"', s)
    if src:
        p3 = src.start()
    else:
        c = re.search(r'<(section|div)\b[^>]*class="closing(?:-section)?(?:\s[^"]*)?"[^>]*>', s)
        if not c:
            raise ValueError('no closing block')
        p3 = block_end(s, c.start())
    if not (p1 < p2 < p3):
        raise ValueError(f'insertion points out of order {p1} {p2} {p3}')
    out = s[:p1] + CTA1 + s[p1:p2] + CTA2 + s[p2:p3] + CTA3 + s[p3:]
    out = out.replace('</style>', CSS + '</style>', 1)
    ctx = lambda p: re.sub(r'\s+', ' ', s[max(0, p-50):p+50])
    return out, f'CTA1@…{ctx(p1)}… | CTA2@…{ctx(p2)}… | CTA3@…{ctx(p3)}…'

if __name__ == '__main__':
    write = '--write' in sys.argv
    for f in [a for a in sys.argv[1:] if a != '--write']:
        s = open(f, encoding='utf-8').read()
        try:
            out, note = apply(s)
        except ValueError as e:
            print(f'FAIL {f}: {e}'); continue
        if out is None:
            print(f'SKIP {f}: {note}'); continue
        assert out.count('class="sub-cta') == 3
        if write:
            open(f, 'w', encoding='utf-8').write(out)
        print(f'{"WROTE" if write else "OK   "} {f}: {note}')
