# Tērauda materiālu fizikālās un mehāniskās īpašības

Tērauda būvkonstrukciju aprēķiniem izmanto stiprības raksturlielumus (plūstamības robežu \\(f_y\\) un stiepes stiprību \\(f_u\\)) un fizikālās konstantes saskaņā ar LVS EN 1993-1-1.

---

## Tērauda stiprības raksturlielumi (LVS EN 1993-1-1 3.1. tabula)

Tērauda stiprība samazinās, palielinoties velmētā elementa biezumam \\(t\\).

**Konstrukciju tērauda stiprības robežvērtības pēc ražošanas standartiem:**

| Standarts un tērauda klase | Tērauda marka | Biezums \\(t \le 40\text{ mm}\\) | Biezums \\(t \le 40\text{ mm}\\) | Biezums \\(40\text{ mm} < t \le 80\text{ mm}\\) | Biezums \\(40\text{ mm} < t \le 80\text{ mm}\\) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| | | **\\(f_y\\) (N/mm²)** | **\\(f_u\\) (N/mm²)** | **\\(f_y\\) (N/mm²)** | **\\(f_u\\) (N/mm²)** |
| EN 10025-2 (Parastie oglekļa tēraudi) | **S 235** | 235 | 360 | 215 | 360 |
| | **S 275** | 275 | 430 | 255 | 410 |
| | **S 355** | 355 | 510 | 335 | 470 |
| | **S 450** | **450** | 550 | 410 | 550 |
| EN 10025-3 (Normalizētie tēraudi) | **S 275 N/NL** | 275 | 390 | 255 | 370 |
| | **S 355 N/NL** | 355 | 490 | 335 | 470 |
| | **S 420 N/NL** | 420 | 520 | 390 | 520 |
| | **S 460 N/NL** | 460 | 540 | 430 | 540 |
| EN 10025-4 (Termomehāniski velmētie tēraudi) | **S 275 M/ML** | 275 | 370 | 255 | 360 |
| | **S 355 M/ML** | 355 | 470 | 335 | 450 |
| | **S 420 M/ML** | 420 | 520 | 390 | 500 |
| | **S 460 M/ML** | 460 | 540 | 430 | 530 |
| EN 10025-5 (Atmosfēras korozijas izturīgie / Corten) | **S 235 W** | 235 | 360 | 215 | 340 |
| | **S 355 W** | 355 | 510 | 335 | 490 |
| EN 10025-6 (Uzlabotie tēraudi pēc rūdīšanas) | **S 460 Q/QL/QL1** | 460 | 570 | 440 | 550 |

*\*Piezīme: Tērauda markai S 450 plūstamības robeža pie \\(t \le 40\text{ mm}\\) ir pareizi norādīta kā \\(450\text{ N/mm}^2\\) (iepriekšējā tabulā bija kļūdaina vērtība 440).*

---

## Konstrukciju tērauda fizikālās konstantes

Būvkonstrukciju elastīgajiem aprēķiniem visā Eirokodeksa saimē izmanto šādas standartizētas tērauda konstantes:

- **Elastības modulis (Junga modulis):**
  \[E = 210\ 000\text{ N/mm}^2 = 210\text{ GPa}\]
- **Bīdes modulis:**
  \[G = \frac{E}{2 \cdot (1 + \nu)} \approx 81\ 000\text{ N/mm}^2 = 81\text{ GPa}\]
- **Puasona koeficients:**
  \[\nu = 0,30\]
- **Lineārās termiskās izplešanās koeficients:**
  \[\alpha = 12 \cdot 10^{-6}\text{ K}^{-1}\text{ (jeb } 1/^\circ\text{C)}\]
- **Blīvums (tilpuma masa):**
  \[\rho = 7850\text{ kg/m}^3\text{ (atbilst tilpumsvaram } \gamma \approx 78,5\text{ kN/m}^3)\]

---

## Korozivitātes (korozijas agresivitātes) klases (ISO 12944-2)

Tērauda elementu pretkorozijas aizsardzības (krāsošanas, cinkošanas) projektēšanai izmanto korozivitātes klases:

| Klase | Korozijas līmenis | Iekštelpu vides raksturojums | Ārtelpu vides raksturojums |
| :---: | :--- | :--- | :--- |
| **C1** | Ļoti zems | Apkurināmas ēkas ar tīru gaisu un zemu mitrumu (biroji, veikali, skolas, viesnīcas). | Nav attiecināms. |
| **C2** | Zems | Neapkurināmas ēkas ar iespējamu kondensāciju (noliktavas, sporta zāles, garāžas). | Lauku apvidi un mazapdzīvotas teritorijas ar zemu gaisa piesārņojumu. |
| **C3** | Vidējs | Ražošanas telpas ar augstu mitrumu un nelielu piesārņojumu (pārtikas cehi, alus darītavas). | Pilsētas un industriālās teritorijas ar mērenu sēra dioksīda piesārņojumu; piekrastes ar zemu sāļumu. |
| **C4** | Augsts | Ķīmiskās rūpnīcas, peldbaseini, kuģu būvētavas. | Industriālās un piekrastes teritorijas ar vidēju sāls aerosola iedarbību. |
| **C5-I** | Ļoti augsts (industriāls) | Telpas ar pastāvīgu kondensāciju un agresīvu ķīmisko piesārņojumu. | Industriāli apgabali ar ļoti augstu mitrumu un agresīvu gaisa piesārņojumu. |
| **C5-M** | Ļoti augsts (jūras) | Telpas ar pastāvīgu mitruma kondensāciju un sāls piesārņojumu. | Piejūras un atklātas jūras (offshore) zonas ar augstu sāls saturu atmosfērā. |
