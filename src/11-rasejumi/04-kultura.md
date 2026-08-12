# Rasēšanas kultūra un lasāmība

Rasēšanas kultūra nenosaka tikai to, vai rasējums tehniski ir pareizs. Tā nosaka, **cik viegli un nepārprotami rasējumu var uztvert un izlasīt būvlaukumā vai metāla apstrādes cehā**. Laba inženiera rasējums ir pašsaprotams, skaidri uztverams pat nogurušam būvniekam un neprasa zvanīt projektētājam pēc papildu skaidrojumiem.

---

## 1. Līniju biezumu hierarhija (Lineweights)

Būvkonstrukciju rasējumu zelta likums: **Griezumiem ir jāizceļas!** Uz papīra neeksistē CAD programmu krāsas (gandrīz visi būvlaukuma rasējumi tiek drukāti melnbalti un bieži A3 samazinātā formātā).

- **0.35 mm – 0.50 mm:** Nesošo elementu (betona, tērauda, mūra) kontūras **griezumā**. Griezuma elementam "jāsit pa aci" pirmajam.
- **0.18 mm – 0.25 mm:** Fona elementi (skati tālākumā), durvis, logi, apdare vai sekundāras detaļas.
- **0.13 mm – 0.18 mm:** Izmēru līnijas, asis, slēptās (pārtrauktās) līnijas, norāžu līnijas, štrihojums.

> **Piezīme:** Līnijām jābūt skaidri atšķiramām arī izprintējot A3 formātā. Ja visas līnijas ir vienādas, rasējums pārvēršas par neatšķetināmu līniju mākoni.

---

## 2. Mērogu pareiza izvēle

Katram informācijas veidam ir savs atbilstošākais mērogs. Nemēģiniet parādīt visu vienā skatā.

- **1:100 vai 1:200:** Ēkas asu shēmas, slodžu plāni, izvietojums. Parāda "lielo bildi" un orientāciju.
- **1:50:** Veidņu plāni, fasādes, galvenie ēkas griezumi. Šeit norāda pamatģeometriju, galvenos atvērumus un piesaistes.
- **1:20 vai 1:25:** Stiegrojuma izvietojuma shēmas, standarta mezgli un siju skati.
- **1:10 vai 1:5:** Detalizēti tērauda mezgli (bultskrūvju piesaistes, metinājumi), specifiskas savienojumu detaļas. Mērogu 1:5 izmanto vietās, kur klājas liels daudzums izmēru nelielā platībā.

---

## 3. Nedublē informāciju! (Single Source of Truth)

Viens no biežākajiem avāriju un brāķu iemesliem būvlaukumā ir pretrunīga informācija rasējumos. Tas rodas, ja inženieris dublē informāciju.

- Ja kolonnas izmērs ir parādīts plānā, to **nevajadzētu** ar izmēru līniju atkārtot griezumā (vai arī tas jāliek iekavās kā informatīvs). 
- Ja mezgla augstums ir nodefinēts mezgla detaļā (1:10), to neliek uz fasādes (1:100).
- **Izmaiņu gadījumā:** Ja informācija atrodas tikai vienā vietā, izmainot to tur, viss projekts paliek korekts. Ja tā ir divās vietās, inženieris bieži aizmirst izlabot otru vietu. Izmantojiet atsauces: *"Piesaistes asīm skatīt plānā X"* vai *"Mezgla detaļas skatīt lapā Y"*.

---

## 4. Vizuālais "Gaiss" (Skaidrība un brīvā vieta)

Rasējums nedrīkst būt pārbāzts kā "zirnekļa tīkls".
1. **Atstarpes:** Starp modeļa līniju un pirmo izmēru ķēdi atstājiet vismaz 10-15 mm atstarpi.
2. **Nepārklāšanās:** Izmēru līnijas un teksti nedrīkst pārklāties viens otram pāri.
3. **Pārtraukts štrihojums:** Vienmēr nodrošiniet, ka fona štrihojums (piemēram, mūra vai grunts hečs) tiek pārtraukts zem teksta (izmantojiet *Text Mask* vai *Background Mask*), lai cipari neiestrēgtu svītrās.
4. **Izvietojums lapā:** Atstājiet skaidras robežas starp dažādiem mezgliem uz vienas lapas. Neiepildiet skatus vienu otrā tā, ka nevar saprast, kuram virsrakstam skats pieder.

---

## 5. Tekstu un fontu standarti

- **Fontu stils:** Izmantojiet tehniski tīrus fontus, piemēram, *ISOCPEUR*, *Arial* vai *RomanS*. Izvairieties no bieziem, izplūdušiem vai "serif" (Times New Roman) fontiem.
- **Raksta augstums:** Optimālais drukātā teksta un izmēru ciparu augstums **izdrukā (uz papīra)** ir **2.5 mm**. 
- **Virsraksti:** Apakšvirsrakstiem izmanto **3.5 mm**, bet galvenajiem lapas skatu virsrakstiem — **5.0 mm**.
- **Pozīcija:** Ja teksts atrodas virs izmēru līnijas, tam jāatrodas apmēram **0.5 - 1.0 mm virs** tās, nekad nepārklājot līniju.
