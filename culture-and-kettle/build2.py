import os

BASE = r"C:\Users\tweaver\.kiro\culture-and-kettle"

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>{title} | Culture &amp; Kettle</title>
  <link rel="stylesheet" href="style.css"/>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
</head>
<body>
"""

NAV = """<nav class="nav">
  <div class="nav-inner">
    <a href="index.html" class="nav-logo"><span class="logo-symbol">&#9651;</span> Culture &amp; Kettle</a>
    <ul class="nav-links">
      <li><a href="index.html">Home</a></li>
      <li><a href="shop.html">Shop</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="locations.html">Locations</a></li>
    </ul>
    <div class="nav-actions">
      <a href="cart.html" class="cart-icon" aria-label="View cart">&#128722;<span class="cart-count" id="cart-count">0</span></a>
      <a href="shop.html" class="btn btn-gold" style="font-size:.75rem;padding:.5rem 1.2rem;">Shop Now</a>
    </div>
    <button class="nav-toggle" aria-label="Toggle menu">&#9776;</button>
  </div>
</nav>
"""

FOOTER = """<footer>
  <div class="footer-inner">
    <div class="footer-brand">
      <div style="font-family:'Playfair Display',serif;font-size:1.2rem;color:#F5EDD6;display:flex;align-items:center;gap:.5rem;"><span style="color:#C9A84C;">&#9651;</span> Culture &amp; Kettle</div>
      <p>Specialty coffee roasted with intention. Every bag tells a story.</p>
    </div>
    <div class="footer-col"><h4>Shop</h4><ul><li><a href="shop.html">All Coffee</a></li><li><a href="shop.html">Light Roast</a></li><li><a href="shop.html">Medium Roast</a></li><li><a href="shop.html">Dark Roast</a></li><li><a href="shop.html">Merch</a></li></ul></div>
    <div class="footer-col"><h4>Company</h4><ul><li><a href="about.html">Our Story</a></li><li><a href="locations.html">Locations</a></li><li><a href="#">Wholesale</a></li><li><a href="#">Careers</a></li></ul></div>
    <div class="footer-col"><h4>Support</h4><ul><li><a href="#">FAQ</a></li><li><a href="#">Shipping</a></li><li><a href="#">Returns</a></li><li><a href="#">Contact</a></li></ul></div>
  </div>
  <div class="footer-bottom"><span>&copy; 2026 Culture &amp; Kettle. All rights reserved.</span><span>Roasted with intention.</span></div>
</footer>
<script src="cart.js"></script>
</body></html>
"""

# ─── shop.html ───────────────────────────────────────────────────────────────
shop = HEAD.format(title="Shop") + NAV + """
<div class="page-hero">
  <div class="page-hero-inner">
    <h1>The Shop</h1>
    <p>Every roast has a reason.</p>
  </div>
</div>

