# Rettifica: tolto il nome dell'editor di note dalle evidenze, 2026-10-13

Su decisione di Sandro del 2026-10-13 il progetto lavora soltanto con file Markdown, senza un editor di note dedicato. Il nome dell'editor usato fino a settembre 2026 è stato tolto da tutto il repository, comprese le evidenze congelate qui sotto. Sandro ha scelto di includere le evidenze sapendo che le loro impronte compaiono nei manifest delle verifiche.

Che cosa è cambiato, sempre e solo in queste frasi:

- catalogo delle normalizzazioni, voce 11: «apparato [nome] (wikilink …)» diventa «apparato di navigazione (wikilink …)»;
- catalogo, voce 12, e verbali che la citano: tolto «[nome] compreso» dall'elenco dei viewer;
- procedura congelata: «niente wikilink [nome]» diventa «niente wikilink `[[…]]`»; tolta la richiesta del frontmatter `aliases` negli indici;
- note e README dei pacchetti: «fuori da [nome]» diventa «in qualsiasi editor Markdown».

Nessun giudizio di verifica, conteggio, testo normativo o esito è cambiato. I manifest non sono stati modificati: per controllare una verifica passata si confronta l'impronta del manifest con la colonna «prima» di questa tabella; quella attuale del file è nella colonna «dopo». Il contenuto originale di ogni file resta nella storia git, al commit precedente a questa rettifica.

