# Konstruktīvās shēmas un darbības principi

Konstruktīvās shēmas izvēle nosaka būves slodžu pārnesi no jumta un stāvu pārsegumiem uz pamatiem un pamatni, kā arī nodrošina ēkas kopējo telpisko noturību un ģeometrisko nemainību.

---

## Risinājumi telpiskās noturības nodrošināšanai

Ēkas telpiskā noturība un pretestība pret horizontālajām iedarbībām (vēju, seismiskajām slodzēm, ģeometriskajām neprecizitātēm) tiek nodrošināta, apvienojot horizontālos un vertikālos stinguma elementus:

- **Horizontālie diski (pārsegumi):** Darbojas kā stingas diafragmas, kas sadala horizontālos spēkus uz vertikālajiem stinguma elementiem.
- **Vertikālie stinguma elementi:**
  - **Stindzināšanas saites (Bracing):** Diagonālie krusti, K-veida vai V-veida saites (raksturīgas tērauda un koka karkasiem). Tie ir visekonomiskākie un mazdeformējamākie elementi.
  - **Bīdes sienas un kodoli (Shear walls / cores):** Monolītā dzelzsbetona kāpņu un liftu šahtas (kodoli) vai nesošās mūra/betona sienas, kas uzņem bīdes spēkus.
  - **Stingie rāmji (Moment frames):** Rāmji ar stingiem (momentizturīgiem) siju-kolonnu mezgliem. Tie ir deformējamāki nekā saites, taču nodrošina lielāku arhitektonisko brīvību.

![Telpiskās noturības shēmas](images/ch06/img013.png)

### Stabilitātes nodrošināšanas situāciju analīze (Skaidrojumi shēmai)

Kā topošajam vai praktizējošam inženierim ir svarīgi izprast, ka telpisko stabilitāti nevar nodrošināt, vienkārši izvietojot bīdes sienas vai kodolus jebkurā ēkas vietā. Ir jāizvērtē slodžu pārvades ceļš, materiālu deformācijas (piemēram, temperatūras izplešanās) un, pats galvenais, **vērpes (rotācijas) ietekme**.

Zemāk apkopoti tehniski skaidrojumi katrai no shēmā attēlotajām situācijām:

#### 1. Rinda: Temperatūras deformācijas un statiskā noteiktība
*   **1. situācija (good):** Simetrisks 4 bīdes sienu novietojums uz ēkas perimetra. Šis ir teicams risinājums, jo ļauj ēkai simetriski un brīvi izplesties temperatūras ietekmē uz visām pusēm (dashed line), neradot papildu spriegumus konstrukcijās.
*   **2. situācija (Possible variation):** Asimetriska sienu izvietojuma gadījumā temperatūras deformācijas ir ierobežotas. Sienu reakcijas rada vērpes momentus un papildu spriegumus pārseguma diskā, kas var izraisīt plaisāšanu.
*   **3. situācija (Structurally adequate):** Minimālais nepieciešamais stinguma sienu skaits pareizai telpiskās stabilitātes nodrošināšanai (2 vertikālas, 1 horizontāla). Sistēma ir statiski noteikta un spēj uzņemt spēkus abos virzienos, kā arī novērst rotāciju.
*   **4. situācija (good):** Trīs diagonāli izvietotas bīdes sienas (piemēram, trīsšķautņu ēkā) nodrošina pilnvērtīgu telpisko stabilitāti un pretestību pret rotāciju jebkura virziena vēja slodzei.

#### 2. Rinda: Stinguma kodolu (šahtu) novietojums un ekscentritāte
*   **5. situācija (Good if core...):** Centrāls, slēgts liftu/kāpņu kodols. Šis ir ļoti efektīvs risinājums, ja kodols ir pietiekami liels un tam ir augsts vērpes stingums (torsional rigidity). Tas ir ideāli piemērots izteikti simetriskām ēkām.
*   **6. situācija (Poor without extra wall...):** Viens kodols stūrī. Horizontālas slodzes gadījumā veidejas liela ekscentritāte starp vēja slodzes rezultējošo spēku un ēkas stinguma centru. Bez papildu bīdes sienas (extra wall) pretējā pusē ēka tiks pakļauta spēcīgai rotācijai.
*   **7. situācija (Poor without extra wall...):** Kodols novietots ārpus ēkas garās malas vidusdaļas. Tāpat kā 6. gadījumā, veidojas liela ekscentritāte. Lai to kompensētu un novērstu vērpi, pretējā fasādē ir nepieciešama papildu stinguma siena.
*   **8. situācija (Possible, but large eccentricity):** Divi kodoli izvietoti vienā ēkas pusē. Šāds risinājums ir pieļaujams, taču tas rada ievērojamu stinguma centra nobīdi (ekscentritāti) pret ēkas ģeometrisko centru.

#### 3. Rinda: Vērpes nestabilitāte un nepietiekams stingums
*   **9. situācija (Not stiffened against rotation):** Krustveida siena ēkas centrā. Lai gan tā nodrošina stabilitāti bīdē abos virzienos, šādam novietojumam ir ļoti mazs inerces moments pret rotāciju, tāpēc ēka nav aizsargāta pret vērpi.
*   **10. situācija (Not stiffened against rotation):** Trīs atsevišķi bīdes sienu segmenti, kas krustojas vienā punktā. Analogi kā 9. situācijā, šis izkārtojums nenodrošina pietiekamu plecu vērpes momentu uzņemšanai.
*   **11. situācija (Lack of stability...):** Paralēlas sienas, kas orientētas tikai vienā virzienā. Ēkai ir izcila stabilitāte šķērsvirzienā, bet pilnībā trūkst stabilitātes garenvirzienā (longitudinal direction) — ēka sabruks kā kāršu namiņš.
*   **12. situācija (Inadequately stiffened...):** Viena garenvirziena siena kreisajā pusē un divas šķērssienas labajā pusē. Lai gan bīdes pretestība ir abos virzienos, sienu novietojums ir pārāk asimetrisks un nepietiekami pasargā ēku pret rotāciju ap kreiso atbalsta punktu.

