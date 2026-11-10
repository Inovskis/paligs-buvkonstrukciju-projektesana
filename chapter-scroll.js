// Pāreja uz nākamo nodaļu, ritinot ar peli lapas beigās.
//
// Kad lapa ir izritināta līdz galam un lasītājs turpina ritināt uz leju, apakšā parādās josla
// ar nākamās nodaļas nosaukumu, kas pakāpeniski piepildās. Kad josla ir pilna, atveras nākamā
// nodaļa. Ja lasītājs apstājas vai ritina atpakaļ, josla iztukšojas — nejauša pārlēkšana nenotiek.
(function () {
    'use strict';

    // Cik daudz "papildu ritināšanas" (px, wheel deltaY summa) vajag pārejai.
    var THRESHOLD = 500; // ~5 peles ritenīša klikšķi
    // Pēc šīs pauzes (ms) bez ritināšanas uzkrātais tiek atiestatīts.
    var RESET_AFTER = 900;
    // Pielaide (px), kurā lapa skaitās izritināta līdz galam.
    var BOTTOM_TOLERANCE = 4;

    var nextLink = document.querySelector('a[rel~="next"]');
    if (!nextLink) { return; }

    // Nākamās nodaļas nosaukums no sānjoslas (ar numuru), citādi — vispārīgs teksts.
    function nextTitle() {
        var target = nextLink.href.split('#')[0];
        var links = document.querySelectorAll('#sidebar .chapter a[href]');
        for (var i = 0; i < links.length; i++) {
            if (links[i].href.split('#')[0] === target) {
                return links[i].textContent.replace(/\s+/g, ' ').trim();
            }
        }
        return '';
    }

    var bar = document.createElement('div');
    bar.className = 'c-next-chapter';
    bar.setAttribute('aria-hidden', 'true');
    var label = document.createElement('span');
    label.className = 'c-next-chapter-label';
    label.textContent = 'Turpini ritināt — nākamā nodaļa';
    var title = document.createElement('span');
    title.className = 'c-next-chapter-title';
    title.textContent = nextTitle() || 'Nākamā nodaļa';
    var fill = document.createElement('span');
    fill.className = 'c-next-chapter-fill';
    bar.appendChild(label);
    bar.appendChild(title);
    bar.appendChild(fill);
    document.body.appendChild(bar);

    var amount = 0;
    var resetTimer = null;
    var leaving = false;

    function atBottom() {
        var el = document.scrollingElement || document.documentElement;
        return el.scrollTop + window.innerHeight >= el.scrollHeight - BOTTOM_TOLERANCE;
    }

    function render() {
        var ratio = Math.min(amount / THRESHOLD, 1);
        fill.style.transform = 'scaleX(' + ratio + ')';
        bar.classList.toggle('visible', amount > 0);
    }

    function reset() {
        amount = 0;
        render();
    }

    function sidebarIsOpenOverContent() {
        return window.innerWidth < 620 && (document.body.classList.contains('sidebar-visible') ||
            document.documentElement.classList.contains('sidebar-visible'));
    }

    window.addEventListener('wheel', function (event) {
        if (leaving) { return; }
        // Ritināšana sānjoslā, meklēšanas rezultātos vai ar Ctrl (tālummaiņa) netiek skaitīta.
        if (event.ctrlKey || (event.target.closest && event.target.closest('#sidebar, #searchbar-outer, #searchresults-outer'))) { return; }
        if (sidebarIsOpenOverContent()) { return; }

        if (event.deltaY <= 0 || !atBottom()) {
            if (amount) { reset(); }
            return;
        }
        // deltaMode 1 = rindas, 2 = lapas (dažas peles/OS); pārrēķina pikseļos.
        var delta = event.deltaY * (event.deltaMode === 1 ? 32 : event.deltaMode === 2 ? window.innerHeight : 1);
        amount += Math.min(delta, 200);
        render();

        clearTimeout(resetTimer);
        resetTimer = setTimeout(reset, RESET_AFTER);

        if (amount >= THRESHOLD) {
            leaving = true;
            bar.classList.add('done');
            window.location.href = nextLink.href;
        }
    }, { passive: true });

    window.addEventListener('scroll', function () {
        if (amount && !atBottom()) { reset(); }
    }, { passive: true });

    // Atgriežoties ar "Atpakaļ" pogu, lapa var nākt no kešatmiņas — joslai jābūt tukšai.
    window.addEventListener('pageshow', function () {
        leaving = false;
        bar.classList.remove('done');
        reset();
    });
})();
