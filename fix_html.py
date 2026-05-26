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

for file in glob.glob("*.html"):
    if file == 'index.html': continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace everything from <!-- ══ HEADER (or <header id="site-header">)
    # until <div class="page-hero (or whatever follows the nav overlay).
    
    # Find start of header
    s1 = content.find('<!-- ══ HEADER')
    if s1 == -1: s1 = content.find('<header id="site-header">')
    
    # Find start of the next main section, usually <div class="page-hero" or similar.
    # It might have been <!-- ══ STORY SECTION
    s2 = content.find('<div class="page-hero')
    if s2 == -1: s2 = content.find('<!-- ══ STORY SECTION')
    if s2 == -1: s2 = content.find('<section style="padding: 100px 0;">')
    if s2 == -1: s2 = content.find('<!-- ══ GALLERY SECTION')
    if s2 == -1: s2 = content.find('<!-- ══ CONTACT SECTION')
    if s2 == -1: s2 = content.find('<!-- ══ DONATION SECTION')
        
    print(f"{file} s1={s1} s2={s2}")
    
    if s1 != -1 and s2 != -1:
        new_content = content[:s1] + header_block + '\n\n  ' + nav_block + content[s2:]
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
    else:
        print(f"Skipped {file} due to bounds not found.")

