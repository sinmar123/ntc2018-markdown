// Configurazione di MathJax per pymdownx.arithmatex (modalità generic).
// Riporta _preambolo-tag.tex: i numeri delle formule fra parentesi quadre,
// \tag{2.4.1} -> [2.4.1]. Le righe \newunicodechar del preambolo non servono:
// MathJax legge direttamente ξ, η, Θ, α, φ, ≤, ≥ e gli apici Unicode.
window.MathJax = {
  loader: { load: ["[tex]/tagformat"] },
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    packages: { "[+]": ["tagformat"] },
    tagformat: { tag: (tag) => "[" + tag + "]" }
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

// I titoli con formule arrivano nei menu come testo grezzo, per esempio «\(q_2\)»:
// MathJax compone solo la classe arithmatex, quindi la si aggiunge a quelle voci.
function formuleNeiMenu() {
  return [...document.querySelectorAll(".md-nav .md-ellipsis, .md-nav .md-nav__link")]
    .filter((e) => e.children.length === 0 && e.textContent.includes("\\("))
    .map((e) => { e.classList.add("arithmatex"); return e; });
}

// Ricomposizione dopo i cambi di pagina; al primo caricamento MathJax compone da sé,
// comprese le voci dei menu se la classe è già al suo posto.
document$.subscribe(() => {
  const menu = formuleNeiMenu();
  if (!MathJax.startup || !MathJax.startup.output) {
    if (MathJax.startup && MathJax.startup.promise && menu.length)
      MathJax.startup.promise.then(() => MathJax.typesetPromise(menu));
    return;
  }
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
