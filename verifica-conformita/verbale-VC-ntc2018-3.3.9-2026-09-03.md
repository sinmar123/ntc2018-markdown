---
scope_id: ntc2018-3.3.9
data: 2026-09-03
stato: VC-OK
markdown_sha256: 67fd21f95d852f39aee88ecd1766916fcc05866604925daed143626a85190f18
fonte_ntc_sha256: dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46
fonte_circolare_sha256: f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c
---

# Verbale di verifica di conformità - NTC 2018 § 3.3.9

Perimetro: `cap03/3.3.9-vento-coefficiente-dinamico.md`, § 3.3.9 NTC a p. fisica 60 e § C3.3.9 Circolare a p. fisica 75. Lo scope comprende due titoli e tre capoversi; non contiene formule numerate o non numerate, tabelle, figure o asset.

Le fonti ufficiali congelate sono state ricalcolate e coincidono con gli hash registrati. La ricognizione G1 R02, estesa a entrambi gli atti dello scope e dotata di stringhe di ricerca ripetibili, non ha individuato modifiche successive incidenti sul § 3.3.9 o sul § C3.3.9; il D.M. 9 marzo 2023 interviene sull'articolo 2 del decreto e sui punti 11.4.2 e 11.5.2, con sospensione terminata il 22 marzo 2025, non sul presente scope.

G0-G5 hanno riconciliato integralmente confini, inventario, prosa e navigazione. Il controllo P1 ha individuato due `ERR-MD` nei soli titoli: cassa non conforme in entrambi e punto aggiunto dopo `C3.3.9`. Un correttore P1 distinto ha applicato soltanto le due sostituzioni congelate; il diff inverso ricostruisce esattamente lo snapshot iniziale. La rigenerazione dell'indice interno ha modificato soltanto l'apparato derivato coerente con il titolo.

Il preflight ha chiuso con copertura 2/2 pagine, 2/2 titoli e 3/3 capoversi, zero apparati, zero asset e zero candidati residui. Il G6 R02 cieco, eseguito da un verificatore P2 `gpt-5.6-sol` xhigh in contesto fresco, ha congelato prima del confronto inventario, esito provvisorio e criterio fonte-prima, ciascuno con hash verificato. Soltanto dopo è stato reso disponibile l'estratto Markdown. Il confronto ha coperto integralmente l'unico blocco di due pagine. Esito: zero `ERR-MD`, zero `ERR-AUDIT` e zero `DUBBIO`.

Le normalizzazioni applicabili sono quelle dell'elenco unico `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md`. Nel presente scope il G6 ha rilevato soltanto la ricomposizione della parola spezzata a fine riga `riferi-` / `mento` in `riferimento`, compresa nella voce 1. Non risultano anomalie di fonte `AF` né correzioni `AF-COR`.

Il controllo aggiuntivo G7 R02 ha sospeso la prima chiusura per tre difetti processuali, poi chiusi dalla ricognizione G1 R02, dal G6 R02 e dalla marcatura dei rapporti precedenti come superati. G7 R03, con P0-D e P2 fresco `gpt-5.6-sol` xhigh, ha chiuso `OK`. Il manifest `verifica-conformita/manifest-sha256-ntc2018-3.3.9-2026-09-03.txt` contiene 44/44 record verificati; SHA-256 del manifest `702e57fcded60a9547b132652082a260d3667536b9c9532a86cfc4ce9e3b06ce`. Indici interni: 311 file e 1.754 collegamenti, `OK`; linter del registro: zero errori e zero avvisi; render finale: una pagina, controllata integralmente.

Tutti i gate G0-G7 sono `OK`. Promozione locale a `VC-OK al 2026-09-03` sul solo snapshot `67fd21f95d852f39aee88ecd1766916fcc05866604925daed143626a85190f18`. I controlli sono stati eseguiti da agenti AI; non è inclusa una revisione umana integrale.

Evidenze: `_tmp_render/cap03/vc-3.3.9-20260903/`.

Firma della redazione: CDX (Codex).
