# Dimensão 2 · Dados do Fiscal Monitor

Há duas bases com finalidades diferentes. [`fm_weo_cache.csv`](data/processed/fm_weo_cache.csv) é o recorte executivo imutável de cinco países: [`baixar_fm.R`](scripts/baixar_fm.R) o reconstrói dos dois JSONs recortados e versionados; [`baixar_fm.py`](scripts/baixar_fm.py) é a alternativa Python. [`fm_global_2026_04.csv`](data/processed/fm_global_2026_04.csv) e [`fm_global_2026_04.json`](data/processed/fm_global_2026_04.json) alimentam apenas o painel: [`gerar_painel.R`](scripts/gerar_painel.R) os reconstrói de três snapshots oficiais completos do DataMapper FM, congelados em `data/raw/`.

```bash
Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline
Rscript 02-dados-fiscal-monitor/scripts/gerar_painel.R --offline
uv run python scripts/validar_contrato.py
```

O CSV executivo preserva a ordem `BRA`, `MEX`, `CHL`, `IND`, `IDN`. O mundial contém 194 economias individuais com ao menos uma observação, inclusive China e Colômbia; agregados regionais ficam fora. Ambos usam os indicadores `GGXWDG_NGDP` e `GGXONLB_NGDP`, anos 2000–2029 e as nove colunas do [`CONTRATO.md`](../CONTRATO.md) v1.5. Ausências são linhas omitidas, nunca zero. O JSON compacto mundial tem números JSON reais, e o validador confere sua equivalência ao CSV, os hashes dos brutos e a sobreposição entre as duas bases. Leia o [dicionário](dicionario-indicadores.md) e as [notas da edição](notas-vintage-2026-04.md) para proveniência e limites.

`Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --consultar-api` tenta consultar a edição **corrente** pela função `imfapi::imf_get`. Ela não escolhe a edição histórica de abril/2026; por isso essa opção não grava o CSV. No teste de 22/09/2026, a consulta falhou ao interpretar um metadado da resposta SDMX (`dataflow$description[[1]]`). A falha é exibida e não altera o cache. A opção equivalente em Python tem a mesma proteção. Para reproduzir a apresentação, use o bruto congelado.

Os pacotes R necessários estão fixados em [`renv.lock`](../renv.lock). Em outra máquina, prepare o ambiente com `Rscript -e 'source("renv/activate.R"); renv::restore(prompt=FALSE)'`. A rota Python usa `uv sync --locked` e `uv run`.
