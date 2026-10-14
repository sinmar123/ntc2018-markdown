# Consegna al verificatore

Leggere solo questa cartella e le integrazioni fonte espressamente consegnate.
Non aprire coordinamento.json, workspace o altri rapporti. Isolamento istruttivo,
salvo sandbox effettivamente documentata. Il canone.md contiene tutti i criteri.

1. FONTE-PRIMA: osservare integralmente le pagine del PERIMETRO.md e i dettagli
necessari. Scrivere inventario.json con firma effettiva, esito_provvisorio
(LEGGIBILE o DUBBIO), elementi ed esclusioni. Ogni elemento richiede id univoco,
pagina (una chiave di input-fonte.json) e riferimento preciso; ogni esclusione
richiede pagina e riferimento. Non copiare la prosa o tutte le celle:
localizzare capoversi e rettangoli di celle, dichiarando estensione e controllo
integrale. Registrare separatamente formule, condizioni, figure e dubbi.
Schema dei campi: {"firma":"identità effettiva", "esito_provvisorio":"LEGGIBILE",
"elementi":[{"id":"ID scelto da V", "pagina":"chiave fonte", "riferimento":"posizione"}],
"esclusioni":[], "dubbi":[]}.
Il coordinatore valida lo schema prima del congelamento; eventuali difetti
di forma si correggono nello stesso contesto prima di ogni rivelazione.
Fermarsi dopo l'inventario: nessun accesso al target prima del via del coordinatore.

2. CONFRONTO: dopo il congelamento e il via leggere tutto testo.md e gli asset
rivelati. Scrivere rapporto-g6.json: firma, esito (OK o KO), coperti (tutti gli
id verificati), normalizzazioni (numeri del catalogo), rilievi, letture (percorsi),
isolamento. Ogni rilievo specifica id, pagina/posizione, prova e classe proposta.
Con zero rilievi bastano gli ID coperti e l'attestazione di confronto integrale,
senza ricopiare inventario e motivazione OK per ciascuna cella. Un gruppo coperto
significa controllo di TUTTI i suoi componenti, mai campionamento.
Niente correzioni degli input. Richiedere prove ulteriori con domanda aperta.
Fermarsi dopo G6; G7 arriverà nello stesso contesto quando le evidenze sono pronte.

Prosa ordinaria entro 300 parole per fase, oltre a ID e rilievi necessari.
Il limite non tronca copertura, dubbi o prove: motivare l'eventuale superamento
nel rapporto stesso. Non riscrivere hash calcolabili o creare rapporti aggiuntivi.
