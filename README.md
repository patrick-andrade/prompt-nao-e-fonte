# Prompt não é fonte

Minicurso da Semana da Economia: análise de dados e IA em economia aplicada. Graduação, laboratório, 2 horas (núcleo 80 min + gordura até 40 min). Raiz do produto = esta pasta (`2026/`).

A fonte da verdade do produto é [`CONTRATO.md`](CONTRATO.md) (v1.2). Não inventar país, coluna, indicador, vintage, formato nem número fiscal.

## Três dimensões (3 pastas numeradas)

| Dimensão | Pasta | O que entrega |
| --- | --- | --- |
| 1 — Demanda simulada | `01-demanda-simulada/` | Briefing, prompt do junior, HTML slop; autópsia só do instrutor |
| 2 — Scripts Python | `02-dados-fiscal-monitor/` | Download FM/WEO abril/2026 e CSV-contrato |
| 3 — Qmd → PPTX / Reveal.js | `03-relatorio-qmd/` | Relatório que lê o CSV; gera PPTX e Reveal.js |

Infraestrutura (sem número): `docs/`, `scripts/`, `outputs/`, `aluno/`, `aula/`.

Saídas da Dimensão 3:

- PPTX → `outputs/pptx/` (reunião interna; **não** vai ao Netlify)
- Reveal.js → `outputs/revealjs-netlify/` (único artefato publicado)
- Template PPTX de referência é **entrada** em `03-relatorio-qmd/`

Deck de aula (instrutor; **não** lê o CSV; fora do zip e do Netlify):

- Fonte: `aula/apresentacao-minicurso.qmd`
- Saída: `outputs/aula-expositiva/`

Mapa pastas ↔ dimensões: [`docs/arquitetura.md`](docs/arquitetura.md). Plano das ondas: [`docs/plano-implementacao.md`](docs/plano-implementacao.md). Checklist de inspeção humana: [`docs/checklist-instrutor.md`](docs/checklist-instrutor.md).

Países (ordem canônica, **sem China**): `BRA`, `MEX`, `CHL`, `IND`, `IDN`.

## Como validar

Na raiz deste repositório (`2026/`; Python 3.11+; `uv sync` para o render Quarto):

```bash
python scripts/validar_contrato.py
```

- **Onda 0 (histórica):** CSV ausente → esqueleto OK / Dimensão 2 pendente, exit 0.
- **A partir da Onda 1:** o mesmo comando valida schema, países, indicadores e vintage do CSV.

Render do briefing (Reveal.js publicado; PPTX só na pasta de saída):

```bash
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx
```

Render do deck de aula (explícito; **não** entra no `render:` padrão de `_quarto.yml`):

```bash
quarto render aula/apresentacao-minicurso.qmd --to revealjs --output-dir outputs/aula-expositiva
python scripts/achatar_saidas.py
```

Não há números fiscais neste README: eles só existem no CSV-contrato.

## Ferramentas

- Python: `pyproject.toml` + `uv`
- Quarto: `_quarto.yml` (Reveal.js + PPTX a partir de `03-relatorio-qmd/`; o deck de aula é CLI à parte)
- Netlify: `netlify.toml` publica **somente** `outputs/revealjs-netlify/`
