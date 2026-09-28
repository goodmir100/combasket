from PIL import Image, ImageFilter
from pathlib import Path
root = Path('public/images')
auth = Image.open(root/'login-reference.png').convert('RGB')
w,h = auth.size
# Rebuild the unobstructed gym backdrop from the clear strips above and below the glass login card.
top = auth.crop((0,0,w,148)).resize((w,390), Image.Resampling.LANCZOS)
bottom = auth.crop((0,875,w,h)).resize((w,h-390), Image.Resampling.LANCZOS)
back = Image.new('RGB',(w,h))
back.paste(top,(0,0)); back.paste(bottom,(0,390))
back = back.filter(ImageFilter.GaussianBlur(2))
back.save(root/'court-background.jpg',quality=91)
profile = Image.open(root/'profile-reference.png').convert('RGB')
# Isolate the original circular basketball photo used in the profile screen.
profile.crop((565,57,875,368)).save(root/'profile-avatar.jpg',quality=94)
