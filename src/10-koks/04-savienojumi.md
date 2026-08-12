# Koka konstrukciju mehāniskie savienojumi (LVS EN 1995-1-1 8. nodaļa)

Koka konstrukciju savienojumu nestspējas noteikšana ir viena no atbildīgākajām koka projektēšanas daļām. Savienojumi ar tapveida stiprinājumiem (skrūves, bultskrūves, naglas, dībeļi) tiek aprēķināti saskaņā ar Johansena tecēšanas teoriju (European Yield Model).

---

## Sabrukuma formas un Johansena teorija

Viena griezuma (single shear) koks-koks vai koks-plātne savienojuma raksturīgā bīdes pretestība $F_{v,Rk}$ uz vienu stiprinājumu un vienu bīdes plakni ir jārēķina kā mazākā vērtība no vairākām iespējamām sabrukuma formām (LVS EN 1995-1-1 8.2.2. tabula).

> **Piezīme:** 
> Vērtējamās sabrukuma formas (a līdz f):
> - **(a) un (b) forma:** Koksnes lokālā spiedes (embedment) sagrāve vienā no savienojuma elementiem (stiprinājums paliek taisns).
> - **(c), (d) un (e) forma:** Kombinēta koksnes spiede un viena vai divu plastisko šarnīru (plastic hinges) veidošanās tērauda stiprinājumā.
> - **f (virves efekts):** Ja stiprinājumam (piemēram, kokskrūvei vai bultskrūvei ar uzgriezni) ir stiepes (izraušanas) nestspēja, bīdes nestspēju var palielināt uz "virves efekta" (rope effect) rēķina – maksimāli par 25% naglām un bultskrūvēm, un par 100% kokskrūvēm.

### Aprēķina pretestība ($F_{v,Rd}$)
Aprēķina nestspēju iegūst, reizinot raksturīgo vērtību ar modifikācijas koeficientu un dalot ar materiāla drošuma koeficientu $\gamma_M$:
\\[F_{v,Rd} = F_{v,Rk} \cdot \frac{k_{\text{mod}}}{\gamma_M}\\]
Koka savienojumiem $\gamma_M = 1,30$. Ja savienoti divi dažādi koka materiāli ar atšķirīgu $k_{\text{mod}}$, aprēķinā izmanto mazāko $k_{\text{mod}}$ vērtību, bet izmanto koksnes $\gamma_M = 1,30$. Ja aprēķina tērauda elementu (piemēram, bultskrūves stiepi), tad pielieto tērauda $\gamma_{M2} = 1,25$.

---

## Minimālie attālumi bultskrūvēm (LVS EN 1995-1-1 8.5. tabula)

Lai novērstu koksnes trauslo šķelšanos (splitting) gar šķiedrām, bultskrūvēm un dībeļiem ir jāievēro stingri ģeometriskie attālumi. 
Zemāk dotās vērtības ir **minimālie** attālumi atkarībā no stiprinājuma diametra $d$ un leņķa $\alpha$ (leņķis starp slodzes spēku un koksnes šķiedru virzienu).

| Attāluma apzīmējums | Minimālā vērtība | Skaidrojums |
| :--- | :---: | :--- |
| **Solis $a_1$ (paralēli šķiedrām)** | $(4 + |\cos\alpha|) \cdot d$ | Solis vienā rindā paralēli šķiedrām. Ja spēks ir gar šķiedrām ($\alpha=0$), $a_1 \ge 5d$. |
| **Solis $a_2$ (perpendikulāri šķiedrām)** | $4d$ | Solis starp rindām perpendikulāri šķiedrām. |
| **Gala attālums $a_{3,t}$ (noslogotam galam)** | $\max(7d, 80\text{ mm})$ | Attālums no noslogotā koka gala līdz skrūvei. Ļoti kritisks parametrs! |
| **Gala attālums $a_{3,c}$ (nenoslogotam galam)** | $4d$ | Attālums līdz brīvajam (nenoslogotajam) koka galam. |
| **Malas attālums $a_{4,t}$ (noslogotai malai)** | $\max((2 + 2\sin\alpha)d, 3d)$ | Attālums līdz sijas / elementa malai, uz kuru vērsts spēks. |
| **Malas attālums $a_{4,c}$ (nenoslogotai malai)** | $3d$ | Attālums līdz sijas pretējai (nenoslogotajai) malai. |

> **Svarīgi!**
> Ja spēks darbojas perpendikulāri koksnes šķiedrām (piem., sija karājas uz skrūvēm), papildus savienojuma bīdes nestspējai, **vienmēr** ir jāpārbauda sijas atšķelšanās (splitting) pretestība (LVS EN 1995-1-1 8.1.4. punkts). Tas ir viens no biežākajiem koka konstrukciju avāriju cēloņiem. Dažkārt, lai novērstu atšķelšanos, ir jāievieto papildu stiegrojošās pilnvitnes skrūves (piem., SPAX vai Rothoblaas).

---

## Tērauda - koka savienojumi (Lokšņu / leņķu stiprināšana)
Ja tiek izmantotas tērauda detaļas (piemēram, biezās plāksnes dībeļu mezglos vai leņķi):
- Plāna tērauda plāksne ($t \le 0,5d$): Plāksnē neveidojas iespīlējums, aprēķina modelī rotācija netiek ierobežota.
- Bieza tērauda plāksne ($t \ge d$ vai precīzāk $t \ge d$ un urbuma pielaide ir $<0,1d$): Stiprinājums tērauda plāksnē tiek uzskatīts par iespīlētu (momentizturīgu šajā punktā). Tas ievērojami palielina mezgla pretestību, jo maina plastiskā šarnīra veidošanās modeli.
