# Dzelzsbetona stiegrošanas un detalizācijas labā prakse

Stiegrojuma izvietojumam un detalizācijai ir jānodrošina konstrukcijas nestspēja, plaisu platuma ierobežošana, kā arī kvalitatīva betona maisījuma iestrāde (vibrēšana).

---

## Plātnes

### Brīvo malu stiegrošana (LVS EN 1992-1-1 9.3.1.4. punkts)
Plātnes brīvajām (nebalstītajām) malām (piemēram, pie konsolēm, kāpņu ailēm vai plātnes perimetra) jābūt stiegrotām ar garenvirziena un šķērsvirziena stiegrām.

- **Konstruktīvais risinājums:** 
  - Garenvirzienā izvieto vismaz $2 \cdot \varnothing 12$ stieņus (vienu augšā, vienu apakšā);
  - Šķērsvirzienā izmanto U-veida skavas, kuru diametrs un solis parasti atbilst plātnes pamatsietam.

![Plātnes malas stiegrošana](../images/ch08/img042.png)

---

## Kolonnas

### Garenstiegrojums (LVS EN 1992-1-1 9.5.2. punkts)
- **Minimālais stieņu skaits:**
  - Taisnstūra un poligonālām kolonnām katrā stūrī jāizvieto vismaz viens stienis (taisnstūra kolonnām — vismaz 4 stieņi);
  - Apaļām kolonnām minimālais garenstieņu skaits ir **6 stieņi** (nevis 4).
- **Stieņu diametrs:** Minimālais garenstieņu diametrs ir $\varnothing ≥ 8 mm$ (Latvijas praksē parasti izmanto $\varnothing ≥ 12 mm$).
- **Attālumi:** Spiestajā zonā attālums starp diviem blakus esošiem garenstieņiem nedrīkst pārsniegt **$150 mm$** no stieņa, kas ir nostiprināts ar aptveri (LVS EN 1992-1-1 9.5.3(6)).

