import re
from bs4 import BeautifulSoup

# 1. Enhance about.html (Team section)
with open('about.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Team cards have <div style="background: white; border-radius: 20px...
for div in soup.find_all('div', style=lambda v: v and 'border-radius: 20px' in v and 'background: white' in v):
    div['class'] = div.get('class', []) + ['team-card']
    del div['style'] # Remove the messy inline styles
    img = div.find('img')
    if img:
        img['class'] = img.get('class', []) + ['team-member-img']
        if 'style' in img.attrs:
            del img['style']

# Inject ambient glows
section = soup.find('section', class_='section')
if section:
    glow = soup.new_tag('div', **{'class': 'ambient-glow'})
    glow['style'] = "top: 20%; left: -10%;"
    section.insert(0, glow)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))


# 2. Enhance programs.html (Cards with background images)
with open('programs.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

photos = [
    '20251121_114422.jpg', # Ceramics
    '20251210_102828.jpg', # Music
    '20251216_103659.jpg', # Occ Therapy
    '20251119_100531.jpg', # Independent
    '20251121_120027.jpg', # Digital
    '20251126_113442.jpg', # Physical
    '20251004_143033.jpg'  # Gardening
]

cards = soup.find_all('div', class_='room-card')
for i, card in enumerate(cards):
    card['class'] = card.get('class', []) + ['has-image']
    card['style'] = f"background-image: url('Photos/{photos[i % len(photos)]}');"
    # Remove inline style if any
    if 'border-bottom-color' in card.get('style', ''):
        pass # actually it's overridden anyway
        
    span = card.find('span', class_='room-emoji')
    if span:
        # Move span above the name
        pass # It's already there

with open('programs.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))


# 3. Enhance index.html (Similar tweaks)
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

glow1 = soup.new_tag('div', **{'class': 'ambient-glow'})
glow1['style'] = "bottom: -20%; right: -20%; transform: scale(1.5);"
soup.body.insert(0, glow1)

# News cards
for div in soup.find_all('div', style=lambda v: v and 'border-radius: 20px' in v and 'background: white' in v):
    div['class'] = div.get('class', []) + ['team-card']
    del div['style']
    img = div.find('img')
    if img:
        img['class'] = img.get('class', []) + ['team-member-img']
        if 'style' in img.attrs:
            del img['style']

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("HTML Enhanced!")
