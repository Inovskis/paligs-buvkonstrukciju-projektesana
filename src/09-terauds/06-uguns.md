# Ugunsdrošu tērauda konstrukciju projektēšana

Ugunsgrēka situācijā tērauda mehāniskās īpašības (plūstamības robeža un elastības modulis) strauji samazinās, paaugstinoties materiāla temperatūrai. Tērauda konstrukciju ugunsizturības aprēķinus veic saskaņā ar standartu **LVS EN 1993-1-2**.

---

## Materiāla parciālie drošības koeficienti ugunsgrēkā ($\gamma_{M,fi}$)

Ugunsgrēks ir ārkārtēja (avārijas) projektējamā situācija (acc. to LVS EN 1990), kurā tiek pieļauta zemāka drošuma rezerve nekā normālos ekspluatācijas apstākļos. Tādēļ materiālu parciālie koeficienti ugunsgrēka situācijā tiek pieņemti vienādi ar **$1,00$**.

| Konstrukcijas pārbaudes veids | Koeficients normālā temperatūrā | Koeficients ugunsgrēka situācijā ($\gamma_{M,fi}$) |
| :--- | :---: | :---: |
| **Šķērsgriezuma nestspējas pārbaude** | $\gamma_{M0} = 1,00$ | $\gamma_{M,fi} = 1,00$ |
| **Elementu stabilitātes (klupšanas) pārbaude** | $\gamma_{M1} = 1,00$ | $\gamma_{M,fi} = 1,00$ |
| **Stieptu elementu trauslais sabrukums** | $\gamma_{M2} = 1,25$ | $\gamma_{M,fi} = 1,00$ |
| **Savienojumu (skrūvju, šuvju) nestspējas pārbaude** | $\gamma_{M2} = 1,25$ | $\gamma_{M,fi} = 1,00$ |

---

## Tērauda stiprības un stinguma samazinājuma koeficienti ($k_y,\theta$, $k_E,\theta$)

Temperatūras ietekmi uz tērauda īpašībām raksturo samazinājuma koeficienti attiecībā pret vērtībām $20\ ^\circ\text{C}$ temperatūrā:
- **Plūstamības robežas samazinājums:** $f_{y,\theta} = k_{y,\theta} \cdot f_y$
- **Elastības moduļa samazinājums:** $E_{a,\theta} = k_{E,\theta} \cdot E_a$

**Tērauda redukcijas koeficienti pie galvenajām temperatūrām (LVS EN 1993-1-2 3.1. tabula):**
- **Līdz $400\ ^\circ\text{C}$:** Tērauda plūstamības robeža nesamazinās ($k_{y,\theta} = 1,00$). Elastības modulis sāk kristies jau pie $100\ ^\circ\text{C}$ ($k_{E,400} = 0,70$).
- **Pie $500\ ^\circ\text{C}$:** $k_{y,500} = 0,78$, $k_{E,500} = 0,60$.
- **Pie $600\ ^\circ\text{C}$:** $k_{y,600} = 0,47$, $k_{E,600} = 0,31$.
- **Pie $700\ ^\circ\text{C}$:** $k_{y,700} = 0,23$, $k_{E,700} = 0,13$.

### Kritiskā tērauda temperatūra ($\theta_{\text{cr}}$)
Kritiskā temperatūra $\theta_{\text{cr}}$ ir tāda tērauda temperatūra, pie kuras konstrukcijas pretestība samazinās līdz iedarbojošos slodžu līmenim ugunsgrēka situācijā. 
- Parastām karkasa konstrukcijām ar vidēju noslodzes pakāpi ($\mu_0 \approx 0,5 \dots 0,6$) neaizsargāta tērauda kritiskā temperatūra parasti ir robežās no **$500\ ^\circ\text{C}$ līdz $600\ ^\circ\text{C}$**.
- Ja nepieciešamais ugunsizturības laiks pārsniedz **R15** (piemēram, R30, R60 vai vairāk), neaizsargātas tērauda konstrukcijas parasti nespēj uzņemt slodzi, un tām ir jāparedz ugunsdrošības aizsarglīdzekļi (reaktīvās krāsas, plātnes vai apmetums).