| File | SHA-256 prima | SHA-256 dopo |
|---|---|---|
| `verifica-conformita/normalizzazioni-dichiarate-NTC2018.md` | `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6` | `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43` |
| `verifica-conformita/vc-3.4.4-20260905/PROCEDURA-VC-congelata.md` | `3ed1723a25f875fad7632b5a7b7ce773d435dcb685fec938ea18df2524be93db` | `66fbf85d9f0e860feca75347de00bae0687e39b28d4bfb1fddb79bbf73dcea1c` |
| `verifica-conformita/vc-3.4.4-20260905/catalogo-congelato.md` | `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6` | `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43` |
| `verifica-conformita/vc-3.4.4-20260905/g6-r01b/b01/canone.md` | `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` | `cf92aa13d12237ab71ff18eb2f8232eff9027fe9a80afc2a862478044f4bb437` |
| `verifica-conformita/vc-ntc2018-3.1-2026-09-12/catalogo.md` | `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6` | `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43` |
| `verifica-conformita/vc-ntc2018-3.1-2026-09-12/g6-r01/b01/canone.md` | `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` | `cf92aa13d12237ab71ff18eb2f8232eff9027fe9a80afc2a862478044f4bb437` |
| `verifica-conformita/vc-ntc2018-3.1-2026-09-12/procedura-r04.md` | `9c43358436f1e4f3ba92b16b95872afccf45e6cdb277d365e4fe5ea16f546a96` | `54abcfbb243b95fdfa4f65ee3e6c7181347835a0ac9ed250aa7bd8dece1194de` |
| `verifica-conformita/vc-ntc2018-3.4.5-2026-09-10/g6/canone.md` | `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` | `cf92aa13d12237ab71ff18eb2f8232eff9027fe9a80afc2a862478044f4bb437` |
| `verifica-conformita/vc-ntc2018-3.4.5-2026-09-10/metodo/PROCEDURA-VC-r03-congelata.md` | `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c` | `efb5f0f2fe9e5e75cb22459cb89e11e7ec84cf73f575bf161c7505ab85974bd1` |
| `verifica-conformita/vc-ntc2018-3.4.5-2026-09-10/metodo/normalizzazioni-congelate.md` | `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6` | `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43` |
| `verifica-conformita/vc-ntc2018-3.4.5-2026-09-10/rettifica-verbale-001/PROCEDURA-VC-r03-congelata.md` | `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c` | `efb5f0f2fe9e5e75cb22459cb89e11e7ec84cf73f575bf161c7505ab85974bd1` |
| `verifica-conformita/vc-ntc2018-3.4.5-2026-09-10/rettifica-verbale-001/normalizzazioni-congelate.md` | `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6` | `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43` |
| `verifica-conformita/vc-ntc2018-3.5-2026-09-11/addendum-lista-correzioni-g6-r01-001.json` | `0b2e128cb0cf3d1ee16d0f689acd91b5c3acffd676ce39a96f9b79cd900e0bb9` | `3360427c2a6e0519e369fbb078da4daf7938b14161f0b52b9c40a7c8045e7709` |
| `verifica-conformita/vc-ntc2018-3.5-2026-09-11/adjudicazione-r01/addendum-lista-correzioni-g6-r01-001.json` | `0b2e128cb0cf3d1ee16d0f689acd91b5c3acffd676ce39a96f9b79cd900e0bb9` | `3360427c2a6e0519e369fbb078da4daf7938b14161f0b52b9c40a7c8045e7709` |
| `verifica-conformita/vc-ntc2018-3.5-2026-09-11/g6-cdx-r01/b01/canone.md` | `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` | `cf92aa13d12237ab71ff18eb2f8232eff9027fe9a80afc2a862478044f4bb437` |
| `verifica-conformita/vc-ntc2018-3.5-2026-09-11/g6-cdx-r02/b01/canone.md` | `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` | `cf92aa13d12237ab71ff18eb2f8232eff9027fe9a80afc2a862478044f4bb437` |
| `verifica-conformita/vc-ntc2018-3.5-2026-09-11/metodo/PROCEDURA-VC-r03-congelata.md` | `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c` | `efb5f0f2fe9e5e75cb22459cb89e11e7ec84cf73f575bf161c7505ab85974bd1` |
| `verifica-conformita/vc-ntc2018-3.5-2026-09-11/metodo/normalizzazioni-congelate.md` | `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6` | `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43` |
| `verifica-conformita/vc-ntc2018-3.5-2026-09-11/pre-e-cdx-r01/cap03/annotazioni/README.md` | `2102b9a19435cf077c2e13c8f3c22824499eb0a9e2eebd682028a0025768ed85` | `47014a2ca64139fc1e3f3235e7a17645a8ff00bd3fcb43b5a6b034846a849aea` |
| `verifica-conformita/vc-ntc2018-3.6-2026-09-11/e-af-r01/pre-e-af/README.md` | `8ee1f5ee97db57d3f82173b8c0082e72bf39e1fba566cc0a01d3a6c88514d5e3` | `95fbb73806628bdc93ea7e64638b802d4a1deb4ed2c48d1545dada64b5db9309` |
| `verifica-conformita/vc-ntc2018-3.6-2026-09-11/g6-r01/b01/canone.md` | `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` | `cf92aa13d12237ab71ff18eb2f8232eff9027fe9a80afc2a862478044f4bb437` |
| `verifica-conformita/vc-ntc2018-3.6-2026-09-11/g6-r01/b02/canone.md` | `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` | `cf92aa13d12237ab71ff18eb2f8232eff9027fe9a80afc2a862478044f4bb437` |
| `verifica-conformita/vc-ntc2018-3.6-2026-09-11/g6-r01/b03/canone.md` | `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` | `cf92aa13d12237ab71ff18eb2f8232eff9027fe9a80afc2a862478044f4bb437` |
| `verifica-conformita/vc-ntc2018-3.6-2026-09-11/g6-r02/b01/canone.md` | `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` | `cf92aa13d12237ab71ff18eb2f8232eff9027fe9a80afc2a862478044f4bb437` |
| `verifica-conformita/vc-ntc2018-3.6-2026-09-11/g6-r02/b02/canone.md` | `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` | `cf92aa13d12237ab71ff18eb2f8232eff9027fe9a80afc2a862478044f4bb437` |
| `verifica-conformita/vc-ntc2018-3.6-2026-09-11/metodo/catalogo-congelato.md` | `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6` | `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43` |
| `verifica-conformita/vc-ntc2018-3.6-2026-09-11/metodo/procedura-congelata.md` | `4bd4440a6f9b204338e97ecf78c9bb74ab0d9e04f7478b9c97c436c62e817c7c` | `efb5f0f2fe9e5e75cb22459cb89e11e7ec84cf73f575bf161c7505ab85974bd1` |
| `verifica-conformita/vc-ntc2018-3.6-2026-09-11/procedura-chiusura-r04-20260912.md` | `9c43358436f1e4f3ba92b16b95872afccf45e6cdb277d365e4fe5ea16f546a96` | `54abcfbb243b95fdfa4f65ee3e6c7181347835a0ac9ed250aa7bd8dece1194de` |
| `verifica-conformita/vc-ntc2018-8.1-2026-09-12/catalogo-congelato.md` | `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6` | `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43` |
| `verifica-conformita/vc-ntc2018-8.1-2026-09-12/procedura-congelata.md` | `9c43358436f1e4f3ba92b16b95872afccf45e6cdb277d365e4fe5ea16f546a96` | `54abcfbb243b95fdfa4f65ee3e6c7181347835a0ac9ed250aa7bd8dece1194de` |
| `verifica-conformita/vc-ntc2018-8.2-2026-09-12/catalogo-congelato.md` | `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6` | `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43` |
| `verifica-conformita/vc-ntc2018-8.2-2026-09-12/procedura-congelata.md` | `658d98340bde641fc683e0e4f63bf1da12ebc8f854f44bcce4a0824a11a9b690` | `ec1bef58e563879f3463c85813511845484931073192d5ca677e9edbd73c28db` |
| `verifica-conformita/vc-ntc2018-8.3-2026-09-30/catalogo-congelato.md` | `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6` | `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43` |
| `verifica-conformita/vc-ntc2018-8.3-2026-09-30/procedura-congelata.md` | `403157d71ba00bababeefad6b920915e631627bdf55e9ff1e9679cdbeea8383c` | `83a04183fca5e0051892e4f33d624be8fef654c5d8d4f66ca416c7225769a531` |
| `verifica-conformita/vc-ntc2018-introduzioni-3.2-3.4-2026-09-12/catalogo.md` | `d71319206ec54bcac3639dfd0b97c41754fa1062655b2d35c36ee5d6cb3036d6` | `dd5f1b9980e6fd37bd0444277d8b69d6ac0c000b91c1cf659a4f9a398b4a7c43` |
| `verifica-conformita/vc-ntc2018-introduzioni-3.2-3.4-2026-09-12/g6-r01/b01/canone.md` | `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` | `cf92aa13d12237ab71ff18eb2f8232eff9027fe9a80afc2a862478044f4bb437` |
| `verifica-conformita/vc-ntc2018-introduzioni-3.2-3.4-2026-09-12/g6-r01/b02/canone.md` | `546023234aec119b42de98bb7499187fdb8445f1ac83e5b32743e13174c1eb44` | `cf92aa13d12237ab71ff18eb2f8232eff9027fe9a80afc2a862478044f4bb437` |
| `verifica-conformita/vc-ntc2018-introduzioni-3.2-3.4-2026-09-12/procedura-r05.md` | `658d98340bde641fc683e0e4f63bf1da12ebc8f854f44bcce4a0824a11a9b690` | `ec1bef58e563879f3463c85813511845484931073192d5ca677e9edbd73c28db` |
| `verifica-conformita/verbale-VC-NTC2018-4.2-A-2026-08-06.md` | `b7b08b8aa2eeba8590979994bd4a9fffe2a7acf568244a1a47e665a95d795eeb` | `64568844a81638cde32b28580b285cc3e903bd692938bbd068a959fadf2f8887` |
| `verifica-conformita/verbale-VC-ntc2018-3.5-2026-09-11.md` | `45020f9bc01d1081bebcb938be5ca4cd7c5b5d0018a9d5c42b89a7b22390af40` | `599ec11d0d9c27e96eb1f8a4f6eb26c4b2beb4f261ca246605e11923e0f46022` |

Firma: CC cloud.
