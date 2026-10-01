---
scope_id: ntc2018-3.1.1
atti:
  - "D.M. 17/01/2018, § 3.1.1 Generalità"
file_markdown: cap03/3.1.1-opere-civili-generalita.md
fonte_ntc: {pdf: verifica-conformita/fonte-ufficiale/GU-2018-42-SO8-DM-17-01-2018.pdf, pagine_fisiche: 46}
fonte_circolare: null
unita_registro: 1
formule_numerate: 0
tabelle: 0
figure: 0
pagine_fonte: 1
stato: CHIUSO
agente: CDX
macchina: W520
presa_in_carico: 2026-08-27T11:54:40+02:00
giro_g6: 1
max_giri: 3
rilievi_aperti: 0
rilievi_persistenti: 0
gate: {G0: OK, G1: OK, G2: OK, G3: OK, G4: OK, G5: OK, G6: OK, G7: OK}
snapshot_sha256: 6b24bfaa2009cab169c81406b2cedce1f2581ed5d60dab5acee3afebdbf4c8a2
attesa_decisione: []
prossimo_passo: "attendere il via libera di Sandro prima di aprire il file 3.1.2"
esecutori:
  apertura: {coordinamento: "CDX/sessione principale", controlli_meccanici: "script locali"}
  g0-g5: {verifica: "subagente P1/gpt-5.6-sol/high", correzione: "CDX/sessione principale", recheck: "subagente P1/gpt-5.6-sol/high"}
  g6-1: {coordinamento: "subagente fresco P2/gpt-5.6-sol/xhigh", inventario: "subagente fresco P2/gpt-5.6-sol/xhigh", blocco: "subagente fresco P2/gpt-5.6-sol/xhigh", esito: "OK, 0 ERR-MD, 0 ERR-AUDIT, 0 DUBBIO"}
  g7: {controlli_deterministici: "script locali", rilascio: "subagente fresco P2/gpt-5.6-sol/xhigh", esito: "OK, manifest 7/7 confermato"}
---

## 2026-08-27 - G7 e rilascio (CDX)

Il controllo finale P2 ha ricalcolato le 7 voci del manifest e ne ha confermato SHA-256 e dimensioni. Snapshot Markdown invariato: `6b24bfaa2009cab169c81406b2cedce1f2581ed5d60dab5acee3afebdbf4c8a2`; rilievi residui: 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`, 0 `AF`, 0 `AF-COR`.

G7 `OK`; scope chiuso e promosso localmente a `VC-OK al 2026-08-27`. Manifest: `verifica-conformita/manifest-sha256-ntc2018-3.1.1-2026-08-27.txt`; verbale: `verifica-conformita/verbale-VC-ntc2018-3.1.1-2026-08-27.md`. Nessun altro file naturale è stato aperto.

## 2026-08-27 - G6 r01 superato (CDX)

G6 eseguito su un unico blocco esterno al workspace, con coordinatore, inventario fonte-prima e verificatore di blocco distinti, tutti P2 `gpt-5.6-sol/xhigh` in contesti freschi. Copertura integrale: 1 titolo, 2 capoversi, 4 frasi; nessun apparato non testuale e nessuna contaminazione dalle sezioni adiacenti.

Esito: 5 occorrenze `NORM` riconducibili a spaziatura, a capo e apostrofo curvo/dritto; 0 `AF`, 0 `AF-COR`, 0 `ERR-MD`, 0 `ERR-AUDIT`, 0 `DUBBIO`. G6 `OK` al primo giro. Evidenza: `_tmp_render/cap03/vc-3.1.1-20260827/g6-r01/rapporto-consolidato.md`.

## 2026-08-27 - G0-G5 e preflight G6 chiusi (CDX)

G0-G5 tutti `OK`. Il primo controllo P1 ha rilevato un solo `ERR-MD`: rubrica `Generalità` anziché `GENERALITÀ`, differenza di cassa non compresa nelle normalizzazioni dichiarate. Corretto il solo H1; un riesame P1 separato ha ricostruito lo snapshot iniziale e confermato che il diff coincide esclusivamente col rilievo.

Il corpo normativo coincide per 546 caratteri su 546 dopo le sole normalizzazioni N di a capo/spazi e apostrofo curvo/dritto. Inventario: 1 titolo, 2 capoversi, 4 frasi, nessun apparato non testuale. Controlli superati: registro senza errori o avvisi; 311 indici interni e 1.754 link conformi; render depurato leggibile; zero candidati residui.

Disegno G6 r01 congelato prima del giro: un inventario fonte-prima e un verificatore di blocco, entrambi P2 `gpt-5.6-sol/xhigh` in contesti freschi; un solo blocco perché lo scope occupa una pagina; nessuna modifica ammessa. Pacchetto esterno al workspace in `%LOCALAPPDATA%\Temp\ntc2018-vc-3.1.1-g6-r01-20260827-1205`; copia delle istruzioni e dei materiali in `_tmp_render/cap03/vc-3.1.1-20260827/g6-r01/` e cartelle collegate.

## 2026-08-27 - apertura dello scope sul file naturale (CDX)

Scope limitato al solo file `cap03/3.1.1-opere-civili-generalita.md` e al § 3.1.1 del D.M. 17/01/2018, pagina fisica 46 della fonte congelata. La Circolare 7/2019 non contiene un § C3.1.1 corrispondente. Il file comprende due capoversi di prosa e nessuna formula, tabella, figura o asset.

Precondizioni di apertura superate: fonte ufficiale presente e ricalcolata con SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`; nessuna scheda esistente e nessun altro scope sul medesimo file. Snapshot Markdown iniziale SHA-256 `1f47bcb83de4e079d65f1fbedc099b1fc550f7e08d5c0fda1ad842abaa82e2ec`.

Routing: controlli meccanici eseguiti con script locali; giudizi G0-G5 riservati a Sol `high`; G6 previsto su un solo blocco cieco con Sol `xhigh` in contesto fresco. Nessuna modifica al Markdown eseguita in apertura.
