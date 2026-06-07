import os
from PIL import ImageFont, ImageDraw, Image

candidates_regular = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    "/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
]
candidates_bold = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
    "/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf",
]

def load_font(size, bold=False):
    candidates = candidates_bold if bold else candidates_regular
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()

# Issue variables
ISSUE_NUM = 15
TITLE_LINE1 = 'The Week AI'
TITLE_LINE2 = 'Moved In'
TAGLINE = "Shadow AI crisis, lab land grab, productivity paradox, SaaS disruption"
TAGS = ['Shadow AI', 'Lab Grab', 'SaaS Shift']
OUTPUT_FILE = 'assets/thumbnail_issue15.png'

# Generate thumbnail
width, height = 1200, 630
img = Image.new('RGB', (width, height), color='#f5f5f5')
draw = ImageDraw.Draw(img)

# Draw title lines
font_size = 120
font = load_font(font_size)
# Center title
bbox = draw.textbbox((0, 0), TITLE_LINE1, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
draw.text(((width - w)/2, height * 0.3), TITLE_LINE1, fill='#2c2c2c', font=font)
bbox = draw.textbbox((0, 0), TITLE_LINE2, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
draw.text(((width - w)/2, height * 0.5), TITLE_LINE2, fill='#2c2c2c', font=font)

# Draw tagline
font_size = 48
font = load_font(font_size)
bbox = draw.textbbox((0, 0), TAGLINE, font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
draw.text(((width - w)/2, height * 0.65), TAGLINE, fill='#555555', font=font)

# Draw tags
font_size = 36
font = load_font(font_size)
for i, tag in enumerate(TAGS):
    bbox = draw.textbbox((0, 0), tag, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (width - w)/2 + (i - 1) * (w + 30)
    draw.text((x, height * 0.8), tag, fill='#4a90e2', font=font)

# Save output
os.makedirs('assets', exist_ok=True)
img.save(OUTPUT_FILE)
print(f'Successfully generated: {OUTPUT_FILE}')