// Mobile nav toggle
function toggleNav() {
  document.querySelector('.nav-links').classList.toggle('open');
}
document.querySelectorAll('.nav-links a').forEach(function(link) {
  link.addEventListener('click', function() {
    document.querySelector('.nav-links').classList.remove('open');
  });
});

// Scroll reveal
var observer = new IntersectionObserver(function(entries) {
  entries.forEach(function(entry) {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.15 });

document.querySelectorAll('.reveal').forEach(function(el, i) {
  el.style.transitionDelay = (i % 3) * 0.1 + 's';
  observer.observe(el);
});

// Nav shrink on scroll
window.addEventListener('scroll', function() {
  document.querySelector('.nav').style.borderBottomColor =
    window.scrollY > 50 ? 'rgba(42,42,58,0.8)' : 'rgba(42,42,58,1)';
});

// Contact form
function handleSubmit(e) {
  e.preventDefault();
  var msg = document.getElementById('form-msg');
  msg.textContent = "Message sent! I'll be in touch within a day.";
  e.target.reset();
}