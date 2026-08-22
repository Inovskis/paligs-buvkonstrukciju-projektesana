# Deformāciju un plaisu robežvērtības dzelzsbetonam

Dzelzsbetona konstrukciju lietojamības robežstāvokļa (SLS) pārbaudēs galvenā vērība jāvelta konstrukciju izliecēm un plaisu platumam.

---

## Vertikālo pārvietojumu (izlieču) robežvērtības

Saskaņā ar standartu LVS EN 1990, par pieļaujamajām deformāciju robežvērtībām projektā ir atsevišķi jāvienojas ar pasūtītāju. LVS EN 1992-1-1 (7.4.1. punkts) nosaka izlieču robežvērtības (balstoties uz standartu ISO 4356), lai nodrošinātu normālu ēkas ekspluatāciju un estētisko izskatu:

- **Estētiskais izskats un normāla ekspluatācija:**
  Izliece $w_{max}$ no ilglaicīgās (kvazipastāvīgās) slodžu kombinācijas nedrīkst pārsniegt:
  \\[w_{max} = \frac{L}{250}\\]
  
- **Trauslu konstrukciju un starpsienu bojājumu novēršana:**
  Izlieces pieaugums $w_{add}$ pēc starpsienu vai apdares izbūves (no kvazipastāvīgās kombinācijas mainīgās daļas un betona šļūdes) nedrīkst pārsniegt:
  \\[w_{add} = \frac{L}{500}\\]

Kur $L$ ir sijas vai plātnes laidums (konsolēm robežvērtību pieņem kā $L_{konsoles} / 125$ un $L_{konsoles} / 250$).

---

## Plaisu platumu robežvērtības $w_{max}$ (LVS EN 1992-1-1 7.1. tabula)

Plaisu platuma ierobežošana ir būtiska stiegrojuma korozijas novēršanai un būves ilgmūžības nodrošināšanai.

 | Vides iedarbības klase | Dzelzsbetona elementi un priekšspriegoti elementi bez saistes w_{max} (mm) | Priekšspriegoti elementi ar saisti w_{max} (mm) | 
 | :--- | :---: | :---: | 
 | X0, XC1 | 0,4^1 | 0,2 | 
 | XC2, XC3, XC4 | 0,3 | 0,2^2 | 
 | XD1, XD2, XD3, XS1, XS2, XS3 | 0,3 | Dekompresija (pārbauda atsevišķi) | 

> **Piezīmes par tabulu:**
> 1. Klasēm X0 un XC1 plaisu platumam nav ietekmes uz ilgizturību, šī robežvērtība ir noteikta tikai vizuālā izskata nodrošināšanai. Ja nav prasību pret vizuālo izskatu, šīs prasības var atvieglot.
> 2. Šīm klasēm priekšspriegotiem elementiem ar saisti papildus ir jāveic dekompresijas pārbaude (stiegrojuma kanāls nedrīkst atrasties stieptajā zonā) pie kvazipastāvīgās slodžu kombinācijas.

> **Svarīgi!** Priekšspriegotiem elementiem ar saisti iedarbības klasēs XD un XS dekompresijas pārbaude (stiegrojuma kanāla atrašanās vismaz $25 mm$ dziļumā spiestajā zonā) ir jāveic pie **biežās slodžu kombinācijas** (frequent combination), nevis kvazipastāvīgās kombinācijas. Šis nosacījums bieži vien projektēšanas praksē tiek kļūdaini jaukts.

---

## Galvenie Latvijā nacionāli noteiktie parametri (NA)

### 1. Betona stiprības ilglaicīgo efektu koeficients $\alpha_{cc}$ (LVS EN 1992-1-1 3.1.6.(1)P)
Saskaņā ar LVS EN 1992-1-1:2005/A2:2020/NA:2020 grozījumiem, koeficienta $\alpha_{cc}$ vērtība ir mainīta no iepriekšējā $0,85$ uz **$1,00$**. 

Betona aprēķina spiedes stiprība $f_{cd}$ tagad tiek noteikta kā:
\\[f_{cd} = \alpha_{cc} \cdot \frac{f_{ck}}{\gamma_c} = 1,00 \cdot \frac{f_{ck}}{1,5}\\]

Stiepes stiprības aprēķina koeficients ir saglabāts $\alpha_{ct} = 1,00$.

### 2. Aizsargslāņa pielaide būvdarbu novirzei $\Delta c_{dev}$ (LVS EN 1992-1-1 4.4.1.3.(1)P)
Nominālo stiegrojuma aizsargslāni $c_{nom}$ nosaka, pieskaitot novirzi $\Delta c_{dev}$ pie minimālā aizsargslāņa $c_{min}$:
\\[c_{nom} = c_{min} + \Delta c_{dev}\\]

Latvijas nacionālajā pielikumā noteiktās novirzes vērtības:
- **Pārsegumu plātnēm, kuru biezums $h < 160 mm$:**
  Pieļaujama reducēta novirze: $0 mm ≤ \Delta c_{dev} ≤ 10 mm$ (parasti pieņem $5 mm$ vai $10 mm$ atkarībā no izbūves tolerances kontroles);
- **Visām pārējām konstrukcijām:**
  Novirze ir stingri noteikta: $\Delta c_{dev} = 10 mm$.
