function toggleNav() {
  document.querySelector('.nav-links').classList.toggle('open');
}
document.querySelectorAll('.nav-links a').forEach(function(l) {
  l.addEventListener('click', function() { document.querySelector('.nav-links').classList.remove('open'); });
});
var obs = new IntersectionObserver(function(entries) {
  entries.forEach(function(e) { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(function(el, i) {
  el.style.transitionDelay = (i % 3) * 0.12 + 's';
  obs.observe(el);
});