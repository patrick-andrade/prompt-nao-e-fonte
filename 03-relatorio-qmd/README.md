# Dimensão 3 — fonte Quarto

Um único `mini-fiscal-monitor.qmd` (Python) lê **somente** o CSV-contrato e renderiza PPTX (reunião) e Reveal.js (navegador).

Cláusulas: [`CONTRATO.md`](../CONTRATO.md) v1.0.

## Entradas

- `02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv`
- Configuração em `_quarto.yml` (`lang: pt-BR`; formatos `revealjs` e `pptx`)

## Saídas

- Reveal.js → pasta `05-revealjs-netlify/` (o que o Netlify publica)
- PPTX → `04-pptx/` / `outputs/` (não se hospeda)

## Validação

`quarto render` gera os dois formatos quando o `.qmd` e o CSV existirem. Números do slide = números do CSV. Render de aula **não** chama API. Sem número inventado neste README nem no stub.

Análise completa, `lab-lacunas.qmd` e roteiro de IA: ondas 1–2.
