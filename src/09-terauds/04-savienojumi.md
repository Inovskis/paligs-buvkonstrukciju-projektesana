# Tērauda konstrukciju savienojumi

Tērauda būvkonstrukciju savienojumu (mezglu) aprēķini un konstruēšana tiek veikta saskaņā ar standartu **LVS EN 1993-1-8**. Mezgli var būt bīdizturīgi (šarnīri) vai momentizturīgi (stingie mezgli).

---

## Metrisko skrūvju parametri un nestspējas (8.8 un 10.9 klase)

Skrūvju ģeometriskie lielumi, šķērsgriezuma laukumi un viena stieņa bīdes un stiepes nestspēja saskaņā ar LVS EN 1993-1-8 Table 3.4:

| Skrūve | Diametrs \\(d\\) (mm) | Urbuma \\(\phi\\) \\(d_0\\) (mm)* | Vītnes laukums \\(A_s\\) (mm²) | Kāta laukums \\(A\\) (mm²) | Bīdes nestspēja \\(F_{v,Rd}\\) (kN) (8.8 klase) | Bīdes nestspēja \\(F_{v,Rd}\\) (kN) (10.9 klase) | Stiepes nestspēja \\(F_{t,Rd}\\) (kN) (8.8 klase) | Stiepes nestspēja \\(F_{t,Rd}\\) (kN) (10.9 klase) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **M12** | 12 | 13 | 84.3 | 113 | 32.4 | 33.7 | 48.6 | 60.7 |
| **M16** | 16 | 18 | 157.0 | 201 | 60.3 | 62.8 | 90.4 | 113.0 |
| **M20** | 20 | 22 | 245.0 | 314 | 94.1 | 98.0 | 141.1 | 176.4 |
| **M24** | 24 | 26 | 353.0 | 452 | 135.6 | 141.2 | 203.3 | 254.2 |
| **M27** | 27 | 30 | 459.0 | 573 | 176.3 | 183.6 | 264.4 | 330.5 |
| **M30** | 30 | 33 | 561.0 | 707 | 215.4 | 224.4 | 323.1 | 403.9 |
| **M36** | 36 | 39 | 817.0 | 1018 | 313.7 | 326.8 | 470.6 | 588.2 |

> **Piezīme par aprēķiniem:**
> - Bīdes nestspēja \\(F_{v,Rd} = \frac{\alpha_v \cdot f_{ub} \cdot A_s}{\gamma_{M2}}\\) ir norādīta **vienai bīdes plaknei**, kas šķērso skrūves vītņoto daļu (\\(\alpha_v = 0.6\\) klasei 8.8; \\(\alpha_v = 0.5\\) klasei 10.9). Ja bīdes plakne šķērso nevītņoto kātu, izmanto laukumu \\(A\\) un \\(\alpha_v = 0.6\\).
> - Stiepes nestspēja \\(F_{t,Rd} = \frac{k_2 \cdot f_{ub} \cdot A_s}{\gamma_{M2}}\\), kur \\(k_2 = 0.9\\) un \\(\gamma_{M2} = 1.25\\).
> - Aprēķinā pieņemts \\(\gamma_{M2} = 1.25\\), \\(f_{ub} = 800\text{ MPa}\\) (8.8 klase) un \\(1000\text{ MPa}\\) (10.9 klase).

---

## Bultskrūvju savienojumu kategorijas (LVS EN 1993-1-8 3.4)

Pirms savienojuma projektēšanas ir jāizvēlas atbilstoša aprēķina kategorija atkarībā no pārnesamajiem spēkiem (bīde vai stiepe) un pieļaujamajām deformācijām.

### Bīdes savienojumi (Shear connections)
* **Kategorija A: Bīdes savienojumi (Bearing type)**  
  Visbiežāk izmantotais standarta savienojuma veids. Pieļauj slīdi (skrūves vītne/kāts atspiežas pret urbuma malu). Skrūves nav iepriekš saspriegtas. Projektē, lai izturētu skrūves bīdi (\\(F_{v,Rd}\\)) un urbuma malas spiedi (\\(F_{b,Rd}\\)).
* **Kategorija B: Pret slīdi nodrošināti SLS (Slip-resistant at SLS)**  
  Skrūves (10.9 vai 8.8) ir iepriekš saspriegtas ar kontrolētu spēku. Ekspluatācijas (SLS) robežstāvoklī savienojums nedrīkst izslīdēt (jāuzņem bīde ar berzi). Nestspējas (ULS) robežstāvoklī slīde ir pieļaujama un savienojums darbojas kā Kategorija A.
* **Kategorija C: Pret slīdi nodrošināti ULS (Slip-resistant at ULS)**  
  Skrūves (10.9 vai 8.8) ir iepriekš saspriegtas. Savienojums nedrīkst izslīdēt pat nestspējas robežstāvoklī (ULS). Pārbauda uz slīdes pretestību (\\(F_{s,Rd}\\)) pie ULS slodzēm. Turklāt urbuma mala un skrūves bīde tiek pārbaudīta kā plastiskajai nestspējai. 

### Stiepes savienojumi (Tension connections)
* **Kategorija D: Nesaspriegti savienojumi (Non-preloaded)**  
  Tiek izmantotas parastas nesaspriegtas skrūves. Nestspēju nosaka skrūvju stiepes (\\(F_{t,Rd}\\)) vai plātnes caurumošanas (punching shear) stiprība.
* **Kategorija E: Saspriegti savienojumi (Preloaded)**  
  Tiek izmantotas iepriekš saspriegtas augstas stiprības skrūves (klase 8.8 vai 10.9). Saspriegums uzlabo noguruma pretestību un stingumu (piem., momentizturīgos atloku mezglos). Nestspēju rēķina tāpat kā Kategorijai D.

**Skrūvju urbumu izvietojuma robežattālumi** (\\(d_0\\) — urbuma diametrs, \\(t\\) — plānākās ārējās plātnes biezums):

