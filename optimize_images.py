import os
from PIL import Image

MAX_SIZE = 2000
SIZE_THRESHOLD = 500 * 1024  # 500 KB

def optimize_image(filepath):
    try:
        size = os.path.getsize(filepath)
        if size < SIZE_THRESHOLD:
            return

        print(f"Optimizing {filepath} (Original size: {size / 1024 / 1024:.2f} MB)")
        img = Image.open(filepath)
        
        # Check if resize is needed
        if img.width > MAX_SIZE or img.height > MAX_SIZE:
            img.thumbnail((MAX_SIZE, MAX_SIZE), Image.Resampling.LANCZOS)
            
        # Save based on format
        ext = filepath.lower().split('.')[-1]
        
        if ext in ['jpg', 'jpeg']:
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            img.save(filepath, 'JPEG', quality=75, optimize=True)
        elif ext == 'png':
            img.save(filepath, 'PNG', optimize=True)
        elif ext == 'webp':
            img.save(filepath, 'WEBP', quality=75)
            
        new_size = os.path.getsize(filepath)
        print(f"  -> New size: {new_size / 1024 / 1024:.2f} MB")
        
    except Exception as e:
        print(f"Error optimizing {filepath}: {e}")

for root, _, files in os.walk('.'):
    if '.git' in root or '.vscode' in root or 'venv' in root or 'alba-theme' in root:
        continue
    for f in files:
        if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            optimize_image(os.path.join(root, f))
