# Lietderīgās slodzes

Lietderīgās slodzes ir mainīgas iedarbības, ko rada cilvēku uzturēšanās un pārvietošanās, mēbeles, iekārtas, transportlīdzekļi un citi pārvietojami objekti.

**Lietderīgās slodzes un to raksturīgās vērtības saskaņā ar LVS EN 1991-1-1/NA:**

| Kat. | Raksturīgā izmantošana | $q_k$ (kN/m²) | $Q_k$ (kN) | Piemēri un skaidrojumi |
| :---: | :--- | :---: | :---: | :--- |
| **A** | **Mājsaimniecības un dzīvojamās telpas**<br>— Grīdas<br>— Kāpnes<br>— Balkoni | <br>2,00<br>3,00<br>2,50 | <br>2,00<br>3,00<br>2,50 | Telpas dzīvojamās mājās, guļamistabas un palātas slimnīcās, guļamistabas viesnīcās un viesu mītnēs, virtuves un tualetes. |
| **B** | **Biroju telpas** | 2,50 | 2,50 | Biroju telpas, sapulču telpas birojos. |
| **C** | **Pulcēšanās platības**<br>— **C1**: Platības ar galdiem<br>— **C2**: Platības ar nostiprinātām sēdvietām<br>— **C3**: Brīvas platības cilvēku kustībai<br>— **C4**: Platības fiziskām darbībām<br>— **C5**: Platības lielām cilvēku masām | <br>2,50<br>3,00<br>4,00<br>5,00<br>6,00 | <br>3,00<br>4,00<br>4,00<br>5,00<br>4,00 | **C1**: Kafejnīcas, restorāni, skolas, ēdnīcas, lasītavas.<br>**C2**: Baznīcas, teātri, kinoteātri, konferenču un lekciju zāles.<br>**C3**: Muzeji, izstāžu zāles, sabiedriskās ēkas, slimnīcas, stacijas.<br>**C4**: Deju zāles, vingrošanas zāles, skatuves.<br>**C5**: Koncertu halles, sporta zāles, tribīnes, terases. |
| **D** | **Tirdzniecības platības**<br>— **D1**: Vispārējie mazumtirdzniecības veikali<br>— **D2**: Universālveikali | <br>4,00<br>5,00 | <br>4,00<br>7,00 | **D1**: Mazumtirdzniecības veikali.<br>**D2**: Universālveikali, lielveikali ar intensīvu preču kustību. |
| **E** | **Noliktavu un industriālās platības**<br>— **E1**: Noliktavas un preču uzglabāšana | 7,50 | 7,00 | Lietderīgā platība uz noliktavu grīdām, grāmatu un arhīvu krātuves. |
| **F** | **Satiksmes platības (bruto svars $\le 30$ kN)** | 2,50 | 20,00 | Vieglo automobiļu garāžas un transportlīdzekļu satiksmes vietas. |
| **G** | **Satiksmes platības ($30\text{ kN} < \text{bruto svars} \le 160\text{ kN}$)** | 5,00 | 90,00 | Transportlīdzekļu satiksmes vietas ar lielākiem transportlīdzekļiem. |
| **H** | **Jumtu lietderīgās slodzes** | 0,40 | 1,00 | Jumti, kas pieejami tikai to uzturēšanai un remontam (analogu slodzi var pieņemt arī apkalpošanas tiltiņiem). |
| **—** | **Neizmantojamas bēniņu platības** | 1,00 | 2,00 | Zonas ap iekārtām un neizmantojami bēniņi (iekļauts 2022. gada nacionālajā pielikumā). |
| **—** | **Kāpnes (ja nav norādīts citādi)** | 3,00 | 3,00 | Koplietošanas kāpņu laukumi un pakāpieni (iekļauts 2022. gada nacionālajā pielikumā). |

---

### Noslogotās platības samazinājuma koeficients $\alpha_A$

Kategorijām no A līdz D slodzi uz nesošajām konstrukcijām (piemēram, sijām un kolonnām) ir atļauts samazināt, reizinot raksturīgo slodzi ar samazinājuma koeficientu $\alpha_A$, kas ievērtē varbūtību, ka visa lielā platība netiks noslogota maksimāli:

$$\alpha_A = \frac{5}{7}\psi_0 + \frac{A_0}{A} \le 1,0$$

Kur:
- $A_0 = 10\text{ m}^2$ (bāzes platība);
- $A$ ir noslogotā (balstītā) laukuma platība ($\text{m}^2$), kas nodod slodzi uz pārbaudāmo elementu;
- $\psi_0$ ir attiecīgās kategorijas slodzes kombinācijas koeficients.

**Ierobežojumi:**
- Kategorijām C un D jānodrošina, ka $\alpha_A \ge 0,60$.
- Kategorijām A un B parasti jānodrošina, ka $\alpha_A \ge 0,60$.
- Noliktavu telpām (E kategorija) slodzes samazināšana pēc platības nav atļauta ($\alpha_A = 1,0$).

---

## Slodžu kombināciju koeficienti ($\psi$ koeficienti)

Kombinējot dažādas iedarbes, jāizmanto kombinācijas koeficienti $\psi_0$, $\psi_1$ un $\psi_2$, kas noteikti LVS EN 1990 un nacionālajos pielikumos. Tie ņem vērā varbūtību, ka ne visas mainīgās slodzes vienlaicīgi sasniegs savu raksturīgo vērtību.

| Iedarbe / Slodze | $\psi_0$ | $\psi_1$ | $\psi_2$ |
| :--- | :---: | :---: | :---: |
| **Lietderīgās slodzes ēkās (pēc kategorijām):** | | | |
| — A kategorija: mājsaimniecības un dzīvojamās telpas | 0,7 | 0,5 | 0,3 |
| — B kategorija: biroju telpas | 0,7 | 0,5 | 0,3 |
| — C kategorija: pulcēšanās telpas | 0,7 | 0,7 | 0,6 |
| — D kategorija: tirdzniecības telpas | 0,7 | 0,7 | 0,6 |
| — E kategorija: noliktavu telpas | 1,0 | 0,9 | 0,8 |
| — F kategorija: transportlīdzekļu kustība, bruto svars $\le 30$ kN | 0,7 | 0,7 | 0,6 |
| — G kategorija: transportlīdzekļu kustība, bruto svars 30–160 kN | 0,7 | 0,5 | 0,3 |
| — H kategorija: jumti (pieejami tikai uzturēšanai) | 0,0 | 0,0 | 0,0 |
| **Sniega slodzes uz ēkām (Latvijā):** | | | |
| — Sniega slodze (references augstums $H \le 1000$ m) | 0,7 | 0,5 | 0,2 |
| **Citas slodzes:** | | | |
| — Vēja slodzes uz ēkām | 0,6 | 0,2 | 0,0 |
| — Temperatūras iedarbība (ne ugunsgrēka gadījumā) | 0,6 | 0,5 | 0,0 |
