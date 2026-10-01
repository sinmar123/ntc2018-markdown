---
scope_id: ntc2018-3.1.1
data: 2026-08-27
stato: VC-OK
markdown_sha256: 6b24bfaa2009cab169c81406b2cedce1f2581ed5d60dab5acee3afebdbf4c8a2
fonte_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
---

# Verbale di verifica di conformità - NTC 2018 § 3.1.1

## Perimetro

Il controllo riguarda esclusivamente `cap03/3.1.1-opere-civili-generalita.md`, corrispondente al § 3.1.1 `GENERALITÀ` dell'allegato al D.M. 17 gennaio 2018. Fonte: Gazzetta Ufficiale, Serie generale n. 42 del 20 febbraio 2018, Supplemento ordinario n. 8, pagina fisica 46 e pagina stampata 42. La Circolare 21 gennaio 2019 n. 7 non contiene un § C3.1.1 corrispondente ed è fuori scope.

Confini: dalla rubrica `3.1.1. GENERALITÀ` fino alla frase `della costruzione.`, prima del § 3.1.2. Inventario: 1 titolo, 2 capoversi, 4 frasi, nessuna formula, tabella, figura, nota o asset.

## Fonte e vigenza

Fonte congelata: `verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf`, SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`.

L'identità dell'atto è stata riscontrata sulla Gazzetta Ufficiale, codice redazionale `18A00716`. Il D.M. 9 marzo 2023 modifica l'art. 2 del decreto e introduce sospensioni temporanee relative ai punti 11.4.2 e 11.5.2; non modifica il testo dell'allegato § 3.1.1.

## Gate

- G0 `OK`: scope e confini accertati.
- G1 `OK`: fonte ufficiale identificata, hash ricalcolato e ricognizione della modifica del 2023 eseguita.
- G2 `OK`: inventario source-first riconciliato al 100%.
- G3 `OK`: confronto testuale integrale; titolo e corpo coincidono dopo le sole normalizzazioni dichiarate.
- G4 `OK`: nessun apparato non testuale nello scope.
- G5 `OK`: file indicizzato, tre link di navigazione e àncora interna risolti; verifica globale degli indici interni superata.
- G6 `OK`: primo giro cieco integrale, un blocco; 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`.
- G7 `OK`: controllo finale P2 superato; tutte le 7 voci del manifest coincidono per SHA-256 e dimensione.

## Scarti e correzioni

Nel preflight G3 è stato rilevato un solo `ERR-MD`: rubrica `Generalità` anziché `GENERALITÀ`. È stata corretta soltanto la cassa del titolo. Un riesame P1 in contesto separato ha ricostruito lo snapshot iniziale e confermato che il diff contiene esclusivamente quel rilievo.

Normalizzazioni di classe N applicate e già comprese nell'elenco unico `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`:

- spaziature, a capo e rientri della pagina;
- apostrofo curvo `’` della fonte reso con apostrofo diritto `'` nel Markdown.

Anomalie conservate `AF`: nessuna. Correzioni della fonte `AF-COR`: nessuna. Testo aggiunto alla fonte: nessuno nel pacchetto di confronto; gli apparati di navigazione sono rimossi meccanicamente.

## G6 e indipendenza

Il G6 è stato coordinato da un subagente fresco P2 `gpt-5.6-sol/xhigh`. Inventario fonte-prima e confronto del blocco sono stati eseguiti da due ulteriori subagenti freschi P2 `gpt-5.6-sol/xhigh`, con materiali minimi in staging esterno al workspace. Nessuno ha ricevuto rilievi attesi o audit precedenti e nessuno ha modificato il Markdown.

I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

## Snapshot ed evidenze

Snapshot iniziale Markdown: `1f47bcb83de4e079d65f1fbedc099b1fc550f7e08d5c0fda1ad842abaa82e2ec`.

Snapshot finale verificato: `6b24bfaa2009cab169c81406b2cedce1f2581ed5d60dab5acee3afebdbf4c8a2`.

Evidenze:

- `_tmp_render/cap03/vc-3.1.1-20260827/preflight/rapporto-preflight.md`;
- `_tmp_render/cap03/vc-3.1.1-20260827/fonte/ntc-p46-scope-3.1.1-600dpi.png`;
- `_tmp_render/cap03/vc-3.1.1-20260827/preflight/md-confronto-render.pdf`;
- `_tmp_render/cap03/vc-3.1.1-20260827/g6-r01/rapporto-consolidato.md`;
- `verifica-conformita/manifest-sha256-ntc2018-3.1.1-2026-08-27.txt`.

La resa dei viewer che non usano il template ufficiale del progetto resta una normalizzazione di visualizzazione dichiarata. Il render di controllo depurato dagli apparati di navigazione è leggibile su una pagina; non contiene tag di formula o didascalie automatiche.

## Rilascio

Tutti i gate G0-G7 sono `OK` e non restano rilievi aperti. Il controllo finale P2 ha ricalcolato e confermato le 7 voci del manifest; SHA-256 del manifest `2708672e91eca104fec0acf604eb853bdcfa5a96ff3048c81cef6d4fd9739936`. Lo scope è promosso localmente a `VC-OK al 2026-08-27`. Il giudizio vale soltanto per lo snapshot e il perimetro dichiarati.

Firma della redazione: CDX (Codex).
