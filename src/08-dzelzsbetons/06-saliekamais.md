# Saliekamais dzelzsbetons

Saliekamā dzelzsbetona konstrukciju projektēšana un izmantošana prasa precīzu izgatavošanas pielaižu (toleranču), transportēšanas gabarītu, balstījuma mezglu un šuvju risinājumu ievērošanu.

> [!TIP]
> **Praktiskās HCS montāžas vadlīnijas:**
> Šī nodaļa ietver saliekamā dzelzsbetona vispārīgos aprēķinus, ražošanas standartus un elementu gabarītus. Detalizētus būvlaukuma nosacījumus par HCS plātņu uzglabāšanu, celšanu, līmeņošanu, tērauda vekseļiem un drenāžu skatīt atsevišķajā nodaļā:
> **[Dobumoto plātņu (HCS) montāža un nosacījumi](06a-hcs-montaza.md)**

---

## Elementu izgatavošanas standarti

Saliekamo dzelzsbetona elementu izgatavošanu un kvalitātes atbilstības novērtēšanu veic saskaņā ar šādiem standartiem:
- **LVS EN 14992+A1:2020:** Saliekamā dzelzsbetona izstrādājumi. Sienas elementi.
- **LVS EN 13225:** Saliekamā dzelzsbetona izstrādājumi. Lineārie konstrukciju elementi (sijas, kolonnas).
- **LVS EN 1168+A3:2011:** Saliekamā dzelzsbetona izstrādājumi. Dobumotās plātnes.

---

## Dobumoto plātņu (HCS) izgriezumu robežvērtības

Veicot dobumoto plātņu gareniskos vai šķērsvirziena izgriezumus (komunikāciju šahtām, kāpņu ailēm), jānodrošina atlikušā plātnes šķērsgriezuma nestspēja un stabilitāte:

![Plātņu izgriezumi](../images/ch08/img046.png)

*Saskaņā ar "Betongelementboken" un ražotāju vadlīnijām, maksimālie pieļaujamie izgriezumu izmēri bez papildu tērauda sadalošajiem elementiem (kārbām vai vekseļiem) ir atkarīgi no plātnes biezuma un izvietojuma (parasti ne vairāk kā 1-2 dobumu platumā).*

### Dobumoto plātņu enkurošana iecirtumos:

![Plātņu enkurošana](../images/ch08/img047.png)

