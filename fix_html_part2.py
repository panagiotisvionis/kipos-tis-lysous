import glob
import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Get the exact correct header
h_start = text.find('<!-- ══ HEADER ')
h_end = text.find('</header>') + len('</header>')
header_block = text[h_start:h_end]

# Get the exact correct overlay
n_start = text.find('<!-- ══ NAV OVERLAY ══ -->')
n_end = text.find('<!-- ══ PAGE HERO / BLURRED BACKGROUND ══ -->')
nav_block = text[n_start:n_end]

skipped = ['services.html', 'gallery.html', 'contact.html', 'collaborations.html']

for file in skipped:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex replace the header
    content = re.sub(r'<!-- ══ HEADER .*?</header>', header_block, content, flags=re.DOTALL)
    content = re.sub(r'<header id="site-header">.*?</header>', header_block, content, flags=re.DOTALL)
    
    # regex replace the nav overlay
    # Find matching </div> for nav-overlay
    s1 = content.find('<div class="nav-overlay" id="nav-overlay">')
    
    # to find matching div, we can just replace until the next <div class="page-hero" or similar.
    # Let's peek into the file to see what's after nav overlay.
    print(f"fixing {file}")
    content = re.sub(r'<!-- ══ NAV OVERLAY ══ -->.*?<div class="page-hero', nav_block + '<div class="page-hero', content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print("Done")
