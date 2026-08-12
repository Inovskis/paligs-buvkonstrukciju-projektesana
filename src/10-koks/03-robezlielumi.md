# Siju izlieču robežvērtības (SLS)

Koka konstrukciju deformācijas lietojamības robežstāvoklī (SLS) pārbauda, salīdzinot aprēķinātās izlieces ar robežvērtībām saskaņā ar LVS EN 1995-1-1.

---

## Izlieču robežvērtības (\\(w_{\text{limit}}\\))

Saskaņā ar LVS EN 1995-1-1/NA ieteicamās robežvērtības siju un plātņu vertikālajām izliecēm:

| Konstrukcijas elements / Shēma | Momentānā izliece \\(w_{\text{inst}}\\) | Neto galīgā izliece \\(w_{\text{net,fin}}\\) | Kopējā galīgā izliece \\(w_{\text{fin}}\\) |
| :--- | :---: | :---: | :---: |
| Sijas uz diviem balstiem (pārsegumi) | \\(L / 400\\) | \\(L / 300\\) | \\(L / 200\\) |
| Konsolsijas (pārkares) | \\(L / 200\\) | \\(L / 150\\) | \\(L / 100\\) |
| Spāres, kopturi un jumta elementi (bez trauslas apdares) | \\(L / 250\\) | \\(L / 200\\) | \\(L / 150\\) |

*Apzīmējumi: \\(L\\) — sijas laidums (konsoles gadījumā \\(L\\) ir konsoles brīvais garums).*

---

## Izlieces komponentes un aprēķina shēma

Koka konstrukciju izliece sastāv no elastīgās (momentānās) izlieces un šļūdes izlieces (mitruma un ilglaicīgas slodzes ietekmē).

