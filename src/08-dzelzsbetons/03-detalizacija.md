# Dzelzsbetona stiegrošanas un detalizācijas labā prakse

Stiegrojuma izvietojumam un detalizācijai ir jānodrošina konstrukcijas nestspēja, plaisu platuma ierobežošana, kā arī kvalitatīva betona maisījuma iestrāde (vibrēšana).

---

## Plātnes

### Brīvo malu stiegrošana (LVS EN 1992-1-1 9.3.1.4. punkts)
Plātnes brīvajām (nebalstītajām) malām (piemēram, pie konsolēm, kāpņu ailēm vai plātnes perimetra) jābūt stiegrotām ar garenvirziena un šķērsvirziena stiegrām.

- **Konstruktīvais risinājums:** 
  - Garenvirzienā izvieto vismaz \\(2 \cdot \varnothing 12\\) stieņus (vienu augšā, vienu apakšā);
  - Šķērsvirzienā izmanto U-veida skavas, kuru diametrs un solis parasti atbilst plātnes pamatsietam.

![Plātnes malas stiegrošana](../images/ch08/img042.png)

---

## Kolonnas

### Garenstiegrojums (LVS EN 1992-1-1 9.5.2. punkts)
- **Minimālais stieņu skaits:**
  - Taisnstūra un poligonālām kolonnām katrā stūrī jāizvieto vismaz viens stienis (taisnstūra kolonnām — vismaz 4 stieņi);
  - Apaļām kolonnām minimālais garenstieņu skaits ir **6 stieņi** (nevis 4).
- **Stieņu diametrs:** Minimālais garenstieņu diametrs ir \\(\varnothing \ge 8\text{ mm}\\) (Latvijas praksē parasti izmanto \\(\varnothing \ge 12\text{ mm}\\)).
- **Attālumi:** Spiestajā zonā attālums starp diviem blakus esošiem garenstieņiem nedrīkst pārsniegt **\\(150\text{ mm}\\)** no stieņa, kas ir nostiprināts ar aptveri (LVS EN 1992-1-1 9.5.3(6)).

### Šķērsstiegrojums (Aptveres)
Šķērsstiegrojuma (aptveru) solis \\(s_{cl,t}\\) nedrīkst pārsniegt maksimālo soli \\(s_{cl,t,max}\\) (skatīt [Maksimālais attālums starp stiegrām](file:///C:/Users/Kasutaja/Dropbox/Projects/paligs-buvkonstrukciju-projektesana/src/08-dzelzsbetons/02-prasibas.md#maksimālais-attālums-starp-stiegrām-aptveru-solis)).

---

## Sijas

### Konstruktīvie stiegrošanas noteikumi
- **Minimālais garenstieņu diametrs:** Sijās nesošajam garenstiegrojumam jāizmanto stieņi ar diametru \\(\varnothing \ge 12\text{ mm}\\).
- **Attālumi betona iestrādei:** Lai nodrošinātu betona maisījuma brīvu plūsmu un tā sablīvēšanu ar dziļumvibratoru, tīrajam horizontālajam attālumam starp paralēliem stieņiem (it īpaši sijas augšdaļā, kur tiek padots betons) vēlams būt vismaz **\\(75\text{ mm}\\)**.
- **Sānu plaisu stiegrojums (Skin reinforcement):** Sijām, kuru kopējais augstums \\(h \ge 1000\text{ mm}\\), pie sānu virsmām ir jāparedz garenisks stiegrojums plaisu ierobežošanai. Tā laukumu pieņem vismaz \\(0,1\%\\) no sijas stieptās zonas betona laukuma katrā pusē, un stieņu solis nedrīkst pārsniegt \\(200\text{ mm}\\).

### Stieptā stiegrojuma minimālais laukums (\\(A_{s,\text{min}}\\))
Siju stieptajā zonā jānodrošina minimālais stiegrojuma laukums, lai novērstu trauslu sabrukumu plaisas rašanās brīdī:

\[A_{s,\text{min}} = 0,26 \cdot \frac{f_{ctm}}{f_{yk}} \cdot b_t \cdot d \ge 0,0013 \cdot b_t \cdot d\]

Kur:
- \\(b_t\\) — vidējais stieptās zonas platums (m);
- \\(d\\) — sijas darba augstums līdz stiegrojuma smaguma centram (m);
- \\(f_{ctm}\\) — betona vidējā stiepes stiprība (MPa);
- \\(f_{yk}\\) — stiegrojuma tecēšanas robeža (MPa).

*Piezīme: Tēraudam B500 un betonam C25/30 šī robeža ir \\(A_{s,\text{min}} \approx 0,00135 \cdot b_t \cdot d\\), bet betonam C30/37 tā ir \\(A_{s,\text{min}} \approx 0,0015 \cdot b_t \cdot d\\).*

### Spiestā stiegrojuma minimālais laukums (\\(A_{sc,\text{min}}\\))
Ja aprēķinā tiek ņemts vērā spiestais stiegrojums (dubulti stiegrotā sijā), tā laukumam jābūt vismaz:
\[A_{sc,\text{min}} \ge 0,002 \cdot A_c\]

### Minimālais aptveru saturs (Šķērsstiegrojuma attiecība \\(\rho_w\\))
Aptveru laukumam pret sijas sieniņas laukumu jānodrošina minimālā attiecība:

\[\rho_w = \frac{A_{sw}}{s \cdot b_w \cdot \sin\alpha} \ge \rho_{w,\text{min}} = \frac{0,08 \cdot \sqrt{f_{ck}}}{f_{yk}}\]

Kur:
- \\(A_{sw}\\) — visu aptveres kāju laukums vienā griezumā (piemēram, divkāršai aptverei \\(2 \cdot A_{s,\text{apt}}\\));
- \\(s\\) — aptveru solis;
- \\(b_w\\) — sijas sieniņas platums;
- \\(\alpha\\) — aptveru leņķis pret sijas garenasi (statnām aptverēm \\(\alpha = 90^\circ\\), t.i., \\(\sin\alpha = 1,0\\)).

*Piemērs (\\(f_{yk} = 500\text{ MPa}\\)):*
- Betonam C25/30: \\(\rho_{w,\text{min}} = 0,080\%\\)
- Betonam C30/37: \\(\rho_{w,\text{min}} = 0,088\%\\)

### Aptveru izvietojuma robežvērtības
- **Minimālais aptveru solis (iestrādes ērtībai):**
  Lielākais no: \\(100\text{ mm}\\) vai \\((50 + 12,5 \cdot n_{\text{kājas}})\text{ mm}\\), kur \\(n_{\text{kājas}}\\) ir aptveres griezuma kāju skaits (piem., 2 vai 4).
- **Maksimālais aptveru solis (\\(s_{\text{max}}\\)):**
  Mazākais no šiem lielumiem:
  - \\(0,75 \cdot d\\) (kur \\(d\\) ir darba augstums);
  - \\(12 \cdot \varnothing_{\text{sp}}\\) (kur \\(\varnothing_{\text{sp}}\\) ir spiestā stiegrojuma minimālais diametrs);
  - \\(300\text{ mm}\\).
- **Minimālais aptveru diametrs:** Sijās šķērsstiegrojumam jāizmanto stieņi ar diametru \\(\varnothing \ge 8\text{ mm}\\).
