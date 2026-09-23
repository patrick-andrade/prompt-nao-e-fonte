# Arquitetura do minicurso

O [`CONTRATO.md`](../CONTRATO.md) v1.3 fixa três dimensões e seus limites.

```text
01-demanda-simulada/          e-mail → prompt → HTML simulado → autópsia
02-dados-fiscal-monitor/      JSON congelado → baixar_fm.R → CSV-contrato
                            └─ baixar_fm.py: rota alternativa
03-relatorio-qmd/             CSV-contrato → mini-fiscal-monitor.qmd (R)
                            ├─ outputs/pptx/ (reunião)
                            └─ outputs/revealjs-netlify/index.html (site)
aula/apresentacao-minicurso.qmd → outputs/aula-expositiva/ (professor)
```

A Dimensão 1 não lê o CSV. A Dimensão 2 é a única que grava o CSV e a única que pode consultar a API. A consulta corrente fica separada do bruto de abril/2026. A Dimensão 3 só lê o CSV para gerar as duas apresentações. O deck da aula não lê o CSV: ele orienta a abertura dos arquivos na sequência didática. O Netlify serve o HTML do produto já versionado, sem render remoto.

As pastas `docs/`, `scripts/`, `outputs/`, `aluno/` e `aula/` são infraestrutura, sem prefixo numérico. [`proposta-organizacao.md`](proposta-organizacao.md) mostra a árvore; [`plano-implementacao.md`](plano-implementacao.md) registra a revisão atual.
