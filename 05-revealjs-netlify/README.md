# Dimensão 3 — saída Reveal.js e Netlify

Site estático da apresentação no navegador. **No Netlify entra só o Reveal.js.** PPTX não se hospeda. Demo do professor; alunos não criam conta. Sem Shinylive no contrato v1.0.

Cláusulas: [`CONTRATO.md`](../CONTRATO.md) v1.0.

## Entradas

- HTML Reveal.js gerado por `quarto render` a partir de `03-relatorio-qmd/mini-fiscal-monitor.qmd`
- `netlify.toml` na raiz (`publish = "05-revealjs-netlify"`)

## Saídas

- Pasta publicável com o deck HTML

## Validação

A pasta é dropável no Netlify. Números do slide = números do CSV. Conteúdo do site: Onda 2. Sem número inventado neste README.
