/* Engineering Signal — interactions (lightweight, reduced-motion aware) */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Scroll reveal */
  var rs = document.querySelectorAll('.reveal');
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.08 });
    rs.forEach(function (el) { io.observe(el); });
  } else {
    rs.forEach(function (el) { el.classList.add('in'); });
  }

  /* Heat-band row hover inspection */
  var bands = document.querySelectorAll('.heatband');
  bands.forEach(function (band) {
    var legend = band.querySelector('.legend');
    band.querySelectorAll('.rowlabel').forEach(function (r) {
      r.addEventListener('mouseenter', function () {
        if (legend) legend.innerHTML = '<b>' + (r.getAttribute('data-name') || '?') +
          '</b> · ' + (r.getAttribute('data-n') || '?') + ' questions';
      });
    });
    if (legend) legend.addEventListener('mouseleave', function () {
      legend.innerHTML = 'hover a row to inspect';
    });
  });
  /* Lazy PDF viewer on collection pages */
  document.querySelectorAll('.pdf-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var wrap = btn.parentElement.parentElement.querySelector('.pdf-wrap');
      if (!wrap) return;
      if (!wrap.querySelector('iframe')) {
        var iframe = document.createElement('iframe');
        iframe.src = btn.getAttribute('data-pdf');
        iframe.title = 'Handbook PDF viewer';
        iframe.setAttribute('loading', 'lazy');
        wrap.appendChild(iframe);
      }
      wrap.hidden = !wrap.hidden;
      if (!wrap.hidden && wrap.querySelector('iframe')) {
        btn.textContent = '收起 PDF ▲';
      } else {
        btn.innerHTML = '在线预览 PDF <span class="k">⇣</span>';
      }
    });
  });
})();