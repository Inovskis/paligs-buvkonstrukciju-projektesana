# Noteikumi aģentam (Project-Scoped Rules)

Šis fails satur noteikumus un vadlīnijas, kuras aģentam jāievēro, strādājot pie šī projekta.

---

## Automātiska koda versiju kontrole (Git Push)

- **Komitēšana un nosūtīšana:** Pēc katra sekmīgi pabeigta uzdevuma vai failu uzlabojumu cikla (kad aģents ir pārliecinājies par rezultāta pareizību), aģentam ir patstāvīgi un automātiski jāveic lokāls `git commit` un `git push` uz attālināto repozitoriju (GitHub).
- **Repozitorija protokols:** Repozitorija adresei origin jābūt iestatītai kā HTTPS (lai izmantotu Git Credential Manager autentifikācijai):
  `https://github.com/Inovskis/paligs-buvkonstrukciju-projektesana.git`
- **Autora konfigurācija:** Ja lokālajā repozitorijā nav iestatīts autora vārds/e-pasts, pirms komitēšanas lokāli jāpalaiž:
  ```bash
  git config user.email "kasutaja@example.com"
  git config user.name "Kasutaja"
  git config windows.appendAtomically false
  ```
