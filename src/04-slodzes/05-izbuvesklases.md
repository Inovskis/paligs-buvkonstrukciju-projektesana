# Izbūves klases tērauda konstrukcijām

Tērauda būvkonstrukciju izpildes (izbūves) klase (Execution Class, EXC) nosaka prasības izgatavošanas un montāžas kvalitātes kontrolei saskaņā ar standartu LVS EN 1090-2.

Parasti izpildes klasi pieņem atbilstoši būves seku klasei (piemēram, EXC1 atbilst CC1, EXC2 atbilst CC2), tomēr vienas būves ietvaros dažādiem elementiem izpildes klases var atšķirties. Saskaņā ar LVS EN 1993-1-1 C pielikumu, izbūves klasi EXC nosaka, balstoties uz trim faktoriem:
1. **Seku klase (CC)** (CC1, CC2 vai CC3);
2. **Izmantošanas klase (SC)** (SC1 vai SC2);
3. **Ražošanas klase (PC)** (PC1 vai PC2).

---

## Izpildes klases (EXC) noteikšanas matrica

| Ražošanas klase | Izmantošanas klase | Seku klase CC1 | Seku klase CC2 | Seku klase CC3 |
| :--- | :--- | :---: | :---: | :---: |
| **PC1**<br>*(Nemetināti elementi, tērauds < S355)* | **SC1** *(statiska)* | EXC1 | EXC2 | EXC3 |
| | **SC2** *(dinamiska)* | EXC2 | EXC3 | EXC3 |
| **PC2**<br>*(Metināti elementi, tērauds \\(\ge\\) S355)* | **SC1** *(statiska)* | EXC2 | EXC2 | EXC3 |
| | **SC2** *(dinamiska)* | EXC2 | EXC3 | EXC4 |

*Piezīme: Parastām ēkām (statiska slodze, seku klase CC2, izmantošanas klase SC1 un metināti elementi no S355 tērauda - PC2) standarta izpildes klase ir **EXC2**.*

---

## Kategoriju skaidrojums

### 1. Izmantošanas klases (Service Categories)
Raksturo konstrukcijas noslogojuma veidu un ekspluatācijas apstākļus:
- **SC1 (statiska):** Konstrukcijas, kas projektētas tikai statiskām vai kvazistatiskām slodzēm (piemēram, parastas dzīvojamās, biroju un noliktavu ēkas).
- **SC2 (dinamiska):** Konstrukcijas, kas pakļautas noguruma iedarbei no dinamiskām slodzēm (piemēram, celtņu ceļu sijas, tilti, torņi, kas pakļauti vēja izraisītām vibrācijām, vai konstrukcijas seismiski aktīvās zonās).

### 2. Ražošanas klases (Production Categories)
Raksturo konstrukcijas ražošanas tehnoloģisko sarežģītību:
- **PC1:** Nemetināti elementi (piemēram, tikai ar skrūvēm savienoti elementi) neatkarīgi no tērauda markas, vai metināti elementi no tērauda markām, kas ir zemākas par S355.
- **PC2:** Metināti elementi no tērauda markas S355 un augstākas (piemēram, S355, S420, S460), vai elementi, kuru izgatavošanā tiek izmantota termiskā griešana, aukstā formēšana vai termiskā apstrāde.
