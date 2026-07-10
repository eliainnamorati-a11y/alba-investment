import re

with open('investment-approach.html', 'r') as f:
    content = f.read()

pattern = r"    <!-- Applied Strategy Section -->.*?    <!-- Stay Informed Section -->"
match = re.search(pattern, content, flags=re.DOTALL)
if match:
    new_content = content[:match.start()] + "    <!-- Stay Informed Section -->" + content[match.end():]
    with open('investment-approach.html', 'w') as f:
        f.write(new_content)
    print("Deleted 'Strategy Application' and orphaned 'Components' block.")
else:
    print("Could not find the block.")