<section class="section">
  <div class="section-inner">
    <div class="filter-bar">
      <button class="filter-btn active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="light">Light Roast</button>
      <button class="filter-btn" data-filter="medium">Medium Roast</button>
      <button class="filter-btn" data-filter="dark">Dark Roast</button>
      <button class="filter-btn" data-filter="merch">Merch</button>
    </div>
    <div class="products-grid">

      <div class="product-card" data-category="light">
        <a href="product.html?id=first-watch" class="product-card-visual light-bg">
          <span class="product-icon">&#9728;</span>
        </a>
        <div class="product-card-body">
          <span class="product-tag">Light Roast</span>
          <h3><a href="product.html?id=first-watch">First Watch</a></h3>
          <p class="product-desc">Bright, citrus-forward, clean.</p>
          <div class="product-footer">
            <span class="product-price">$18.00</span>
            <button class="btn btn-gold btn-sm" onclick="addToCart('first-watch','First Watch',18.00,'&#9728;','light-bg')">Add to Cart</button>
          </div>
        </div>
      </div>

      <div class="product-card" data-category="medium">
        <a href="product.html?id=late-checkout" class="product-card-visual medium-bg">
          <span class="product-icon">&#128682;</span>
        </a>
        <div class="product-card-body">
          <span class="product-tag">Medium Roast</span>
          <h3><a href="product.html?id=late-checkout">Late Checkout</a></h3>
          <p class="product-desc">Smooth, balanced, unhurried.</p>
          <div class="product-footer">
            <span class="product-price">$18.00</span>
            <button class="btn btn-gold btn-sm" onclick="addToCart('late-checkout','Late Checkout',18.00,'&#128682;','medium-bg')">Add to Cart</button>
          </div>
        </div>
      </div>

      <div class="product-card" data-category="dark">
        <a href="product.html?id=full-moon" class="product-card-visual dark-bg">
          <span class="product-icon">&#127765;</span>
        </a>
        <div class="product-card-body">
          <span class="product-tag">Dark Roast</span>
          <h3><a href="product.html?id=full-moon">Full Moon</a></h3>
          <p class="product-desc">Bold, smoky, deeply satisfying.</p>
          <div class="product-footer">
            <span class="product-price">$18.00</span>
            <button class="btn btn-gold btn-sm" onclick="addToCart('full-moon','Full Moon',18.00,'&#127765;','dark-bg')">Add to Cart</button>
          </div>
        </div>
      </div>

      <div class="product-card" data-category="medium">
        <a href="product.html?id=the-ritual" class="product-card-visual medium-bg">
          <span class="product-icon">&#9749;</span>
        </a>
        <div class="product-card-body">
          <span class="product-tag">Espresso Blend</span>
          <h3><a href="product.html?id=the-ritual">The Ritual</a></h3>
          <p class="product-desc">Concentrated. Intentional. Yours.</p>
          <div class="product-footer">
            <span class="product-price">$20.00</span>
            <button class="btn btn-gold btn-sm" onclick="addToCart('the-ritual','The Ritual',20.00,'&#9749;','medium-bg')">Add to Cart</button>
          </div>
        </div>
      </div>

      <div class="product-card" data-category="light">
        <a href="product.html?id=harvest-season" class="product-card-visual light-bg">
          <span class="product-icon">&#127810;</span>
        </a>
        <div class="product-card-body">
          <span class="product-tag">Seasonal Blend</span>
          <h3><a href="product.html?id=harvest-season">Harvest Season</a></h3>
          <p class="product-desc">Limited. Warm. Worth the wait.</p>
          <div class="product-footer">
            <span class="product-price">$22.00</span>
            <button class="btn btn-gold btn-sm" onclick="addToCart('harvest-season','Harvest Season',22.00,'&#127810;','light-bg')">Add to Cart</button>
          </div>
        </div>
      </div>

      <div class="product-card" data-category="merch">
        <a href="product.html?id=ck-mug" class="product-card-visual merch-bg">
          <span class="product-icon">&#9749;</span>
        </a>
        <div class="product-card-body">
          <span class="product-tag">Merch</span>
          <h3><a href="product.html?id=ck-mug">C&amp;K Mug</a></h3>
          <p class="product-desc">12oz ceramic. Logo embossed in gold.</p>
          <div class="product-footer">
            <span class="product-price">$24.00</span>
            <button class="btn btn-gold btn-sm" onclick="addToCart('ck-mug','C&amp;K Mug',24.00,'&#9749;','merch-bg')">Add to Cart</button>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>
<script>
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const filter = btn.dataset.filter;
      document.querySelectorAll('.product-card').forEach(card => {
        card.style.display = (filter === 'all' || card.dataset.category === filter) ? '' : 'none';
      });
    });
  });
</script>
""" + FOOTER

with open(os.path.join(BASE, "shop.html"), "w", encoding="utf-8") as f:
    f.write(shop)
print("Written: shop.html")

# ─── product.html ────────────────────────────────────────────────────────────
product = HEAD.format(title="Product") + NAV + """
<div class="page-hero">
  <div class="page-hero-inner">
    <h1 id="product-page-title">Loading...</h1>
    <p id="product-page-tag"></p>
  </div>
</div>

