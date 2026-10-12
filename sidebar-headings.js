// Atvērtās lapas virsraksti kreisajā sānjoslā, zem aktīvās nodaļas.
//
// mdBook 0.4 sānjoslu veido tikai no SUMMARY.md, tāpēc virsraksti lapas iekšienē
// (## ...) tajā nav redzami. Šis skripts tos pievieno kā trešo līmeni:
//   nodaļa (Tērauda konstrukcijas) > apakšnodaļa (Papildu prasības) > virsraksts.
// Lasot lapu, sānjoslā tiek iezīmēts virsraksts, kuru lasītājs šobrīd redz.
(function () {
    'use strict';

    // Kuri virsraksti tiek rādīti. Ja vajag arī ### līmeni: '#content main h2, #content main h3'.
    var HEADING_SELECTOR = '#content main h2';
    // Virsraksts skaitās "sasniegts", kad tā augšmala ir augstāk par šo atstatumu (px no loga augšas).
    // Jābūt lielākam par mdBook izvēlnes joslas augstumu, jo uz virsrakstu pārlec zem tās.
    var REACHED_OFFSET = 100;
    // mdBook sānjosla pārklāj saturu zem šī loga platuma (px).
    var NARROW_WIDTH = 620;

    var sidebar = document.getElementById('sidebar');
    if (!sidebar) { return; }
    var scrollbox = sidebar.querySelector('.sidebar-scrollbox');
    var activeLink = sidebar.querySelector('.chapter a.active');
    if (!scrollbox || !activeLink) { return; }

    var headings = document.querySelectorAll(HEADING_SELECTOR);
    if (!headings.length) { return; }

    // Virsraksta teksts sānjoslai. MathJax 2 formulu \( ... \) aizstāj ar zīmētu attēlojumu un TeX tekstu
    // glabā <script type="math/tex">; ja MathJax jau ir paspējis, formula tiek atjaunota TeX pierakstā,
    // lai to sānjoslā uzzīmētu no jauna.
    function labelFor(heading) {
        var source = heading.querySelector('a.header') || heading;
        var copy = source.cloneNode(true);
        Array.prototype.forEach.call(
            copy.querySelectorAll('.MathJax, .MathJax_Preview, .MathJax_Display, .MJX_Assistive_MathML'),
            function (node) { node.parentNode.removeChild(node); }
        );
        Array.prototype.forEach.call(copy.querySelectorAll('script[type^="math/tex"]'), function (node) {
            node.parentNode.replaceChild(document.createTextNode('\\(' + node.textContent + '\\)'), node);
        });
        return copy.textContent.replace(/\s+/g, ' ').trim();
    }

    var holder = document.createElement('li');
    // "expanded" vajadzīgs, lai mdBook noteikums ".chapter li:not(.expanded) + li > ol" neapslēptu
    // apakšnodaļu sarakstu, kas seko aiz šī elementa.
    holder.className = 'chapter-item expanded page-headings';
    var list = document.createElement('ol');
    list.className = 'section page-headings-list';
    holder.appendChild(list);

    var items = [];
    Array.prototype.forEach.call(headings, function (heading) {
        if (!heading.id) { return; }
        var item = document.createElement('li');
        item.className = 'page-heading';
        var link = document.createElement('a');
        link.href = '#' + heading.id;
        link.textContent = labelFor(heading);
        item.appendChild(link);
        list.appendChild(item);
        items.push({ heading: heading, link: link, item: item });
    });
    if (!items.length) { return; }

    var activeItem = activeLink.parentElement;
    activeItem.parentNode.insertBefore(holder, activeItem.nextSibling);

    // Ja MathJax jau ir ielādēts, formulas jaunajā sarakstā jāzīmē pašam; ja nav, MathJax tās atradīs startā.
    if (window.MathJax && window.MathJax.Hub && window.MathJax.Hub.Queue) {
        window.MathJax.Hub.Queue(['Typeset', window.MathJax.Hub, list]);
    }

    // Sānjosla ir ritināma; iezīmētajam punktam jāpaliek redzamam.
    function keepVisible(element) {
        var box = scrollbox.getBoundingClientRect();
        var rect = element.getBoundingClientRect();
        var margin = 40;
        if (rect.top < box.top + margin) {
            scrollbox.scrollTop += rect.top - box.top - margin;
        } else if (rect.bottom > box.bottom - margin) {
            scrollbox.scrollTop += rect.bottom - box.bottom + margin;
        }
    }

    var current = null;
    function update() {
        var reached = null;
        for (var i = 0; i < items.length; i++) {
            if (items[i].heading.getBoundingClientRect().top <= REACHED_OFFSET) {
                reached = items[i];
            } else {
                break;
            }
        }
        if (reached === current) { return; }
        if (current) {
            current.link.classList.remove('current');
            current.link.removeAttribute('aria-current');
        }
        if (reached) {
            reached.link.classList.add('current');
            reached.link.setAttribute('aria-current', 'location');
            keepVisible(reached.item);
        }
        current = reached;
    }

    var queued = false;
    function onScroll() {
        if (queued) { return; }
        queued = true;
        window.requestAnimationFrame(function () {
            queued = false;
            update();
        });
    }
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('hashchange', onScroll);
    window.addEventListener('load', update);
    update();

    // Šaurā logā sānjosla aizsedz saturu, tāpēc pēc pārejas uz virsrakstu tā tiek aizvērta.
    // Klasi "sidebar-visible" mdBook 0.4 liek uz <body>, jaunākās versijas — uz <html>.
    function sidebarIsOpen() {
        return document.body.classList.contains('sidebar-visible') ||
            document.documentElement.classList.contains('sidebar-visible');
    }
    list.addEventListener('click', function (event) {
        var target = event.target;
        while (target && target !== list && target.tagName !== 'A') { target = target.parentNode; }
        if (!target || target === list) { return; }
        var toggle = document.getElementById('sidebar-toggle');
        if (toggle && window.innerWidth < NARROW_WIDTH && sidebarIsOpen()) {
            toggle.click();
        }
    });
})();
