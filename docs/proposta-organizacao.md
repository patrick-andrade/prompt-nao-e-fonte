# Proposta de organização

Árvore-alvo do minicurso (raiz = `2026/`). Fonte da verdade: [`CONTRATO.md`](../CONTRATO.md) v1.2.

O produto vive **inteiro** nesta pasta. Pastas de infraestrutura não recebem prefixo numérico. A Dimensão 3 tem um único número (`03-relatorio-qmd/`); PPTX e Reveal.js são saídas em `outputs/`, não pastas de produto. O deck de aula vive em `aula/` (instrutor).

```
2026/
  CONTRATO.md
  AGENTS.md
  README.md
  pyproject.toml
  _quarto.yml
  netlify.toml
  .gitignore
  .cursor/rules/minicurso.mdc
  docs/                         ← sem número
    plano-implementacao.md
    arquitetura.md
    proposta-organizacao.md
    roteiro-netlify.md
    checklist-instrutor.md
    plano-aula-2h.md
  scripts/validar_contrato.py
  outputs/                      ← infraestrutura (não é pasta de produto)
    README.md
    pptx/                       ← reunião interna; fora do Netlify
    revealjs-netlify/           ← único artefato publicado
    aula-expositiva/            ← deck de aula; fora do Netlify
  aluno/                        ← README aponta o clone; zip opcional
  aula/                         ← apresentação do professor; HTML gerado fora do Netlify
    apresentacao-minicurso.qmd
    imagens/
  01-demanda-simulada/
  02-dados-fiscal-monitor/
  03-relatorio-qmd/             ← único número da Dimensão 3
```

## Por que 3 números, não 5

Cada dimensão de produto tem README, entradas, saídas e validação. `04-pptx/` e `05-revealjs-netlify/` como pastas numeradas misturavam **fonte** e **artefato**. A fonte fica em `03-relatorio-qmd/`; os renders vão para `outputs/pptx/` e `outputs/revealjs-netlify/`.

O CSV-contrato **não muda de caminho:** `02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv`. Países, indicadores e vintage permanecem.

## Regras de pasta

- **Netlify** = somente Reveal.js (`publish = "outputs/revealjs-netlify"`). PPTX não se hospeda. `outputs/aula-expositiva/` também **não** se publica.
- Template PPTX de referência é **entrada** em `03-relatorio-qmd/`, não em `outputs/`.
- `aluno/` aponta o clone público; zip opcional (`minicurso-prompt-nao-e-fonte.zip`, sem `instrutor/autopsia.md` e sem `aula/`).
- Cue de arquivo no deck = caminho relativo no repositório. Hiperlink só para URL público.
- Onda 0 (esqueleto), Onda 1 (slop + CSV + `.qmd` que lê o cache) e Onda 2 (análise, template, Netlify) estão feitas (produto). Onda 3 = inspeção humana; ver [`plano-implementacao.md`](plano-implementacao.md).

Sem números fiscais neste arquivo. Sem China no produto.