<section class="section">
  <div class="section-inner">
    <div class="product-detail">
      <div class="product-detail-visual" id="product-visual">
        <span class="product-detail-icon" id="product-icon"></span>
      </div>
      <div class="product-detail-info">
        <span class="product-tag" id="product-tag"></span>
        <h1 id="product-name"></h1>
        <p class="product-tagline" id="product-tagline"></p>
        <p class="product-desc-full" id="product-desc"></p>
        <div class="product-price-row">
          <span class="product-price-large" id="product-price"></span>
        </div>
        <div class="option-group">
          <p class="option-label">Grind</p>
          <div class="option-btns">
            <button class="option-btn active" data-grind="Whole Bean">Whole Bean</button>
            <button class="option-btn" data-grind="Medium Grind">Medium Grind</button>
            <button class="option-btn" data-grind="Fine Grind">Fine Grind</button>
          </div>
        </div>
        <div class="qty-row">
          <p class="option-label">Quantity</p>
          <div class="qty-selector">
            <button class="qty-btn" id="qty-minus">&#8722;</button>
            <span class="qty-display" id="qty-display">1</span>
            <button class="qty-btn" id="qty-plus">&#43;</button>
          </div>
        </div>
        <button class="btn btn-gold btn-full" id="add-to-cart-btn">Add to Cart</button>
        <ul class="product-notes">
          <li>&#9679; Ethically sourced</li>
          <li>&#9679; Roasted to order</li>
          <li>&#9679; Free shipping over $40</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<script>
const products = {
  'first-watch': { name:'First Watch', tag:'Light Roast \u00b7 12 oz', tagline:'Fuel for what\'s ahead.', price:'18.00', icon:'\u2600', bg:'light-bg', desc:'A bright, citrus-forward light roast with notes of lemon zest, jasmine, and stone fruit. Sourced from high-altitude farms in Ethiopia, roasted light to preserve every delicate layer.' },
  'late-checkout': { name:'Late Checkout', tag:'Medium Roast \u00b7 12 oz', tagline:'Ease into the moment.', price:'18.00', icon:'\u25A1', bg:'medium-bg', desc:'A smooth, balanced medium roast with notes of milk chocolate, toasted hazelnut, and a hint of caramel. The kind of cup you linger over.' },
  'full-moon': { name:'Full Moon', tag:'Dark Roast \u00b7 12 oz', tagline:'Wind down. Take it in.', price:'18.00', icon:'\u25CF', bg:'dark-bg', desc:'A bold, full-bodied dark roast with deep notes of dark chocolate, cedar, and a long smoky finish. Best enjoyed slowly, in the quiet.' },
  'the-ritual': { name:'The Ritual', tag:'Espresso Blend \u00b7 12 oz', tagline:'Concentrated. Intentional. Yours.', price:'20.00', icon:'\u2615', bg:'medium-bg', desc:'A precision espresso blend built for clarity and crema. Notes of brown sugar, dried cherry, and bittersweet cocoa. Pull a shot or pour it long.' },
  'harvest-season': { name:'Harvest Season', tag:'Seasonal Blend \u00b7 12 oz', tagline:'Limited. Warm. Worth the wait.', price:'22.00', icon:'\u2767', bg:'light-bg', desc:'Our limited seasonal release. This year\'s harvest brings notes of cinnamon, dried fig, and warm spice. Once it\'s gone, it\'s gone.' },
  'ck-mug': { name:'C&K Mug', tag:'Merch \u00b7 12 oz Ceramic', tagline:'Your ritual deserves the right vessel.', price:'24.00', icon:'\u2615', bg:'merch-bg', desc:'A 12oz ceramic mug with the Culture & Kettle triangle logo embossed in gold. Dishwasher safe. Microwave safe. Vibe-safe.' }
};

const params = new URLSearchParams(window.location.search);
const id = params.get('id') || 'first-watch';
const p = products[id] || products['first-watch'];

document.getElementById('product-page-title').textContent = p.name;
document.getElementById('product-page-tag').textContent = p.tag;
document.getElementById('product-tag').textContent = p.tag;
document.getElementById('product-name').textContent = p.name;
document.getElementById('product-tagline').textContent = p.tagline;
document.getElementById('product-desc').textContent = p.desc;
document.getElementById('product-price').textContent = '$' + p.price;
document.getElementById('product-icon').textContent = p.icon;
document.getElementById('product-visual').className = 'product-detail-visual ' + p.bg;

let qty = 1;
let grind = 'Whole Bean';

document.getElementById('qty-minus').addEventListener('click', () => {
  if (qty > 1) { qty--; document.getElementById('qty-display').textContent = qty; }
});
document.getElementById('qty-plus').addEventListener('click', () => {
  qty++; document.getElementById('qty-display').textContent = qty;
});

