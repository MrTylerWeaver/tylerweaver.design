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