<div class="table-wrapper">
  <table class="bolt-spacing">
    <thead><tr><th>Izvietojums</th><th>Skice</th><th>Robežattālumi (LVS EN 1993-1-8, 3.3. tab.)</th></tr></thead>
    <tbody>
      <tr><td><strong>Simetrisks urbumu izvietojums</strong></td><td><svg class="weld-fig" viewBox="0 0 240 142" width="240" role="img" aria-label="Simetrisks urbumu izvietojums"><path class="sk-plate" d="M200 20 H30 V120 H200"/><line class="sk-axis" x1="36" y1="52" x2="196" y2="52"/><line class="sk-axis" x1="36" y1="88" x2="196" y2="88"/><line class="sk-axis" x1="62" y1="26" x2="62" y2="114"/><line class="sk-axis" x1="98" y1="26" x2="98" y2="114"/><line class="sk-axis" x1="134" y1="26" x2="134" y2="114"/><circle class="sk-hole" cx="62" cy="52" r="6"/><circle class="sk-hole" cx="62" cy="88" r="6"/><circle class="sk-hole" cx="98" cy="52" r="6"/><circle class="sk-hole" cx="98" cy="88" r="6"/><circle class="sk-hole" cx="134" cy="52" r="6"/><circle class="sk-hole" cx="134" cy="88" r="6"/><text class="sk-text" x="40" y="40">d<tspan class="sk-sub" dy="3">0</tspan><tspan dy="-3"></tspan></text><line class="sk-ext" x1="30" y1="120" x2="30" y2="136"/><line class="sk-ext" x1="62" y1="94" x2="62" y2="136"/><line class="sk-ext" x1="98" y1="94" x2="98" y2="136"/><line class="sk-ext" x1="134" y1="94" x2="134" y2="136"/><line class="sk-thin" x1="30" y1="132" x2="62" y2="132"/><polygon class="sk-fill" points="30.0,132.0 36.0,129.7 36.0,134.3"/><polygon class="sk-fill" points="62.0,132.0 56.0,134.3 56.0,129.7"/><text class="sk-text" x="46.0" y="128.0" text-anchor="middle">e<tspan class="sk-sub" dy="3">1</tspan><tspan dy="-3"></tspan></text><line class="sk-thin" x1="62" y1="132" x2="98" y2="132"/><polygon class="sk-fill" points="62.0,132.0 68.0,129.7 68.0,134.3"/><polygon class="sk-fill" points="98.0,132.0 92.0,134.3 92.0,129.7"/><text class="sk-text" x="80.0" y="128.0" text-anchor="middle">p<tspan class="sk-sub" dy="3">1</tspan><tspan dy="-3"></tspan></text><line class="sk-thin" x1="98" y1="132" x2="134" y2="132"/><polygon class="sk-fill" points="98.0,132.0 104.0,129.7 104.0,134.3"/><polygon class="sk-fill" points="134.0,132.0 128.0,134.3 128.0,129.7"/><text class="sk-text" x="116.0" y="128.0" text-anchor="middle">p<tspan class="sk-sub" dy="3">1</tspan><tspan dy="-3"></tspan></text><line class="sk-ext" x1="200" y1="20" x2="216" y2="20"/><line class="sk-ext" x1="140" y1="52" x2="216" y2="52"/><line class="sk-ext" x1="140" y1="88" x2="216" y2="88"/><line class="sk-ext" x1="200" y1="120" x2="216" y2="120"/><line class="sk-thin" x1="212" y1="20" x2="212" y2="52"/><polygon class="sk-fill" points="212.0,20.0 214.3,26.0 209.7,26.0"/><polygon class="sk-fill" points="212.0,52.0 209.7,46.0 214.3,46.0"/><text class="sk-text" x="224" y="40" text-anchor="start">e<tspan class="sk-sub" dy="3">2</tspan><tspan dy="-3"></tspan></text><line class="sk-thin" x1="212" y1="52" x2="212" y2="88"/><polygon class="sk-fill" points="212.0,52.0 214.3,58.0 209.7,58.0"/><polygon class="sk-fill" points="212.0,88.0 209.7,82.0 214.3,82.0"/><text class="sk-text" x="224" y="74" text-anchor="start">p<tspan class="sk-sub" dy="3">2</tspan><tspan dy="-3"></tspan></text><line class="sk-thin" x1="212" y1="88" x2="212" y2="120"/><polygon class="sk-fill" points="212.0,88.0 214.3,94.0 209.7,94.0"/><polygon class="sk-fill" points="212.0,120.0 209.7,114.0 214.3,114.0"/><text class="sk-text" x="224" y="108" text-anchor="start">e<tspan class="sk-sub" dy="3">2</tspan><tspan dy="-3"></tspan></text><polygon class="sk-fill" points="70.0,8.0 78.0,5.0 78.0,11.0"/><polygon class="sk-fill" points="130.0,8.0 122.0,11.0 122.0,5.0"/><line class="sk-line" x1="70" y1="8" x2="130" y2="8"/></svg></td><td>\(e_1 \ge 1.2\,d_0\)<br>\(p_1 \ge 2.2\,d_0\)<br>\(e_2 \ge 1.2\,d_0\)<br>\(p_2 \ge 2.4\,d_0\)</td></tr>
      <tr><td><strong>Šahveida urbumu izvietojums spiedē</strong></td><td><svg class="weld-fig" viewBox="0 0 240 142" width="240" role="img" aria-label="Šahveida urbumu izvietojums spiedē"><path class="sk-plate" d="M200 20 H40 V120 H200"/><line class="sk-axis" x1="46" y1="50" x2="196" y2="50"/><line class="sk-axis" x1="46" y1="90" x2="196" y2="90"/><circle class="sk-hole" cx="62" cy="50" r="6"/><line class="sk-axis" x1="62" y1="40" x2="62" y2="60"/><circle class="sk-hole" cx="98" cy="50" r="6"/><line class="sk-axis" x1="98" y1="40" x2="98" y2="60"/><circle class="sk-hole" cx="134" cy="50" r="6"/><line class="sk-axis" x1="134" y1="40" x2="134" y2="60"/><circle class="sk-hole" cx="170" cy="50" r="6"/><line class="sk-axis" x1="170" y1="40" x2="170" y2="60"/><circle class="sk-hole" cx="80" cy="90" r="6"/><line class="sk-axis" x1="80" y1="80" x2="80" y2="100"/><circle class="sk-hole" cx="116" cy="90" r="6"/><line class="sk-axis" x1="116" y1="80" x2="116" y2="100"/><circle class="sk-hole" cx="152" cy="90" r="6"/><line class="sk-axis" x1="152" y1="80" x2="152" y2="100"/><text class="sk-text" x="46" y="38">d<tspan class="sk-sub" dy="3">0</tspan><tspan dy="-3"></tspan></text><line class="sk-ext" x1="62" y1="44" x2="62" y2="28"/><line class="sk-ext" x1="98" y1="44" x2="98" y2="28"/><line class="sk-thin" x1="62" y1="32" x2="98" y2="32"/><polygon class="sk-fill" points="62.0,32.0 68.0,29.7 68.0,34.3"/><polygon class="sk-fill" points="98.0,32.0 92.0,34.3 92.0,29.7"/><text class="sk-text" x="80.0" y="28.0" text-anchor="middle">p<tspan class="sk-sub" dy="3">1</tspan><tspan dy="-3"></tspan></text><line class="sk-ext" x1="80" y1="96" x2="80" y2="132"/><line class="sk-ext" x1="116" y1="96" x2="116" y2="132"/><line class="sk-thin" x1="80" y1="128" x2="116" y2="128"/><polygon class="sk-fill" points="80.0,128.0 86.0,125.7 86.0,130.3"/><polygon class="sk-fill" points="116.0,128.0 110.0,130.3 110.0,125.7"/><text class="sk-text" x="98.0" y="124.0" text-anchor="middle">p<tspan class="sk-sub" dy="3">1</tspan><tspan dy="-3"></tspan></text><line class="sk-thin" x1="186" y1="50" x2="186" y2="90"/><polygon class="sk-fill" points="186.0,50.0 188.3,56.0 183.7,56.0"/><polygon class="sk-fill" points="186.0,90.0 183.7,84.0 188.3,84.0"/><text class="sk-text" x="192" y="74" text-anchor="start">p<tspan class="sk-sub" dy="3">2</tspan><tspan dy="-3"></tspan></text><line class="sk-line" x1="8" y1="70" x2="34" y2="70"/><polygon class="sk-fill" points="34.0,70.0 26.0,73.0 26.0,67.0"/><line class="sk-line" x1="232" y1="70" x2="206" y2="70"/><polygon class="sk-fill" points="206.0,70.0 214.0,67.0 214.0,73.0"/></svg></td><td>\(p_1 \le \min(14t;\ 200\text{ mm})\)<br>\(p_2 \le \min(14t;\ 200\text{ mm})\)</td></tr>
      <tr><td><strong>Šahveida urbumu izvietojums stiepē</strong></td><td><svg class="weld-fig" viewBox="0 0 240 142" width="240" role="img" aria-label="Šahveida urbumu izvietojums stiepē"><path class="sk-plate" d="M200 30 H40 V120"/><line class="sk-axis" x1="40" y1="120" x2="200" y2="120"/><line class="sk-axis" x1="46" y1="60" x2="196" y2="60"/><line class="sk-axis" x1="46" y1="94" x2="196" y2="94"/><circle class="sk-hole" cx="62" cy="60" r="6"/><line class="sk-axis" x1="62" y1="50" x2="62" y2="70"/><circle class="sk-hole" cx="98" cy="60" r="6"/><line class="sk-axis" x1="98" y1="50" x2="98" y2="70"/><circle class="sk-hole" cx="134" cy="60" r="6"/><line class="sk-axis" x1="134" y1="50" x2="134" y2="70"/><circle class="sk-hole" cx="170" cy="60" r="6"/><line class="sk-axis" x1="170" y1="50" x2="170" y2="70"/><circle class="sk-hole" cx="80" cy="94" r="6"/><line class="sk-axis" x1="80" y1="84" x2="80" y2="104"/><circle class="sk-hole" cx="152" cy="94" r="6"/><line class="sk-axis" x1="152" y1="84" x2="152" y2="104"/><text class="sk-text" x="46" y="48">d<tspan class="sk-sub" dy="3">0</tspan><tspan dy="-3"></tspan></text><line class="sk-ext" x1="62" y1="54" x2="62" y2="12"/><line class="sk-ext" x1="98" y1="54" x2="98" y2="12"/><line class="sk-thin" x1="62" y1="16" x2="98" y2="16"/><polygon class="sk-fill" points="62.0,16.0 68.0,13.7 68.0,18.3"/><polygon class="sk-fill" points="98.0,16.0 92.0,18.3 92.0,13.7"/><text class="sk-text" x="80" y="11" text-anchor="middle">p<tspan class="sk-sub" dy="3">1,0</tspan><tspan dy="-3"></tspan></text><text class="sk-label" x="104" y="20">Ārējā rinda</text><line class="sk-ext" x1="80" y1="100" x2="80" y2="116"/><line class="sk-ext" x1="152" y1="100" x2="152" y2="116"/><line class="sk-thin" x1="80" y1="112" x2="152" y2="112"/><polygon class="sk-fill" points="80.0,112.0 86.0,109.7 86.0,114.3"/><polygon class="sk-fill" points="152.0,112.0 146.0,114.3 146.0,109.7"/><text class="sk-text" x="116" y="108" text-anchor="middle">p<tspan class="sk-sub" dy="3">1,i</tspan><tspan dy="-3"></tspan></text><text class="sk-label" x="160" y="114">Iekšējā rinda</text><line class="sk-line" x1="34" y1="132" x2="8" y2="132"/><polygon class="sk-fill" points="8.0,132.0 16.0,129.0 16.0,135.0"/><line class="sk-line" x1="206" y1="132" x2="232" y2="132"/><polygon class="sk-fill" points="232.0,132.0 224.0,135.0 224.0,129.0"/></svg></td><td>\(p_{1,0} \le \min(14t;\ 200\text{ mm})\)<br>\(p_{1,i} \le \min(28t;\ 400\text{ mm})\)</td></tr>
      <tr><td><strong>Pagarināts (ovāls) urbums</strong></td><td><svg class="weld-fig" viewBox="0 0 240 142" width="240" role="img" aria-label="Pagarināts urbums"><path class="sk-plate" d="M200 20 H40 V120 H200"/><rect class="sk-hole" x="76" y="56" width="78" height="24" rx="12"/><line class="sk-axis" x1="66" y1="68" x2="196" y2="68"/><line class="sk-axis" x1="88" y1="46" x2="88" y2="90"/><line class="sk-ext" x1="40" y1="20" x2="40" y2="8"/><line class="sk-ext" x1="88" y1="50" x2="88" y2="8"/><line class="sk-thin" x1="40" y1="12" x2="88" y2="12"/><polygon class="sk-fill" points="40.0,12.0 46.0,9.7 46.0,14.3"/><polygon class="sk-fill" points="88.0,12.0 82.0,14.3 82.0,9.7"/><text class="sk-text" x="64.0" y="8.0" text-anchor="middle">e<tspan class="sk-sub" dy="3">4</tspan><tspan dy="-3"></tspan></text><line class="sk-thin" x1="120" y1="56" x2="120" y2="80"/><polygon class="sk-fill" points="120.0,56.0 122.3,62.0 117.7,62.0"/><polygon class="sk-fill" points="120.0,80.0 117.7,74.0 122.3,74.0"/><text class="sk-text" x="126" y="72" text-anchor="start">d<tspan class="sk-sub" dy="3">0</tspan><tspan dy="-3"></tspan></text><line class="sk-ext" x1="76" y1="82" x2="76" y2="100"/><line class="sk-thin" x1="76" y1="96" x2="88" y2="96"/><polygon class="sk-fill" points="76.0,96.0 82.0,93.7 82.0,98.3"/><polygon class="sk-fill" points="88.0,96.0 82.0,98.3 82.0,93.7"/><text class="sk-text" x="92" y="104">0.5d<tspan class="sk-sub" dy="3">0</tspan><tspan dy="-3"></tspan></text><line class="sk-ext" x1="200" y1="120" x2="216" y2="120"/><line class="sk-ext" x1="158" y1="68" x2="216" y2="68"/><line class="sk-thin" x1="212" y1="68" x2="212" y2="120"/><polygon class="sk-fill" points="212.0,68.0 214.3,74.0 209.7,74.0"/><polygon class="sk-fill" points="212.0,120.0 209.7,114.0 214.3,114.0"/><text class="sk-text" x="222" y="98" text-anchor="start">e<tspan class="sk-sub" dy="3">3</tspan><tspan dy="-3"></tspan></text></svg></td><td>\(e_3 \ge 1.5\,d_0\)<br>\(e_4 \ge 1.5\,d_0\)</td></tr>
    </tbody>
  </table>
