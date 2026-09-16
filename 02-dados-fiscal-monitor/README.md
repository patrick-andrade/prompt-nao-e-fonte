# Dimensão 2 — Análise real em Python

Scripts que baixam, empilham, validam e gravam o CSV-contrato (Fiscal Monitor / WEO abril/2026). Não é laboratório do aluno: é o motor que torna a demanda uma **rotina**.

Cláusulas: [`CONTRATO.md`](../CONTRATO.md) v1.2.

## Entradas

- IMF DataMapper, dataset FM, vintage abril/2026 (`FM-2026-04`).
- Título da edição (referência, não número): *Fiscal Policy under Pressure: High Debt, Rising Risks*.
- Notas: [`notas-vintage-2026-04.md`](notas-vintage-2026-04.md), [`dicionario-indicadores.md`](dicionario-indicadores.md).

## Saídas

- `data/raw/` — JSON recortado (cinco iso3; dump mundial não entra no git).
- `data/processed/fm_weo_cache.csv` — CSV canônico.
- Colunas: `iso3`, `country`, `year`, `indicator_code`, `indicator_name`, `value`, `unit`, `vintage`, `source`.
- Países (ordem canônica, sem China): `BRA`, `MEX`, `CHL`, `IND`, `IDN`.
- Indicadores: `GGXWDG_NGDP`, `GGXONLB_NGDP`. Anos: 2000–2029.

## Como gerar

```bash
uv run python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline
uv run python scripts/validar_contrato.py
```

`--offline` reconstrói o CSV a partir de `data/raw/` (caminho da aula). Sem `--offline` tenta o DataMapper; se a rede devolver 403, cai no bruto em disco.

## Validação

Na Onda 0 o CSV ainda não existia. A partir desta onda o mesmo script exige schema, países, indicadores, vintage e ausência de NA crítico nos anos-chave.

Este README não contém números fiscais.
