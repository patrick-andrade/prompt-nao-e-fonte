# Saídas geradas

Sem números fiscais aqui.

| Pasta | Artefato | Destino |
| --- | --- | --- |
| `outputs/pptx/` | PPTX da reunião interna (Dimensão 3) | **Não** vai ao Netlify |
| `outputs/revealjs-netlify/` | HTML Reveal.js do briefing (`index.html`) | Único publish do Netlify (`netlify.toml`) |
| `outputs/aula-expositiva/` | HTML Reveal.js da aula (`aula/apresentacao-minicurso.qmd`) | Instrutor; **não** vai ao Netlify nem ao zip |

O template de referência PPTX é **entrada** em `03-relatorio-qmd/template-referencia.pptx`, não nesta pasta.

Render do produto:

```bash
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx
```

Render do deck de aula (explícito; fora do `render:` padrão de `_quarto.yml`):

```bash
quarto render aula/apresentacao-minicurso.qmd --to revealjs --output-dir outputs/aula-expositiva
python scripts/achatar_saidas.py
```

O Quarto aninha a subpasta da fonte no `--output-dir`; `scripts/achatar_saidas.py` achata `03-relatorio-qmd/` (produto) e `aula/` (deck).

Publicação (demo do professor): [`docs/roteiro-netlify.md`](../docs/roteiro-netlify.md). Zip do aluno: `aluno/minicurso-prompt-nao-e-fonte.zip`.
