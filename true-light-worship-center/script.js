function toggleNav() {
  document.querySelector('.nav-links').classList.toggle('open');
}
document.querySelectorAll('.nav-links a').forEach(function(l) {
  l.addEventListener('click', function() { document.querySelector('.nav-links').classList.remove('open'); });
});
// Set active nav link
var path = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-links a').forEach(function(a) {
  if (a.getAttribute('href') === path) a.classList.add('active');
});
// Scroll reveal
var obs = new IntersectionObserver(function(entries) {
  entries.forEach(function(e) { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach(function(el, i) {
  el.style.transitionDelay = (i % 3) * 0.1 + 's';
  obs.observe(el);
});