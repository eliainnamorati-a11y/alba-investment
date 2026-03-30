import os
import shutil

src_dir = '.'
theme_dir = 'alba-theme'

if not os.path.exists(theme_dir):
    os.makedirs(theme_dir)

# 1. Write style.css
with open(os.path.join(theme_dir, 'style.css'), 'w') as f:
    f.write('''/*
Theme Name: Alba Investment Partners
Theme URI: 
Author: Alba
Description: Custom landing page theme for Alba.
Version: 1.0
*/
''')

# 2. Copy and modify index.html to index.php
with open('index.html', 'r') as f:
    content = f.read()

# Replace asset URLs with WP template directory paths
replacements = [
    # Fonts and CSS backgrounds
    ("url('LinotypeAperto-Roman.ttf')", "url('<?php echo get_template_directory_uri(); ?>/LinotypeAperto-Roman.ttf')"),
    ("url('FINNEWS (1).jpg')", "url('<?php echo get_template_directory_uri(); ?>/FINNEWS (1).jpg')"),
    
    # HTML Images
    ("src=\"logos/Untitled%20design%20(73).png\"", "src=\"<?php echo get_template_directory_uri(); ?>/logos/Untitled%20design%20(73).png\""),
    
    # JS String Replacements (Note: quotes must exact match the JS code)
    ("src = 'logos/Untitled%20design%20(72).png'", "src = '<?php echo get_template_directory_uri(); ?>/logos/Untitled%20design%20(72).png'"),
    ("src = 'logos/Untitled%20design%20(73).png'", "src = '<?php echo get_template_directory_uri(); ?>/logos/Untitled%20design%20(73).png'"),
    ("src=\"Untitled design (1).mp4\"", "src=\"<?php echo get_template_directory_uri(); ?>/Untitled design (1).mp4\""),
    ("'new bridge/bridge_lines_color_' + i + '.jpg'", "'<?php echo get_template_directory_uri(); ?>/new bridge/bridge_lines_color_' + i + '.jpg'")
]

for old, new in replacements:
    content = content.replace(old, new)
    
# Ensure generic string replacing for JS just in case spaces were different
content = content.replace("'logos/Untitled%20design%20(72).png'", "'<?php echo get_template_directory_uri(); ?>/logos/Untitled%20design%20(72).png'")
content = content.replace("'logos/Untitled%20design%20(73).png'", "'<?php echo get_template_directory_uri(); ?>/logos/Untitled%20design%20(73).png'")

# Add WordPress hooks
content = content.replace('</head>', '<?php wp_head(); ?>\n</head>')
content = content.replace('</body>', '<?php wp_footer(); ?>\n</body>')

with open(os.path.join(theme_dir, 'index.php'), 'w') as f:
    f.write(content)

# 3. Copy assets
assets = ['LinotypeAperto-Roman.ttf', 'FINNEWS (1).jpg', 'Untitled design (1).mp4', 'logos', 'new bridge']
for asset in assets:
    if os.path.exists(asset):
        if os.path.isdir(asset):
            shutil.copytree(asset, os.path.join(theme_dir, asset), dirs_exist_ok=True)
        else:
            shutil.copy2(asset, theme_dir)

# 4. Zip the theme
shutil.make_archive('alba-theme', 'zip', theme_dir)
print("Theme alba-theme.zip created successfully!")
