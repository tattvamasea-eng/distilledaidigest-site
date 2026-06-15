#!/usr/bin/env python3
"""
build_template.py — Lock the D·A·D issue template against a known-good issue.

Reads an existing verified issue HTML and replaces issue-specific values with
{{TOKENS}}, producing templates/issue-template.html. Run ONCE (already run to
seed from issue-19). Re-run only if you intentionally change the design and want
to re-lock the template from a newer issue.

Usage:
  python3 scripts/build_template.py issues/issue-19.html
"""
import sys, re, pathlib

src = sys.argv[1] if len(sys.argv) > 1 else "issues/issue-19.html"
repo = pathlib.Path(__file__).resolve().parent.parent
html = (repo / src).read_text(encoding="utf-8")

# Order matters: most specific first.
subs = [
    ("The Week AI Got Grounded", "{{TITLE}}"),
    ("Issue #19", "Issue #{{NUM}}"),
    ("issue #19", "issue #{{NUM}}"),
    ("ISSUE #19", "ISSUE #{{NUM}}"),
    ("June 8&ndash;14, 2026", "{{DATE_RANGE}}"),
    ("June 8-14, 2026", "{{DATE_RANGE}}"),
    ("thumbnail_issue19.png", "thumbnail_issue{{NUM}}.png"),
]
for a, b in subs:
    html = html.replace(a, b)

out = repo / "templates" / "issue-template.html"
out.write_text(html, encoding="utf-8")

required = ["{{NUM}}", "{{TITLE}}", "{{DATE_RANGE}}"]
missing = [t for t in required if t not in html]
print(f"Wrote {out} ({len(html)} bytes)")
print("Tokens OK" if not missing else f"WARNING missing tokens: {missing}")
print("NOTE: Story bodies remain as issue-19 content — Claude rewrites the body")
print("each week. The template's value is the LOCKED CSS/structure, not the prose.")
