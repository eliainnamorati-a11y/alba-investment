import re

files = {
    'stefano-tittarelli.html': 'stefano.png',
    'luigi-mantrino.html': 'luigi.png',
    'guillaume-di-liberatore.html': 'guillaume.png',
    'nicolas-el-alam.html': 'nicolas.png'
}

for file_name, img_name in files.items():
    try:
        with open(file_name, 'r') as f:
            content = f.read()

        # Fix CSS
        content = re.sub(
            r'\.bio-container\s*\{\s*display:\s*flex;\s*min-height:\s*100vh;\s*background:\s*#fff;\s*position:\s*relative;\s*\}',
            '.bio-container { display: flex; min-height: 100vh; background: #fff; position: relative; padding-top: 100px; }',
            content
        )

        content = re.sub(
            r'\.bio-image-col\s*\{\s*flex:\s*0\s*0\s*50%;\s*height:\s*100vh;\s*position:\s*sticky;\s*top:\s*0;\s*background:\s*#f5f5f5;\s*overflow:\s*hidden;\s*\}',
            '.bio-image-col { flex: 0 0 50%; height: calc(100vh - 100px); position: sticky; top: 100px; background: #f5f5f5; overflow: hidden; }',
            content
        )

        # Fix mobile height CSS just in case
        content = re.sub(
            r'\.bio-image-col\s*\{\s*height:\s*70vh;\s*flex:\s*none;\s*position:\s*relative;\s*\}',
            '.bio-image-col { height: 70vh; flex: none; position: relative; top: 0; }',
            content
        )

        # Fix Image Src
        # Find <div class="bio-image-col"> ... <img src="...">
        # We can just do a regex replace for the img tag right after bio-image-col
        content = re.sub(
            r'<div class="bio-image-col">\s*<img src="[^"]+" alt="([^"]+)">',
            f'<div class="bio-image-col">\n            <img src="{img_name}" alt="\\1">',
            content
        )

        with open(file_name, 'w') as f:
            f.write(content)
        print(f"Updated {file_name}")
    except Exception as e:
        print(f"Failed to update {file_name}: {e}")