document.querySelectorAll('.option-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.option-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    grind = btn.dataset.grind;
  });
});

document.getElementById('add-to-cart-btn').addEventListener('click', () => {
  for (let i = 0; i < qty; i++) {
    addToCart(id, p.name, parseFloat(p.price), p.icon, p.bg, grind);
  }
});
</script>
""" + FOOTER

with open(os.path.join(BASE, "product.html"), "w", encoding="utf-8") as f:
    f.write(product)
print("Written: product.html")

# ─── cart.html ───────────────────────────────────────────────────────────────
cart = HEAD.format(title="Cart") + NAV + """
<div class="page-hero">
  <div class="page-hero-inner">
    <h1>Your Cart</h1>
    <p>Review your order before checkout.</p>
  </div>
</div>

<section class="section">
  <div class="section-inner">
    <div class="cart-layout">
      <div class="cart-items-col">
        <div id="cart-items"></div>
      </div>
      <div class="cart-summary">
        <h3>Order Summary</h3>
        <div class="summary-row"><span>Subtotal</span><span id="summary-subtotal">$0.00</span></div>
        <div class="summary-row"><span>Shipping</span><span id="summary-shipping">$5.99</span></div>
        <div class="summary-row summary-total"><span>Total</span><span id="summary-total">$5.99</span></div>
        <button class="btn btn-gold btn-full" onclick="alert('This is a portfolio demo \u2014 no real checkout!')">Proceed to Checkout</button>
        <a href="shop.html" class="cart-continue">&#8592; Continue Shopping</a>
      </div>
    </div>
  </div>
</section>
""" + FOOTER

with open(os.path.join(BASE, "cart.html"), "w", encoding="utf-8") as f:
    f.write(cart)
print("Written: cart.html")

# ─── about.html ──────────────────────────────────────────────────────────────
about = HEAD.format(title="About") + NAV + """
<div class="about-hero">
  <div class="about-hero-inner">
    <p class="section-label">Our Story</p>
    <h1>We brew culture,<br>one cup at a time.</h1>
    <p class="about-hero-sub">Culture &amp; Kettle was built on the belief that great coffee is more than a drink. It's a ritual, a community, and a conversation.</p>
  </div>
</div>

<section class="about-story section">
  <div class="section-inner">
    <div class="about-story-grid">
      <div class="about-story-text">
        <p class="section-label">The Beginning</p>
        <h2>Born from a belief</h2>
        <p>Culture &amp; Kettle started in a small Atlanta kitchen with a single roaster, a notebook full of flavor notes, and an obsession with getting it right. Our founder, a former barista turned sourcing nerd, spent years traveling to farms in Ethiopia, Colombia, and Guatemala before bringing those relationships home.</p>
        <p>What began as weekend pop-ups at local markets grew into something we never expected: a community of people who cared as much about the story behind the cup as the cup itself. Today, we roast out of our West End facility and serve from four Atlanta locations, but the intention hasn't changed.</p>
      </div>
      <div class="about-stats-grid">
        <div class="about-stat"><span class="stat-number">2018</span><span class="stat-label">Founded</span></div>
        <div class="about-stat"><span class="stat-number">4</span><span class="stat-label">Locations</span></div>
        <div class="about-stat"><span class="stat-number">12+</span><span class="stat-label">Farm Partners</span></div>
        <div class="about-stat"><span class="stat-number">100%</span><span class="stat-label">Direct Trade</span></div>
      </div>
    </div>
  </div>
</section>

<section class="about-values section">
  <div class="section-inner">
    <p class="section-label">What We Stand For</p>
    <h2>Our values</h2>
    <div class="values-grid">
      <div class="value-card">
        <span class="value-icon">&#9679;</span>
        <h3>Intentional Sourcing</h3>
        <p>We work directly with farmers who share our commitment to quality and sustainability. Every origin we carry has a face, a name, and a story we're proud to tell.</p>
      </div>
      <div class="value-card">
        <span class="value-icon">&#9679;</span>
        <h3>Roasted Fresh</h3>
        <p>Every bag is roasted to order. We don't sit on inventory. When your coffee ships, it was roasted within the last 48 hours. That's not a marketing line, it's just how we operate.</p>
      </div>
      <div class="value-card">
        <span class="value-icon">&#9679;</span>
        <h3>Community First</h3>
        <p>Our cafes are gathering places. We host events, support local artists, and invest in the neighborhoods we're part of. Coffee is the reason you walk in. Community is the reason you stay.</p>
      </div>
    </div>
  </div>
