with open('index.html', 'r') as f:
    content = f.read()

content = content.replace("document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));", 
                          "document.querySelectorAll('.fade-up, .watercolor-reveal').forEach(el => observer.observe(el));")

content = content.replace(".watercolor-reveal.visible", ".watercolor-reveal.in-view")

with open('index.html', 'w') as f:
    f.write(content)
print("Observer updated")
