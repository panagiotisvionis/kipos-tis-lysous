with open('js/kdif.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Completely remove the TEXT REVEAL logic
import re
js = re.sub(r'// ══════════════════════════════════════════════════════════\s*// TEXT REVEAL ANIMATION.*?function startCounter\(el\)', 'function startCounter(el)', js, flags=re.DOTALL)

with open('js/kdif.js', 'w', encoding='utf-8') as f:
    f.write(js)
    
print("Fixed kdif.js text-reveal conflict.")
