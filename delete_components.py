import re

with open('investment-approach.html', 'r') as f:
    content = f.read()

pattern = r"        <div class=\"bond-components-wrap fade-up\".*?        </div>\n"
match = re.search(pattern, content, flags=re.DOTALL)
if match:
    new_content = content[:match.start()] + content[match.end():]
    with open('investment-approach.html', 'w') as f:
        f.write(new_content)
    print("Deleted 'Components of a Bond' section.")
else:
    print("Could not find the section.")