### Šķērsstiegrojums (Aptveres)
Šķērsstiegrojuma (aptveru) solis $s_{cl,t}$ nedrīkst pārsniegt maksimālo soli $s_{cl,t,max}$ (skatīt [Maksimālais attālums starp stiegrām](02-prasibas.md#maksimālais-attālums-starp-stiegrām-aptveru-solis)).

---

## Sijas

### Konstruktīvie stiegrošanas noteikumi
- **Minimālais garenstieņu diametrs:** Sijās nesošajam garenstiegrojumam jāizmanto stieņi ar diametru $\varnothing ≥ 12 mm$.
- **Attālumi betona iestrādei:** Lai nodrošinātu betona maisījuma brīvu plūsmu un tā sablīvēšanu ar dziļumvibratoru, tīrajam horizontālajam attālumam starp paralēliem stieņiem (it īpaši sijas augšdaļā, kur tiek pa... betons) vēlams būt vismaz **$75 mm$**.
- **Sānu plaisu stiegrojums (Skin reinforcement):** Sijām, kuru kopējais augstums $h ≥ 1000 mm$, pie sānu virsmām ir jāparedz garenisks stiegrojums plaisu ierobežošanai. Tā laukumu pieņem vismaz $0,1\%$ no sijas stieptās zonas betona laukuma katrā pusē, un stieņu solis nedrīkst pārsniegt $200 mm$.

### Stieptā stiegrojuma minimālais laukums ($A_{s,min}$)
Siju stieptajā zonā jānodrošina minimālais stiegrojuma laukums, lai novērstu trauslu sabrukumu plaisas rašanās brīdī:

\\[A_{s,min} = 0,26 \cdot \frac{f_{ctm}}{f_{yk}} \cdot b_t \cdot d ≥ 0,0013 \cdot b_t \cdot d\\]

Kur:
- $b_t$ — vidējais stieptās zonas platums (m);
- $d$ — sijas darba augstums līdz stiegrojuma smaguma centram (m);
- $f_{ctm}$ — betona vidējā stiepes stiprība (MPa);
- $f_{yk}$ — stiegrojuma tecēšanas robeža (MPa).

> **Piezīme:** Tēraudam B500 un betonam C25/30 šī robeža ir $A_{s,min} \approx 0,00135 \cdot b_t \cdot d$, bet betonam C30/37 tā ir $A_{s,min} \approx 0,0015 \cdot b_t \cdot d$.

### Spiestā stiegrojuma minimālais laukums ($A_{sc,min}$)
Ja aprēķinā tiek ņemts vērā spiestais stiegrojums (dubulti stiegrotā sijā), tā laukumam jābūt vismaz:
\\[A_{sc,min} ≥ 0,002 \cdot A_c\\]

### Minimālais aptveru saturs (Šķērsstiegrojuma attiecība $\rho_w$)
Aptveru laukumam pret sijas sieniņas laukumu jānodrošina minimālā attiecība:

\\[\rho_w = \frac{A_{sw}}{s \cdot b_w \cdot \sin\alpha} ≥ \rho_{w,min} = \frac{0,08 \cdot \sqrt{f_{ck}}}{f_{yk}}\\]

Kur:
- $A_{sw}$ — visu aptveres kāju laukums vienā griezumā (piemēram, divkāršai aptverei $2 \cdot A_{s,apt}$);
- $s$ — aptveru solis;
- $b_w$ — sijas sieniņas platums;
- $\alpha$ — aptveru leņķis pret sijas garenasi (statnām aptverēm $\alpha = 90^\circ$, t.i., $\sin\alpha = 1,0$).

> **Piemērs ($f_{yk} = 500 MPa$):**
> - Betonam C25/30: $\rho_{w,min} = 0,080\%$
> - Betonam C30/37: $\rho_{w,min} = 0,088\%$

### Aptveru izvietojuma robežvērtības
- **Minimālais aptveru solis (iestrādes ērtībai):**
  Lielākais no: $100 mm$ vai $(50 + 12,5 \cdot n_{kājas}) mm$, kur $n_{kājas}$ ir aptveres griezuma kāju skaits (piem., 2 vai 4).
- **Maksimālais aptveru solis ($s_{max}$):**
  Mazākais no šiem lielumiem:
  - $0,75 \cdot d$ (kur $d$ ir darba augstums);
  - $12 \cdot \varnothing_{sp}$ (kur $\varnothing_{sp}$ ir spiestā stiegrojuma minimālais diametrs);
  - $300 mm$.
- **Minimālais aptveru diametrs:** Sijās šķērsstiegrojumam jāizmanto stieņi ar diametru $\varnothing ≥ 8 mm$.

---

## Stiegrojuma enkurošana un pārlaidumi (LVS EN 1992-1-1 8.4 un 8.7)

Stiegrojuma enkurošanas garumam un pārlaidumiem ir jānodrošina pilnīga spēku pārnese no stiegrojuma uz betonu (vai starp diviem stieņiem) bez betona plaisāšanas vai nošķelšanās.

### Pamata enkurošanas garums ({b,rqd}$)

Vajadzīgais pamata enkurošanas garums, lai uzņemtu pilnu stieņa aprēķina spriegumu $\sigma_{sd}$, tiek noteikts kā:
\\[l_{b,rqd} = \left( \frac{\varnothing}{4} \right) \cdot \frac{\sigma_{sd}}{f_{bd}}\\]
kur {bd}$ ir aprēķina saistes stiprība starp betonu un stiegrojumu, kas atkarīga no betona klases, stieņa diametra un saistes apstākļiem (labi vai slikti).

### Aprēķina enkurošanas garums ({bd}$)

Faktisko aprēķina enkurošanas garumu nosaka, reizinot pamata garumu ar koeficientiem:
\\[l_{bd} = \alpha_1 \cdot \alpha_2 \cdot \alpha_3 \cdot \alpha_4 \cdot \alpha_5 \cdot l_{b,rqd} ≥ l_{b,min}\\]
kur koeficienti $\alpha_i$ ņem vērā stieņa gala formu (taisns, āķis, cilpa), betona aizsargkārtu, šķērsstiegrojuma ietekmi u.c.
- **{b,min}$** stieptiem stieņiem nedrīkst būt mazāks par lielāko no: ,3 l_{b,rqd}$, \varnothing$ vai  mm$.

> **Piezīme praktiskai projektēšanai:**
> Lielākajā daļā standarta gadījumu (B500B stiegrojums, C30/37 betons, labi saistes apstākļi, bez papildu šķērsstiegrojuma efektiem), taisnam stienim aprēķina enkurošanas garums stieptajā zonā ir aptuveni **\varnothing ... 40\varnothing$**.

### Pārlaiduma garums ($)

Pārlaiduma garumu stiegru savienojumiem aprēķina līdzīgi, izmantojot papildu koeficientu $\alpha_6$, kas ņem vērā to, cik liels procents no stiegrām tiek savienots vienā šķērsgriezumā:
\\[l_0 = \alpha_1 \cdot \alpha_2 \cdot \alpha_3 \cdot \alpha_5 \cdot \alpha_6 \cdot l_{b,rqd} ≥ l_{0,min}\\]
- Ja vienā vietā pārlaidumu veido $> 50\%$ stiegru, $\alpha_6 = 1,5$.
- Pārlaiduma vietās vienmēr jāparedz papildu šķērsstiegrojums (skavas vai aptveres) atbilstoši EN 1992-1-1 prasībām.
