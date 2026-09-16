# Arquitetura: 3 dimensões ↔ 3 pastas numeradas

O produto tem **três dimensões**. A árvore física tem **três pastas numeradas de produto** mais infraestrutura sem número (`docs/`, `scripts/`, `outputs/`, `aluno/`, `aula/`). Fonte da verdade: [`CONTRATO.md`](../CONTRATO.md) v1.2.

```
Dimensão 1  →  01-demanda-simulada/
Dimensão 2  →  02-dados-fiscal-monitor/     →  fm_weo_cache.csv
Dimensão 3  →  03-relatorio-qmd/            (único número da Dimensão 3; fonte .qmd)
                 ├─ PPTX     →  outputs/pptx/              (reunião; não vai ao Netlify)
                 └─ Reveal.js →  outputs/revealjs-netlify/  (único publish do Netlify)

Aula (instrutor) →  aula/apresentacao-minicurso.qmd
                 └─ Reveal.js →  outputs/aula-expositiva/   (fora do Netlify)
```

O template de referência PPTX é **entrada** em `03-relatorio-qmd/`, não em `outputs/`.

Fluxo contratual: demanda e slop (Dim. 1) motivam a rotina em Python (Dim. 2), que grava o CSV-contrato; o `.qmd` (Dim. 3) só lê esse CSV e gera PPTX e Reveal.js. O Netlify publica **somente** o Reveal.js do produto. O deck de aula **não** lê o CSV: aponta caminhos relativos (`Abrir agora: …`) e, depois do deploy, o URL público. Pacote da turma: clone do GitHub.

A Diretoria de Pesquisa Aplicada é a demanda realista de estágio / trainee / júnior, não um tom a suavizar no briefing.

Não há números fiscais neste mapa. Países canônicos: `BRA`, `MEX`, `CHL`, `IND`, `IDN` (sem China).

Plano das ondas: [`plano-implementacao.md`](plano-implementacao.md). Organização das pastas: [`proposta-organizacao.md`](proposta-organizacao.md). Inspeção humana: [`checklist-instrutor.md`](checklist-instrutor.md).