<div align="center" style="margin: 2em 0;">
  <svg width="600" height="260" viewBox="0 0 600 260" xmlns="http://www.w3.org/2000/svg">
    <style>
      .baseline { stroke: #a0aec0; stroke-width: 2; stroke-dasharray: 6,4; }
      .curve-precamber { fill: none; stroke: #48bb78; stroke-width: 3; stroke-dasharray: 4,4; }
      .curve-inst { fill: none; stroke: #3182ce; stroke-width: 3; }
      .curve-fin { fill: none; stroke: #e53e3e; stroke-width: 3; }
      .arrow { stroke: #2d3748; stroke-width: 1.5; fill: none; }
      .arrow-head { fill: #2d3748; }
      .text-small { font-family: 'Inter', sans-serif; font-size: 13px; fill: #4a5568; }
      .text-bold { font-family: 'Inter', sans-serif; font-size: 14px; fill: #2d3748; font-weight: bold; font-style: italic; }
      .support { fill: #e2e8f0; stroke: #4a5568; stroke-width: 2; }
    </style>

    <!-- Atbalsti -->
    <polygon points="50,130 40,150 60,150" class="support"/>
    <polygon points="550,130 540,150 560,150" class="support"/>
    <line x1="30" y1="150" x2="570" y2="150" class="baseline" style="stroke:#4a5568; stroke-dasharray: none;" />

    <!-- Sākotnējā horizontālā ass (bez priekšizlieces) -->
    <line x1="50" y1="130" x2="550" y2="130" class="baseline" />

    <!-- Priekšizliece w_c (uz augšu) -->
    <path d="M50 130 Q300 30 550 130" class="curve-precamber" />
    
    <!-- Momentānā izliece no horizontāles -->
    <!-- (Kopējā momentānā, rēķinot no horizontāles = w_inst - w_c) -->
    <!-- Parasti grafikos w_inst mēra no priekšizlieces līnijas. -->
    <path d="M50 130 Q300 170 550 130" class="curve-inst" />

    <!-- Galīgā izliece -->
    <path d="M50 130 Q300 230 550 130" class="curve-fin" />

    <!-- Bultiņas un apzīmējumi vidū -->
    <line x1="300" y1="80" x2="300" y2="130" class="arrow" />
    <polygon points="300,80 297,87 303,87" class="arrow-head"/>
    <polygon points="300,130 297,123 303,123" class="arrow-head"/>
    <text x="310" y="110" class="text-bold" fill="#48bb78">w_c</text>

    <!-- Momentānā -->
    <!-- w_inst no w_c līdz inst -->
    <line x1="280" y1="80" x2="280" y2="150" class="arrow" />
    <polygon points="280,150 277,143 283,143" class="arrow-head"/>
    <polygon points="280,80 277,87 283,87" class="arrow-head"/>
    <text x="235" y="125" class="text-bold" fill="#3182ce">w_inst</text>

    <!-- Šļūde (w_creep) -->
    <line x1="300" y1="150" x2="300" y2="180" class="arrow" />
    <polygon points="300,150 297,157 303,157" class="arrow-head"/>
    <polygon points="300,180 297,173 303,173" class="arrow-head"/>
    <text x="310" y="170" class="text-bold" fill="#e53e3e">w_creep</text>

    <!-- Neto galīgā (no horizontāles) -->
    <line x1="330" y1="130" x2="330" y2="180" class="arrow" />
    <polygon points="330,130 327,137 333,137" class="arrow-head"/>
    <polygon points="330,180 327,173 333,173" class="arrow-head"/>
    <text x="340" y="160" class="text-bold">w_net,fin</text>

    <!-- Leģenda -->
    <text x="30" y="30" class="text-small">
       <tspan fill="#48bb78" font-weight="bold">---</tspan> Priekšizliece
    </text>
    <text x="30" y="50" class="text-small">
       <tspan fill="#3182ce" font-weight="bold">───</tspan> Momentānā (elastīgā) stāvoklis
    </text>
    <text x="30" y="70" class="text-small">
       <tspan fill="#e53e3e" font-weight="bold">───</tspan> Galīgais (šļūdes) stāvoklis
    </text>
  </svg>
</div>

### Deformācijas komponentu definīcijas:
- **\\(w_c\\)** — konstruktīvā priekšizliece (precamber) nenoslogotā stāvoklī;
- **\\(w_{\text{inst}}\\)** — momentānā (elastīgā) izliece tūlīt pēc slodzes pielikšanas;
- **\\(w_{\text{creep}}\\)** — šļūdes (deformāciju pieauguma) izlieces daļa laika gaitā;
- **\\(w_{\text{fin}}\\)** — galīgā (kopējā) izliece, ņemot vērā šļūdi: \\(w_{\text{fin}} = w_{\text{inst}} + w_{\text{creep}}\\);
- **\\(w_{\text{net,fin}}\\)** — neto galīgā izliece, kas paliek pēc priekšizlieces \\(w_c\\) atskaitīšanas:
  \\[w_{\text{net,fin}} = w_{\text{fin}} - w_c\\]

---

## Izlieču aprēķina formulas (ilglaicīgo efektu ievērtēšana)

Izlieces komponentes nosaka, izmantojot šļūdes koeficientu \\(k_{\text{def}}\\) (skat. [Slodžu ilgumi un modifikācijas koeficienti](02-koeficienti.md)):

### 1. Momentānā izliece:
\\[w_{\text{inst}} = w_{\text{inst},g} + w_{\text{inst},q,1} + \sum w_{\text{inst},q,i}\\]

### 2. Galīgā izliece:
- **Pastāvīgajām slodzēm \\(G\\):**
  \\[w_{\text{fin},g} = w_{\text{inst},g} \cdot (1 + k_{\text{def}})\\]
- **Vadošajai mainīgajai slodzei \\(Q_1\\):**
  \\[w_{\text{fin},q,1} = w_{\text{inst},q,1} \cdot (1 + \psi_2 \cdot k_{\text{def}})\\]
- **Pavadītājām mainīgajām slodzēm \\(Q_i\\):**
  \\[w_{\text{fin},q,i} = w_{\text{inst},q,i} \cdot (\psi_{0,i} + \psi_{2,i} \cdot k_{\text{def}})\\]

Kopējā galīgā izliece \\(w_{\text{fin}}\\) ir visu galīgo izlieču summa:
\\[w_{\text{fin}} = w_{\text{fin},g} + w_{\text{fin},q,1} + \sum w_{\text{fin},q,i}\\]

*Kur \\(\psi_0\\) un \\(\psi_2\\) ir slodžu kombināciju koeficienti saskaņā ar LVS EN 1990 (piemēram, lietderīgajai slodzei dzīvojamās ēkās \\(\psi_2 = 0,3\\)).*
