# Saídas do projeto

| Pasta | Artefato | Versionamento/publicação |
| --- | --- | --- |
| `pptx/` | Apresentação interna de 20 minutos | Gerada localmente; fora do Netlify |
| `revealjs-netlify/` | Portal `index.html`, slides em `apresentacao/` e painel em `painel/` | Três HTMLs estáticos e versionados; diretório publicado no Netlify |
| `aula-expositiva/` | `index.html` da aula | Gerado localmente; fora do Netlify |

O `.qmd` da Dimensão 3 gera PPTX e Reveal.js a partir do CSV executivo. O painel usa um derivado mundial separado, preparado em R. O deck da aula é um `.qmd` separado, sem leitura de CSV. Comandos: [`README.md`](../README.md). O `post-render` em `_quarto.yml` coloca os slides na rota `apresentacao/`, sem sobrescrever o portal.
