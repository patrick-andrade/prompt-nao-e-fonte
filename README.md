# Prompt não é fonte

Minicurso da Semana da Economia: análise de dados e IA em economia aplicada. Graduação, laboratório, 2 horas.

A fonte da verdade do produto é [`CONTRATO.md`](CONTRATO.md) (v1.0). Não inventar país, coluna, indicador, vintage, formato nem número fiscal.

## Três dimensões

| Dimensão | Pastas | O que entrega |
| --- | --- | --- |
| 1 — Demanda simulada | `01-demanda-simulada/` | Briefing, prompt do junior, HTML slop; autópsia só do instrutor |
| 2 — Scripts Python | `02-dados-fiscal-monitor/` | Download FM/WEO abril/2026 e CSV-contrato |
| 3 — Qmd → PPTX / Reveal.js | `03-relatorio-qmd/`, `04-pptx/`, `05-revealjs-netlify/` | Relatório que lê o CSV; PPTX interno; site Reveal.js no Netlify |

Mapa pastas ↔ dimensões: [`docs/arquitetura.md`](docs/arquitetura.md).

Países (ordem canônica, **sem China**): `BRA`, `MEX`, `CHL`, `IND`, `IDN`.

## Como validar

Na raiz do repositório (Python 3.11+; não exige `uv sync` nesta onda):

```bash
python scripts/validar_contrato.py
```

- **Onda 0:** CSV ainda não existe. O script deve sair com código 0 e status de esqueleto OK / Dimensão 2 pendente.
- **A partir da Dimensão 2:** o mesmo comando valida schema, países, indicadores e vintage do CSV.

Render Quarto e deploy Netlify entram nas ondas seguintes. Não há números fiscais neste README: eles só existem no CSV-contrato depois da Dimensão 2.

## Ferramentas

- Python: `pyproject.toml` + `uv`
- Quarto: `_quarto.yml` (Reveal.js + PPTX a partir de `03-relatorio-qmd/`)
- Netlify: `netlify.toml` publica **somente** `05-revealjs-netlify/`
