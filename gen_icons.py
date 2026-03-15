#!/usr/bin/env python3
import subprocess, sys

try:
    from PIL import Image, ImageDraw, ImageFont
    import io, math
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow', '--break-system-packages', '-q'])
    from PIL import Image, ImageDraw
    import io, math

def make_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Deep navy background circle
    draw.ellipse([0, 0, size-1, size-1], fill=(5, 6, 26, 255))
    # Moon — gold circle
    cx, cy = size * 0.5, size * 0.45
    r = size * 0.22
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(232, 213, 163, 255))
    # Moon shadow cutout (slightly offset)
    ox, oy = cx + r*0.35, cy - r*0.22
    r2 = r * 0.72
    draw.ellipse([ox-r2, oy-r2, ox+r2, oy+r2], fill=(5, 6, 26, 255))
    # Subtle star dots
    stars = [(0.22, 0.28), (0.75, 0.22), (0.18, 0.62), (0.80, 0.60), (0.50, 0.82), (0.65, 0.35)]
    for sx, sy in stars:
        px, py = int(sx * size), int(sy * size)
        sr = max(1, int(size * 0.012))
        draw.ellipse([px-sr, py-sr, px+sr, py+sr], fill=(200, 210, 255, 160))
    return img

for sz in [192, 512]:
    img = make_icon(sz)
    img.save(f'/home/claude/somnia/icons/icon-{sz}.png')
    print(f'Generated icon-{sz}.png')

print('Icons created successfully')
