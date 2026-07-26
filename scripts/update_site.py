#!/usr/bin/env python3
"""
update_site.py — Update index.html (featured card + recent grid) and archive.html
for a new D·A·D issue.

index.html : (1) swap featured "Latest Issue" card; (2) rotate Recent Issues grid
             so the previous featured issue becomes the first grid card (N-1, N-2, N-3).
archive.html: INSERT a new card at the top of the issues grid.

Idempotent: if issue-N is already linked in a file, that file is left untouched.

Usage:
  python3 scripts/update_site.py <NUM> "<TITLE>" "<DATE_RANGE>" "<EXCERPT>"
Example:
  python3 scripts/update_site.py 27 "The Week AI Took the Wheel" "July 26–Aug 1, 2026" "Excerpt here."
"""
import sys, re, pathlib

if len(sys.argv) < 5:
    sys.exit("usage: update_site.py <NUM> <TITLE> <DATE_RANGE> <EXCERPT>")

NUM, TITLE, DATES, EXCERPT = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
repo = pathlib.Path(__file__).resolve().parent.parent

def extract_featured_card_data(html):
    """Extract title, dates, excerpt, issue number and link from the current featured card."""
    data = {}
    m = re.search(r'<p class="latest-issue-meta">(#\d+[^<]*)</p>', html)
    if m:
        data['meta'] = m.group(1).strip()
    m = re.search(r'class="latest-issue-meta">[^<]*#(\d+)', html)
    if m:
        data['num'] = m.group(1)
    m = re.search(r'<h2[^>]*class="[^"]*latest-issue[^"]*"[^>]*>(.*?)</h2>|latest-issue.*?<h2[^>]*>(.*?)</h2>', html, re.S)
    if not m:
        # Try to match the featured title via class
        m = re.search(r'class="featured-title"[^>]*>(.*?)</h2>|<h2[^>]*class="featured-title"[^>]*>(.*?)</h2>', html, re.S)
    if m:
        data['title'] = (m.group(1) or m.group(2) or '').strip()
    m = re.search(r'<p class="featured-excerpt">(.*?)</p>', html, re.S)
    if m:
        data['excerpt'] = m.group(1).strip()
    m = re.search(r'<span class="issue-date">(.*?)</span>', html)
    if m:
        data['dates'] = m.group(1).strip()
    m = re.search(r'thumbnail_issue(\d+)\.png" alt="Issue #\d+ thumbnail', html)
    if m:
        data['thumb_num'] = m.group(1)
    m = re.search(r'href="[^"]*issues/issue-(\d+)[^"]*"[^>]*class="btn-read"', html)
    if m:
        data['link_num'] = m.group(1)
    return data

# ---------- index.html : read current state ----------
ip = repo / "index.html"
idx = ip.read_text(encoding="utf-8")

if f"issue-{NUM}.html" in idx or f"issue-{NUM}\"" in idx:
    print(f"index.html: issue-{NUM} already present in featured card, checking recent-grid...")
