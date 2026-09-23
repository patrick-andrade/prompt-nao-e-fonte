# Dimensão 3 · Apresentação reprodutível

[`mini-fiscal-monitor.qmd`](mini-fiscal-monitor.qmd) usa chunks **R/knitr** que só leem o CSV contratado. A narrativa de cerca de 11 slides atende à reunião simulada de 20 minutos: pergunta, método, comparação, trajetórias, Brasil, limites e síntese. Nenhum render consulta API nem cola valores fiscais no Markdown.

O mesmo arquivo produz:

```bash
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx
```

O `post-render` em `_quarto.yml` move os artefatos para a raiz das pastas de saída. `outputs/revealjs-netlify/index.html` usa `embed-resources: true`, é autossuficiente, está versionado e é o único conteúdo publicado no Netlify. O PPTX é saída local. O deck de aula em `aula/` é outro produto e fica fora do site.

O [template PPTX](template-referencia.pptx) e o [tema Reveal.js](tema-relatorio-azul.scss) adaptam capa azul-marinho, páginas claras, tipografia forte e destaques azuis inspirados no [OECD Economic Outlook, volume 2026/1](https://www.oecd.org/en/publications/oecd-economic-outlook-volume-2026-issue-1_2d1956f0-en.html). O slide final credita a referência visual. Não há cópia de marca ou fotografia.

Para regenerar o template a partir da referência padrão do Pandoc: `uv run python scripts/gerar_template_pptx.py` na raiz do projeto.

Nesta pasta também estão o [roteiro de IA profissional](roteiro-ia-profissional.md) e o [laboratório de lacunas](lab-lacunas.qmd). O contrato v1.3 está em [`CONTRATO.md`](../CONTRATO.md).
