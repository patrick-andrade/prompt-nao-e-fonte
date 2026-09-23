# Organização do repositório

Árvore em uso na raiz `2026/`, alinhada ao [`CONTRATO.md`](../CONTRATO.md) v1.4:

```text
AGENTS.md                         instruções concisas para Codex
CONTRATO.md                       fonte da verdade do projeto
.cursor/rules/minicurso.mdc       compatibilidade curta para Cursor
renv.lock                         versões dos pacotes R
pyproject.toml + uv.lock           rota Python
01-demanda-simulada/              pedido e slop
02-dados-fiscal-monitor/          bruto, scripts e CSV-contrato
03-relatorio-qmd/                 fonte única do produto e templates
site/                            fontes do portal e do painel estático
aula/                             roteiro do professor
docs/                             guias e checklists
scripts/                          validador, template, pós-render e zip
outputs/pptx/                     saída local
outputs/revealjs-netlify/          portal, apresentação e painel versionados
outputs/aula-expositiva/           saída local fora do site
aluno/                            guia e zip opcional
```

PPTX e Reveal.js são **saídas** da Dimensão 3, portanto não recebem novas pastas numeradas. O painel é outro produto web, alimentado pelo derivado mundial da Dimensão 2 e publicado no mesmo diretório Netlify. `template-referencia.pptx` é **entrada** dentro de `03-relatorio-qmd/`. O zip opcional omite `aula/` e a autópsia; o clone público é o material principal.
