from PIL import Image, ImageDraw
from pathlib import Path
p = Path('work/video_frames')
fs = sorted(p.glob('frame-*.jpg'))
W, H = 480, 270
cols = 4
sheet = Image.new('RGB', (W * cols, (H + 24) * ((len(fs) + cols - 1) // cols)), (240,240,240))
d = ImageDraw.Draw(sheet)
for i, f in enumerate(fs):
    im = Image.open(f).resize((W,H))
    x, y = (i % cols) * W, (i // cols) * (H+24)
    sheet.paste(im, (x,y))
    d.text((x+7,y+H+4), f'{i*2}s', fill=(0,0,0))
sheet.save(p/'contact.jpg', quality=90)
print('frames', len(fs), 'contact', p/'contact.jpg')
