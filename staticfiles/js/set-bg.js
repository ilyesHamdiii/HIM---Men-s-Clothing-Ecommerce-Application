document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.set-bg').forEach(function(el) {
    const bg = el.getAttribute('data-setbg');
    if (bg) {
      el.style.backgroundImage = `url(${bg})`;
    }
  });
});
