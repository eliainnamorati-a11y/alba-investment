import os
from PIL import Image

png_files = [
    'guillaume.png',
    'stefano.png',
    'e2cc44c0-8d69-49a9-aa4b-18327d3236cf.png',
    'nicolas.png',
    'luigi.png'
]

for png in png_files:
    if os.path.exists(png):
        print(f"Converting {png}...")
        img = Image.open(png)
        webp_name = png.replace('.png', '.webp')
        img.save(webp_name, 'WEBP', quality=80)
        print(f"Saved {webp_name}. Size: {os.path.getsize(webp_name)/1024:.1f} KB")
