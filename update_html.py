import glob
import re

# Read the template components from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

header_match = re.search(r'<!-- ══ HEADER \(Premium Purple \+ Orange\) ══ -->(.*?)</header>', index_content, re.DOTALL)
if header_match:
    header_content = header_match.group(0)
else:
    print("Could not find new header in index.html")
    exit(1)

nav_match = re.search(r'<!-- ══ NAV OVERLAY ══ -->(.*?)<!-- ══', index_content, re.DOTALL)
if nav_match:
    nav_content = nav_match.group(0)[:-8] # remove the next section comment start
else:
    print("Could not find new nav overlay in index.html")
    exit(1)


for filename in glob.glob('*.html'):
    if filename == 'index.html':
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace old header
    content = re.sub(r'<header id="site-header">.*?</header>', header_content, content, flags=re.DOTALL)
    # Also replace if it had the comment
    content = re.sub(r'<!-- ══ HEADER .*?══ -->\s*<header id="site-header">.*?</header>', header_content, content, flags=re.DOTALL)
    
    # Replace old nav overlay
    content = re.sub(r'<div class="nav-overlay" id="nav-overlay">.*?<!-- ══', nav_content + '\n\n  <!-- ══', content, flags=re.DOTALL)
    content = re.sub(r'<!-- ══ NAV OVERLAY ══ -->\s*<div class="nav-overlay" id="nav-overlay">.*?(<(div|section|!-- ══|header class="page-hero))', r'<!-- ══ NAV OVERLAY ══ -->\n  ' + nav_content.split('<!-- ══ NAV OVERLAY ══ -->')[1].strip() + r'\n\n  \1', content, flags=re.DOTALL)

    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated all HTML files.")
