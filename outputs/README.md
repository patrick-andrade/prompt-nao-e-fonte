# Saídas do projeto

| Pasta | Artefato | Versionamento/publicação |
| --- | --- | --- |
| `pptx/` | Apresentação interna de 20 minutos | Gerada localmente; fora do Netlify |
| `revealjs-netlify/` | `index.html` do produto | HTML autossuficiente **versionado**; único publish do Netlify |
| `aula-expositiva/` | `index.html` da aula | Gerado localmente; fora do Netlify |

O `.qmd` da Dimensão 3 gera PPTX e Reveal.js a partir do mesmo CSV. O deck da aula é um `.qmd` separado, sem leitura do CSV. Comandos: [`README.md`](../README.md). O `post-render` em `_quarto.yml` usa `scripts/achatar_saidas.py` para colocar cada arquivo na raiz da pasta indicada.
