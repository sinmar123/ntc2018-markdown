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

// Ricomposizione dopo i cambi di pagina; al primo caricamento MathJax compone da sé.
document$.subscribe(() => {
  if (!MathJax.startup || !MathJax.startup.output) return;
  MathJax.startup.output.clearCache();
  MathJax.typesetClear();
  MathJax.texReset();
  MathJax.typesetPromise();
});