else:
    # Extract existing featured card data BEFORE we overwrite it
    old = extract_featured_card_data(idx)
    old_num = old.get('thumb_num') or old.get('link_num') or old.get('num', '')
    old_meta = old.get('meta', f'#{old_num}')
    old_title = old.get('title', '')
    old_excerpt = old.get('excerpt', '')
    old_dates = old.get('dates', '')

    if not old_num:
        print("index.html: WARNING could not detect previous issue number, featured card skipped")
    else:
        p = int(old_num)
        idx2 = idx

        # 1. Swap featured card
        idx2 = idx2.replace(
            f'thumbnail_issue{p}.png" alt="Issue #{p} thumbnail',
            f'thumbnail_issue{NUM}.png" alt="Issue #{NUM} thumbnail')
        idx2 = re.sub(
            r'(<p class="latest-issue-meta">)(.*?)(</p>)',
            lambda m: m.group(1) + f'#{NUM} {DATES}' + m.group(3), idx2, count=1, flags=re.S)
        idx2 = re.sub(
            r'(<h2[^>]*>)(.*?)(</h2>)(?=.*class="featured-excerpt"|.*btn-read)',
            lambda m: m.group(1) + TITLE + m.group(3), idx2, count=1, flags=re.S)
        idx2 = re.sub(
            r'(<p class="featured-excerpt">)(.*?)(</p>)',
            lambda m: m.group(1) + EXCERPT + m.group(3), idx2, count=1, flags=re.S)
        # Replace the read-link for the featured card
        idx2 = re.sub(
            rf'(href="[^"]*issues/issue-{p}[^"]*"[^>]*class="btn-read">Read issue #){p}( →)',
            lambda m: m.group(1).replace(f'issue-{p}', f'issue-{NUM}.html') + NUM + m.group(2),
            idx2, count=1)
        # Simpler replacement for read link
        idx2 = idx2.replace(
            f'issues/issue-{p}" class="btn-read">Read issue #{p} →',
            f'issues/issue-{NUM}.html" class="btn-read">Read issue #{NUM} →')
        idx2 = idx2.replace(
            f'issues/issue-{p}.html" class="btn-read">Read issue #{p} →',
            f'issues/issue-{NUM}.html" class="btn-read">Read issue #{NUM} →')

        ip.write_text(idx2, encoding="utf-8")
        print(f"index.html: featured card updated #{p} -> #{NUM}")

        # 2. Rotate recent-grid: insert N-1 at top, drop the 4th (oldest) card
        idx3 = ip.read_text(encoding="utf-8")
        grid_start = idx3.find('<div class="recent-grid">')
        grid_end = idx3.find('</div>', grid_start)
        # Find end of recent-grid (it contains 3 issue-card divs)
        # Count nested divs to find the closing </div> of recent-grid
        pos = grid_start + len('<div class="recent-grid">')
        depth = 1
        while pos < len(idx3) and depth > 0:
            next_open = idx3.find('<div', pos)
            next_close = idx3.find('</div>', pos)
            if next_open != -1 and next_open < next_close:
                depth += 1
                pos = next_open + 4
            elif next_close != -1:
                depth -= 1
                pos = next_close + 6
            else:
                break
        grid_end = pos  # just after the closing </div> of recent-grid

        grid_html = idx3[grid_start:grid_end]

        # Find all issue-card divs in the grid
        cards = list(re.finditer(r'<div class="issue-card">.*?</div>\s*</div>', grid_html, re.S))
        if len(cards) >= 3:
            # Build new N-1 card
            new_card = f'''    <div class="issue-card">
      <img src="/assets/thumbnail_issue{p}.png" alt="Issue #{p} thumbnail">
      <p class="issue-card-meta">#{p} {old_dates}</p>
      <h3>{old_title}</h3>
      <p>{old_excerpt}</p>
      <a href="https://www.distilledaidigest.com/issues/issue-{p}" class="read-link">Read issue →</a>
    </div>'''
            # Keep first 2 existing cards (N-2, N-3), drop the 3rd (N-4)
            new_grid = '<div class="recent-grid">\n' + new_card + '\n' + cards[0].group(0) + '\n' + cards[1].group(0) + '\n  </div>'
            idx4 = idx3[:grid_start] + new_grid + idx3[grid_end:]
            ip.write_text(idx4, encoding="utf-8")
            print(f"index.html: recent-grid rotated — #{p} inserted, oldest card dropped")
        else:
            print(f"index.html: recent-grid has fewer than 3 cards ({len(cards)}), manual update needed")

# ---------- archive.html : insert new card at top of issue-grid ----------
ap = repo / "archive.html"
arc = ap.read_text(encoding="utf-8")
if f"issue-{NUM}.html" in arc or f"issue-{NUM}\"" in arc:
    print(f"archive.html: issue-{NUM} already present, skipped")
else:
    # The archive uses a different card structure — insert at top of first issue-grid
    new_card = (
        f'      <div class="issue-card">\n'
        f'        <img src="/assets/thumbnail_issue{NUM}.png" alt="Issue #{NUM}">\n'
        f'        <p class="issue-card-meta">#{NUM} {DATES}</p>\n'
        f'        <h3>{TITLE}</h3>\n'
        f'        <p>{EXCERPT}</p>\n'
        f'        <a href="https://distilledaidigest.com/issues/issue-{NUM}.html" class="read-link">Read issue →</a>\n'
        f'      </div>\n'
    )
    anchor = '<div class="issue-grid">'
    if anchor in arc:
        arc2 = arc.replace(anchor, anchor + '\n' + new_card, 1)
        ap.write_text(arc2, encoding="utf-8")
        print(f"archive.html: inserted issue-{NUM} at top of issue-grid")
    else:
        print("archive.html: WARNING issue-grid anchor not found, skipped")

print("Done. Review the diffs before committing.")