</section>
""" + FOOTER

with open(os.path.join(BASE, "about.html"), "w", encoding="utf-8") as f:
    f.write(about)
print("Written: about.html")

# ─── locations.html ──────────────────────────────────────────────────────────
locations = HEAD.format(title="Locations") + NAV + """
<div class="page-hero">
  <div class="page-hero-inner">
    <h1>Find Your Cup</h1>
    <p>Four Atlanta locations. One intention.</p>
  </div>
</div>

<section class="section">
  <div class="section-inner">
    <div class="locations-page">

      <div class="location-full-card">
        <div class="location-info">
          <p class="location-neighborhood">Midtown</p>
          <h3>Culture &amp; Kettle Midtown</h3>
          <p class="location-address">412 Peachtree St NE<br>Atlanta, GA 30308</p>
          <a href="#" class="btn btn-outline btn-sm">Get Directions</a>
        </div>
        <div class="location-hours">
          <h4>Hours</h4>
          <ul>
            <li><span>Mon &ndash; Fri</span><span>6:00 am &ndash; 7:00 pm</span></li>
            <li><span>Sat &ndash; Sun</span><span>7:00 am &ndash; 6:00 pm</span></li>
          </ul>
        </div>
        <div class="location-amenities">
          <h4>Amenities</h4>
          <ul>
            <li>&#10003; WiFi</li>
            <li>&#10003; Outdoor Seating</li>
            <li>&#10003; Pour-Over Bar</li>
          </ul>
        </div>
      </div>

      <div class="location-full-card">
        <div class="location-info">
          <p class="location-neighborhood">West End</p>
          <h3>Culture &amp; Kettle West End</h3>
          <p class="location-address">880 Ralph D. Abernathy Blvd<br>Atlanta, GA 30310</p>
          <a href="#" class="btn btn-outline btn-sm">Get Directions</a>
        </div>
        <div class="location-hours">
          <h4>Hours</h4>
          <ul>
            <li><span>Mon &ndash; Fri</span><span>7:00 am &ndash; 6:00 pm</span></li>
            <li><span>Sat &ndash; Sun</span><span>8:00 am &ndash; 5:00 pm</span></li>
          </ul>
        </div>
        <div class="location-amenities">
          <h4>Amenities</h4>
          <ul>
            <li>&#10003; WiFi</li>
            <li>&#10003; Community Events</li>
            <li>&#10003; Local Art</li>
          </ul>
        </div>
      </div>

      <div class="location-full-card">
        <div class="location-info">
          <p class="location-neighborhood">Decatur</p>
          <h3>Culture &amp; Kettle Decatur</h3>
          <p class="location-address">119 E Court Square<br>Decatur, GA 30030</p>
          <a href="#" class="btn btn-outline btn-sm">Get Directions</a>
        </div>
        <div class="location-hours">
          <h4>Hours</h4>
          <ul>
            <li><span>Mon &ndash; Sun</span><span>7:00 am &ndash; 7:00 pm</span></li>
          </ul>
        </div>
        <div class="location-amenities">
          <h4>Amenities</h4>
          <ul>
            <li>&#10003; WiFi</li>
            <li>&#10003; Dog Friendly</li>
            <li>&#10003; Pastries</li>
          </ul>
        </div>
      </div>

      <div class="location-full-card">
        <div class="location-info">
          <p class="location-neighborhood">Ponce City Market</p>
          <h3>Culture &amp; Kettle PCM</h3>
          <p class="location-address">675 Ponce De Leon Ave NE<br>Atlanta, GA 30308</p>
          <a href="#" class="btn btn-outline btn-sm">Get Directions</a>
        </div>
        <div class="location-hours">
          <h4>Hours</h4>
          <ul>
            <li><span>Mon &ndash; Sun</span><span>8:00 am &ndash; 8:00 pm</span></li>
          </ul>
        </div>
        <div class="location-amenities">
          <h4>Amenities</h4>
          <ul>
            <li>&#10003; WiFi</li>
            <li>&#10003; Market Access</li>
            <li>&#10003; Cold Brew on Tap</li>
          </ul>
        </div>
      </div>

    </div>
  </div>
