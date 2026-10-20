#!/usr/bin/env python3
"""Render selected evidence pages into readable two-page contact sheets."""
import argparse
import json
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('course_id')
p.add_argument('member_fragment')
p.add_argument('pages', help='Comma-separated one-based physical PDF pages')
p.add_argument('--label', default='check')
p.add_argument('--tile', action='store_true', help='Render tall pages at 1000-pixel width and split into 1400-pixel tiles')
p.add_argument('--sample-tall', action='store_true', help='Sample top, middle, and bottom of tall pages; not a complete visual pass')
a = p.parse_args()
records = json.loads((ROOT / '.cache' / a.course_id / 'evidence_manifest.json').read_text())
matches = [r for r in records if a.member_fragment in r['member'] and 'pages' in r]
if len(matches) != 1:
    raise SystemExit(f'Expected one PDF, found {len(matches)}')
record = matches[0]
out = ROOT / '.cache' / a.course_id / 'rendered'
out.mkdir(parents=True, exist_ok=True)
images = []
for page in map(int, a.pages.split(',')):
    if not 1 <= page <= record['pages']:
        raise SystemExit(f'Page {page} out of range')
    stem = out / f'{a.label}-{page}'
    scale = ['-scale-to-x', '1000', '-scale-to-y', '-1'] if a.tile or a.sample_tall else ['-scale-to', '1500']
    subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page), *scale,
                    '-singlefile', '-png', str(ROOT / record['source']), str(stem)],
                   check=True, capture_output=True)
    im = Image.open(str(stem) + '.png').convert('RGB')
    if a.tile or a.sample_tall:
        positions = sorted(set([0, max(0, im.height//2-700), max(0, im.height-1400)])) if a.sample_tall else range(0, im.height, 1350)
        for y in positions:
            images.append((f'{page}, y={y}/{im.height}', im.crop((0, y, im.width, min(y+1400, im.height)))))
    else:
        images.append((page, im))
for start in range(0, len(images), 2):
    pair = images[start:start + 2]
    sheet = Image.new('RGB', (sum(im.width for _, im in pair), max(im.height for _, im in pair)+30), 'white')
    draw = ImageDraw.Draw(sheet)
    x = 0
    for page, im in pair:
        draw.text((x+10, 5), f'{a.label}: PDF page {page}', fill='black')
        sheet.paste(im, (x, 30))
        x += im.width
    path = out / f'{a.label}-contact-{start // 2 + 1}.png'
    sheet.save(path)
    print(path.relative_to(ROOT))
