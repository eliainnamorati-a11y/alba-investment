import re
import shutil

# Copy Guillaume's page as a template
shutil.copy('guillaume-di-liberatore.html', 'nicolas-el-alam.html')

with open('nicolas-el-alam.html', 'r') as f:
    content = f.read()

# Replace references to Guillaume with Nicolas
content = content.replace('Guillaume Di Liberatore', 'Nicolas El Alam')
content = content.replace('Guillaume', 'Nicolas')
# His title is unknown, let's use "Team Member" instead of Chief Research Officer
content = content.replace('Chief Research Officer', 'Team Member')

# Replace the image src
img_pattern = r"<img src=\"[^\"]+\" alt=\"Nicolas El Alam, CFA\""
# Actually he probably doesn't have CFA since the user didn't specify. I'll just remove CFA.
content = content.replace(', CFA', '')
content = re.sub(r"<img src=\"[^\"]+\" alt=\"Nicolas El Alam\"", r'<img src="Nicolas El Alam.png" alt="Nicolas El Alam"', content)
# Also fix any other references.

with open('nicolas-el-alam.html', 'w') as f:
    f.write(content)
print("Created nicolas-el-alam.html")