---

## Darbības principi lineāriem pārseguma elementiem

Lineārie elementi (sijas, dobumotie paneļi, kopnes) uzņem šķērsslodzes un darbojas galvenokārt uz lieci un bīdi. To statiskās shēmas izvēle nosaka piepūļu sadalījumu un konstrukcijas augstumu:

### 1. Vienlaiduma (šarnīrveida) sija
- **Statika:** Statiski nosakāma sistēma. Abos galos ir šarnīrveida atbalsti, kas neuzņem momentu.
- **Moments laidumā:** Maksimālais moments ir laiduma vidū:
  \\[M_{\text{max}} = \frac{q \cdot L^2}{8}\\]
- **Priekšrocības:** Vienkārša montāža un mezglu izveide, nav jutīga pret atbalstu sēšanos.
- **Trūkumi:** Lielākas izlieces un nepieciešams lielāks šķērsgriezuma augstums.

### 2. Konsoles sija
- **Statika:** Sija ar vienu brīvu galu un otru stingi iespīlētu atbalstā.
- **Moments balstā:** Maksimālais moments veidojas iespīlējuma vietā (stiepta augšējā šķiedra):
  \\[M_{\text{max}} = -\frac{q \cdot L^2}{2}\\]
- **Trūkumi:** Ļoti jutīga pret iespīlējuma mezgla rotāciju un deformācijām.

### 3. Nepārtraukta (vairāklaidumu) sija
- **Statika:** Statiski nenoteicama sistēma ar starpatbalstiem.
- **Darbības princips:** Momentu diagramma ir vienmērīgāka — virs starpatbalstiem veidojas negatīvi momenti (stiepta augšējā šķiedra), kas samazina momentus laidumos.
- **Priekšrocības:** Mazākas izlieces un mazāks nepieciešamais šķērsgriezuma augstums salīdzinājumā ar vienlaiduma siju.
- **Trūkumi:** Sarežģītāki mezgli, papildu piepūles no atbalstu sēšanās vai temperatūras deformācijām.

<div align="center">
  <svg width="600" height="250" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg">
    <style>
      .beam { stroke: #2c5282; stroke-width: 6; stroke-linecap: round; }
      .support { fill: none; stroke: #4a5568; stroke-width: 2; }
      .ground { stroke: #4a5568; stroke-width: 2; stroke-dasharray: 4,4; }
      .text { font-family: 'Inter', sans-serif; font-size: 14px; fill: #2d3748; font-weight: bold; }
    </style>

    <!-- 1. Vienlaiduma sija -->
    <text x="300" y="30" text-anchor="middle" class="text">1. Vienlaiduma (šarnīrveida) sija</text>
    <line x1="100" y1="60" x2="500" y2="60" class="beam" />
    <!-- Kreisais balsts (Pin) -->
    <polygon points="100,60 90,80 110,80" class="support" fill="#e2e8f0"/>
    <line x1="80" y1="80" x2="120" y2="80" class="ground" />
    <!-- Labais balsts (Roller) -->
    <polygon points="500,60 490,75 510,75" class="support" fill="#e2e8f0"/>
    <circle cx="495" cy="80" r="3" fill="#4a5568"/>
    <circle cx="505" cy="80" r="3" fill="#4a5568"/>
    <line x1="480" y1="83" x2="520" y2="83" class="ground" />

    <!-- 2. Konsoles sija -->
    <text x="300" y="115" text-anchor="middle" class="text">2. Konsoles sija</text>
    <line x1="100" y1="140" x2="500" y2="140" class="beam" />
    <!-- Iespīlējums kreisajā pusē -->
    <line x1="100" y1="120" x2="100" y2="160" class="support" stroke-width="4"/>
    <line x1="90" y1="120" x2="90" y2="160" class="ground" />
    <!-- Svītriņas iespīlējumam -->
    <path d="M100 125 L90 135 M100 135 L90 145 M100 145 L90 155" class="support" stroke-width="1"/>

    <!-- 3. Nepārtraukta sija -->
    <text x="300" y="195" text-anchor="middle" class="text">3. Nepārtraukta (vairāklaidumu) sija</text>
    <line x1="100" y1="220" x2="500" y2="220" class="beam" />
    <!-- Balsti -->
    <polygon points="100,220 90,240 110,240" class="support" fill="#e2e8f0"/>
    <line x1="80" y1="240" x2="120" y2="240" class="ground" />
    
    <polygon points="233,220 223,235 243,235" class="support" fill="#e2e8f0"/>
    <circle cx="228" cy="240" r="3" fill="#4a5568"/> <circle cx="238" cy="240" r="3" fill="#4a5568"/>
    <line x1="210" y1="243" x2="253" y2="243" class="ground" />

    <polygon points="366,220 356,235 376,235" class="support" fill="#e2e8f0"/>
    <circle cx="361" cy="240" r="3" fill="#4a5568"/> <circle cx="371" cy="240" r="3" fill="#4a5568"/>
    <line x1="343" y1="243" x2="386" y2="243" class="ground" />

    <polygon points="500,220 490,235 510,235" class="support" fill="#e2e8f0"/>
    <circle cx="495" cy="240" r="3" fill="#4a5568"/> <circle cx="505" cy="240" r="3" fill="#4a5568"/>
    <line x1="480" y1="243" x2="520" y2="243" class="ground" />
  </svg>
</div>
