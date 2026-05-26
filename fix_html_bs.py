import glob
from bs4 import BeautifulSoup
import copy

with open('index.html', 'r', encoding='utf-8') as f:
    idx = BeautifulSoup(f, 'html.parser')
    
header_node = idx.find('header', {'id': 'site-header'})
nav_node = idx.find('div', {'id': 'nav-overlay'})

for file in glob.glob('*.html'):
    if file == 'index.html': continue
    
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    # Replace header
    old_h = soup.find('header', {'id': 'site-header'})
    if old_h:
        old_h.replace_with(copy.copy(header_node))
        
    # Find all nav-overlay elements. Some files might have multiple due to bad scripts.
    navs = soup.find_all('div', class_='nav-overlay')
    if navs:
        for i, n in enumerate(navs):
            if i == 0:
                n.replace_with(copy.copy(nav_node))
            else:
                n.decompose()
    
    # Also look for trailing nav-overlay-top fragments that got detached
    fragments = soup.find_all('div', class_='nav-overlay-top')
    for f in fragments:
        if not f.find_parent('div', id='nav-overlay'):
            f.decompose() # kill the orphaned tops
            
    # Remove any extra overlay nav blocks
    fragments2 = soup.find_all('nav', class_='overlay-nav')
    for f in fragments2:
        if not f.find_parent('div', id='nav-overlay'):
            f.decompose()

    fragments3 = soup.find_all('div', class_='nav-overlay-footer')
    for f in fragments3:
        if not f.find_parent('div', id='nav-overlay'):
            f.decompose()
            
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("Successfully fixed all HTML files using BS4.")
