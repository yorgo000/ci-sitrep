/* CI SITREP broadcast scene (F-19).
   Cycles the report: State of the market first, then every finding, one at
   a time. Data: window.CI_SITREP_DATA from findings-inline.js (generated
   with the export — the file:// path OBS uses), refreshed from
   ../data/findings.json every 15 minutes when served over HTTP.

   Voiceover hook: each slide sets #finding's data-voiceover attribute to
   the exact speakable text (headline + one line), exposes it as
   window.CI_SITREP_VOICEOVER, and dispatches a 'ci-sitrep-slide' event
   with {index, total, kind, id, voiceover}. A voiceover driver listens
   for the event — it never has to scrape the DOM.
*/
(function () {
  'use strict';

  var ARTICLE_MS = 15000;   // ~15s per finding: 81 findings ≈ 20 minutes
  var SOTM_MS = 75000;      // State of the market: full synthesis, spoken
  var REFRESH_MS = 15 * 60 * 1000;
  var MARQUEE_PX_PER_SEC = 140;

  var params = new URLSearchParams(location.search);
  if (params.get('dev') === '1') document.body.classList.add('dev');
  if (params.get('transparent') === '1') document.body.classList.add('transparent');

  var data = window.CI_SITREP_DATA || null;
  var slides = [];
  var index = 0;
  var timer = null;

  var $ = function (id) { return document.getElementById(id); };

  function speakable(text) {
    return text
      .replace(/×/g, ' times ').replace(/~/g, 'about ').replace(/→/g, ' to ')
      .replace(/—/g, ', ').replace(/–/g, ' to ').replace(/%/g, ' percent')
      .replace(/&/g, ' and ').replace(/\$/g, ' dollars ')
      .replace(/\s+/g, ' ').trim();
  }

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  /* ---------- clocks ---------- */
  var fmtET = new Intl.DateTimeFormat('en-US', {
    timeZone: 'America/New_York', hour: '2-digit', minute: '2-digit',
    second: '2-digit', hour12: false
  });
  var fmtUTC = new Intl.DateTimeFormat('en-US', {
    timeZone: 'UTC', hour: '2-digit', minute: '2-digit', second: '2-digit',
    hour12: false
  });
  function tickClocks() {
    var now = new Date();
    $('clock-et').textContent = fmtET.format(now);
    $('clock-utc').textContent = fmtUTC.format(now);
  }
  tickClocks();
  setInterval(tickClocks, 1000);

  /* ---------- static panels ---------- */
  function renderDeadline() {
    var list = (data.deadlines || []).slice().sort(function (a, b) {
      return a.date < b.date ? -1 : 1;
    });
    var today = new Date();
    today.setHours(0, 0, 0, 0);
    var next = null;
    for (var i = 0; i < list.length; i++) {
      var d = new Date(list[i].date + 'T12:00:00');
      if (d >= today) { next = list[i]; break; }
    }
    if (!next) {
      $('deadline-text').textContent = 'No upcoming deadline tracked';
      $('deadline-days').textContent = '';
      return;
    }
    var d = new Date(next.date + 'T12:00:00'); // noon: DST-safe
    var days = Math.floor((d - today) / 86400000); // floor, not round: the noon offset adds half a day
    $('deadline-text').textContent = next.label + ' — ' + next.display;
    $('deadline-days').textContent = days === 0 ? 'Today'
      : days === 1 ? 'Tomorrow' : 'in ' + days + ' days';
  }

  function barRow(side, entry, max) {
    var pct = Math.max(6, Math.round(entry.value / max * 100));
    return '<div class="bar-row"><span class="bar-value">' + esc(entry.display) +
      '</span><span class="bar-track"><span class="bar-fill ' + side +
      '" style="width:' + pct + '%"></span></span><span class="bar-label">' +
      esc(entry.label) + '</span></div>';
  }

  function renderGauges() {
    var html = '';
    (data.gauges || []).forEach(function (g) {
      html += '<div class="gauge"><div class="gauge-title">' + esc(g.title) + '</div>';
      html += '<div class="gauge-headline">' + esc(g.headline) + '</div>';
      if (g.kind === 'pair') {
        var max = Math.max(g.ci.value, g.ei.value);
        html += barRow('ci', g.ci, max) + barRow('ei', g.ei, max);
      } else {
        html += '<div class="gauge-stat"><span class="stat-value">' +
          esc(g.display) + '</span><span class="stat-label">' +
          esc(g.headline.replace(g.display, '').trim()) + '</span></div>';
      }
      if (g.note) html += '<div class="gauge-note">' + esc(g.note) + '</div>';
      html += '<div class="gauge-src">' + esc(g.source || '') +
        (g.date ? ', ' + esc(g.date) : '') +
        (g.rating ? ' &nbsp;·&nbsp; <span class="dots">' +
          {'established': '●●●●', 'corroborated': '●●●○',
           'reported': '●●○○', 'claimed': '●○○○'}[g.rating] +
          '</span> ' + esc(g.rating) : '') + '</div></div>';
    });
    $('gauges').innerHTML = html || '<p class="gauge-note">No gauges in this export.</p>';
  }

  function marquee(trackEl, itemsHtml) {
    // Two copies for a seamless -50% loop; speed constant, duration from width.
    trackEl.innerHTML = itemsHtml + itemsHtml;
    var half = trackEl.scrollWidth / 2;
    trackEl.style.animationDuration = Math.max(60, Math.round(half / MARQUEE_PX_PER_SEC)) + 's';
  }

  function renderMarquees() {
    var g = (data.glossary || []).map(function (e) {
      var def = e.definition.split(/(?<=[.!?])\s/)[0];
      if (def.length > 110) def = def.slice(0, 107) + '…';
      return '<span class="item"><b>' + esc(e.term) + '</b> — ' + esc(def) +
        '</span><span class="sep">●</span>';
    }).join('');
    marquee($('glossary-track'), g);
    var t = (data.whats_new || []).map(function (w) {
      return '<span class="item"><b>' + esc(w.date || '') + '</b> — ' +
        esc(w.title) + (w.source ? ' <span style="color:var(--muted)">(' +
        esc(w.source) + ')</span>' : '') + '</span><span class="sep">●</span>';
    }).join('');
    marquee($('ticker-track'), t);
  }

  /* ---------- slides ---------- */
  function buildSlides() {
    slides = [{ kind: 'sotm', ms: SOTM_MS }];
    (data.articles || []).forEach(function (a) {
      slides.push({ kind: 'article', ms: ARTICLE_MS, article: a });
    });
  }

  function showSlide(i) {
    index = i;
    var slide = slides[index];
    var finding = $('finding');
    var vo = '';
    if (slide.kind === 'sotm') {
      finding.classList.add('sotm');
      $('section-chip').textContent = 'STATE OF THE MARKET';
      $('rating').style.visibility = 'hidden';
      $('counter').textContent = 'Cycle opener';
      $('headline').textContent = 'State of the market';
      $('summary').textContent = data.state_of_the_market || '';
      $('source-line').innerHTML = 'The report&rsquo;s own synthesis — every claim ' +
        'traceable to a section below. ' + (data.counts ? data.counts.articles +
        ' findings, every one confidence-rated.' : '');
      vo = speakable('State of the market. ' + (data.state_of_the_market || ''));
    } else {
      var a = slide.article;
      finding.classList.remove('sotm');
      $('section-chip').textContent = (a.section || '').toUpperCase();
      $('rating').style.visibility = 'visible';
      $('rating-dots').textContent = a.rating_dots || '';
      $('rating-label').textContent = a.rating || '';
      $('counter').textContent = 'Finding ' + index + ' / ' + (slides.length - 1);
      $('headline').textContent = a.headline;
      $('summary').textContent = a.bullets && a.bullets[0] ? a.bullets[0] : '';
      var src = '<b>' + esc(a.source || '') + '</b>' +
        (a.date ? ', ' + esc(a.date) : '') +
        (a.subsection ? ' &nbsp;·&nbsp; ' + esc(a.subsection) : '') +
        (a.flag ? ' &nbsp;·&nbsp; <span class="flag">[' + esc(a.flag) + ']</span>' : '');
      $('source-line').innerHTML = src;
      vo = a.voiceover || speakable(a.headline);
    }
    finding.setAttribute('data-voiceover', vo);
    window.CI_SITREP_VOICEOVER = vo;
    var cap = $('vo-caption');
    if (document.body.classList.contains('dev')) {
      cap.hidden = false;
      cap.textContent = vo;
    }
    document.dispatchEvent(new CustomEvent('ci-sitrep-slide', { detail: {
      index: index, total: slides.length, kind: slide.kind,
      id: slide.article ? slide.article.id : 'state-of-the-market',
      voiceover: vo
    }}));
    var bar = $('progress-bar');
    bar.style.transition = 'none';
    bar.style.width = '0%';
    void bar.offsetWidth;
    bar.style.transition = 'width ' + slide.ms + 'ms linear';
    bar.style.width = '100%';
    clearTimeout(timer);
    timer = setTimeout(function () {
      showSlide((index + 1) % slides.length);
    }, slide.ms);
  }

  /* ---------- data ---------- */
  function renderAll() {
    $('asof-date').textContent = data.as_of || data.as_of_date || '—';
    renderDeadline();
    renderGauges();
    renderMarquees();
    buildSlides();
    if (index >= slides.length) index = 0;
    showSlide(index);
  }

  function refreshFromServer() {
    if (location.protocol === 'file:') return; // fetch is blocked under file://
    fetch('../data/findings.json', { cache: 'no-store' })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (fresh) {
        if (!data || fresh.generated_at > data.generated_at) {
          data = fresh;
          renderAll();
        }
      })
      .catch(function () { /* keep the inline data; try again next cycle */ });
  }

  if (!data) {
    // No inline data (export not run?) — try the server path once.
    refreshFromServer();
    setTimeout(function () {
      if (!data) $('data-error').hidden = false;
    }, 3000);
  } else {
    renderAll();
    setInterval(refreshFromServer, REFRESH_MS);
  }
})();
