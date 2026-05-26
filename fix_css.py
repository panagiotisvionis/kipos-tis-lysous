import re

with open('css/kdif.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Glows
glow_css = """
/* ══════════════════════════════════════════════════════════
   AMBIENT GLOWS & BENTO CARDS
   ══════════════════════════════════════════════════════════ */
.ambient-glow {
  position: absolute;
  width: 60vw; height: 60vw;
  background: radial-gradient(circle, rgba(91, 37, 137, 0.08) 0%, rgba(248, 152, 29, 0.03) 50%, transparent 80%);
  border-radius: 50%;
  filter: blur(80px);
  z-index: 0; pointer-events: none;
  animation: floatAmbient 10s ease-in-out infinite alternate;
}
@keyframes floatAmbient {
  0% { transform: translate(0, 0) scale(1); }
  100% { transform: translate(5%, 5%) scale(1.1); }
}

"""

# Add glowing CSS before SECTIONS
css = css.replace("/* ══════════════════════════════════════════════════════════\n   SECTIONS & CARDS", glow_css + "/* ══════════════════════════════════════════════════════════\n   SECTIONS & CARDS")


# Redesign room-card for images and bento
cards_old = """
.rooms-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(400px, 1fr)); gap: 4rem; }
.room-card { 
  background: var(--white); padding: 4rem; border-radius: var(--radius-md); 
  box-shadow: var(--shadow-sm); border-bottom: 8px solid var(--secondary); transition: var(--transition);
  position: relative; overflow: hidden;
}
.room-card::after {
  content: ''; position: absolute; top: 0; right: 0; width: 80px; height: 80px; background: var(--secondary);
  opacity: 0.05; border-radius: 0 0 0 100%; transition: var(--transition);
}
.room-card:hover { transform: translateY(-20px); box-shadow: var(--shadow-lg); }
.room-card:hover::after { width: 120px; height: 120px; opacity: 0.1; }

.room-emoji { font-size: 4rem; margin-bottom: 2.5rem; display: block; filter: drop-shadow(0 5px 15px rgba(0,0,0,0.1)); }
.room-name { font-size: 1.8rem; margin-bottom: 1rem; color: var(--primary); }
.room-teacher { font-size: 0.85rem; font-weight: 900; text-transform: uppercase; color: var(--secondary); margin-bottom: 1.5rem; letter-spacing: 1.5px; }
"""

cards_new = """
.rooms-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); 
  gap: 2.5rem; 
  position: relative; z-index: 1;
}

/* Base Card (White Mode) */
.room-card { 
  background: var(--white); 
  padding: 3rem; 
  border-radius: 30px; 
  box-shadow: var(--shadow-md); 
  border-bottom: 5px solid var(--secondary); 
  transition: all 0.6s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative; overflow: hidden;
  display: flex; flex-direction: column; justify-content: flex-end;
  min-height: 380px;
  transform-style: preserve-3d;
  will-change: transform;
}
.room-card::after {
  content: ''; position: absolute; top: -50px; right: -50px; width: 150px; height: 150px; background: var(--secondary);
  opacity: 0.03; border-radius: 50%; transition: var(--transition);
}

/* Image Card (Dark Photo Mode) */
.room-card.has-image {
  background-size: cover;
  background-position: center;
  border-bottom: none;
  border-radius: 30px;
  color: white;
}
.room-card.has-image::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(16,44,87, 0.95) 0%, rgba(16,44,87, 0.4) 50%, rgba(16,44,87, 0.1) 100%);
  transition: var(--transition);
  z-index: 1;
}
.room-card.has-image > * { position: relative; z-index: 2; }
.room-card.has-image .room-name { color: white; text-shadow: 0 2px 10px rgba(0,0,0,0.5); }
.room-card.has-image .room-teacher { color: var(--secondary-light); }
.room-card.has-image .room-desc, .room-card.has-image ul { color: rgba(255,255,255,0.9); }

/* Hover Effects */
.room-card:hover { 
  transform: translateY(-15px) scale(1.02); 
  box-shadow: 0 30px 60px rgba(16, 44, 87, 0.15); 
}
.room-card.has-image:hover::before {
  background: linear-gradient(to top, rgba(91, 37, 137, 0.95) 0%, rgba(91, 37, 137, 0.3) 60%, rgba(0,0,0, 0) 100%);
}
.room-card:hover::after { transform: scale(1.5) translate(-10px, 10px); opacity: 0.06; }

.room-emoji { 
  font-size: 3.5rem; margin-bottom: auto; 
  display: block; filter: drop-shadow(0 5px 15px rgba(0,0,0,0.1)); 
  transition: var(--transition);
}
.room-card:hover .room-emoji { transform: scale(1.1) rotate(5deg); }

.room-name { font-size: 1.8rem; margin-bottom: 0.5rem; color: var(--primary); transition: var(--transition); line-height: 1.1; }
.room-teacher { font-size: 0.8rem; font-weight: 900; text-transform: uppercase; color: var(--secondary); margin-bottom: 1rem; letter-spacing: 2px; }

/* Enhanced Team Image Reveal */
.team-member-img {
  height: 350px; width: 100%; object-fit: cover;
  transition: all 0.8s cubic-bezier(0.24, 1, 0.32, 1);
  filter: grayscale(100%) contrast(1.1);
}
.team-card {
  background: white; border-radius: 30px; overflow: hidden; 
  box-shadow: var(--shadow-md); position: relative;
  transition: all 0.6s ease;
}
.team-card:hover { transform: translateY(-15px); box-shadow: var(--shadow-lg); }
.team-card:hover .team-member-img { filter: grayscale(0%) contrast(1.05); transform: scale(1.05); }

/* Animated Buttons */
.btn {
  position: relative; overflow: hidden;
  z-index: 1;
}
.btn::before {
  content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
  transition: 0.5s; z-index: -1;
}
.btn:hover::before { left: 100%; }

/* Text Reveal Animation Prep */
.text-reveal { display: inline-block; overflow: hidden; }
.text-reveal span { display: inline-block; transform: translateY(100%); transition: transform 0.8s cubic-bezier(0.24, 1, 0.32, 1); }
.text-reveal.visible span { transform: translateY(0); }

"""

# It's safer to use regex to replace the section and cards.
import re
css = re.sub(r'\.rooms-grid {.*?\.room-teacher {.*?}', cards_new, css, flags=re.DOTALL)

with open('css/kdif.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS Overhauled!")
