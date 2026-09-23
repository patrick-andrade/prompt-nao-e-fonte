# Arquitetura do minicurso

O [`CONTRATO.md`](../CONTRATO.md) v1.4 fixa três dimensões e distingue o recorte executivo do universo do painel.

```text
01-demanda-simulada/          e-mail → prompt → HTML simulado → autópsia
02-dados-fiscal-monitor/      JSON recortado → baixar_fm.R → CSV executivo
                            ├─ baixar_fm.py: rota alternativa
                            └─ JSON DataMapper mundial congelado → R → derivado mundial
03-relatorio-qmd/             CSV executivo → mini-fiscal-monitor.qmd (R)
                            ├─ outputs/pptx/ (reunião)
                            └─ outputs/revealjs-netlify/apresentacao/index.html
site/                       derivado mundial → HTML do painel
                            └─ outputs/revealjs-netlify/painel/index.html
outputs/revealjs-netlify/index.html → portal das duas rotas
aula/apresentacao-minicurso.qmd → outputs/aula-expositiva/ (professor)
```

A Dimensão 1 não lê dados contratados. A Dimensão 2 grava os dois derivados e é a única que pode consultar a API; a consulta corrente não troca a vintage congelada. O CSV executivo continua com `BRA`, `MEX`, `CHL`, `IND`, `IDN`; o derivado mundial contém economias individuais da edição, inclusive `CHN` e `COL`, sem agregados. A Dimensão 3 só lê o CSV executivo para gerar as duas apresentações. O painel recebe o derivado mundial preparado em R e interage no navegador, sem API ou servidor R. O deck da aula não lê CSV: ele orienta a abertura dos arquivos na sequência didática. O Netlify serve o portal e os dois HTMLs já versionados, sem render remoto.

As pastas `docs/`, `scripts/`, `outputs/`, `aluno/` e `aula/` são infraestrutura, sem prefixo numérico. [`proposta-organizacao.md`](proposta-organizacao.md) mostra a árvore; [`plano-implementacao.md`](plano-implementacao.md) registra a revisão atual.
