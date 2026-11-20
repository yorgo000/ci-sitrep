// Round 4b FILTER_JS test: minimal DOM shim + the REAL filter script
// (extracted from build_dashboard.py) + a fixture built from the REAL
// built index.html. No jsdom on the VM, so the shim implements exactly
// the DOM surface FILTER_JS uses.
// Snapshots: regenerate r4b-fixture.json with regen_fixture.py (same
// directory) and r4b-filter-js.txt from the EVALUATED FILTER_JS
// (import build_dashboard; never regex-extract from source) whenever
// the build or the generator changes — then update this file's
// hard-coded snapshot numbers (totals, Black Duck, pre-click) from
// the values regen_fixture.py prints. Current snapshot: 62 figures,
// 114 articles (2026-11-20 ledger fix).
'use strict';
const fs = require('fs');
const path = require('path');
const fixture = JSON.parse(fs.readFileSync(path.join(__dirname, 'r4b-fixture.json'), 'utf8'));

// ---------- minimal DOM ----------
class ClassList {
  constructor(el) { this.el = el; }
  contains(c) { return this.el._classes.has(c); }
  add(c) { this.el._classes.add(c); }
  remove(c) { this.el._classes.delete(c); }
  toggle(c, force) {
    if (force === undefined) { this.contains(c) ? this.remove(c) : this.add(c); }
    else force ? this.add(c) : this.remove(c);
  }
}
function parseCompound(sel) {
  // tag? (#id)? (.class)* ([attr] | [attr="v"] | [attr^="v"])*
  const out = { tag: null, id: null, classes: [], attrs: [] };
  let m;
  const tagM = sel.match(/^[a-zA-Z][a-zA-Z0-9]*/);
  if (tagM) { out.tag = tagM[0].toUpperCase(); sel = sel.slice(tagM[0].length); }
  while (sel.length) {
    if (sel[0] === '#') { m = sel.match(/^#([\w-]+)/); out.id = m[1]; sel = sel.slice(m[0].length); }
    else if (sel[0] === '.') { m = sel.match(/^\.([\w-]+)/); out.classes.push(m[1]); sel = sel.slice(m[0].length); }
    else if (sel[0] === '[') {
      m = sel.match(/^\[([\w-]+)(\^?=)"?([^"\]]*)"?\]/) || sel.match(/^\[([\w-]+)\]/);
      if (!m) throw new Error('bad selector part: ' + sel);
      out.attrs.push({ name: m[1], op: m[2] || null, val: m[3] || null });
      sel = sel.slice(m[0].length);
    } else throw new Error('bad selector part: ' + sel);
  }
  return out;
}
function matchCompound(el, c) {
  if (c.tag && el.tagName !== c.tag) return false;
  if (c.id && el.id !== c.id) return false;
  for (const cl of c.classes) if (!el.classList.contains(cl)) return false;
  for (const a of c.attrs) {
    const v = el.getAttribute(a.name);
    if (a.op === null) { if (v === null) return false; }
    else if (a.op === '=') { if (v !== a.val) return false; }
    else if (a.op === '^=') { if (v === null || !v.startsWith(a.val)) return false; }
  }
  return true;
}
function matchSelector(el, selector) {
  // comma groups of descendant chains
  for (const group of selector.split(',')) {
    const parts = group.trim().split(/\s+/).map(parseCompound);
    let cur = el;
    let ok = true;
    for (let i = parts.length - 1; i >= 0; i--) {
      while (cur && !matchCompound(cur, parts[i])) cur = cur.parentElement;
      if (!cur) { ok = false; break; }
      cur = cur.parentElement;
    }
    if (ok) return true;
  }
  return false;
}
class El {
  constructor(tag, attrs = {}) {
    this.tagName = tag.toUpperCase();
    this.id = attrs.id || '';
    this._classes = new Set((attrs.class || '').split(/\s+/).filter(Boolean));
    this.classList = new ClassList(this);
    this._attrs = new Map(Object.entries(attrs.attrs || {}));
    if (attrs.id) this._attrs.set('id', attrs.id);
    if (attrs.class) this._attrs.set('class', attrs.class);
    this.children = [];
    this.parentElement = null;
    this.style = { display: '' };
    this.textContent = attrs.text || '';
    this.hidden = !!attrs.hidden;
    this.value = attrs.value !== undefined ? attrs.value : '';
    this.checked = !!attrs.checked;
    this.disabled = !!attrs.disabled;
    this.open = !!attrs.open;
    this._listeners = {};
  }
  getAttribute(n) { const v = this._attrs.get(n); return v === undefined ? null : v; }
  setAttribute(n, v) { this._attrs.set(n, String(v)); if (n === 'id') this.id = String(v); }
  appendChild(k) {
    const i = k.parentElement ? k.parentElement.children.indexOf(k) : -1;
    if (i >= 0) k.parentElement.children.splice(i, 1);
    k.parentElement = this;
    this.children.push(k);
    return k;
  }
  addEventListener(t, fn) { (this._listeners[t] = this._listeners[t] || []).push(fn); }
  dispatch(t, evt = {}) {
    evt.target = evt.target || this;
    for (const fn of (this._listeners[t] || [])) fn.call(this, evt);
  }
  querySelectorAll(sel) {
    const out = [];
    const walk = (el) => { for (const k of el.children) { if (matchSelector(k, sel)) out.push(k); walk(k); } };
    walk(this);
    return out;
  }
  querySelector(sel) { return this.querySelectorAll(sel)[0] || null; }
  closest(sel) { let cur = this; while (cur) { if (matchSelector(cur, sel)) return cur; cur = cur.parentElement; } return null; }
  contains(node) { let cur = node; while (cur) { if (cur === this) return true; cur = cur.parentElement; } return false; }
  get nextElementSibling() {
    if (!this.parentElement) return null;
    const sibs = this.parentElement.children;
    const i = sibs.indexOf(this);
    return i >= 0 && i + 1 < sibs.length ? sibs[i + 1] : null;
  }
  get previousElementSibling() {
    if (!this.parentElement) return null;
    const sibs = this.parentElement.children;
    const i = sibs.indexOf(this);
    return i > 0 ? sibs[i - 1] : null;
  }
}
const documentListeners = {};
const documentStub = {
  _byId: {},
  getElementById(id) { return this._byId[id] || null; },
  querySelectorAll(sel) { return root.querySelectorAll(sel); },
  querySelector(sel) { return root.querySelector(sel); },
  addEventListener(t, fn) { (documentListeners[t] = documentListeners[t] || []).push(fn); },
  createElement(tag) { return new El(tag); },
};
function registerIds(el) {
  if (el.id) documentStub._byId[el.id] = el;
  for (const k of el.children) registerIds(k);
}
const root = new El('div', { id: 'root' });

// ---------- build the fixture DOM ----------
// Filter bar
const bar = new El('div', { id: 'dash-filters', class: 'dash-filters' });
root.appendChild(bar);
const SELECT_DIMS = ['industry', 'severity', 'pnl-impact', 'horizon', 'register',
                     'subject', 'confidence', 'jurisdiction', 'company'];
const selects = {};
for (const dim of SELECT_DIMS) {
  const s = new El('select', { attrs: { 'data-filter': dim } });
  bar.appendChild(s);
  selects[dim] = s;
}
const TYPE_VALUES = ['benchmark', 'study', 'product', 'incident', 'regulation',
                     'guidance', 'survey', 'framework', 'practice', 'verdict'];
const typeBoxes = {};
for (const v of TYPE_VALUES) {
  const b = new El('input', { attrs: { type: 'checkbox', 'data-filter': 'type' } });
  b.value = v;
  bar.appendChild(b);
  typeBoxes[v] = b;
}
const sortSel = new El('select', { id: 'dash-sort' });
sortSel.value = 'panel';
bar.appendChild(sortSel);
const sortDirBtn = new El('button', { id: 'dash-sort-dir', class: 'dash-sort-dir' });
sortDirBtn.disabled = true;
sortDirBtn.setAttribute('aria-disabled', 'true');
const sortDirLabel = new El('span', { class: 'sort-dir-label', text: 'Descending' });
sortDirBtn.appendChild(sortDirLabel);
bar.appendChild(sortDirBtn);
const moreFilters = new El('details', { class: 'dash-more-filters' });
bar.appendChild(moreFilters);
const clearBtnBar = new El('button', { attrs: { 'data-clear-filters': '' }, class: 'dash-clear-btn' });
bar.appendChild(clearBtnBar);
const countEl = new El('p', { id: 'dash-count', text: 'Showing 62 of 62 figures · 114 of 114 articles' });
bar.appendChild(countEl);
const indicatorEl = new El('span', { id: 'sfp-active', class: 'sfp-active', text: '' });
root.appendChild(indicatorEl);

// Dashboard embed: panels with section bodies + grids
const embed = new El('div', { class: 'dash-embed' });
root.appendChild(embed);
const dashEmpty = new El('p', { id: 'dash-empty', class: 'dash-empty', hidden: true });
const clearBtnDash = new El('button', { attrs: { 'data-clear-filters': '' }, class: 'dash-clear-btn' });
dashEmpty.appendChild(clearBtnDash);
embed.appendChild(dashEmpty);
const grids = [];
for (const p of fixture.panels) {
  const h = new El('h3', { id: p.id, class: 'dash-panel' });
  embed.appendChild(h);
  const body = new El('div', { class: 'section-body' });
  embed.appendChild(body);
  const grid = new El('div', { class: 'tile-grid' });
  body.appendChild(grid);
  grids.push(grid);
  for (const k of p.kids) {
    if (k.kind === 'label') {
      grid.appendChild(new El('p', { class: 'block-label', text: k.text }));
    } else {
      const t = new El('div', { id: k.id, class: k.classes.join(' '), attrs: {} });
      for (const [dim, v] of Object.entries(k.attrs)) t.setAttribute('data-' + dim, v);
      grid.appendChild(t);
    }
  }
}
// Report embed: nested heading/body tree
const report = new El('div', { class: 'report-embed' });
root.appendChild(report);
let artN = 0;
const articleEls = [];
function buildReport(node, parentBody) {
  for (const child of node.children) {
    const h = new El('h' + child.level, { id: child.id });
    parentBody.appendChild(h);
    const body = new El('div', { class: 'section-body' });
    parentBody.appendChild(body);
    for (const a of child.articles) {
      const d = new El('details', { id: 'art-' + (artN++), attrs: {} });
      for (const [dim, v] of Object.entries(a)) d.setAttribute('data-' + dim, v);
      body.appendChild(d);
      articleEls.push(d);
    }
    buildReport(child, body);
  }
}
buildReport(fixture.report, report);
const reportEmpty = new El('p', { id: 'report-empty', class: 'dash-empty', hidden: true });
const clearBtnReport = new El('button', { attrs: { 'data-clear-filters': '' }, class: 'dash-clear-btn' });
reportEmpty.appendChild(clearBtnReport);
root.appendChild(reportEmpty);
// Feed ("New in the last 7 days"): 3 tagged entries + empty state.
// Hand-built, not from the fixture JSON — the fixture predates feed
// tagging. An untagged entry is appended later, by the test that
// needs one (the empty state can only show while none exists).
const feedList = new El('ul', { class: 'whats-new-feed' });
report.appendChild(feedList);
const feedItems = [];
function addFeedLi(attrs) {
  const li = new El('li', { attrs: {} });
  for (const [dim, v] of Object.entries(attrs)) li.setAttribute('data-' + dim, v);
  feedList.appendChild(li);
  feedItems.push(li);
  return li;
}
addFeedLi({ subject: '3', industry: 'banking', severity: 'material' });
addFeedLi({ subject: '1', industry: 'software', severity: 'critical' });
addFeedLi({ subject: '2', industry: 'software', severity: 'directional' });
const feedEmpty = new El('p', { id: 'feed-empty', class: 'dash-empty', hidden: true });
report.appendChild(feedEmpty);
// An anchor link into the report, for the share-link test
const anchor = new El('a', { attrs: { href: '#art-5' } });
root.appendChild(anchor);
registerIds(root);

// ---------- load the REAL filter script ----------
let filterJs = fs.readFileSync(path.join(__dirname, 'r4b-filter-js.txt'), 'utf8');
filterJs = filterJs.replace(/^\s*<script>\n?/, '').replace(/\n?<\/script>\n?$/, '');
const document = documentStub;
eval(filterJs); // runs the IIFE: init + applyFilters()

// ---------- test helpers ----------
let pass = 0, fail = 0;
function check(name, cond, extra = '') {
  if (cond) { pass++; console.log('PASS  ' + name); }
  else { fail++; console.log('FAIL  ' + name + (extra ? ' — ' + extra : '')); }
}
const tiles = () => embed.querySelectorAll('.tile-grid .tile');
const visibleTiles = () => tiles().filter(t => t.style.display !== 'none');
const visibleArticles = () => articleEls.filter(a => a.style.display !== 'none');
function setSelect(dim, val) { selects[dim].value = val; selects[dim].dispatch('change'); }
function setType(vals) {
  for (const v of TYPE_VALUES) typeBoxes[v].checked = vals.includes(v);
  typeBoxes[vals[0] || 'benchmark'].dispatch('change');
}
function setFilters(f) {
  for (const dim of SELECT_DIMS) if (f[dim]) setSelect(dim, f[dim][0]);
  if (f.type) setType(f.type);
}
function clearAll() { clearBtnBar.dispatch('click'); }
function clickAnchor() {
  for (const fn of (documentListeners.click || [])) fn({ target: anchor });
}

// ---------- tests ----------
check('fresh count line', countEl.textContent === 'Showing 62 of 62 figures · 114 of 114 articles', countEl.textContent);
check('fresh indicator empty', indicatorEl.textContent === '');
check('fresh toggle disabled', sortDirBtn.disabled === true);
check('fresh all tiles visible', visibleTiles().length === 62, String(visibleTiles().length));
check('fresh all articles visible', visibleArticles().length === 114, String(visibleArticles().length));
check('fresh dash-empty hidden', dashEmpty.hidden === true);
check('fresh report-empty hidden', reportEmpty.hidden === true);

// filter scenarios vs independent Python expectations
for (const [name, filters] of Object.entries(fixture.scenarios)) {
  if (name === 'fresh') continue;
  clearAll();
  setFilters(filters);
  const [ef, ea] = fixture.expected[name];
  const vf = visibleTiles().length, va = visibleArticles().length;
  check(`scenario ${name}: figures ${vf}==${ef}`, vf === ef, `got ${vf}`);
  check(`scenario ${name}: articles ${va}==${ea}`, va === ea, `got ${va}`);
  check(`scenario ${name}: count line`, countEl.textContent === `Showing ${ef} of 62 figures · ${ea} of 114 articles`, countEl.textContent);
}

// indicator text
clearAll(); setSelect('severity', 'critical');
check('indicator 1 filter', indicatorEl.textContent === ' · 1 filter active: Severity', JSON.stringify(indicatorEl.textContent));
clearAll(); setType(['benchmark', 'study']);
check('indicator Type counts once', indicatorEl.textContent === ' · 1 filter active: Type', JSON.stringify(indicatorEl.textContent));
clearAll(); setSelect('severity', 'critical'); setType(['benchmark']);
check('indicator 2 filters in control order', indicatorEl.textContent === ' · 2 filters active: Severity, Type', JSON.stringify(indicatorEl.textContent));
clearAll();
setSelect('industry', 'software'); setSelect('severity', 'critical');
setSelect('pnl-impact', 'risk'); setSelect('horizon', 'immediate'); setSelect('register', 'technical');
check('indicator 5 filters capped at 3 names', indicatorEl.textContent === ' · 5 filters active: Industry, Severity, P&L impact +2 more', JSON.stringify(indicatorEl.textContent));

// section hiding on a zero-article filter
clearAll(); setSelect('jurisdiction', 'eu');
const heads = report.querySelectorAll('h2, h3, h4');
let hiddenHeads = 0, visibleNoArtHeads = 0, hiddenNoArtHeads = 0;
for (const hd of heads) {
  const body = hd.nextElementSibling;
  const arts = body ? body.querySelectorAll('details[data-subject]') : [];
  if (arts.length === 0) {
    if (hd.style.display === 'none') hiddenNoArtHeads++;
    else visibleNoArtHeads++;
  } else if (hd.style.display === 'none') hiddenHeads++;
}
check('eu: every heading with articles hides', hiddenHeads === heads.filter(hd => { const b = hd.nextElementSibling; return b && b.querySelectorAll('details[data-subject]').length; }).length, `${hiddenHeads} hidden`);
check('eu: headings without articles stay visible', hiddenNoArtHeads === 0 && visibleNoArtHeads > 0, `visible-no-art=${visibleNoArtHeads} hidden-no-art=${hiddenNoArtHeads}`);
check('eu: report-empty shows', reportEmpty.hidden === false);
check('eu: dash-empty stays hidden (untagged tiles remain)', dashEmpty.hidden === true);
// untagged exemption: exactly the 4 untagged tiles visible
const visIds = visibleTiles().map(t => t.id);
check('eu: only untagged tiles visible', visibleTiles().length === 4 && visibleTiles().every(t => t.classList.contains('tile-untagged')), visIds.join(','));
// panel hiding: panels 1,2,4 hide; 3 (untagged §3.6) and 5 (bignote) stay
const panelHeads = embed.querySelectorAll('h3.dash-panel');
const visPanels = panelHeads.filter(hd => hd.style.display !== 'none').map(hd => hd.id);
check('eu: panels right-vs-wrong + money stay, others hide', JSON.stringify(visPanels) === JSON.stringify(['right-vs-wrong', 'money']), visPanels.join(','));

// company multi-word matching (comma-joined data-company)
clearAll(); setSelect('company', 'Black Duck');
check('company Black Duck: 1 article', visibleArticles().length === 1, String(visibleArticles().length));
check('company Black Duck: 6 figures', visibleTiles().length === 6, String(visibleTiles().length));

// sort: severity desc in governance-gap (no pinned tiles there)
clearAll();
const govGrid = grids[1];
const origGov = govGrid.children.map(k => k.id || ('label:' + k.textContent));
sortSel.value = 'severity'; sortSel.dispatch('change');
check('sort severity: toggle enabled', sortDirBtn.disabled === false);
check('sort severity: default Descending', sortDirLabel.textContent === 'Descending', sortDirLabel.textContent);
const RANK = { critical: 4, material: 3, directional: 2, background: 1 };
const sevSeq = govGrid.children.filter(k => k.classList.contains('tile')).map(t => RANK[t.getAttribute('data-severity')]);
const nonInc = sevSeq.every((v, i) => i === 0 || v <= sevSeq[i - 1]);
check('sort severity desc: ranks non-increasing', nonInc, sevSeq.join(','));
// pinned positions in panel 3 (untagged §3.6 figures keep their slots)
const p3 = grids[2];
const beforeP3 = p3.children.map(k => k.id || ('label:' + k.textContent));
const pinnedBefore = beforeP3.map((id, i) => ({ id, i })).filter(x => {
  const el = p3.children[x.i];
  return el.classList && el.classList.contains('tile-untagged');
});
sortSel.value = 'date'; sortSel.dispatch('change');
const afterP3 = p3.children.map(k => k.id || ('label:' + k.textContent));
const pinnedKept = pinnedBefore.every(x => afterP3[x.i] === x.id);
check('sort date: untagged tiles keep positions', pinnedKept, `before ${JSON.stringify(beforeP3)} after ${JSON.stringify(afterP3)}`);
// money bignote stays first under a sort
const money = grids[4];
const bignoteId = money.children[0].id;
sortSel.value = 'confidence'; sortSel.dispatch('change');
check('sort confidence: bignote stays first', money.children[0].id === bignoteId, money.children[0].id);
// sort by company asc: alphabetical by first value, no-company last
sortSel.value = 'company'; sortSel.dispatch('change');
check('sort company: default Ascending', sortDirLabel.textContent === 'Ascending', sortDirLabel.textContent);
const compSeq = govGrid.children.filter(k => k.classList.contains('tile')).map(t => {
  const c = t.getAttribute('data-company');
  return c ? c.split(',')[0].toLowerCase() : null;
});
let compOk = true, seenNull = false;
for (const v of compSeq) {
  if (v === null) seenNull = true;
  else if (seenNull) compOk = false;
}
const withComp = compSeq.filter(v => v !== null);
const sortedComp = [...withComp].sort();
check('sort company asc: alphabetical, missing last', compOk && JSON.stringify(withComp) === JSON.stringify(sortedComp), compSeq.join('|'));
// sort by date desc then toggle to asc
sortSel.value = 'date'; sortSel.dispatch('change');
check('sort date: default Descending', sortDirLabel.textContent === 'Descending');
const dateSeq = govGrid.children.filter(k => k.classList.contains('tile')).map(t => t.getAttribute('data-date'));
const datedDesc = dateSeq.filter(Boolean);
const descOk = datedDesc.every((v, i) => i === 0 || v <= datedDesc[i - 1]);
check('sort date desc: newest first', descOk, datedDesc.slice(0, 4).join(','));
sortDirBtn.dispatch('click');
check('toggle click: label Ascending', sortDirLabel.textContent === 'Ascending');
const dateSeq2 = govGrid.children.filter(k => k.classList.contains('tile')).map(t => t.getAttribute('data-date'));
const datedAsc = dateSeq2.filter(Boolean);
const ascOk = datedAsc.every((v, i) => i === 0 || v >= datedAsc[i - 1]);
check('sort date asc: oldest first', ascOk, datedAsc.slice(0, 4).join(','));
// horizon default is ascending (soonest first)
sortSel.value = 'horizon'; sortSel.dispatch('change');
check('sort horizon: default Ascending (soonest first)', sortDirLabel.textContent === 'Ascending', sortDirLabel.textContent);
// panel order restores exactly
sortSel.value = 'panel'; sortSel.dispatch('change');
const restoredGov = govGrid.children.map(k => k.id || ('label:' + k.textContent));
check('panel order restores editorial order', JSON.stringify(restoredGov) === JSON.stringify(origGov));
check('panel order: toggle disabled again', sortDirBtn.disabled === true);

// clear-all resets everything
setSelect('severity', 'critical'); setType(['benchmark', 'study']);
sortSel.value = 'severity'; sortSel.dispatch('change');
moreFilters.open = true;
clearAll();
check('clear-all: selects cleared', SELECT_DIMS.every(d => selects[d].value === ''));
check('clear-all: type boxes unchecked', TYPE_VALUES.every(v => !typeBoxes[v].checked));
check('clear-all: sort back to panel', sortSel.value === 'panel');
check('clear-all: toggle reset to Descending + disabled', sortDirLabel.textContent === 'Descending' && sortDirBtn.disabled === true);
check('clear-all: More filters collapsed', moreFilters.open === false);
check('clear-all: counts restored', countEl.textContent === 'Showing 62 of 62 figures · 114 of 114 articles', countEl.textContent);
check('clear-all: indicator empty', indicatorEl.textContent === '');

// anchor click into the report clears filters (share links open unfiltered)
setSelect('severity', 'critical');
check('pre-click: filtered', visibleArticles().length === 14, String(visibleArticles().length));
clickAnchor();
check('anchor click clears filters', visibleArticles().length === 114 && countEl.textContent === 'Showing 62 of 62 figures · 114 of 114 articles', countEl.textContent);

// feed filtering (Round 5 fix: entries inherit their article's tags)
const visibleFeed = () => feedItems.filter(li => li.style.display !== 'none');
clearAll();
check('feed fresh: all visible, empty hidden', visibleFeed().length === 3 && feedEmpty.hidden === true, `${visibleFeed().length} visible`);
setSelect('industry', 'banking');
check('feed banking: 1 visible', visibleFeed().length === 1, String(visibleFeed().length));
check('feed banking: empty hidden', feedEmpty.hidden === true);
check('feed banking: count line counts tiles+articles only',
  countEl.textContent === `Showing ${visibleTiles().length} of 62 figures · ${visibleArticles().length} of 114 articles`, countEl.textContent);
clearAll(); setSelect('jurisdiction', 'eu');
check('feed eu: 0 visible', visibleFeed().length === 0, String(visibleFeed().length));
check('feed eu: empty shows', feedEmpty.hidden === false);
// untagged entry (no identifiable article): appended now, stays
// visible under the same filter, and the empty state hides again.
const untaggedLi = new El('li', { attrs: {} });
feedList.appendChild(untaggedLi);
feedItems.push(untaggedLi);
setSelect('jurisdiction', 'eu'); // re-apply so the JS re-evaluates
check('feed eu + untagged: untagged visible', untaggedLi.style.display !== 'none');
check('feed eu + untagged: empty hidden', feedEmpty.hidden === true);
clearAll();
check('feed clear-all: all visible, empty hidden', visibleFeed().length === 4 && feedEmpty.hidden === true, `${visibleFeed().length} visible`);

console.log(`\n${pass} passed, ${fail} failed.`);
process.exit(fail ? 1 : 0);
