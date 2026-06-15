#!/usr/bin/env python3
"""
update_site.py — Update index.html (featured card) and archive.html (new card)
for a new D·A·D issue. Matched to the ACTUAL file structures confirmed at Issue #19.

index.html : single "Latest Issue" featured-card — swap 5 fields in place.
archive.html: archive-grid newest-first — INSERT a new card at the top of the grid.

Idempotent: if issue-N is already linked in a file, that file is left untouched.

Usage:
  python3 scripts/update_site.py <NUM> "<TITLE>" "<DATE_RANGE>" "<EXCERPT>"
Example:
  python3 scripts/update_site.py 20 "The Week the Models Multiplied" "June 15\u201321, 2026" "Excerpt text here."
"""
import sys, re, pathlib

if len(sys.argv) < 5:
    sys.exit("usage: update_site.py <NUM> <TITLE> <DATE_RANGE> <EXCERPT>")

NUM, TITLE, DATES, EXCERPT = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
repo = pathlib.Path(__file__).resolve().parent.parent

def prev_num(s):
    nums = [int(n) for n in re.findall(r'issue-(\d+)\.html', s)]
    return max(nums) if nums else None

# ---------- index.html : swap the single featured card ----------
ip = repo / "index.html"
idx = ip.read_text(encoding="utf-8")
if f"issue-{NUM}.html" in idx:
    print(f"index.html: issue-{NUM} already present, skipped")
else:
    p = prev_num(idx)
    if p is None:
        print("index.html: WARNING no previous issue link found, skipped")
    else:
        # Swap the featured block fields from the previous issue to this one.
        idx2 = idx
        idx2 = idx2.replace(f'thumbnail_issue{p}.png" alt="Issue #{p} thumbnail',
                            f'thumbnail_issue{NUM}.png" alt="Issue #{NUM} thumbnail')
        idx2 = idx2.replace(f'<span class="issue-badge">#{p}</span>',
                            f'<span class="issue-badge">#{NUM}</span>')
        # date, title, excerpt, button: replace within the featured section only.
        # These are unique enough in the featured card to replace globally-safely
        # because the featured card is the only place the PREVIOUS latest appears
        # outside archive.html.
        idx2 = re.sub(r'(<h2 class="featured-title">)(.*?)(</h2>)',
                      lambda m: m.group(1) + TITLE + m.group(3), idx2, count=1, flags=re.S)
        idx2 = re.sub(r'(<p class="featured-excerpt">)(.*?)(</p>)',
                      lambda m: m.group(1) + EXCERPT + m.group(3), idx2, count=1, flags=re.S)
        idx2 = re.sub(r'(<span class="issue-date">)(.*?)(</span>\s*</div>\s*<h2 class="featured-title">)',
                      lambda m: m.group(1) + DATES + m.group(3), idx2, count=1, flags=re.S)
        idx2 = idx2.replace(f'issues/issue-{p}.html" class="btn-primary">Read issue #{p} \u2192',
                            f'issues/issue-{NUM}.html" class="btn-primary">Read issue #{NUM} \u2192')
        ip.write_text(idx2, encoding="utf-8")
        print(f"index.html: featured card updated #{p} -> #{NUM}")

# ---------- archive.html : insert new card at top of grid ----------
ap = repo / "archive.html"
arc = ap.read_text(encoding="utf-8")
if f"issue-{NUM}.html" in arc:
    print(f"archive.html: issue-{NUM} already present, skipped")
else:
    card = (
        f'      <div class="archive-grid">\n\n'
        f'        <!-- Issue {NUM} -->\n'
        f'        <article class="archive-card">\n'
        f'          <div class="archive-thumb">\n'
        f'            <img src="assets/thumbnail_issue{NUM}.png" alt="Issue #{NUM}" />\n'
        f'          </div>\n'
        f'          <div class="archive-body">\n'
        f'            <div class="issue-meta">\n'
        f'              <span class="issue-badge">#{NUM}</span>\n'
        f'              <span class="issue-date">{DATES}</span>\n'
        f'            </div>\n'
        f'            <h2 class="archive-title">{TITLE}</h2>\n'
        f'            <p class="archive-excerpt">{EXCERPT}</p>\n'
        f'            <a href="issues/issue-{NUM}.html" class="read-link">Read issue \u2192</a>\n'
        f'          </div>\n'
        f'        </article>\n'
    )
    anchor = '      <div class="archive-grid">'
    if anchor in arc:
        arc2 = arc.replace(anchor, card, 1)
        ap.write_text(arc2, encoding="utf-8")
        print(f"archive.html: inserted issue-{NUM} at top of grid")
    else:
        print("archive.html: WARNING archive-grid anchor not found, skipped")

print("Done. Review the diffs before committing.")
