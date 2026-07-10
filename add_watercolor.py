with open('index.html', 'r') as f:
    content = f.read()

# Add the CSS for watercolor-reveal
css_block = """
    <style>
        .watercolor-reveal {
            opacity: 0;
            filter: grayscale(100%) blur(15px) contrast(150%);
            clip-path: inset(10% 10% 10% 10%);
            transform: scale(1.05);
            transition: opacity 2s cubic-bezier(0.4, 0, 0.2, 1), 
                        filter 2.5s cubic-bezier(0.4, 0, 0.2, 1),
                        clip-path 2.5s cubic-bezier(0.4, 0, 0.2, 1),
                        transform 3s cubic-bezier(0.2, 0.8, 0.2, 1);
        }
        .watercolor-reveal.visible {
            opacity: 1;
            filter: grayscale(0%) blur(0px) contrast(100%);
            clip-path: inset(0% 0% 0% 0%);
            transform: scale(1);
        }
    </style>
"""

# Inject before </head> or just anywhere in body
if "<style>" in content:
    content = content.replace("<style>", css_block + "<style>", 1)

# Replace fade-up with watercolor-reveal on those two images
import re
content = re.sub(
    r'<img src="jet deau.jpeg" class="fade-up" alt="Jet d\'Eau Geneva"',
    r'<img src="jet deau.jpeg" class="watercolor-reveal" alt="Jet d\'Eau Geneva"',
    content
)

content = re.sub(
    r'<img src="cathedral.jpeg" class="fade-up" alt="Cathedral"',
    r'<img src="cathedral.jpeg" class="watercolor-reveal" alt="Cathedral"',
    content
)

with open('index.html', 'w') as f:
    f.write(content)
print("Updated index.html with watercolor effect.")
