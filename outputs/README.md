# Saídas geradas

Sem números fiscais aqui.

| Pasta | Artefato | Destino |
| --- | --- | --- |
| `outputs/pptx/` | PPTX da reunião interna (Dimensão 3) | **Não** vai ao Netlify |
| `outputs/revealjs-netlify/` | HTML Reveal.js do briefing (`index.html`) | Único publish do Netlify (`netlify.toml`) |
| `outputs/aula-expositiva/` | HTML Reveal.js da aula (`aula/apresentacao-minicurso.qmd`) | Instrutor; **não** vai ao Netlify |

O template de referência PPTX é **entrada** em `03-relatorio-qmd/template-referencia.pptx`, não nesta pasta.

Render do produto:

```bash
uv run -- quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify
uv run -- quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx
```

Render do deck de aula (explícito; fora do `render:` padrão de `_quarto.yml`):

```bash
uv run -- quarto render aula/apresentacao-minicurso.qmd --profile aula --to revealjs
```

O Quarto aninha a subpasta da fonte no `--output-dir`; `scripts/achatar_saidas.py` achata `03-relatorio-qmd/` (produto) e `aula/` (deck).

Publicação (demo do professor): [`docs/roteiro-netlify.md`](../docs/roteiro-netlify.md). Pacote da turma: clone [https://github.com/patrick-andrade/prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte). Zip opcional: `aluno/minicurso-prompt-nao-e-fonte.zip`.
