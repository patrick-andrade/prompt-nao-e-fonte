# Dimensão 2 — Análise real em Python

Scripts que baixam, empilham, validam e gravam o CSV-contrato (Fiscal Monitor / WEO abril/2026). Não é laboratório do aluno: é o motor que torna a demanda uma **rotina**.

Cláusulas: [`CONTRATO.md`](../CONTRATO.md) v1.0.

## Entradas

- API ou arquivos oficiais FM/WEO, vintage abril/2026 (`FM-2026-04` / `WEO-2026-04`).
- Título da edição (referência, não número): *Fiscal Policy under Pressure: High Debt, Rising Risks*.

## Saídas

- `data/raw/` — dumps brutos (PDFs grandes não entram no git).
- `data/processed/fm_weo_cache.csv` — CSV canônico.
- Colunas: `iso3`, `country`, `year`, `indicator_code`, `indicator_name`, `value`, `unit`, `vintage`, `source`.
- Países (ordem canônica, sem China): `BRA`, `MEX`, `CHL`, `IND`, `IDN`.
- Indicadores: `GGXWDG_NGDP`, `GGXONLB_NGDP`. Anos: 2000–2029.

## Validação

```bash
python scripts/validar_contrato.py
```

Na Onda 0 o CSV ainda não existe: o validador deve reportar esqueleto OK e Dimensão 2 pendente. Com o CSV, o mesmo script exige schema, países, indicadores, vintage e ausência de NA crítico nos anos-chave.

Este README não contém números fiscais. Download e cache: Onda 1.
