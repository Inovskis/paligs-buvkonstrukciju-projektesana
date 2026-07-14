# Drošības un stiprības modifikācijas koeficienti

Koka konstrukciju aprēķinā materiālu stiprības un deformācijas īpašības koriģē ar drošības koeficientiem (\\(\gamma_M\\)) un ietekmes koeficientiem (\\(k_{\text{mod}}\\), \\(k_{\text{def}}\\)), kas atkarīgi no slodzes ilguma un vides mitruma.

---

## Materiāla parciālie drošības koeficienti (\\(\gamma_M\\))

Saskaņā ar LVS EN 1995-1-1 materiālu drošības koeficientu vērtības nestspējas robežstāvoklim (ULS):

| Materiāls / Slodžu kombinācija | Parciālais koeficients \\(\gamma_M\\) |
| :--- | :---: |
| Pamata kombinācija (ULS): | |
| — Masīvā koksne | 1,30 |
| — Līmētā koksne (Glulam) | 1,25 |
| — Finiera sloksņu materiāls (LVL), saplāksnis, OSB | 1,20 |
| — Kokskaidu plātnes | 1,30 |
| — Kokšķiedru plātnes (cietās, vidēji cietās, MDF, mīkstās) | 1,30 |
| — Savienojumi (stiprinājuma elementi) | 1,30 |
| — Perforēto metāla plākšņu savienotājlīdzekļi | 1,25 |
| Ārkārtējā (avārijas, ugunsgrēka) kombinācija: | |
| — Visām pārbaudēm un materiāliem | 1,00 |

---

## Modifikācijas koeficienta \\(k_{\text{mod}}\\) vērtības (LVS EN 1995-1-1/NA)

Koeficients \\(k_{\text{mod}}\\) ņem vērā slodzes darbības ilguma un koksnes mitruma ietekmi uz materiāla stiprību. Koka aprēķina stiprību \\(f_d\\) nosaka kā:
\\[f_d = k_{\text{mod}} \cdot \frac{f_k}{\gamma_M}\\]

| Materiāls | Standarts / Tips | Ekspluatācijas klase | Pastāvīgā slodze | Ilgstošā slodze | Vidēja ilguma slodze | Īslaicīgā slodze | Acumirklīgā slodze |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Masīvkoksne | EN 14081-1 | 1 | 0,60 | 0,70 | 0,80 | 0,90 | 1,10 |
| | | 2 | 0,60 | 0,70 | 0,80 | 0,90 | 1,10 |
| | | 3 | 0,50 | 0,55 | 0,65 | 0,70 | 0,90 |
| Līmētais koks (Glulam) | EN 14080 | 1 | 0,60 | 0,70 | 0,80 | 0,90 | 1,10 |
| | | 2 | 0,60 | 0,70 | 0,80 | 0,90 | 1,10 |
| | | 3 | 0,50 | 0,55 | 0,65 | 0,70 | 0,90 |
| **LVL** | EN 14374, EN 14279 | 1 | 0,60 | 0,70 | 0,80 | 0,90 | 1,10 |
| | | 2 | 0,60 | 0,70 | 0,80 | 0,90 | 1,10 |
| | | 3 | 0,50 | 0,55 | 0,65 | 0,70 | 0,90 |
| Saplāksnis | EN 636 | 1 | 0,60 | 0,70 | 0,80 | 0,90 | 1,10 |
| | (Tips EN 636-1, -2, -3) | 2 | 0,60 | 0,70 | 0,80 | 0,90 | 1,10 |
| | | 3 | 0,50 | 0,55 | 0,65 | 0,70 | 0,90 |
| **OSB** | EN 300 (OSB/2) | 1 | 0,30 | 0,45 | 0,65 | 0,85 | 1,10 |
| | EN 300 (OSB/3, OSB/4) | 1 | 0,40 | 0,50 | 0,70 | 0,90 | 1,10 |
| | EN 300 (OSB/3, OSB/4) | 2 | 0,30 | 0,40 | 0,55 | 0,70 | 0,90 |
| Kokskaidu plātnes | EN 312 (P4, P5) | 1 | 0,30 | 0,45 | 0,65 | 0,85 | 1,10 |
| | EN 312 (P5) | 2 | 0,20 | 0,30 | 0,45 | 0,60 | 0,80 |
| | EN 312 (P6, P7) | 1 | 0,40 | 0,50 | 0,70 | 0,90 | 1,10 |
| | EN 312 (P7) | 2 | 0,30 | 0,40 | 0,55 | 0,70 | 0,90 |
| Cietās kokšķiedru plātnes | EN 622-2 (HB.LA, HB.HLA) | 1 | 0,30 | 0,45 | 0,65 | 0,85 | 1,10 |
| | EN 622-2 (HB.HLA 1 vai 2) | 2 | 0,20 | 0,30 | 0,45 | 0,60 | 0,80 |

