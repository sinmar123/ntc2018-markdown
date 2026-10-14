"""Applica in ordine le voci attuale/proposto: ogni attuale deve comparire una sola volta nel file al momento dell'applicazione."""
import json, sys
voci=[v for p in sys.argv[1:] for v in json.load(open(p))]
cache={}
for v in voci:
    f=v["file"]; t=cache.get(f) or open(f,encoding="utf-8").read()
    n=t.count(v["attuale"])
    if n!=1: sys.exit(f"{v['id']}: attuale presente {n} volte in {f}")
    cache[f]=t.replace(v["attuale"],v["proposto"])
for f,t in cache.items(): open(f,"w",encoding="utf-8").write(t)
print("voci applicate:",len(voci),"file:",len(cache))