</div>

*Piezīme: vecākajā ENV redakcijā bija \\(e_2 \ge 1.5\,d_0\\) un \\(p_2 \ge 3.0\,d_0\\); tabulā dotas pašreizējās LVS EN 1993-1-8 minimālās vērtības.*

---

## Metinātie savienojumi (šuvju noformēšana)

Stūra šuvju izmērus nosaka pēc to rīkles biezuma \\(a\\) (metinājuma teorētiskais augstums) vai katetes izmēra \\(s\\) (\\(s \approx a \cdot \sqrt{2}\\)):

<div align="center" style="margin: 2em 0;">
  <svg width="320" height="270" viewBox="0 0 320 270" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Stūra šuve: rīkles biezums a un katete s">
    <style>
      .fw-plate { fill: #cbd5e0; stroke: #4a5568; stroke-width: 2; }
      .fw-weld { fill: #718096; stroke: #2d3748; stroke-width: 1.5; }
      .fw-throat { stroke: #e53e3e; stroke-width: 2; stroke-dasharray: 4 3; }
      .fw-dim { stroke: #2d3748; stroke-width: 1; fill: none; }
      .fw-ext { stroke: #2d3748; stroke-width: 0.75; fill: none; }
      .fw-text { font-family: 'IBM Plex Sans', sans-serif; font-size: 16px; font-weight: bold; fill: #2d3748; }
      .fw-text-a { font-family: 'IBM Plex Sans', sans-serif; font-size: 16px; font-weight: bold; fill: #e53e3e; }
    </style>
    <!-- Horizontālā plāksne -->
    <rect x="20" y="180" width="260" height="40" class="fw-plate" />
    <!-- Vertikālā plāksne -->
    <rect x="130" y="20" width="40" height="160" class="fw-plate" />
    <!-- Stūra šuve (katete s = 80) -->
    <polygon points="170,180 170,100 250,180" class="fw-weld" />
    <!-- Rīkles biezums a: no saknes perpendikulāri šuves virsmai -->
    <line x1="170" y1="180" x2="210" y2="140" class="fw-throat" />
    <text x="214" y="134" class="fw-text-a">a</text>
    <!-- Katete s vertikāli -->
    <line x1="174" y1="100" x2="282" y2="100" class="fw-ext" />
    <line x1="254" y1="180" x2="282" y2="180" class="fw-ext" />
    <line x1="275" y1="100" x2="275" y2="180" class="fw-dim" />
    <line x1="270" y1="105" x2="280" y2="95" class="fw-dim" />
    <line x1="270" y1="185" x2="280" y2="175" class="fw-dim" />
    <text x="284" y="146" class="fw-text">s</text>
    <!-- Katete s horizontāli (zem plāksnes) -->
    <line x1="170" y1="224" x2="170" y2="252" class="fw-ext" />
    <line x1="250" y1="224" x2="250" y2="252" class="fw-ext" />
    <line x1="170" y1="245" x2="250" y2="245" class="fw-dim" />
    <line x1="165" y1="250" x2="175" y2="240" class="fw-dim" />
    <line x1="245" y1="250" x2="255" y2="240" class="fw-dim" />
    <text x="205" y="264" class="fw-text">s</text>
  </svg>
</div>

**Šuvju veidi atkarībā no savienojuma veida:**

<div class="table-wrapper">
  <table class="weld-types">
    <thead><tr><th rowspan="2">Šuves veids</th><th colspan="3">Savienojuma veids</th></tr><tr><th>Sadursavienojums</th><th>T veida savienojums</th><th>Pārlaidsavienojums</th></tr></thead>
    <tbody>
      <tr><td><strong>Stūra šuve</strong></td><td></td><td><figure class="sk-cell"><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="skice"><rect class="sk-plate" x="20" y="4" width="8" height="42"/><rect class="sk-plate" x="28" y="19" width="58" height="12"/><polygon class="sk-weld" points="28,19 28,11 36,19"/><polygon class="sk-weld" points="28,31 28,39 36,31"/></svg></figure></td><td><figure class="sk-cell"><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="skice"><rect class="sk-plate" x="8" y="28" width="84" height="8"/><rect class="sk-plate" x="32" y="20" width="36" height="8"/><polygon class="sk-weld" points="32,20 32,28 24,28"/><polygon class="sk-weld" points="68,20 68,28 76,28"/></svg></figure></td></tr>
      <tr><td><strong>Gropes šuve (stūra šuve caurumā vai rievā)</strong></td><td></td><td></td><td><figure class="sk-cell"><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="skice"><rect class="sk-plate" x="6" y="28" width="74" height="8"/><rect class="sk-plate" x="22" y="20" width="22" height="8"/><rect class="sk-plate" x="56" y="20" width="38" height="8"/><polygon class="sk-weld" points="44,21 44,28 50,28"/><polygon class="sk-weld" points="56,21 56,28 50,28"/></svg></figure></td></tr>
      <tr><td><strong>Pilnīgi aizpildīta saduršuve</strong></td><td><figure class="sk-cell"><figcaption>vienpusēja V šuve</figcaption><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="vienpusēja V šuve"><rect class="sk-plate" x="8" y="18" width="42" height="14"/><rect class="sk-plate" x="50" y="18" width="42" height="14"/><polygon class="sk-weld" points="42,18 58,18 51,32 49,32"/></svg></figure><figure class="sk-cell"><figcaption>divpusēja V šuve</figcaption><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="divpusēja V šuve"><rect class="sk-plate" x="8" y="18" width="42" height="14"/><rect class="sk-plate" x="50" y="18" width="42" height="14"/><polygon class="sk-weld" points="42,18 58,18 51,25 58,32 42,32 49,25"/></svg></figure><figure class="sk-cell"><figcaption>vienpusēja U šuve</figcaption><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="vienpusēja U šuve"><rect class="sk-plate" x="8" y="18" width="42" height="14"/><rect class="sk-plate" x="50" y="18" width="42" height="14"/><path class="sk-weld" d="M43 18 H57 C57 26 53 28 52 32 H48 C47 28 43 26 43 18 Z"/></svg></figure><figure class="sk-cell"><figcaption>divpusēja U šuve</figcaption><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="divpusēja U šuve"><rect class="sk-plate" x="8" y="18" width="42" height="14"/><rect class="sk-plate" x="50" y="18" width="42" height="14"/><path class="sk-weld" d="M43 18 H57 C57 22 53 24 52 25 H48 C47 24 43 22 43 18 Z M43 32 H57 C57 28 53 26 52 25 H48 C47 26 43 28 43 32 Z"/></svg></figure></td><td><figure class="sk-cell"><figcaption>vienpusēja HV šuve</figcaption><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="vienpusēja HV šuve"><rect class="sk-plate" x="20" y="4" width="8" height="42"/><rect class="sk-plate" x="28" y="19" width="58" height="12"/><polygon class="sk-weld" points="28,19 38,19 30,31 28,31"/></svg></figure><figure class="sk-cell"><figcaption>divpusēja HV šuve</figcaption><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="divpusēja HV šuve"><rect class="sk-plate" x="20" y="4" width="8" height="42"/><rect class="sk-plate" x="28" y="19" width="58" height="12"/><polygon class="sk-weld" points="28,19 36,19 30,25 36,31 28,31"/></svg></figure><figure class="sk-cell"><figcaption>vienpusēja J šuve</figcaption><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="vienpusēja J šuve"><rect class="sk-plate" x="20" y="4" width="8" height="42"/><rect class="sk-plate" x="28" y="19" width="58" height="12"/><path class="sk-weld" d="M28 19 H37 C37 25 32 27 30 31 H28 Z"/></svg></figure><figure class="sk-cell"><figcaption>divpusēja J šuve</figcaption><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="divpusēja J šuve"><rect class="sk-plate" x="20" y="4" width="8" height="42"/><rect class="sk-plate" x="28" y="19" width="58" height="12"/><path class="sk-weld" d="M28 19 H36 C36 22 32 24 30 25 C32 26 36 28 36 31 H28 Z"/></svg></figure></td><td></td></tr>
      <tr><td><strong>Daļēji aizpildīta saduršuve</strong></td><td><figure class="sk-cell"><figcaption>divpusēja Y šuve</figcaption><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="divpusēja Y šuve"><rect class="sk-plate" x="8" y="18" width="42" height="14"/><rect class="sk-plate" x="50" y="18" width="42" height="14"/><polygon class="sk-weld" points="43,18 57,18 51,23 49,23"/><polygon class="sk-weld" points="43,32 57,32 51,27 49,27"/></svg></figure><figure class="sk-cell"><figcaption>divpusēja U šuve</figcaption><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="divpusēja U šuve"><rect class="sk-plate" x="8" y="18" width="42" height="14"/><rect class="sk-plate" x="50" y="18" width="42" height="14"/><path class="sk-weld" d="M44 18 H56 C56 21 53 22 52 23 H48 C47 22 44 21 44 18 Z M44 32 H56 C56 29 53 28 52 27 H48 C47 28 44 29 44 32 Z"/></svg></figure></td><td><figure class="sk-cell"><figcaption>divpusēja HY šuve</figcaption><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="divpusēja HY šuve"><rect class="sk-plate" x="20" y="4" width="8" height="42"/><rect class="sk-plate" x="28" y="19" width="58" height="12"/><polygon class="sk-weld" points="28,15 28,19 34,19 30,23 28,23"/><polygon class="sk-weld" points="28,35 28,31 34,31 30,27 28,27"/></svg></figure></td><td></td></tr>
      <tr><td><strong>Caurumu šuve</strong></td><td></td><td><figure class="sk-cell"><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="skice"><rect class="sk-plate" x="20" y="4" width="12" height="42"/><rect class="sk-plate" x="32" y="19" width="56" height="12"/><rect class="sk-weld" x="22" y="19" width="10" height="12"/></svg></figure></td><td><figure class="sk-cell"><svg class="weld-fig" viewBox="0 0 100 50" width="110" role="img" aria-label="skice"><rect class="sk-plate" x="10" y="6" width="80" height="38"/><rect class="sk-plate sk-dashed" x="30" y="12" width="66" height="26"/><circle class="sk-weld" cx="48" cy="20" r="5"/><circle class="sk-weld" cx="48" cy="31" r="5"/><rect class="sk-weld" x="64" y="21" width="20" height="9" rx="4.5"/></svg></figure></td></tr>
    </tbody>
  </table>
</div>

**Efektīvais rīkles biezums necaurmetinātām un koniskām šuvēm:**

<div class="table-wrapper">
  <table class="weld-throat">
    <thead><tr><th>Šuves veids</th><th>Skice</th><th>Efektīvais biezums</th></tr></thead>
    <tbody>
      <tr><td rowspan="2"><strong>Necaurmetināta šuve</strong></td><td><svg class="weld-fig" viewBox="0 0 200 116" width="220" role="img" aria-label="Necaurmetināta šuve T savienojumā"><rect class="sk-plate" x="30" y="72" width="150" height="16"/><rect class="sk-plate" x="90" y="22" width="30" height="50"/><polygon class="sk-weld" points="72,72 90,54 98,72"/><polygon class="sk-weld" points="138,72 120,54 112,72"/><line class="sk-ext" x1="90" y1="22" x2="90" y2="8"/><line class="sk-ext" x1="120" y1="22" x2="120" y2="8"/><line class="sk-thin" x1="90" y1="12" x2="120" y2="12"/><polygon class="sk-fill" points="90.0,12.0 96.0,9.7 96.0,14.3"/><polygon class="sk-fill" points="120.0,12.0 114.0,14.3 114.0,9.7"/><text class="sk-text" x="105.0" y="8.0" text-anchor="middle">t<tspan class="sk-sub" dy="3">1</tspan><tspan dy="-3"></tspan></text><line class="sk-thin" x1="112" y1="72" x2="129" y2="63"/><line class="sk-thin" x1="137" y1="46" x2="150" y2="70"/><polygon class="sk-fill" points="137.0,46.0 141.9,50.2 137.9,52.4"/><polygon class="sk-fill" points="150.0,70.0 145.1,65.8 149.1,63.6"/><text class="sk-text" x="150" y="52">a<tspan class="sk-sub" dy="3">1</tspan><tspan dy="-3"></tspan></text><line class="sk-thin" x1="98" y1="72" x2="81" y2="63"/><line class="sk-thin" x1="73" y1="46" x2="60" y2="70"/><polygon class="sk-fill" points="73.0,46.0 72.1,52.4 68.1,50.2"/><polygon class="sk-fill" points="60.0,70.0 60.9,63.6 64.9,65.8"/><text class="sk-text" x="48" y="52">a<tspan class="sk-sub" dy="3">2</tspan><tspan dy="-3"></tspan></text><line class="sk-ext" x1="98" y1="72" x2="98" y2="104"/><line class="sk-ext" x1="112" y1="72" x2="112" y2="104"/><line class="sk-thin" x1="98" y1="100" x2="112" y2="100"/><polygon class="sk-fill" points="98.0,100.0 104.0,97.7 104.0,102.3"/><polygon class="sk-fill" points="112.0,100.0 106.0,102.3 106.0,97.7"/><text class="sk-text" x="116" y="110">c</text></svg></td><td>\(a_1 = a_{nom,1} - 2\text{ mm}\)<br>\(a_2 = a_{nom,2} - 2\text{ mm}\)</td></tr>
      <tr><td><svg class="weld-fig" viewBox="0 0 200 80" width="220" role="img" aria-label="Necaurmetināta saduršuve"><rect class="sk-plate" x="22" y="30" width="38" height="28"/><rect class="sk-plate" x="60" y="30" width="38" height="28"/><polygon class="sk-weld" points="54,30 66,30 61,39 59,39"/><polygon class="sk-weld" points="54,58 66,58 61,49 59,49"/><line class="sk-ext" x1="16" y1="30" x2="54" y2="30"/><line class="sk-ext" x1="16" y1="39" x2="59" y2="39"/><line class="sk-thin" x1="14" y1="30" x2="14" y2="39"/><polygon class="sk-fill" points="14.0,30.0 16.3,36.0 11.7,36.0"/><polygon class="sk-fill" points="14.0,39.0 11.7,33.0 16.3,33.0"/><text class="sk-text" x="4" y="38">a</text><rect class="sk-plate" x="122" y="30" width="34" height="28"/><rect class="sk-plate" x="156" y="30" width="34" height="28"/><polygon class="sk-weld" points="150,58 162,58 157,47 155,47"/><line class="sk-ext" x1="116" y1="47" x2="155" y2="47"/><line class="sk-ext" x1="116" y1="58" x2="150" y2="58"/><line class="sk-thin" x1="114" y1="47" x2="114" y2="58"/><polygon class="sk-fill" points="114.0,47.0 116.3,53.0 111.7,53.0"/><polygon class="sk-fill" points="114.0,58.0 111.7,52.0 116.3,52.0"/><text class="sk-text" x="104" y="56">a</text></svg></td><td>\(a = a_{nom} - 2\text{ mm}\)</td></tr>
      <tr><td rowspan="2"><strong>Koniskas šuves</strong></td><td><small>apaļiem stieņiem</small><svg class="weld-fig" viewBox="0 0 200 120" width="220" role="img" aria-label="Koniskas šuves apaļiem stieņiem"><rect class="sk-plate" x="92" y="8" width="10" height="104"/><circle class="sk-plate" cx="72" cy="40" r="20"/><circle class="sk-plate" cx="72" cy="80" r="20"/><path class="sk-weld" d="M92 22 L92 40 Q88 28 80 22 Z"/><path class="sk-weld" d="M92 50 L92 70 L85 60 Z"/><line class="sk-ext" x1="102" y1="50" x2="118" y2="50"/><line class="sk-ext" x1="102" y1="70" x2="118" y2="70"/><line class="sk-thin" x1="114" y1="50" x2="114" y2="70"/><polygon class="sk-fill" points="114.0,50.0 116.3,56.0 111.7,56.0"/><polygon class="sk-fill" points="114.0,70.0 111.7,64.0 116.3,64.0"/><text class="sk-text" x="120" y="64">a</text><circle class="sk-plate" cx="166" cy="40" r="20"/><circle class="sk-plate" cx="166" cy="80" r="20"/><path class="sk-weld" d="M146 46 L146 74 L163 60 Z"/><line class="sk-ext" x1="146" y1="46" x2="146" y2="14"/><line class="sk-ext" x1="166" y1="20" x2="166" y2="14"/><line class="sk-thin" x1="146" y1="16" x2="166" y2="16"/><polygon class="sk-fill" points="146.0,16.0 152.0,13.7 152.0,18.3"/><polygon class="sk-fill" points="166.0,16.0 160.0,18.3 160.0,13.7"/><text class="sk-text" x="152" y="11">a</text></svg></td><td rowspan="2">Efektīvo biezumu \(a\) nosaka, kā parādīts skicē.</td></tr>
      <tr><td><small>liektiem profiliem</small><svg class="weld-fig" viewBox="0 0 200 112" width="220" role="img" aria-label="Koniskas šuves liektiem profiliem"><rect class="sk-plate" x="20" y="72" width="160" height="10"/><path class="sk-plate" d="M60 12 V58 A14 14 0 0 1 46 72 H22 V66 H46 A8 8 0 0 0 54 58 V12 Z"/><path class="sk-plate" d="M66 12 V58 A14 14 0 0 0 80 72 H104 V66 H80 A8 8 0 0 1 72 58 V12 Z"/><path class="sk-weld" d="M60 54 A14 14 0 0 1 56 66 L63 72 L70 66 A14 14 0 0 1 66 54 Z"/><line class="sk-ext" x1="56" y1="82" x2="56" y2="100"/><line class="sk-ext" x1="70" y1="82" x2="70" y2="100"/><line class="sk-thin" x1="56" y1="96" x2="70" y2="96"/><polygon class="sk-fill" points="56.0,96.0 62.0,93.7 62.0,98.3"/><polygon class="sk-fill" points="70.0,96.0 64.0,98.3 64.0,93.7"/><text class="sk-text" x="74" y="104">a</text><rect class="sk-plate" x="120" y="20" width="60" height="10"/><path class="sk-plate" d="M150 30 V102 H156 V44 A14 14 0 0 1 170 30 Z"/><path class="sk-weld" d="M156 30 H168 A12 12 0 0 0 156 42 Z"/><line class="sk-ext" x1="156" y1="20" x2="156" y2="8"/><line class="sk-ext" x1="166" y1="30" x2="166" y2="8"/><line class="sk-thin" x1="156" y1="12" x2="166" y2="12"/><polygon class="sk-fill" points="156.0,12.0 162.0,9.7 162.0,14.3"/><polygon class="sk-fill" points="166.0,12.0 160.0,14.3 160.0,9.7"/><text class="sk-text" x="170" y="12">a</text></svg></td></tr>
    </tbody>
  </table>
</div>

### Metināto šuvju apzīmējumi rasējumos (ISO 2553):


<div align="center" style="margin: 2em 0;">
  <svg width="540" height="150" viewBox="0 0 540 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Metinājuma apzīmējuma uzbūve">
    <style>
      .ws-line { stroke: #2d3748; stroke-width: 2; fill: none; }
      .ws-arrow { fill: #2d3748; }
      .ws-text { font-family: 'IBM Plex Sans', sans-serif; font-size: 14px; fill: #4a5568; text-anchor: middle; }
      .ws-text-bold { font-family: 'IBM Plex Sans', sans-serif; font-size: 14px; font-weight: bold; fill: #2d3748; }
    </style>
    <!-- Atsauces līnija -->
    <line x1="150" y1="80" x2="400" y2="80" class="ws-line" />
    <!-- Bultiņas līnija -->
    <line x1="150" y1="80" x2="80" y2="130" class="ws-line" />
    <polygon points="80,130 85,118 94,124" class="ws-arrow" />
    <!-- Astīte -->
    <polyline points="420,60 400,80 420,100" class="ws-line" />
    <!-- Teksti -->
    <text x="60" y="145" class="ws-text-bold">Bulta</text>
    <text x="275" y="30" class="ws-text">Otrā pusē (virs līnijas)</text>
    <text x="275" y="105" class="ws-text">Bultas pusē (zem līnijas)</text>
    <text x="485" y="85" class="ws-text">Astīte (piezīmes)</text>
    <text x="170" y="70" class="ws-text-bold">a / s</text>
    <text x="315" y="70" class="ws-text-bold">l (garums)</text>
  </svg>
</div>

**Apzīmējumu skaidrojums:**

<div class="table-wrapper">
  <table class="weld-symbols">
    <thead><tr><th>Nr.</th><th>Apzīmējums rasējumā</th><th>Metinājuma apraksts un izpildes kārtība</th></tr></thead>
    <tbody>
      <tr><td><strong>1</strong></td><td><svg class="weld-sym" viewBox="0 0 160 50" width="160" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M44 16 H136 M44 16 L16 46 M4 46 H72"/><path d="M86 16 V28 L98 16"/><text x="73" y="29" font-size="11" fill="currentColor" stroke="none" font-family="inherit">6</text></g><polygon points="16,46 23.7,42.2 19.3,38.1" fill="currentColor"/></svg></td><td>Nepārtraukta vienpusēja stūra šuve ar \(6\text{ mm}\) kāti (kateti) gar bultas norādīto līniju. Šuve atrodas bultas pusē.</td></tr>
      <tr><td><strong>2</strong></td><td><svg class="weld-sym" viewBox="0 0 160 50" width="160" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M44 16 H136 M44 16 L16 46 M4 46 H72"/><path d="M86 16 V4 L98 16"/></g><polygon points="16,46 23.7,42.2 19.3,38.1" fill="currentColor"/></svg></td><td>Tāpat kā 1, bet šuve atrodas pretējā pusē bultas norādītajai līnijai.</td></tr>
      <tr><td><strong>3</strong></td><td><svg class="weld-sym" viewBox="0 0 160 50" width="160" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M44 16 H136 M44 16 L16 46 M4 46 H72"/><path d="M86 16 V4 L98 16"/><path d="M86 16 V28 L98 16"/></g><polygon points="16,46 23.7,42.2 19.3,38.1" fill="currentColor"/></svg></td><td>Nepārtraukta divpusēja stūra šuve.</td></tr>
      <tr><td><strong>4</strong></td><td><svg class="weld-sym" viewBox="0 0 160 50" width="160" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M44 16 H136 M44 16 L16 46 M4 46 H72"/><path d="M86 16 V28 L98 16"/><text x="73" y="29" font-size="11" fill="currentColor" stroke="none" font-family="inherit">6</text><text x="101" y="29" font-size="11" fill="currentColor" stroke="none" font-family="inherit">70 (110)</text></g><polygon points="16,46 23.7,42.2 19.3,38.1" fill="currentColor"/></svg></td><td>Pārtraukta \(6\text{ mm}\) stūra šuve ar \(70\text{ mm}\) posmiem, izvietotiem ik pēc \(180\text{ mm}\). Tikai bultas pusē.</td></tr>
      <tr><td><strong>5</strong></td><td><svg class="weld-sym" viewBox="0 0 160 50" width="160" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M44 16 H136 M44 16 L16 46 M4 46 H72"/><path d="M78 16 V4 L90 16"/><path d="M86 16 V28 L98 16"/><text x="73" y="29" font-size="11" fill="currentColor" stroke="none" font-family="inherit">6</text><text x="101" y="29" font-size="11" fill="currentColor" stroke="none" font-family="inherit">70 (110)</text></g><polygon points="16,46 23.7,42.2 19.3,38.1" fill="currentColor"/></svg></td><td>Šaha veidā izvietota pārtraukta stūra šuve abās pusēs.</td></tr>
      <tr><td><strong>6</strong></td><td><svg class="weld-sym" viewBox="0 0 160 50" width="160" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M44 16 H136 M44 16 L16 46 M4 46 H72"/><path d="M44 16 V2"/><polygon points="44,2 56,5 44,8" fill="currentColor" stroke="none"/><path d="M86 16 V4 L98 16"/><path d="M86 16 V28 L98 16"/></g><polygon points="16,46 23.7,42.2 19.3,38.1" fill="currentColor"/></svg></td><td>Tāpat kā 3, bet karodziņš norāda, ka šuve veicama montāžas vietā (būvlaukumā).</td></tr>
      <tr><td><strong>7</strong></td><td><svg class="weld-sym" viewBox="0 0 160 50" width="160" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M44 16 H136 M44 16 L16 46 M4 46 H72"/><circle cx="44" cy="16" r="5"/><path d="M86 16 V28 L98 16"/><text x="73" y="29" font-size="11" fill="currentColor" stroke="none" font-family="inherit">6</text></g><polygon points="16,46 23.7,42.2 19.3,38.1" fill="currentColor"/></svg></td><td>Tāpat kā 1, bet šuve veicama pa visu elementa perimetru (aplis uz bultas lūzuma punkta).</td></tr>
      <tr><td><strong>8</strong></td><td><span class="weld-sym-item"><small>(a)</small><svg class="weld-sym" viewBox="0 0 90 50" width="90" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 18 H86 M2 44 H58"/><path d="M32 18 L22 30 L32 44"/><path d="M60 18 V30 M60 18 L68 28"/></g><polygon points="32,44 25.8,39.8 30,36.8" fill="currentColor"/></svg></span><span class="weld-sym-item"><small>(b)</small><svg class="weld-sym" viewBox="0 0 90 50" width="90" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 18 H86 M2 44 H58"/><path d="M32 18 L12 44"/><path d="M60 18 L53 29 M60 18 L67 29"/></g><polygon points="12,44 18.4,40 14.2,36.8" fill="currentColor"/></svg></span><span class="weld-sym-item"><small>(c)</small><svg class="weld-sym" viewBox="0 0 90 50" width="90" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 18 H86 M2 44 H58"/><path d="M32 18 L12 44"/><path d="M60 18 V21 M55 30 V26 A5 5 0 0 1 65 26 V30"/></g><polygon points="12,44 18.4,40 14.2,36.8" fill="currentColor"/></svg></span></td><td>Vienpusēji sadurmetinājumi: (a) vienpusēja slīpā šuve, (b) vienpusēja V-veida šuve, (c) vienpusēja U-veida šuve.</td></tr>
      <tr><td><strong>9</strong></td><td><span class="weld-sym-item"><small>(d)</small><svg class="weld-sym" viewBox="0 0 90 50" width="90" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 18 H86 M2 44 H58"/><path d="M32 18 L22 30 L32 44"/><path d="M60 6 V30 M60 18 L68 8 M60 18 L68 28"/></g><polygon points="32,44 25.8,39.8 30,36.8" fill="currentColor"/></svg></span><span class="weld-sym-item"><small>(e)</small><svg class="weld-sym" viewBox="0 0 90 50" width="90" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 18 H86 M2 44 H58"/><path d="M32 18 L12 44"/><path d="M53 7 L67 29 M67 7 L53 29"/></g><polygon points="12,44 18.4,40 14.2,36.8" fill="currentColor"/></svg></span><span class="weld-sym-item"><small>(f)</small><svg class="weld-sym" viewBox="0 0 90 50" width="90" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M32 18 H86 M2 44 H58"/><path d="M32 18 L12 44"/><path d="M60 15 V21 M55 6 V10 A5 5 0 0 0 65 10 V6 M55 30 V26 A5 5 0 0 1 65 26 V30"/></g><polygon points="12,44 18.4,40 14.2,36.8" fill="currentColor"/></svg></span></td><td>Divpusēji sadurmetinājumi: (d) divpusēja slīpā, (e) divpusēja V-veida, (f) divpusēja U-veida šuve.</td></tr>
      <tr><td><strong>10</strong></td><td><svg class="weld-sym" viewBox="0 0 160 50" width="160" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M44 16 H136 M44 16 L16 46 M4 46 H72"/><path d="M86 4 V28 M86 16 L94 6 M86 16 L94 26 M136 16 L144 9 M136 16 L144 23"/><text x="147" y="27" font-size="11" fill="currentColor" stroke="none" font-family="inherit">9</text></g><polygon points="16,46 23.7,42.2 19.3,38.1" fill="currentColor"/></svg></td><td>Tāpat kā 9(d), bet jāizmanto īpaša procedūra, kas norādīta metināšanas procedūras lapas 9. punktā (skaitlis astītē).</td></tr>
      <tr><td><strong>11</strong></td><td><svg class="weld-sym" viewBox="0 0 160 50" width="160" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M44 16 H136 M44 16 L16 46 M4 46 H72"/><path d="M86 16 L79 28 M86 16 L93 28 M78 31 Q86 38 94 31"/></g><polygon points="16,46 23.7,42.2 19.3,38.1" fill="currentColor"/></svg></td><td>Tāpat kā 8(b), bet šuvei jābūt ar izliektu virsmu.</td></tr>
      <tr><td><strong>12</strong></td><td><svg class="weld-sym" viewBox="0 0 160 50" width="160" height="50" role="img" aria-hidden="true"><g fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M44 16 H136 M44 16 L16 46 M4 46 H72"/><path d="M86 16 L79 28 M86 16 L93 28 M78 32 H94"/></g><polygon points="16,46 23.7,42.2 19.3,38.1" fill="currentColor"/></svg></td><td>Tāpat kā 8(b), bet šuves virsmai jābūt noslīpētai līdzenai.</td></tr>
      <tr><td><strong>13</strong></td><td>—</td><td>Tāpat kā 8(b), izmantojot metināšanas paliktni (backing bar).</td></tr>
      <tr><td><strong>14</strong></td><td>—</td><td>Tāpat kā 8(b), kur šuves sakne pirms pretmetināšanas ir jāizgriež/jāizstrādā.</td></tr>
      <tr><td><strong>15</strong></td><td>—</td><td>Tāpat kā 14, bet abas šuves virsmas pēc tam jānoslīpē līdzenas.</td></tr>
      <tr><td><strong>16</strong></td><td>—</td><td>Divpusēja slīpā saduršuve ar papildu stūra šuvēm labākai spriegumu pārejai un noguruma stiprībai.</td></tr>
      <tr><td><strong>17</strong></td><td>—</td><td>Sadursavienojums bez malu noslīpināšanas (taisnstūra šuve, tikai plānām loksnēm \(t \le 3\text{ mm}\)).</td></tr>
      <tr><td><strong>18</strong></td><td>—</td><td>Aizpildmetinājums (plug weld / apaļš vai iegarens aizmetināts caurums).</td></tr>
    </tbody>
  </table>
</div>

---

### Metināto šuvju nestspēja S355 tēraudam (\\(f_u = 490\text{ MPa}\\))

Robežstiprība uz vienu šuves garuma milimetru (aprēķināta pēc vienkāršotās metodes ar konservatīvu \\(f_u = 490\text{ MPa}\\)):

| Katete \\(s\\) (mm) | Rīkle \\(a\\) (mm) | Stiprība garenvirzienā \\(P_L\\) (kN/mm) | Stiprība šķērsvirzienā \\(P_T\\) (kN/mm) |
| :---: | :---: | :---: | :---: |
| 3.0 | 2.1 | 0.53 | 0.66 |
| 4.0 | 2.8 | 0.70 | 0.88 |
| 5.0 | 3.5 | 0.88 | 1.09 |
| 6.0 | 4.2 | 1.05 | 1.31 |
| 8.0 | 5.6 | 1.40 | 1.75 |
| 10.0 | 7.0 | 1.75 | 2.19 |
| 12.0 | 8.4 | 2.10 | 2.62 |
| 15.0 | 10.5 | 2.62 | 3.28 |
| 18.0 | 12.6 | 3.15 | 3.94 |
| 20.0 | 14.0 | 3.50 | 4.38 |
| 22.0 | 15.4 | 3.85 | 4.81 |
| 25.0 | 17.5 | 4.38 | 5.47 |

---

## Bīdizturīgi savienojumi ar ausi (Fin Plate Joints)

Šos savienojumus plaši izmanto sekundāro siju pieslēgšanai pie galvenajām sijām vai kolonnām. Tie uzņem tikai šķērsspēku (šarnīrs).

### 1. Skrūvju izvietojuma robežattālumi (M16 un M20, klase 8.8)

| Skrūve | Urbuma \\(\phi\\) \\(d_0\\) | Minimālais malas attālums \\(e_1, e_2\\) | Minimālais solis \\(p_1\\) (rindā) | Minimālais solis \\(p_2\\) (starp rindām) |
| :---: | :---: | :---: | :---: | :---: |
| **M16** | 18 mm | 22 mm (\\(1.2 d_0\\)) | 40 mm (\\(2.2 d_0\\)) | 44 mm (\\(2.4 d_0\\)) |
| **M20** | 22 mm | 27 mm (\\(1.2 d_0\\)) | 49 mm (\\(2.2 d_0\\)) | 53 mm (\\(2.4 d_0\\)) |

### 2. Standarta auss plākšņu konfigurācijas

| Skrūvju skaits | M16 izvietojums (solis) | M20 izvietojums (solis) | M16 auss izmēri (\\(B \times H \times t\\)) | M20 auss izmēri (\\(B \times H \times t\\)) |
| :---: | :--- | :--- | :---: | :---: |
| 2 skrūves | Vertikāli, 40 mm attālums | Vertikāli, 49 mm attālums | \\(110 \times 128 \times 10\text{ mm}\\) | \\(120 \times 148 \times 10\text{ mm}\\) |
| 3 skrūves | Vertikāli, \\(2 \times 40\text{ mm}\\) | Vertikāli, \\(2 \times 49\text{ mm}\\) | \\(110 \times 168 \times 10\text{ mm}\\) | \\(120 \times 198 \times 10\text{ mm}\\) |
| 4 skrūves | 2 rindās pa 2 (\\(44 \times 40\text{ mm}\\)) | 2 rindās pa 2 (\\(53 \times 49\text{ mm}\\)) | \\(154 \times 128 \times 10\text{ mm}\\) | \\(173 \times 148 \times 10\text{ mm}\\) |
| 6 skrūves | 2 rindās pa 3 (\\(44 \times 80\text{ mm}\\)) | 2 rindās pa 3 (\\(53 \times 98\text{ mm}\\)) | \\(154 \times 168 \times 10\text{ mm}\\) | \\(173 \times 198 \times 10\text{ mm}\\) |

---

### 3. Savienojuma šķērsspēka nestspēja (kN) IPE profiliem
*Auss biezums \\(t = 10\text{ mm}\\), S355 tērauds. Noteicošā ir sijas sieniņas bīde vai skrūvju nestspēja.*

| Profils | Sieniņa \\(t_w\\) (mm) | 2 × M16 | 3 × M16 | 4 × M16 (2x2) | 6 × M16 (2x3) | 2 × M20 | 3 × M20 | 4 × M20 (2x2) | 6 × M20 (2x3) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| IPE 180 | 5.3 | 76 | 114 | 152 | 228 | 119 | — | 238 | — |
| IPE 200 | 5.6 | 80 | 120 | 160 | 240 | 126 | — | 251 | 376 |
| IPE 240 | 6.2 | 89 | 133 | 178 | 266 | 139 | 209 | 278 | 418 |
| IPE 300 | 7.1 | 101 | 152 | 203 | 304 | 159 | 239 | 318 | 478 |
| IPE 360 | 8.0 | 114 | 171 | 228 | 342 | 179 | 269 | 359 | 538 |
| IPE 400 | 8.6 | 123 | 184 | 245 | 368 | 193 | 289 | 386 | 578 |
| IPE 450 | 9.4 | 134 | 201 | 268 | 403 | 211 | 316 | 421 | 632 |
| IPE 500 | 10.2 | 146 | 218 | 291 | 437 | 229 | 343 | 458 | 687 |

---

### 4. Savienojuma šķērsspēka nestspēja (kN) HEA profiliem

| Profils | Sieniņa \\(t_w\\) (mm) | 2 × M16 | 3 × M16 | 4 × M16 (2x2) | 6 × M16 (2x3) | 2 × M20 | 3 × M20 | 4 × M20 (2x2) | 6 × M20 (2x3) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| HEA 160 | 6.0 | 86 | 129 | 172 | 258 | 135 | — | 269 | — |
| HEA 180 | 6.0 | 86 | 129 | 172 | 258 | 135 | — | 269 | — |
| HEA 200 | 6.5 | 93 | 139 | 186 | 279 | 146 | 219 | 292 | 437 |
| HEA 240 | 7.5 | 107 | 161 | 215 | 322 | 168 | 253 | 337 | 505 |
| HEA 260 | 7.5 | 107 | 161 | 215 | 322 | 168 | 253 | 337 | 505 |
| HEA 280 | 8.0 | 114 | 171 | 228 | 342 | 179 | 269 | 359 | 538 |
| HEA 300 | 8.5 | 122 | 182 | 243 | 365 | 191 | 287 | 383 | 574 |

*Slodžu grupu krāsu kodi (projektēšanas atvieglošanai):*
- *Zaļš: \\(< 100\text{ kN}\\)*
- *Zils: \\(100 \dots 200\text{ kN}\\)*
- *Gaiši oranžs: \\(200 \dots 300\text{ kN}\\)*
- *Tumši oranžs: \\(> 300\text{ kN}\\)*

---

## Metinājuma šuves izvēle saskaņā ar skrūvju nestspēju

Lai garantētu, ka savienojuma metinājums nav vājākais posms, šuves tiek dimensionētas pēc nosacījuma:
\\[V_{Rd,\text{weld}} \ge 1.2 \cdot V_{Rd,\text{bolts}}\\]
Auss tiek metināta ar divpusēju stūra šuvi (rīkle \\(a\\)) pie nesošā elementa.

| Skrūves | Skrūvju grupas nestspēja | Nepieciešamā šuves pretestība | Auss augstums | Izvēlētais šuves biezums \\(a\\) | Šuvju faktiskā nestspēja |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 2 × M16 | 121 kN | 145 kN | 128 mm | **\\(a = 4\text{ mm}\\)** | 149 kN |
| 3 × M16 | 181 kN | 217 kN | 168 mm | **\\(a = 5\text{ mm}\\)** | 249 kN |
| 4 × M16 | 241 kN | 289 kN | 128 mm | **\\(a = 7\text{ mm}\\)** | 334 kN |
| 6 × M16 | 362 kN | 434 kN | 168 mm | **\\(a = 8\text{ mm}\\)** | 481 kN |
| 2 × M20 | 188 kN | 226 kN | 148 mm | **\\(a = 6\text{ mm}\\)** | 270 kN |
| 3 × M20 | 282 kN | 338 kN | 198 mm | **\\(a = 6\text{ mm}\\)** | 361 kN |
| 4 × M20 | 376 kN | 451 kN | 148 mm | **\\(a = 9\text{ mm}\\)** | 481 kN |
| 6 × M20 | 565 kN | 678 kN | 198 mm | **\\(a = 9\text{ mm}\\)** | 723 kN |

---

## Rekomendētie risinājumi pēc siju šķērsgriezuma

| Profils | Profila augstums | Ieteicamais mezgla risinājums | Alternatīvais risinājums |
| :--- | :---: | :--- | :--- |
| IPE 180 | 180 mm | 3 × M16 vertikāli (114 kN) | 4 × M16 rindā 2x2 (152 kN) |
| IPE 200 | 200 mm | 4 × M16 rindā 2x2 (160 kN) | 4 × M20 rindā 2x2 (251 kN) |
| IPE 240 | 240 mm | 4 × M20 rindā 2x2 (278 kN) | 3 × M20 vertikāli (209 kN) |
| IPE 300+ | 300+ mm | 6 × M20 rindā 2x3 (478+ kN) | 4 × M20 rindā 2x2 (318+ kN) |
| HEA 160-180 | 160-180 mm | 3 × M16 vertikāli (129 kN) | 4 × M16 rindā 2x2 (172 kN) |
| HEA 200 | 200 mm | 4 × M20 rindā 2x2 (292 kN) | 3 × M20 vertikāli (219 kN) |
| HEA 240+ | 240+ mm | 6 × M20 rindā 2x3 (505+ kN) | 4 × M20 rindā 2x2 (337+ kN) |

---

## Rekomendētie risinājumi pēc šķērsspēka lieluma

| Aprēķina šķērsspēks \\(V_{Ed}\\) | 1. Izvēles risinājums | 2. Izvēles risinājums | 3. Izvēles risinājums |
| :--- | :--- | :--- | :--- |
| \\(50 \dots 100\text{ kN}\\) | 3 × M16 vertikāli | 2 × M16 vertikāli | 2 × M20 vertikāli |
| \\(100 \dots 150\text{ kN}\\) | 4 × M16 (2x2) | 3 × M16 vertikāli | 2 × M20 vertikāli |
| \\(150 \dots 250\text{ kN}\\) | 4 × M20 (2x2) | 4 × M16 (2x2) | 3 × M20 vertikāli |
| \\(250 \dots 400\text{ kN}\\) | 6 × M20 (2x3) | 6 × M16 (2x3) | 4 × M20 (2x2) |
| \\(> 400\text{ kN}\\) | 6 × M20 (2x3) | 6 × M20 (2x3) | 6 × M20 (2x3) |

---

## Siju augstuma ierobežojumi skrūvju izvietošanai

Lai skrūves fiziski ietilptu sijas augstumā, ievērojot minimālos attālumus līdz siju plauktiem un rādiusiem:

| Skrūvju konfigurācija | Nepieciešamais sijas sieniņas augstums | Piemērojamie IPE/HEA profili |
| :--- | :---: | :--- |
| 3 × M16 vertikāli | 168 mm | IPE 180+ / HEA 160+ |
| 3 × M20 vertikāli | 198 mm | IPE 240+ / HEA 200+ |
| 6 × M16 (2x3) | 208 mm | IPE 240+ / HEA 200+ |
| 6 × M20 (2x3) | 296 mm | IPE 360+ / HEA 280+ |
