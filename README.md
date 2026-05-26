# ΚΔΗΦ Καλαμάτα – Ο Κήπος της Λυσούς
## Ιστότοπος – Οδηγίες Επεξεργασίας

---

## Δομή Αρχείων

```
kipos_website/
├── index.html          → Αρχική σελίδα
├── programs.html       → Τα Προγράμματά μας
├── about.html          → Ποιοι Είμαστε
├── news.html           → Δράσεις & Νέα
├── support.html        → Στηρίξτε μας
├── contact.html        → Επικοινωνία
├── css/
│   └── kdif.css        → Κύριο stylesheet
├── js/
│   └── kdif.js         → Κύριο JavaScript
├── Logos/              → Λογότυπα
└── Photos/             → Φωτογραφίες & Βίντεο
```

---

## Πώς να Επεξεργαστείτε το Περιεχόμενο

### 1. Αλλαγή Αριθμών (Impact Stats)

Στο `index.html`, βρείτε:
```html
<div class="stat-value" data-target="87" data-suffix="+">0</div>
```
Αλλάξτε το `data-target` στον επιθυμητό αριθμό. Το `data-suffix` προσθέτει ένα suffix (π.χ. "+").

### 2. Προσθήκη Νέου Photo στο Hero

Στο `index.html`, βρείτε:
```html
<div class="hero-slider">
  <div class="hero-slide active" style="background-image:url('Photos/ΦΩΤΟ.jpg')"></div>
  ...
```
Προσθέστε νέο `<div class="hero-slide" ...>` και αντίστοιχο `<button class="hero-dot" ...>`.

### 3. Προσθήκη Νέας Δράσης (News)

Στο `news.html`, αντιγράψτε ένα `<article class="news-card">` και αλλάξτε:
- `data-category`: `parastasi` | `erasmus` | `sxoleio` | `ergastirio` | `erevna`
- Φωτογραφία, τίτλο, ημερομηνία, περίληψη

### 4. Ενημέρωση Στοιχείων Επικοινωνίας

Αναζητήστε `+30 27210 XXXXX` σε όλα τα αρχεία και αντικαταστήστε με τον πραγματικό αριθμό.
Αναζητήστε `info@kdif-kalamata.gr` για το email.

### 5. Ενημέρωση Google Maps

Στο `contact.html`, αντικαταστήστε το `src` του `<iframe>` με τον σωστό embed link από:
1. Ανοίξτε το Google Maps
2. Βρείτε τη Μεγάλη Μαντίνεια
3. Κάντε κλικ "Share" → "Embed a map"
4. Αντιγράψτε τον κώδικα iframe

### 6. Προσθήκη Μέλους Ομάδας

Στο `about.html`, βρείτε το `<div class="team-grid">` και προσθέστε:
```html
<div class="team-card">
  <img src="Photos/ΟΝΟΜΑ_ΦΩΤΟ.jpg" alt="Όνομα" class="team-photo" loading="lazy">
  <div class="team-info">
    <h4>Ονοματεπώνυμο</h4>
    <p>Τίτλος / Ρόλος</p>
  </div>
</div>
```

### 7. Google Analytics

Στο κάθε HTML αρχείο, βρείτε:
```html
<!-- <script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script> -->
```
Αφαιρέστε τα σχόλια και αντικαταστήστε `GA_TRACKING_ID` με το ID σας.

---

## Χρωματική Παλέτα

| Χρώμα | Hex | Χρήση |
|-------|-----|-------|
| Primary Blue | `#1E88E5` | Headers, links, CTAs |
| Dark Blue | `#1565C0` | Hover states |
| Secondary Orange | `#FF6F00` | CTAs, badges |
| Accent Green | `#66BB6A` | Nature, success |
| Light Gray | `#F5F5F5` | Backgrounds |
| Dark Gray | `#424242` | Text |

---

## Phase 2 - Μελλοντικές Δυνατότητες

- [ ] Blog με CMS για "Δράσεις & Νέα"
- [ ] Blockchain transparency page με live data
- [ ] CRM platform integration (parents' portal)
- [ ] Multilingual υποστήριξη (Αγγλικά)
- [ ] Event calendar για παραστάσεις/workshops
- [ ] Photo/video galleries με lightbox
- [ ] Backend για forms (email delivery)
- [ ] PayPal/Stripe integration για δωρεές

---

## Τεχνολογίες

- **HTML5** – Semantic markup, WCAG AA accessibility
- **Vanilla CSS** – Custom design system, CSS variables
- **Vanilla JavaScript** – No frameworks, no dependencies
- **Font Awesome 6.4** – Icons
- **Google Fonts** – Montserrat + Open Sans

---

*Για τεχνική υποστήριξη ή ερωτήσεις σχετικά με τον κώδικα, επικοινωνήστε με την ομάδα ανάπτυξης.*
