// Filtro della pagina «Registro delle verifiche»: testo libero e stato.
// Agisce solo se la pagina contiene i controlli #filtri-registro.
document$.subscribe(() => {
  const filtri = document.getElementById("filtri-registro");
  if (!filtri) return;
  const tabella = document.querySelector("article table");
  if (!tabella) return;
  const testo = document.getElementById("filtro-testo");
  const stato = document.getElementById("filtro-stato");
  const conteggio = document.getElementById("filtro-conteggio");
  const righe = [...tabella.tBodies[0].rows];
  const applica = () => {
    const t = testo.value.trim().toLowerCase();
    const s = stato.value;
    let visibili = 0;
    for (const r of righe) {
      const ok = (!s || r.cells[2].textContent.trim() === s) &&
                 (!t || r.textContent.toLowerCase().includes(t));
      r.hidden = !ok;
      if (ok) visibili++;
    }
    conteggio.textContent = `${visibili} di ${righe.length} righe`;
  };
  testo.addEventListener("input", applica);
  stato.addEventListener("change", applica);
  applica();
});