*Stropēšanas un montāžas paņēmienus plātnēm ar izgriezumiem skatīt nodaļā [3. HCS plātņu celšanas un stropēšanas tehnoloģijas](06a-hcs-montaza.md#3-celšana-stropēšana-un-drošības-ķēdes).*

---

## Dobumoto paneļu ugunsizturība šķērsspēkā un enkurojumā (LVS EN 1168 G pielikums)

Ugunsgrēka apstākļos dobumotajās plātnēs rodas augsts temperatūras gradients, kas izraisa betona termisko izplešanos un plaisāšanu, ietekmējot šķērsspēka nestspēju un saspriegto stiegru enkurojuma saķeri.

Saskaņā ar LVS EN 1168 G pielikumu, ugunsizturības klasēm, kas ir vienādas vai lielākas par **R60**, ir jāveic šķērsspēka un enkurojuma nestspējas pārbaude ugunsgrēka apstākļos. Klasei < R60 šī pārbaude nav nepieciešama.

### Empīriskais šķērsspēka un enkurojuma vienādojums ugunsgrēka apstākļos:

$$V_{Rd,c,fi} = (C_{\theta,1} + \alpha_k \cdot C_{\theta,2}) \cdot b_w \cdot d$$

Kur:
- $\alpha_k = 1 + \sqrt{200 / d} ≤ 2.0$ (izmēra faktors, kur darba augstums d ir milimetros);
- $b_w$ — sieniņu kopējais platums (samazināts, ņemot vērā plaisas);
- $d$ — darba augstums normālā temperatūrā;
- $C_{\theta,1}$ — koeficients, kas ievērtē betona spriegumu ugunsgrēka apstākļos;
- $C_{\theta,2}$ — koeficients, kas ievērtē enkurotā garenstiegrojuma ietekmi paaugstinātā temperatūrā;
- $\sigma_{cp,20^\circC}$ — vidējais betona spriegums no saspriegojuma spēka normālā temperatūrā;
- $f_{c,fi,m}$ — betona vidējā spiedes stiprība paaugstinātā temperatūrā;
- $F_{R,a,fi} = F_{R,a,fi,p} + F_{R,a,fi,s}$ (kopējā saspriegtā un parastā stiegrojuma spēka kapacitāte);
- $f_{bpd,fi}$ — saķeres stiprība saspriegtajām stiegrām ugunsgrēka apstākļos.

 | G.2. attēls — Aprēķina modelis ar parasto enkurojumu | G.3. attēls — Aprēķina modelis ar izvirzītām dzīslām | 
 | :---: | :---: | 
 | ![Modelis 1](../images/ch08/img048_diagram.png) | ![Modelis 2](../images/ch08/img050_diagram.png) | 

*Apzīmējumi: 1 — apskatāmais šķērsgriezums (balsta malā), 2 — savienojuma stiegrojums (skavas), 3 — saspriegtā dzīsla, 4 — monolītais šuvju aizpildījuma betons.*

---

## Saliekamo fasādes elementu šuvju hidroizolācija un blīvēšana

Ārsienu trīsslāņu paneļu šuvju ilgmūžību un aizsardzību pret mitrumu nodrošina hermētiķi un blīvslāņi.

**Prasības šuvju izmēriem pēc DIN 18540:**

 | Kustība šuvē ΔL (mm) | Nominālais šuves platums b pie +10 °C (mm)* | Minimālais šuves platums min b (mm) | Blīvējuma (hermētiķa) dziļums d (mm) | 
 | :---: | :---: | :---: | :---: | 
 | ≤ 2 | 15 | 10 | 8 ± 2 | 
 | > 2 ... ≤ 3.5 | 20 | 15 | 10 ± 2 | 
 | > 3.5 ... ≤ 5 | 25 | 20 | 12 ± 2 | 
 | > 5 ... ≤ 6.5 | 30 | 25 | 15 ± 3 | 
 | > 6.5 ... ≤ 8 | 35 | 30 | 15 ± 3 | 

*\* Nominālā šuves platuma pieļaujamā būvdarbu novirze ir ±5 mm. Hermētiķa dziļuma un platuma attiecība parasti ir robežās no 1:1 līdz 1:2.*

---

## Maksimālie elementu gabarīti transportēšanai

Saliekamo dzelzsbetona elementu dizainā ir jāņem vērā autotransporta gabarītu ierobežojumi Latvijas teritorijā:

 | Autotransporta veids | Augstums bez atļaujas (mm) | Platums bez atļaujas (mm) | Garums bez atļaujas (mm) | Svars bez atļaujas (t) | Augstums ar atļauju (mm) | Platums ar atļauju (mm) | Garums ar atļauju (mm) | 
 | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
 | Standarta platforma / tents | 2600 | 2450 | 13500 | 24 | 3100 | 2750 | 18000 | 
 | Zemas grīdas treileris (JUMBO) | 3000 | 2450 | 9000 | 24 | 3300 | 2750 | 9000 | 
 | Zemās grīdas treileris (Titāniks) | 3800 | 1500 | 9500 | 22 | 4200 | 1500 | 9500 | 

---

## Nominālie elementu balstījuma garumi

Minimālie balsta garumi (*bearing lengths*) uz nesošajām konstrukcijām, kas nodrošina drošu slodzes pārnesi un pieļauj būvdarbu novirzes:

 | Balstāmais elements | Nesošā konstrukcija | Plātnes biezums h vai laidums L | Minimālais nominālais balsta garums (mm) | 
 | :--- | :--- | :--- | :---: | 
 | Dobumotās plātnes (HCS) | Betons / Tērauds | h ≤ 300 mm | 60 – 80 | 
 | Dobumotās plātnes (HCS) | Betons / Tērauds | h > 300 mm | 100 – 120 | 
 | Dobumotās plātnes (HCS) | Mūris | h ≤ 250 mm | 100 | 
 | Dobumotās plātnes (HCS) | Mūris | h > 250 mm | 120 | 
 | Masīvās plātnes (Floor planks) | Betons | Ar palīgatbalstiem montāžā / Bez palīgatbalstiem | 30 / 50 | 
 | Masīvās plātnes (Floor planks) | Mūris | Ar palīgatbalstiem montāžā / Bez palīgatbalstiem | 40 / 50 | 
 | Ribotie pārsegumi (TT-plātnes) | Betons | Laidums L ≤ 15 m | 150 | 
 | Sekundārās jumta sijas | Betons | Laidums L ≤ 8 m | 140 | 
 | Pārseguma sijas | Betons | Laidums L = 12 ... 20 m | 200 – 230 | 
 | Jumta sijas | Betons | Laidums L ≤ 24 m | 195 | 
 | Jumta sijas | Betons | Laidums L ≤ 40 m | 225 | 

---

## Nestspējas līknes un gala zonas spriegumi

Saspriegto TT-plātņu un siju nestspējas līknes atkarībā no laiduma un slodzēm (pēc Consolis un TMB datiem pie slodžu sadalījuma 50/50):

 | Consolis RT un L saspriegtās sijas | TMB saspriegto siju nestspēja | 
 | :---: | :---: | 
 | ![Līknes 1](../images/ch08/img057.png) | ![Līknes 2](../images/ch08/img058.png) | 

Atšķelšanās (sašķelšanās) spriegumi saspriegto elementu gala zonās, ko rada spriegojuma spēka enkurošanās betona masīvā:

 | Spriegumu izkliede saspriegtā elementa gala zonā | Atšķelšanās spriegumu sadalījums | 
 | :---: | :---: | 
 | ![Spriegumi 1](../images/ch08/img059.png) | ![Spriegumi 2](../images/ch08/img060.png) | 
