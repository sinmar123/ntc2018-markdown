# Istruzioni G7 R07, rettifica append-only del verbale

Riprendere lo stesso contesto V `20260909_165403_00ba4e`. Verificare esclusivamente la cartella `/blocco/g7/rettifica-verbale-001` e il suo manifest; non riaprire G6, inventario, render o confronto.

Il verbale originario ha SHA-256 `8a89b8834b51b3a9102d8308fbb25a3165533e4729d343da155b8ed334abcd2b` ed è immutato. La rettifica ha SHA-256 `21c410847bdb497c9c3af8500fd697e700b735f9bf38773e9e1ad0c327eb710c`.

Controllare tre punti:

1. dichiarazione della natura AI, dell'assenza di revisione umana integrale e dell'isolamento reale;
2. classificazione `AF-3.4.5-01` come A/AF per il punto finale assente dopo `1 W/m²K°`, forma conservata nel target, non N, non AF-COR e non ERR-MD;
3. presenza degli URL ufficiali per D.M. 17 gennaio 2018, Circolare n. 7/2019 e D.M. 9 marzo 2023.

Il giudizio base R06 è `OK`, manifest di rilascio SHA-256 `e338cac1d900f68473c48e30f7dfe11a6070cd4abf4649d8faf39415759a4586`, zero rilievi. Se il delta è completo e coerente, scrivere `/blocco/giudizio-g7.json` con G0-G7 `OK`, zero rilievi, il manifest base invariato e l'impronta del manifest della rettifica in un campo separato.