</section>
""" + FOOTER

with open(os.path.join(BASE, "locations.html"), "w", encoding="utf-8") as f:
    f.write(locations)
print("Written: locations.html")

# ─── cart.js ─────────────────────────────────────────────────────────────────
cartjs = """
const CART_KEY = 'ck_cart';

function getCart() {
  return JSON.parse(localStorage.getItem(CART_KEY) || '[]');
}

function saveCart(cart) {
  localStorage.setItem(CART_KEY, JSON.stringify(cart));
}

function updateCartCount() {
  const cart = getCart();
  const total = cart.reduce((sum, item) => sum + item.qty, 0);
  const badge = document.getElementById('cart-count');
  if (badge) badge.textContent = total;
}

function showToast(msg) {
  const toast = document.createElement('div');
  toast.textContent = msg;
  toast.style.cssText = 'position:fixed;bottom:2rem;right:2rem;background:#C9A84C;color:#0F0A06;padding:.75rem 1.5rem;font-weight:600;z-index:9999;border-radius:4px;opacity:1;transition:opacity .5s ease;font-family:Inter,sans-serif;font-size:.9rem;';
  document.body.appendChild(toast);
  setTimeout(() => { toast.style.opacity = '0'; }, 1800);
  setTimeout(() => { toast.remove(); }, 2400);
}

function addToCart(id, name, price, icon, bgClass, grind) {
  const cart = getCart();
  const grindVal = grind || 'Whole Bean';
  const existing = cart.find(i => i.id === id && i.grind === grindVal);
  if (existing) {
    existing.qty++;
  } else {
    cart.push({ id, name, price, icon, bgClass, grind: grindVal, qty: 1 });
  }
  saveCart(cart);
  updateCartCount();
  showToast('Added to cart!');
}

function removeFromCart(id, grind) {
  let cart = getCart();
  cart = cart.filter(i => !(i.id === id && i.grind === grind));
  saveCart(cart);
  updateCartCount();
  if (typeof renderCart === 'function') renderCart();
}

function renderCart() {
  const cart = getCart();
  const container = document.getElementById('cart-items');
  if (!container) return;

  if (cart.length === 0) {
    container.innerHTML = '<div class="cart-empty"><p>Your cart is empty.</p><a href="shop.html" class="btn btn-gold">Browse the Shop</a></div>';
    document.getElementById('summary-subtotal').textContent = '$0.00';
    document.getElementById('summary-shipping').textContent = '$5.99';
    document.getElementById('summary-total').textContent = '$5.99';
    return;
  }

  let html = '';
  let subtotal = 0;
  cart.forEach(item => {
    const lineTotal = (item.price * item.qty).toFixed(2);
    subtotal += item.price * item.qty;
    html += `
      <div class="cart-item">
        <div class="cart-item-visual ${item.bgClass}">
          <span>${item.icon}</span>
        </div>
        <div class="cart-item-info">
          <h4>${item.name}</h4>
          <p class="cart-item-meta">${item.grind} &middot; Qty: ${item.qty}</p>
          <p class="cart-item-price">$${lineTotal}</p>
        </div>
        <button class="cart-item-remove" onclick="removeFromCart('${item.id}','${item.grind}')">&#10005;</button>
      </div>`;
  });
  container.innerHTML = html;

  const shipping = subtotal >= 40 ? 0 : 5.99;
  const total = subtotal + shipping;
  document.getElementById('summary-subtotal').textContent = '$' + subtotal.toFixed(2);
  document.getElementById('summary-shipping').textContent = shipping === 0 ? 'Free' : '$5.99';
  document.getElementById('summary-total').textContent = '$' + total.toFixed(2);
}

document.addEventListener('DOMContentLoaded', () => {
  updateCartCount();
  if (document.getElementById('cart-items')) renderCart();
});
"""

with open(os.path.join(BASE, "cart.js"), "w", encoding="utf-8") as f:
    f.write(cartjs.strip())
print("Written: cart.js")

print("\\nAll files written successfully.")
