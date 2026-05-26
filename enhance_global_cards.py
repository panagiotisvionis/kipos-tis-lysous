from bs4 import BeautifulSoup
import glob

# Random thematic photos for cards
value_photos = ['20251121_114158.jpg', '20251004_143011.jpg', '20251004_143119.jpg']
eu_photos = ['20251121_120027.jpg', '20251121_104434.jpg', '20251216_103726.jpg']

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

cards = soup.find_all('div', class_='room-card')
# In index.html, there are 6 room-cards (3 values, 3 EU)
for i, card in enumerate(cards):
    card['class'] = card.get('class', []) + ['has-image']
    if i < 3:
        photo = value_photos[i % len(value_photos)]
    else:
        photo = eu_photos[i % len(eu_photos)]
    
    card['style'] = f"background-image: url('Photos/{photo}');"
    # Remove any messy inline styles like background, border-bottom
    existing_style = card.get('style', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Global cards upgraded on index.html!")
