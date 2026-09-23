# Ferramentas e extensões

O projeto separa **fonte**, **código**, **contrato** e **apresentação**. O [`CONTRATO.md`](../CONTRATO.md) v1.4 distingue o recorte executivo do universo mundial do painel, mantendo indicadores, vintage e schema; [`AGENTS.md`](../AGENTS.md) orienta o Codex, e `.cursor/rules/minicurso.mdc` mantém compatibilidade com Cursor. A extensão `.mdc` não registra o contrato para o Codex.

| Ferramenta | Quem usa | Função |
| --- | --- | --- |
| Navegador / GitHub | Todos | Ler briefing, código, CSV e o HTML publicado |
| VS Code ou editor | Alunos e professor | Procurar país, ano, indicador e vintage |
| R + `jsonlite` + `imfapi` | Professor | Reconstruir offline o CSV executivo e demonstrar consulta corrente |
| R + bruto FMI congelado | Professor | Preparar o derivado mundial do painel |
| Quarto + R/knitr + `ggplot2` | Professor | Gerar PPTX e Reveal.js do mesmo `.qmd` |
| Python | Alunos | Validar contrato com biblioteca padrão; rota alternativa de dados |
| Netlify | Professor | Servir portal, apresentação e painel versionados sem render remoto |

| Extensão | O que é | Exemplo |
| --- | --- | --- |
| `.md` / `.mdc` | Texto e instruções; `.mdc` é regra do Cursor | `CONTRATO.md`, `AGENTS.md`, `minicurso.mdc` |
| `.R` / `.py` | Código executável | `baixar_fm.R`, `baixar_fm.py`, `validar_contrato.py` |
| `.json` / `.csv` | Brutos congelados / tabelas derivadas | `data/raw/`, `fm_weo_cache.csv`, derivado mundial |
| `.qmd` | Markdown com chunks R | `mini-fiscal-monitor.qmd` |
| `.scss` / `.pptx` | Tema Reveal.js / template ou saída PowerPoint | `tema-executivo-escuro.scss`, `template-referencia.pptx` |
| `.html` | Apresentação e páginas interativas | slop, portal, Reveal.js e painel |
| `.lock` | Versões de pacotes | `renv.lock`, `uv.lock` |

O `.qmd` do produto **só lê o CSV executivo**. O HTML do slop não lê CSV. O painel mundial usa outro derivado preparado em R da edição FMI abril/2026. As páginas públicas são saídas prontas, não consultas vivas. O PDF do BCB sustenta a autópsia da simulação; a comparação executiva usa o cache dos cinco países.

## Participação sem instalação em sala

1. Navegador: ler o CSV como tabela no GitHub e ver portal, slides e painel no Netlify.
2. Editor + clone: localizar a linha `BRA` · 2025 · `GGXONLB_NGDP`.
3. Python do laboratório: `python scripts/validar_contrato.py` (biblioteca padrão).

O professor prepara R, pacotes do [`renv.lock`](../renv.lock) e Quarto antes da aula. Para casa, o Python do `lab-lacunas.qmd` usa `pyproject.toml` + `uv.lock` com `uv sync --locked`. [`requisitos-laboratorio.md`](requisitos-laboratorio.md) detalha máquinas e rede.
