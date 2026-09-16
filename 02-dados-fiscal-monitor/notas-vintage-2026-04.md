# Notas de vintage — abril/2026

Sem séries numéricas neste arquivo. Números só no CSV-contrato.

## Identificação

| Campo | Valor |
| --- | --- |
| Edição | Fiscal Monitor, abril/2026 |
| Título | *Fiscal Policy under Pressure: High Debt, Rising Risks* |
| Corte da informação (MSA) | dados disponíveis até 1º de abril de 2026 |
| Coluna `vintage` no CSV | `FM-2026-04` |
| Coluna `source` no CSV | `IMF Fiscal Monitor April 2026 (DataMapper)` |
| Base das projeções | mesma base do WEO de abril/2026 (o contrato aceita `WEO-2026-04` se a fonte for o WEO) |

Página da edição: [Fiscal Monitor, April 2026](https://www.imf.org/en/publications/fm/issues/2026/04/15/fiscal-monitor-april-2026).

## Como o cache foi montado

1. IMF DataMapper, dataset **FM** (não o recorte WEO do DataMapper: lá não há `GGXONLB_NGDP`).
2. Recorte: cinco iso3 canônicos, anos 2000–2029, dois indicadores.
3. China e demais países do dump mundial **não** entram no JSON bruto versionado nem no CSV.
4. Uma lacuna conhecida: o DataMapper FM não devolve o primário do Brasil em **2000**. A linha não é inventada; simplesmente não existe no cache. Anos-chave 2023–2026 estão completos.

## Rede e aula

Algumas redes devolvem HTTP 403 no DataMapper para clientes script. Por isso o bruto recortado vive em `data/raw/` e a aula reroda com:

```bash
uv run python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline
```

Download ao vivo (quando a API responder):

```bash
uv run python 02-dados-fiscal-monitor/scripts/baixar_fm.py
```

Render de aula **não** chama a API: o `.qmd` lê o CSV.
