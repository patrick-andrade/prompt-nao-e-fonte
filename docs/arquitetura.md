# Arquitetura: 3 dimensões ↔ 5 pastas

O produto tem **três dimensões**. A árvore física tem **cinco pastas numeradas** mais `docs/`, `scripts/`, `outputs/` e `aluno/`. Fonte da verdade: [`CONTRATO.md`](../CONTRATO.md) v1.0.

```
Dimensão 1  →  01-demanda-simulada/
Dimensão 2  →  02-dados-fiscal-monitor/
Dimensão 3  →  03-relatorio-qmd/   (fonte .qmd)
            →  04-pptx/            (template + artefato PPTX)
            →  05-revealjs-netlify/ (HTML Reveal.js + deploy)
```

Fluxo contratual: demanda e slop (Dim. 1) motivam a rotina em Python (Dim. 2), que grava o CSV-contrato; o `.qmd` (Dim. 3) só lê esse CSV e gera PPTX e Reveal.js. O Netlify publica **somente** o Reveal.js.

Não há números fiscais neste mapa. Países canônicos: `BRA`, `MEX`, `CHL`, `IND`, `IDN` (sem China).
