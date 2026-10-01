import json
import re
from pathlib import Path

import fitz


BLOCCO = Path(r"C:\Users\sandro\AppData\Local\Temp\vc36-g6-r02-20260911\b02")
MD = (BLOCCO / "testo.md").read_text(encoding="utf-8")

rubriche = [
    "3.6.3. URTI",
    "3.6.3.1 GENERALITÀ",
    "3.6.3.2 CLASSIFICAZIONE DELLE AZIONI DOVUTE AGLI URTI",
    "3.6.3.3 URTI DA TRAFFICO VEICOLARE",
    "3.6.3.3.1 Traffico veicolare sotto ponti o altre strutture",
    "3.6.3.3.2 Traffico veicolare sopra i ponti",
    "3.6.3.4 URTI DA TRAFFICO FERROVIARIO",
    "3.6.3.5 URTI DI IMBARCAZIONI ED AEROMOBILI",
    "C3.6 AZIONI ECCEZIONALI",
    "C3.6.1 INCENDIO",
    "C3.6.1.1 DEFINIZIONI",
    "C3.6.1.2 RICHIESTE DI PRESTAZIONE",
    "C3.6.1.3 CLASSI DI RESISTENZA AL FUOCO",
    "C3.6.1.4 CRITERI DI PROGETTAZIONE",
    "C3.6.1.5 PROCEDURA DI ANALISI DELLA RESISTENZA AL FUOCO",
    "C3.6.1.5.1 Incendio di progetto",
    "C3.6.1.5.3 Analisi del comportamento meccanico",
    "C3.6.1.5.4 Verifiche di sicurezza",
    "C3.6.2 ESPLOSIONI",
    "C3.6.2.3 MODELLAZIONE DELLE AZIONI DOVUTE ALLE ESPLOSIONI",
]
for r in rubriche:
    assert r in MD, r

formule = [
    r"$$F_{d,y} = 0{,}50 F_{d,x} \tag{3.6.7}$$",
    r"$$F = r \cdot F_{d,x} \tag{3.6.8}$$",
    r"$$F = 5 W \tag{3.6.9}$$",
    r"($q_{f,d}$)",
]
for f in formule:
    assert f in MD, f

tab_ii = [
    "| Categoria di azione | Possibili effetti |",
    "| 1 | Effetti trascurabili sulle strutture |",
    "| 2 | Effetti localizzati su parte delle strutture |",
    "| 3 | Effetti generalizzati sulle strutture |",
]
tab_iii = [
    "| Tipo di strada | Tipo di veicolo | Forza $F_{d,x}$ [kN] |",
    "| Autostrade, strade extraurbane | - | 1000 |",
    "| Strade locali | - | 750 |",
    "| Strade urbane | - | 500 |",
    "| Aree di parcheggio e autorimesse | Automobili | 50 |",
    "| Aree di parcheggio e autorimesse | Veicoli destinati al trasporto di merci, aventi massa massima superiore a 3,5 t | 150 |",
]
for row in tab_ii + tab_iii:
    assert row in MD, row

condizioni = [
    "- per d ≤ 5 m:",
    "  - 4000 kN in direzione parallela alla direzione di marcia dei convogli ferroviari;",
    "  - 1500 kN in direzione perpendicolare alla direzione di marcia dei convogli ferroviari;",
    "- per 5 m < d ≤ 15 m:",
    "  - 2000 kN in direzione parallela alla direzione di marcia dei convogli ferroviari;",
    "  - 750 kN in direzione perpendicolare alla direzione di marcia dei convogli ferroviari;",
    "- per d > 15 m pari a zero in entrambe le direzioni.",
    "- curva nominale d'incendio, da individuare tra quelle indicate successivamente, per l'intervallo di tempo di esposizione pari alla classe di resistenza al fuoco prevista, senza alcuna fase di raffreddamento;",
    "- curva naturale d'incendio, da individuare tenendo conto dell'intera durata dello stesso, compresa la fase di raffreddamento fino al ritorno alla temperatura ambiente oppure a condizioni termiche ritenute ininfluenti per le strutture.",
]
for c in condizioni:
    assert c in MD, c

stili = [
    "*carico d'incendio*",
    "*carico d'incendio specifico*",
    "[lorda]{.underline}",
    "*lignei*",
    '*"slow heating curve"*',
    '*"tunnel curve"*',
]
for s in stili:
    assert s in MD, s

doc = fitz.open(BLOCCO / "resa-target" / "target-blocco.pdf")
assert len(doc) == 5
for i, page in enumerate(doc):
    blocks = [b for b in page.get_text("blocks") if b[6] == 0]
    assert blocks, i
    assert all(0 <= b[0] < b[2] <= page.rect.width and 0 <= b[1] < b[3] <= page.rect.height for b in blocks), i

inv = json.loads((BLOCCO / "inventario.json").read_text(encoding="utf-8"))
assert len(inv["elementi"]) == 54
assert len({e["id"] for e in inv["elementi"]}) == 54

print("rubriche", len(rubriche), "OK")
print("formule_inline", len(formule), "OK")
print("righe_tabelle_controllate", len(tab_ii) + len(tab_iii), "OK")
print("condizioni", len(condizioni), "OK")
print("stili_inline", len(stili), "OK")
print("pagine_resa", len(doc), "OK; blocchi entro pagina")
print("id_inventario", len(inv["elementi"]), "unici")
