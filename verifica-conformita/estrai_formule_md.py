# -*- coding: utf-8 -*-
"""Estrae dal markdown vivo i blocchi formula $$...$$ dei lotti F02/F03/F04/F05."""
import re

text = open('cap08/8-esistenti.md', encoding='utf-8').read()
blocks = re.findall(r'\$\$(.*?)\$\$', text, re.S)
targets = ('C8.7.1.', 'C8.7.2.', 'C8.7.4.', 'C8.8.5.')
tag_re = re.compile(r'\\tag\{(C8\.[0-9a-z.]+)\}')

found = []
for b in blocks:
    m = tag_re.search(b)
    if m and any(m.group(1).startswith(t) for t in targets):
        found.append((m.group(1), b.strip()))

for tag, body in found:
    print('=== ' + tag + ' ===')
    print(body)
    print()

print('TOTALE BLOCCHI ESTRATTI:', len(found))
