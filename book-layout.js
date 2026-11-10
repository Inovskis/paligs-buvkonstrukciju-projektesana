// Maketa "Rasējuma lapa" papildinājumi, ko ar Markdown vien nevar izdarīt:
//   1) spiedogs lapas augšā (nodaļas numurs, nodaļa, grāmata);
//   2) ## apakšpunktu numerācija pēc sānjoslas numura (6.1 → 6.1.1, 6.1.2 …);
//   3) tabulās skaitliskās šūnas un īsie kategoriju apzīmējumi (A, C3, E1) pirmajā kolonnā;
//   4) citātu bloku veids pēc pirmā treknā vārda: Piezīme / Svarīgi / Piemērs, kā arī [!TIP] u.c.
// Skriptam jāizpildās pirms sidebar-headings.js (book.toml additional-js secībā),
// jo tas sānjoslā izmanto šeit piešķirtos numurus.
(function () {
    'use strict';

    var main = document.querySelector('#content main');
    if (!main) { return; }

    function text(node) { return (node && node.textContent || '').replace(/\s+/g, ' ').trim(); }

    // ---------- 1) un 2) Nodaļas numurs no sānjoslas ----------
    var activeLink = document.querySelector('#sidebar .chapter a.active');
    var numberEl = activeLink && activeLink.querySelector('strong');
    var sectionNo = numberEl ? text(numberEl).replace(/\.$/, '') : '';

    if (sectionNo) {
        var activeItem = activeLink.parentElement;
        var next = activeItem.nextElementSibling;
        var hasChildren = !!(next && !next.querySelector(':scope > a') && next.querySelector(':scope > ol.section'));

        // Nodaļas nosaukums: apakšnodaļai — vecāknodaļa, citādi pati lapa.
        var chapterTitle = '';
        var parentList = activeItem.parentElement;
        if (parentList && parentList.classList.contains('section')) {
            var holder = parentList.parentElement;
            var parentItem = holder && holder.previousElementSibling;
            var parentLink = parentItem && parentItem.querySelector(':scope > a');
            if (parentLink) {
                var clone = parentLink.cloneNode(true);
                var num = clone.querySelector('strong');
                if (num) { num.parentNode.removeChild(num); }
                chapterTitle = text(clone);
            }
        }
        if (!chapterTitle) {
            var own = activeLink.cloneNode(true);
            var ownNum = own.querySelector('strong');
            if (ownNum) { ownNum.parentNode.removeChild(ownNum); }
            chapterTitle = text(own);
        }
        var bookTitle = text(document.querySelector('.menu-title')) || document.title;

        var firstH1 = main.querySelector('h1');
        if (firstH1) {
            var stamp = document.createElement('div');
            stamp.className = 'c-stamp';
            stamp.setAttribute('aria-hidden', 'true');
            [['c-stamp-no', sectionNo], ['c-stamp-chapter', chapterTitle], ['c-stamp-book', bookTitle]].forEach(function (cell) {
                var span = document.createElement('span');
                span.className = cell[0];
                span.textContent = cell[1];
                stamp.appendChild(span);
            });
            firstH1.parentNode.insertBefore(stamp, firstH1);
        }

        // Nodaļas ievadlapai ar apakšnodaļām ## nenumurē, lai 6.1 nesakristu ar apakšnodaļu 6.1.
        if (!hasChildren) {
            var count = 0;
            Array.prototype.forEach.call(main.querySelectorAll('h2'), function (h2) {
                count += 1;
                var no = sectionNo + '.' + count;
                h2.setAttribute('data-c-no', no);
                var target = h2.querySelector('a.header') || h2;
                var span = document.createElement('span');
                span.className = 'c-no';
                span.setAttribute('aria-hidden', 'true');
                span.textContent = no;
                target.insertBefore(span, target.firstChild);
            });
        }
    }

    // ---------- 3) Tabulas ----------
    var NUMERIC = /^[\d\s.,:;–—\-−+±×·\/()%<>≤≥=~≈]+$/;
    Array.prototype.forEach.call(main.querySelectorAll('table tbody td'), function (td) {
        var t = text(td);
        if (t && /\d/.test(t) && NUMERIC.test(t) && !td.querySelector('script, .MathJax, mjx-container')) {
            td.classList.add('c-num');
        }
    });
    Array.prototype.forEach.call(main.querySelectorAll('table tbody td:first-child'), function (td) {
        var strong = td.children.length === 1 ? td.children[0] : null;
        if (!strong || strong.tagName !== 'STRONG') { return; }
        if (text(td) !== text(strong)) { return; }
        var t = text(strong);
        if (t.length >= 1 && t.length <= 4 && /^[A-Z][A-Z0-9]{0,3}$/.test(t)) {
            strong.classList.add('c-tag');
        }
    });

    // ---------- 4) Citātu bloku veidi ----------
    var ALERT = /^\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*/i;
    Array.prototype.forEach.call(main.querySelectorAll('blockquote'), function (bq) {
        var first = bq.firstElementChild;
        var kind = 'note';

        // GitHub stila brīdinājumi [!TIP] — mdBook 0.4 tos atstāj kā tekstu.
        if (first && first.tagName === 'P' && ALERT.test(first.textContent)) {
            var m = first.textContent.match(ALERT)[1].toUpperCase();
            if (m === 'WARNING' || m === 'CAUTION' || m === 'IMPORTANT') { kind = 'warn'; }
            var node = first.firstChild;
            while (node && node.nodeType === 3 && !node.nodeValue.trim()) { node = node.nextSibling; }
            if (node && node.nodeType === 3) {
                node.nodeValue = node.nodeValue.replace(ALERT, '');
                if (!node.nodeValue.trim()) {
                    var after = node.nextSibling;
                    node.parentNode.removeChild(node);
                    if (after && after.tagName === 'BR') { after.parentNode.removeChild(after); }
                }
            }
        }

        var lead = first && first.querySelector(':scope > strong:first-child');
        if (lead && first.firstChild !== lead) {
            var before = first.firstChild;
            if (!(before && before.nodeType === 3 && !before.nodeValue.trim() && before.nextSibling === lead)) { lead = null; }
        }
        var leadText = lead ? text(lead) : '';
        if (/^Svarīgi/i.test(leadText)) { kind = 'warn'; }
        else if (/^Piemēr/i.test(leadText)) { kind = 'ex'; }

        if (kind !== 'note') { bq.classList.add('c-' + kind); }
        // Īsu ievadvārdu ("Piezīme:", "Svarīgi!", "Piemērs:") parāda kā marķējumu.
        if (lead && leadText.replace(/[:!.]+$/, '').length <= 12) {
            lead.textContent = leadText.replace(/[:!.]+$/, '');
            lead.classList.add('c-label');
        }
    });
})();
