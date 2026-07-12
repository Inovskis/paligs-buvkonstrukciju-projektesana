# Betona un stiegrojuma fizikāli mehāniskās īpašības

Šajā sadaļā apkopotas būvkonstrukciju aprēķiniem nepieciešamās materiālu īpašības saskaņā ar LVS EN 1992-1-1.

---

## Betona stiprības un deformācijas raksturlielumi

Tālāk dotajā tabulā ir apkopoti betona stiprības klašu parametri (no C12/15 līdz C90/105) saskaņā ar **LVS EN 1992-1-1 Table 3.1**:

| Lielums (Parametrs) | C12/15 | C16/20 | C20/25 | C25/30 | C30/37 | C35/45 | C40/50 | C45/55 | C50/60 | C55/67 | C60/75 | C70/85 | C80/95 | C90/105 | Analītiskā izteiksme / Piezīmes |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **$f_{ck}$** (MPa) | 12 | 16 | 20 | 25 | 30 | 35 | 40 | 45 | 50 | 55 | 60 | 70 | 80 | 90 | Betona raksturīgā cilindriskā stiprība spiedē (5% nodrošinājums) |
| **$f_{ck,cube}$** (MPa) | 15 | 20 | 25 | 30 | 37 | 45 | 50 | 55 | 60 | 67 | 75 | 85 | 95 | 105 | Betona raksturīgā kubiskā stiprība spiedē |
| **$f_{cm}$** (MPa) | 20 | 24 | 28 | 33 | 38 | 43 | 48 | 53 | 58 | 63 | 68 | 78 | 88 | 98 | $f_{cm} = f_{ck} + 8$ (vidējā spiedes stiprība) |
| **$f_{ctm}$** (MPa) | 1,6 | 1,9 | 2,2 | 2,6 | 2,9 | 3,2 | 3,5 | 3,8 | 4,1 | 4,2 | 4,4 | 4,6 | 4,8 | 5,0 | $f_{ctm} = 0,30 \cdot f_{ck}^{2/3}$ (līdz C50/60)<br>$f_{ctm} = 2,12 \cdot \ln(1 + f_{cm}/10)$ (virs C50/60) |
| **$f_{ctk,0,05}$** (MPa) | 1,1 | 1,3 | 1,5 | 1,8 | 2,0 | 2,2 | 2,5 | 2,7 | 2,9 | 3,0 | 3,1 | 3,2 | 3,4 | 3,5 | $f_{ctk,0,05} = 0,7 \cdot f_{ctm}$ (5% fraktile — aksiālās stiepes stiprība) |
| **$f_{ctk,0,95}$** (MPa) | 2,0 | 2,5 | 2,9 | 3,3 | 3,8 | 4,2 | 4,6 | 4,9 | 5,3 | 5,5 | 5,7 | 6,0 | 6,3 | 6,6 | $f_{ctk,0,95} = 1,3 \cdot f_{ctm}$ (95% fraktile) |
| **$E_{cm}$** (GPa) | 27 | 29 | 30 | 31 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 41 | 42 | 44 | $E_{cm} = 22 \cdot (f_{cm}/10)^{0,3}$ (sekantes elastības modulis) |
| **$\varepsilon_{c1}$** (‰) | 1,8 | 1,9 | 2,0 | 2,1 | 2,2 | 2,25 | 2,3 | 2,4 | 2,45 | 2,5 | 2,6 | 2,7 | 2,8 | 2,8 | $\varepsilon_{c1} = 0,7 \cdot f_{cm}^{0,31} \le 2,8$ (deformācija pie $f_{cm}$) |
| **$\varepsilon_{cu1}$** (‰) | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,2 | 3,0 | 2,8 | 2,8 | 2,8 | Robeždeformācija pie aksiālas spiedes ($\le$ C50/60: 3,5)<br>$\ge$ C55/67: $2,8 + 27 \cdot [(98 - f_{cm})/100]^4$ |
| **$\varepsilon_{c2}$** (‰) | 2,0 | 2,0 | 2,0 | 2,0 | 2,0 | 2,0 | 2,0 | 2,0 | 2,0 | 2,2 | 2,3 | 2,4 | 2,5 | 2,6 | Deformācija parabolas-taisnstūra diagrammai<br>$\ge$ C55/67: $2,0 + 0,085 \cdot (f_{ck} - 50)^{0,53}$ |
| **$\varepsilon_{cu2}$** (‰) | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,1 | 2,9 | 2,7 | 2,6 | 2,6 | Robeždeformācija parabolas-taisnstūra diagrammai<br>$\ge$ C55/67: $2,6 + 35 \cdot [(90 - f_{ck})/100]^4$ |
| **$n$** | 2,0 | 2,0 | 2,0 | 2,0 | 2,0 | 2,0 | 2,0 | 2,0 | 2,0 | 1,75 | 1,6 | 1,45 | 1,4 | 1,4 | Eksponents parabolas-taisnstūra diagrammai<br>$\ge$ C55/67: $1,4 + 23,4 \cdot [(90 - f_{ck})/100]^4$ |
| **$\varepsilon_{c3}$** (‰) | 1,75 | 1,75 | 1,75 | 1,75 | 1,75 | 1,75 | 1,75 | 1,75 | 1,75 | 1,8 | 1,9 | 2,0 | 2,2 | 2,3 | Deformācija taisnstūra-trapeces diagrammai<br>$\ge$ C55/67: $1,75 + 0,55 \cdot [(f_{ck} - 50)/40]$ |
| **$\varepsilon_{cu3}$** (‰) | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,5 | 3,1 | 2,9 | 2,7 | 2,6 | 2,6 | Robeždeformācija taisnstūra-trapeces diagrammai<br>$\ge$ C55/67: $2,6 + 35 \cdot [(90 - f_{ck})/100]^4$ |

