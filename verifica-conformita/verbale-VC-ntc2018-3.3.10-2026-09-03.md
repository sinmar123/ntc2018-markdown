---
scope_id: ntc2018-3.3.10
data: 2026-09-03
stato: VC-OK
markdown_sha256: 888c0d25d5eae5094ded93d635002b3a22964b1294a1a7b98f2ffb4441d98097
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - NTC 2018 § 3.3.10

Perimetro: `cap03/3.3.10-vento-avvertenze-progettuali.md`, § 3.3.10 NTC a p. fisica 60 e § C3.3.10 Circolare a p. fisica 75. Lo scope comprende due titoli e sette capoversi, sei NTC e uno Circolare; non contiene formule, tabelle, figure o asset.

Le fonti ufficiali congelate sono state ricalcolate e coincidono con gli hash registrati. La ricognizione G1 ha considerato entrambi gli atti e conservato una traccia ufficiale ripetibile. Il D.M. 9 marzo 2023 interviene sull'articolo 2 del decreto e sui punti 11.4.2 e 11.5.2, non sul § 3.3.10; non sono state individuate modifiche successive incidenti sul § 3.3.10 o sul § C3.3.10 alla data del controllo.

G0-G5 hanno riconciliato integralmente confini, inventario, prosa e navigazione. Sullo snapshot iniziale sono stati individuati quattro `ERR-MD`: cassa del titolo NTC, `dei fenomeni` anziché `di fenomeni`, `e il flutter` anziché `ed il flutter`, cassa e punto aggiunto nel titolo Circolare. Un correttore P1 distinto ha applicato esclusivamente le quattro sostituzioni congelate; il diff inverso ricostruisce lo snapshot iniziale e la rigenerazione dell'indice interno ha modificato soltanto la voce derivata dal titolo Circolare. Un P1 verificatore diverso ha riconfermato G3 e G5 `OK`.

Le normalizzazioni applicabili sono quelle dell'elenco unico `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`. Nel presente scope sono state riscontrate soltanto spaziature, a capo, ricomposizioni di parole spezzate a fine riga e varianti Unicode degli apostrofi, comprese nelle voci 1 e 2. La disuniformità fonte `NTC 2008`/`NTC2008` varia esclusivamente per uno spazio ed è quindi classe N, non un'anomalia permanente.

La Circolare stampa `nei con fronti`; il Markdown conserva la sequenza alla lettera e la documenta come `AF-3.3-14` in `cap03/annotazioni/3.3-anomalie-fonte.md`. Non risultano altre `AF` nello scope e non vi sono `AF-COR`.

Il G6 R01 cieco è stato eseguito da un P2 fresco `gpt-5.6-sol` xhigh. Prima di rendere disponibile il Markdown sono stati prodotti e congelati inventario, esito provvisorio e criterio fonte-prima, poi ricalcolati dal coordinatore. L'integrità è stata confermata 3/3 per il congelamento e 11/11 per il pacchetto di confronto. Il controllo ha coperto integralmente 9/9 oggetti testuali. L'addendum finale ha fissato i conteggi autoritativi: una `AF`, zero `AF-COR`, zero `ERR-MD`, zero `ERR-AUDIT` e zero `DUBBIO`. Esito G6 `OK`.

Il G7 ha impiegato prima un P0-D per il ricalcolo deterministico e poi un P2 fresco `gpt-5.6-sol` xhigh. Il manifest `verifica-conformita/manifest-sha256-ntc2018-3.3.10-2026-09-03.txt` contiene 39/39 record verificati; SHA-256 del manifest `2884803bb46b52cdd662e1ad606e7d6695ecff446a7a7c52f272566853939b57`. Il P2 ha ripetuto il confronto dei ritagli a 600 dpi col testo canonico, ispezionato il render di una pagina e confermato separazione dei ruoli, catena G0-G6 e assenza di residui. Esito G7 `OK`.

Controlli finali: indici interni, 311 file e 1.754 collegamenti, `OK`; linter del registro, zero errori e zero avvisi; cinque link locali risolti; zero U+FFFD; render finale di una pagina controllato integralmente.

Tutti i gate G0-G7 sono `OK`. Promozione locale a `VC-OK al 2026-09-03` sul solo snapshot `888c0d25d5eae5094ded93d635002b3a22964b1294a1a7b98f2ffb4441d98097`. I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

Evidenze: `_tmp_render/cap03/vc-3.3.10-20260903/`.

Firma della redazione: CDX (Codex).

