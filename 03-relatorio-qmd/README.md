# Dimensão 3 — fonte Quarto (PPTX e Reveal.js)

Um único `mini-fiscal-monitor.qmd` (Python) lê **somente** o CSV-contrato e renderiza PPTX (reunião interna) e Reveal.js (navegador / Netlify).

Cláusulas: [`CONTRATO.md`](../CONTRATO.md) v1.2.

## Entradas

- `02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv`
- Configuração em `_quarto.yml` (`lang: pt-BR`; formatos `revealjs` e `pptx`)
- Tema Reveal.js `tema-slate-indigo-sky.scss`
- Template de referência PPTX `template-referencia.pptx` (paleta slate/indigo/sky) — **entrada** nesta pasta, não em `outputs/` (gerador: `scripts/gerar_template_pptx.py`)

## Saídas

- Reveal.js → `outputs/revealjs-netlify/` (único artefato que o Netlify publica; demo do professor; alunos não criam conta; sem Shinylive)
- PPTX → `outputs/pptx/` (reunião de time / direção; **não** se hospeda)

Análise narrativa, lab de lacunas e roteiro de IA profissional estão nesta pasta. O slop **não** vive aqui. O deck de aula do professor vive em `aula/` (não lê o CSV; não entra neste `render:`).

## Também nesta pasta (não vão ao Netlify)

- `lab-lacunas.qmd` — exercício; o aluno completa chunks
- `roteiro-ia-profissional.md` — dois prompts (contraste com o prompt preguiçoso da Dimensão 1)

Render:

```bash
uv run -- quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify
uv run -- quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx
```

O Quarto aninha `03-relatorio-qmd/` dentro do `--output-dir`. O `post-render` em `_quarto.yml` (`python scripts/achatar_saidas.py`) sobe `index.html` e o PPTX para a raiz de cada pasta de saída.

No Windows, mantenha o prefixo `uv run --` nos comandos acima; assim o Quarto recebe automaticamente o Python e o Jupyter resolvidos pelo projeto, sem caminho absoluto gravado na configuração.

Mapa das pastas de saída: [`outputs/README.md`](../outputs/README.md). Publicação: [`docs/roteiro-netlify.md`](../docs/roteiro-netlify.md).

## Validação

`quarto render` gera os dois formatos quando o `.qmd` e o CSV existirem. Números do slide = números do CSV-contrato. Render de aula **não** chama API. Sem número inventado neste README.

A pasta `outputs/revealjs-netlify/` é o publish do site ligado ao git (`netlify.toml`: `publish = "outputs/revealjs-netlify"`).