---

## Stiegrojuma tērauda īpašības

Latvijā dzelzsbetona konstrukcijās visbiežāk izmanto **B500A** (zemas plastiskuma klases) un **B500B** (vidējas plastiskuma klases) marku stiegrojumu tēraudu ar šādām stiprības un elastības īpašībām:

| Nosaukums / Marka | $f_{tk}$ (N/mm²) | $f_{td}$ (N/mm²) | $f_{yk}$ (N/mm²) | $f_{yd}$ (N/mm²) | $\varepsilon_{uk}$ (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **B500A** (Zems elastīgums) | 525 | 455 | 500 | 435 | $\ge 2,5$ |
| **B500B** (Vidējs elastīgums) | 540 | 470 | 500 | 435 | $\ge 5,0$ |

Kur:
- $f_{yk}$ — raksturīgā tecēšanas robeža (plūstamības robeža);
- $f_{yd} = f_{yk} / \gamma_S = 500 / 1,15 \approx 435\text{ N/mm}^2$ (stiegrojuma aprēķina stiprība);
- $f_{tk}$ — raksturīgā stiepes stiprība (pārraušanas robeža);
- $f_{td} = f_{tk} / \gamma_S$ (stiegrojuma aprēķina stiepes stiprība);
- $\varepsilon_{uk}$ — raksturīgā deformācija pie maksimālās slodzes;
- Tērauda elastības modulis: $E_s = 200\text{ GPa} = 200\ 000\text{ N/mm}^2$.

---

## Nerūsējošā tērauda stiegrojuma īpašības

Agresīvās vidēs (piemēram, pretledus sāļu iedarbībā vai jūras hidrotehniskajās būvēs) izmanto nerūsējošā tērauda stiegrojumu:

| Ražošanas veids | Tērauda marka (EN) | Izmērs (mm) | Plūstamības robeža $R_{p0,2}$ (N/mm²) | Pārraušanas pretestība $R_m$ (N/mm²) | $A_{gt}/A_j$ (%) | Relatīvais pagarinājums $A_5$ (%) | Attiecība $R_m/R_{p0,2}$ | Elastības modulis $E$ (GPa) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Auksti vilkts** | 1.4301 | 3 – 16 | $\ge 550$ | $\ge 600$ | $\ge 5$ / $\ge 8$ | $\ge 15$ | $\ge 1,10$ | 200 |
| | 1.4436 | 3 – 16 | $\ge 550$ | $\ge 600$ | $\ge 5$ / $\ge 8$ | $\ge 15$ | $\ge 1,10$ | 200 |
| | 1.4571 | 3 – 16 | $\ge 550$ | $\ge 600$ | $\ge 5$ / $\ge 8$ | $\ge 15$ | $\ge 1,10$ | 200 |
| **Karstā velmējuma** | 1.4301 | 20 – 40 | $\ge 500$ / $\ge 550$ | $\ge 700$ | $\ge 5$ / $\ge 8$ | $\ge 15$ | $\ge 1,10$ | 200 |
| | 1.4571 | 20 – 32 | $\ge 500$ / $\ge 550$ | $\ge 700$ | $\ge 5$ / $\ge 8$ | $\ge 15$ | $\ge 1,10$ | 200 |
| | 1.4462 (Duplex) | 20 – 50 | $\ge 500$ / $\ge 550$ | $\ge 700$ | $\ge 5$ / $\ge 8$ | $\ge 15$ | $\ge 1,10$ | 200 |