---

## Slodzes iedarbības ilguma klašu noteikšana

Koka konstrukciju aprēķinos katra slodze tiek klasificēta pēc tās iedarbības ilguma:

| Slodzes iedarbības ilguma klase | Tipiskais ilgums | Piemērojamie slodžu veidi |
| :---: | :---: | :--- |
| Pastāvīgā | Vairāk par 10 gadiem | Konstrukciju pašsvars, grunts un pastāvīgs ūdens spiediens. |
| Ilgstošā | 6 mēneši līdz 10 gadi | Materiālu uzglabāšanas slodze noliktavās, smagu tehnoloģisko iekārtu slodze. |
| Vidēja ilguma | 1 nedēļa līdz 6 mēneši | Lietderīgās slodzes uz pārsegumiem (dzīvojamās un sabiedriskās ēkas), sniega slodze (parasti Latvijā tiek pieņemta kā vidēja ilguma slodze). |
| Īslaicīgā | Mazāk par 1 nedēļu | Vēja slodze (statiskā daļa), slodzes uz kāpnēm, margām, tehniskās apkopes un montāžas slodzes. |
| Acumirklīgā | Dažas sekundes | Vēja brāzmas (dinamiskā daļa), trieciena slodzes, avārijas vai sprādziena slodzes. |

---

## Ekspluatācijas klases (Service Classes)

Lai ievērtētu apkārtējās vides temperatūras un relatīvā mitruma ietekmi uz konstrukciju, tās iedala trīs ekspluatācijas klasēs:

- **1. ekspluatācijas klase:** 
  Raksturojas ar koksnes mitrumu, kas atbilst temperatūrai \\(20\ ^\circ\text{C}\\) un apkārtējā gaisa relatīvajam mitrumam, kas pārsniedz \\(65\%\\) tikai dažas nedēļas gadā. Šajos apstākļos skuju koku vidējais līdzsvara mitrums nepārsniedz **\\(12\%\\)** (piemēram, slēgtas, apkurināmas ēkas). Šajā klasē jāņem vērā plaisāšanas risks koksnes žūšanas laikā.
- **2. ekspluatācijas klase:** 
  Raksturojas ar koksnes mitrumu, kas atbilst temperatūrai \\(20\ ^\circ\text{C}\\) un apkārtējā gaisa relatīvajam mitrumam, kas pārsniedz \\(85\%\\) tikai dažas nedēļas gadā. Līdzsvara mitrums nepārsniedz **\\(20\%\\)** (piemēram, ventilējami bēniņi, nojumes, neapkurināmas ēkas).
- **3. ekspluatācijas klase:** 
  Apstākļi, kas rada lielāku mitruma saturu nekā 2. klasē (līdzsvara mitrums **\\(> 20\%\\)**). Attiecināma uz āra apstākļiem pakļautām konstrukcijām bez pārseguma.

*Svarīgi: Izvēloties ekspluatācijas klasi, jāpievērš uzmanība ne tikai vidējam mitrumam, bet arī tā cikliskām izmaiņām (samirkšanai un izžūšanai), kas var izraisīt lielākas deformācijas un plaisas nekā pastāvīgi augsts mitrums.*
