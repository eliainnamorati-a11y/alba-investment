with open('our-people.html', 'r') as f:
    content = f.read()

# Replace the broken Stefano block
import re

pattern = r"(<a href=\"stefano-tittarelli.html\" style=\"display: flex; flex-direction: column; cursor: pointer; text-decoration: none; color: inherit;\" class=\"team-card fade-up\">\n\s*<div.*?)</div>\n\s*<h3"
# Actually easier: just replace the block.
# I'll just write a specific replacement script.
