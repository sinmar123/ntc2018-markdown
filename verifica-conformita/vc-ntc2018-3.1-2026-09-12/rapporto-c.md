# Rapporto C - § 3.1 introduzione

Data: 2026-09-12. Agente: Codex / CDX. Target: `cap03/3.1-introduzione.md`, SHA-256 `fdccd3a8f264017ed05a72cfb78bfd9c8397f6d3e46e8429b153f293c8d4caf4`.

## Confini e inventario

G0 **OK**. Perimetro depurato: due rubriche, una NTC e una Circolare. NTC: PDF ufficiale p. fisica 46, dalla rubrica `3.1.` fino a prima di `3.1.1.`. Circolare: PDF ufficiale p. fisica 46, dalla rubrica `C3.1` fino a prima di `C3.1.3`. Fra le rubriche e i successivi sottoparagrafi non vi sono prosa o altri contenuti. Esclusi navigazione, separatori e indicazioni editoriali del corpus. Inventario: 2 rubriche; 0 capoversi, formule, tabelle, figure, note o rinvii normativi.

G1 **OK** per riuso della ricognizione del 2026-09-09 sugli stessi atti e ricontrollo mirato GU del 2026-09-12, conservati in `g1/`. Il D.M. 9 marzo 2023 interviene sull'art. 2 del D.M. 17 gennaio 2018 e sui punti 11.4.2 e 11.5.2 delle NTC: non modifica la rubrica 3.1. Nessuna modifica successiva pertinente alla rubrica C3.1 risulta dai contesti ufficiali conservati; i contatori dei segnaposto HTML non sono stati usati come prova negativa.

## Esito G2-G4

G2-G3 **KO**: confronto testuale completo, 2 `ERR-MD` aperti, entrambi di sola presentazione. Il catalogo non ammette la conversione maiuscolo/minuscolo né l'aggiunta del punto dopo `C3.1`. G4 **OK** sul conteggio riconciliato: nessun apparato presente.

| ID | Posizione | Prima | Dopo | Prova | Classe / effetto | Esito |
|---|---|---|---|---|---|---|
| NC-3.1-INTRO-001 | riga 3 | `# 3.1. Opere civili e industriali` | `# 3.1. OPERE CIVILI E INDUSTRIALI` | `ntc-p46-rubrica-e-confine-600dpi.png` | ERR-MD / sola presentazione | aperta, da approvare |
| NC-3.1-INTRO-002 | riga 11 | `## C3.1. Opere civili ed industriali` | `## C3.1 OPERE CIVILI ED INDUSTRIALI` | `circolare-p46-rubrica-e-confine-600dpi.png` | ERR-MD / sola presentazione | aperta, da approvare |

## Provenienza delle prove

Ritagli PyMuPDF della pagina PDF 46 (indice 45), rasterizzati a 600 dpi e verificati visivamente. NTC: rettangolo PDF `(55,88,300,145)`, PNG SHA-256 `7f8d8c64207ec72df0f32a603116c78ed3be183618e5a1631e2ab441c98a7216`, PDF SHA-256 `dda1e397d56d71aa0f5bc457c3ba9b77064a468699dfc37bd056ac6c47105a46`. Circolare: `(55,88,305,141)`, PNG SHA-256 `de3e3f1e42a3681ce384c4fccd5bf9342e4da1e6bd651b6c06fd57c876513c6b`, PDF SHA-256 `f7c3b8d1f443aadb6b3e020b6b6c19813683492ecaadd2c15bf6bf1939aaed7c`.

Stop prima delle correzioni. G5 non eseguito.

## Addendum dopo approvazione

Addendum 2026-09-12, CDX. G2-G3 **OK**: diff 2/2 identico alla lista approvata, nessuna modifica estranea; rubriche corrette coincidenti con le prove NTC p. 46 e Circolare p. 46. G4 resta **OK**. G5 **OK**: depurato di tre righe, due rubriche non vuote, mappa `NTC46`/`CIRC46` completa; pagina canonica unica verificata visivamente, leggibile e priva di tagli, sovrapposizioni o caratteri mancanti. G0-G5 **OK**, zero residui, snapshot `eed07e9a0857055ac55c4e03cdd2413ec08575d2e3434cb847522a39651f80de`. V può partire.
