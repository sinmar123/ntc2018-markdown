---
scope_id: ntc2018-3.3.2
data: 2026-08-31
stato: VC-OK
markdown_sha256: b9c678cce3396e90f10fec3f435b27b8d34dc7379253851dbe1e8f5fbfe1d80e
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - NTC 2018 § 3.3.2

## Perimetro e metodo

Il controllo riguarda esclusivamente `cap03/3.3.2-vento-velocita-di-riferimento.md`, §§ 3.3.2 del D.M. 17 gennaio 2018 e C3.3.2 della Circolare 21 gennaio 2019 n. 7, pagine fisiche NTC 57 e Circolare 54-55.

Il contenuto naturale corrente è risultato canonicamente identico allo staging della ricomposizione del 26 agosto, salvo i soli apparati di navigazione. Sono stati pertanto riusati G0-G5 e i controlli storici già validi, senza ripeterli. Il G6 finale ha invece ricontrollato integralmente lo scope naturale corrente: 2 titoli, 7 capoversi, 5 voci di elenco, 4 formule con 4 tag, 7 definizioni, una figura e una didascalia.

## Correzioni, asset e apparati

Sono stati trasferiti quattro `ERR-MD` congelati dal G6 storico: cassa del titolo NTC, rimozione dei due punti dopo il primo `dove`, rubrica C3.3.2 senza punto e in maiuscolo, `ed in documenti`. I due `≥` sono stati resi col LaTeX equivalente `\ge` perché il carattere Unicode risultava illeggibile nel PDF di controllo.

La Fig. C3.3.1 è stata ripristinata byte-identica dalla copia già verificata nel G4/G6 storico, SHA-256 `f1b7efd2d676230afd24dede8dd915cb03cd765e45b7c07761d22d5f72faf503`. Il preparatore G6 e il renderer sono stati corretti affinché rinvii redazionali e block ID restino nel Markdown interrogabile ma non entrino nei pacchetti ciechi e nei render.

## Gate ed esito

- G0-G5 `OK` per riuso validato e continuità documentata.
- G6 R01: zero `ERR-MD`, un `ERR-AUDIT` del pacchetto, zero `DUBBIO`.
- G6 R02: `OK`, zero `ERR-MD`, zero `ERR-AUDIT`, zero `DUBBIO`, 3 `AF` conservate.
- G7 P0-D Luna: `OK`, manifest 26/26, linter e indici conformi.
- G7 P2 Sol: `OK` sullo snapshot finale.

Snapshot iniziale: `55565963876a9934e8b3b0f1a287f02c11a534e3ceaad1aabd0f64a2d3236ff5`.

Snapshot finale: `b9c678cce3396e90f10fec3f435b27b8d34dc7379253851dbe1e8f5fbfe1d80e`.

Manifest: `verifica-conformita/manifest-sha256-ntc2018-3.3.2-2026-08-31.txt`, 26 voci, SHA-256 `1e9bd7ea83cc4613000ab33094452f888f32c3963f5a96837c40d05efb28c9ce`.

Evidenze: `_tmp_render/cap03/vc-3.3.2-20260831/`, compresi continuità, G6 R01-R02, G7 e render finale di due pagine.

Tutti i gate G0-G7 sono `OK`. Lo scope è promosso localmente a `VC-OK al 2026-08-31`, esclusivamente sul perimetro e sullo snapshot dichiarati. I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

Firma della redazione: CDX (Codex).
