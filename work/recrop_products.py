from PIL import Image
from pathlib import Path
root=Path('public/images')
home=Image.open(root/'home-reference.png').convert('RGB')
# Original home screenshot is 1440 x 3072; remove its tile frames so CSS draws the borders once.
for name,x in [('leggings',50),('socks',324),('ball-yellow',597),('ball-chocolate',872),('apparel',1146)]:
    home.crop((x+2,770,x+243,1110)).save(root/f'{name}.jpg',quality=94)
# Best-seller tiles occupy the middle/lower part of the reference home screen.
for name,x in [('ball-blue',58),('best-sleeve',533),('best-chocolate',1010)]:
    home.crop((x+2,2087,x+378,2499)).save(root/f'{name}.jpg',quality=94)
