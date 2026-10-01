import re
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path


P = Path(r"C:\Users\sandro\AppData\Local\Temp\vc36-prove-v-r02-20260911\b02")


def prepara(s: str, origine: str) -> str:
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("ﬀ", "ff").replace("ﬁ", "fi").replace("ﬂ", "fl")
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"(?<=\w)-\s*\n\s*(?=\w)", "", s)
    s = s.replace("ǂ", "≤")
    if origine == "target":
        s = re.sub(r"(?m)^\s*[1-5]\s*$", " ", s)
        # Espansione ammessa della cella accorpata nel corpo di Tab. 3.6.III.
        occ = [m.start() for m in re.finditer(r"Aree di parcheggio e\s+autorimesse", s)]
        if len(occ) >= 2:
            a = occ[1]
            m = re.match(r"Aree di parcheggio e\s+autorimesse", s[a:])
            s = s[:a] + " " + s[a + m.end():]
    return re.sub(r"\s+", " ", s).strip()


def taglia_tabelle(s: str) -> str:
    s = re.sub(
        r"Tab\.\s*3\.6\.II\s*[-–—]\s*Categorie di azione.*?(?=Le azioni dovute agli urti devono)",
        " TAB36II ",
        s,
        flags=re.S,
    )
    s = re.sub(
        r"Tab\.\s*3\.6\.III\s*[-–—]\s*Forze statiche equivalenti agli urti di veicoli.*?(?=Per urti di automobili)",
        " TAB36III ",
        s,
        flags=re.S,
    )
    return s


def tokenizza(s: str):
    return re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]+|\d+(?:[.,/]\d+)*|[≤<>§]", s.lower())


ntc = (P / "estratto-fonte-ntc.txt").read_text(encoding="utf-8")
circ = (P / "estratto-fonte-circ.txt").read_text(encoding="utf-8")
target = (P / "estratto-target.txt").read_text(encoding="utf-8")

ntc = ntc[ntc.index("3.6.3."):]
circ = circ[circ.index("C3.6\x03"):]

for nome in ("ntc", "circ"):
    valore = locals()[nome]
    valore = re.sub(r"(?m)^.*Supplemento ordinario.*GAZZETTA UFFICIALE.*$", "", valore)
    valore = re.sub(r"(?m)^\s*[—-]\s*(?:66|67|77|78|79)\s*[—-]\s*$", "", valore)
    valore = re.sub(r">(3\.6\.[789])@", r"\1", valore)
    locals()[nome] = valore

# Le tre rubriche hanno ToUnicode difettoso nella fonte; la stampa è verificata
# separatamente con ritagli a 600 dpi e dati vettoriali.
circ = re.sub(r"[\x00-\x1f ]+Incendio di progetto", " C3.6.1.5.1 Incendio di progetto", circ)
circ = re.sub(r"[\x00-\x1f ]+Analisi del comportamento meccanico", " C3.6.1.5.3 Analisi del comportamento meccanico", circ)
circ = re.sub(r"[\x00-\x1f ]+Verifiche di sicurezza", " C3.6.1.5.4 Verifiche di sicurezza", circ)

fonte = prepara(ntc + "\n" + circ, "fonte")
target = prepara(target, "target")

fonte = taglia_tabelle(fonte)
target = taglia_tabelle(target)

tf = tokenizza(fonte)
tt = tokenizza(target)
sm = SequenceMatcher(None, tf, tt, autojunk=False)
diffs = [x for x in sm.get_opcodes() if x[0] != "equal"]

print("token_fonte", len(tf))
print("token_target", len(tt))
print("ratio", f"{sm.ratio():.9f}")
print("differenze", len(diffs))
for tag, i1, i2, j1, j2 in diffs:
    print(tag, i1, i2, tf[max(0, i1 - 8):min(len(tf), i2 + 8)], "=>", j1, j2, tt[max(0, j1 - 8):min(len(tt), j2 + 8)])
