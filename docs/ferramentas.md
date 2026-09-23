# Ferramentas e extensões

O projeto separa **fonte**, **código**, **contrato** e **apresentação**. O [`CONTRATO.md`](../CONTRATO.md) v1.3 fixa países, indicadores, vintage e schema; [`AGENTS.md`](../AGENTS.md) orienta o Codex, e `.cursor/rules/minicurso.mdc` mantém compatibilidade com Cursor. A extensão `.mdc` não registra o contrato para o Codex.

| Ferramenta | Quem usa | Função |
| --- | --- | --- |
| Navegador / GitHub | Todos | Ler briefing, código, CSV e o HTML publicado |
| VS Code ou editor | Alunos e professor | Procurar país, ano, indicador e vintage |
| R + `jsonlite` + `imfapi` | Professor | Reconstruir offline e demonstrar consulta corrente |
| Quarto + R/knitr + `ggplot2` | Professor | Gerar PPTX e Reveal.js do mesmo `.qmd` |
| Python | Alunos | Validar contrato com biblioteca padrão; rota alternativa de dados |
| Netlify | Professor | Servir o `index.html` versionado sem render remoto |

| Extensão | O que é | Exemplo |
| --- | --- | --- |
| `.md` / `.mdc` | Texto e instruções; `.mdc` é regra do Cursor | `CONTRATO.md`, `AGENTS.md`, `minicurso.mdc` |
| `.R` / `.py` | Código executável | `baixar_fm.R`, `baixar_fm.py`, `validar_contrato.py` |
| `.json` / `.csv` | Bruto recortado / tabela canônica | `data/raw/`, `fm_weo_cache.csv` |
| `.qmd` | Markdown com chunks R | `mini-fiscal-monitor.qmd` |
| `.scss` / `.pptx` | Tema Reveal.js / template ou saída PowerPoint | `tema-relatorio-azul.scss`, `template-referencia.pptx` |
| `.html` | Apresentação no navegador | slop e `outputs/revealjs-netlify/index.html` |
| `.lock` | Versões de pacotes | `renv.lock`, `uv.lock` |

O `.qmd` do produto **só lê o CSV**. O HTML do slop não lê o CSV. O HTML público é uma saída pronta, não uma consulta viva. O PDF do BCB sustenta a autópsia da simulação; a comparação final usa o cache da edição FMI abril/2026.

## Participação sem instalação em sala

1. Navegador: ler o CSV como tabela no GitHub e ver o produto no Netlify.
2. Editor + clone: localizar a linha `BRA` · 2025 · `GGXONLB_NGDP`.
3. Python do laboratório: `python scripts/validar_contrato.py` (biblioteca padrão).

O professor prepara R, pacotes do [`renv.lock`](../renv.lock) e Quarto antes da aula. Para casa, o Python do `lab-lacunas.qmd` usa `pyproject.toml` + `uv.lock` com `uv sync --locked`. [`requisitos-laboratorio.md`](requisitos-laboratorio.md) detalha máquinas e rede.
