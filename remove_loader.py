import glob
from bs4 import BeautifulSoup

for file in glob.glob("*.html"):
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    loader = soup.find('div', id='loader')
    if loader:
        loader.decompose()
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
print("Removed loader from all files.")
