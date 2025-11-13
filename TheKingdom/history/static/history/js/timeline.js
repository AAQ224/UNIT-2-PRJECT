document.addEventListener('DOMContentLoaded', () => {
  const items = document.querySelectorAll('.tl-item');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
      }
    });
  }, { threshold: 0.15 });

  items.forEach(item => observer.observe(item));
});
