#!/usr/bin/env python3
"""D·A·D weekly thumbnail — Issue #17 visual template (navy + gold). Match #31/#32."""
from PIL import Image, ImageDraw, ImageFont
import argparse, os

W, H = 1200, 630
NAVY, GOLD, WHITE = "#1C2F50", "#B8862F", "#FFFFFF"

SERIF = [
    "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "/Library/Fonts/Georgia Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
]
SANS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
]
SANS_REG = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
]

def load(paths, size):
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--issue", type=int, required=True)
    ap.add_argument("--month", required=True, help="e.g. SEPTEMBER 2026")
    ap.add_argument("--title1", required=True)
    ap.add_argument("--title2", required=True, help="gold second line")
    ap.add_argument("--subtitle", required=True)
    ap.add_argument("--tags", required=True, help="comma-separated, 3 tags")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    MX, TOP = 56, 36
    brand, meta = load(SERIF, 28), load(SANS, 20)
    title, sub, tagf, foot = load(SERIF, 64), load(SANS_REG, 22), load(SANS, 18), load(SANS, 18)

    d.text((MX, TOP), "Distilled AI Digest (D·A·D)", fill=GOLD, font=brand)
    meta_t = f"ISSUE #{args.issue}  ·  {args.month.upper()}"
    bb = d.textbbox((0, 0), meta_t, font=meta)
    d.text((W - MX - (bb[2]-bb[0]), TOP + 6), meta_t, fill=WHITE, font=meta)
    y1 = TOP + 48
    d.line([(MX, y1), (W - MX, y1)], fill=GOLD, width=2)

    b1 = d.textbbox((0, 0), args.title1, font=title)
    b2 = d.textbbox((0, 0), args.title2, font=title)
    w1, h1 = b1[2]-b1[0], b1[3]-b1[1]
    w2, h2 = b2[2]-b2[0], b2[3]-b2[1]
    ty = 175
    d.text(((W-w1)/2, ty), args.title1, fill=WHITE, font=title)
    d.text(((W-w2)/2, ty+h1+12), args.title2, fill=GOLD, font=title)
    y2 = ty + h1 + 12 + h2 + 36
    d.line([(MX, y2), (W - MX, y2)], fill=GOLD, width=2)

    # wrap subtitle roughly at ~55 chars
    words = args.subtitle.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textbbox((0,0), trial, font=sub)[2] > W - 2*MX - 40 and cur:
            lines.append(cur); cur = w
        else:
            cur = trial
    if cur: lines.append(cur)
    sy = y2 + 28
    for i, line in enumerate(lines[:3]):
        bb = d.textbbox((0,0), line, font=sub)
        d.text(((W-(bb[2]-bb[0]))/2, sy+i*30), line, fill=WHITE, font=sub)

    pad_x, pad_y, gap = 18, 10, 16
    widths = [d.textbbox((0,0), t, font=tagf)[2]-d.textbbox((0,0), t, font=tagf)[0] + 2*pad_x for t in tags]
    total = sum(widths) + gap*(len(tags)-1)
    x = (W-total)/2
    ty = sy + len(lines)*30 + 36
    th = 20 + 2*pad_y
    for i, t in enumerate(tags):
        tw = widths[i]
        d.rounded_rectangle([x, ty, x+tw, ty+th], radius=4, outline=GOLD, width=2)
        tb = d.textbbox((0,0), t, font=tagf)
        d.text((x+(tw-(tb[2]-tb[0]))/2, ty+(th-(tb[3]-tb[1]))/2-2), t, fill=WHITE, font=tagf)
        x += tw + gap

    bar_h = 56
    d.rectangle([0, H-bar_h, W, H], fill=GOLD)
    ft = "DISTILLED AI DIGEST  ·  The signal, without the noise."
    fb = d.textbbox((0,0), ft, font=foot)
    d.text(((W-(fb[2]-fb[0]))/2, H-bar_h+(bar_h-(fb[3]-fb[1]))/2-2), ft, fill=NAVY, font=foot)

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    img.save(args.out, "PNG")
    print("wrote", args.out)

if __name__ == "__main__":
    main()
