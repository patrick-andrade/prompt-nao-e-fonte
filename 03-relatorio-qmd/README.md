# Dimensão 3 · Apresentação reprodutível

[`mini-fiscal-monitor.qmd`](mini-fiscal-monitor.qmd) usa chunks **R/knitr** que só leem o CSV executivo dos cinco países. A narrativa de cerca de 11 slides atende à reunião simulada de 20 minutos: pergunta, método, comparação, trajetórias, Brasil, limites e síntese. Nenhum render consulta API nem cola valores fiscais no Markdown. O painel mundial é um artefato separado, com outro derivado da mesma edição.

O mesmo arquivo produz:

```bash
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify/apresentacao
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx
```

O `post-render` em `_quarto.yml` move o Reveal para `outputs/revealjs-netlify/apresentacao/index.html`, sem sobrescrever o portal da raiz. O Reveal usa `embed-resources: true` e está versionado. O PPTX é saída local. O deck de aula em `aula/` é outro produto e fica fora do site.

O [template PPTX](template-referencia.pptx) mantém a saída interna; o [tema executivo Reveal.js](tema-executivo-escuro.scss) usa alto contraste, hierarquia tipográfica e cartões inspirados na força visual do HTML simulado, sem copiar seus números ou inferências. O slide final credita também a referência visual do [OECD Economic Outlook, volume 2026/1](https://www.oecd.org/en/publications/oecd-economic-outlook-volume-2026-issue-1_2d1956f0-en.html). Não há cópia de marca ou fotografia.

Para regenerar o template a partir da referência padrão do Pandoc: `uv run python scripts/gerar_template_pptx.py` na raiz do projeto.

Nesta pasta também estão o [roteiro de IA profissional](roteiro-ia-profissional.md) e o [laboratório de lacunas](lab-lacunas.qmd). O contrato v1.5 está em [`CONTRATO.md`](../CONTRATO.md).
