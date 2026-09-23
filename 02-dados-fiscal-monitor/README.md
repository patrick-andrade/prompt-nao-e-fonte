# Dimensão 2 · Dados do Fiscal Monitor

O script [`baixar_fm.R`](scripts/baixar_fm.R) é o caminho principal da aula. Sem argumento, usa `--offline`: lê os dois JSONs recortados e versionados em `data/raw/`, verifica metadados de abril/2026 e reconstrói [`fm_weo_cache.csv`](data/processed/fm_weo_cache.csv). O script [`baixar_fm.py`](scripts/baixar_fm.py) oferece a mesma reconstrução como alternativa.

```bash
Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline
python scripts/validar_contrato.py
```

O CSV preserva a ordem `BRA`, `MEX`, `CHL`, `IND`, `IDN`; os indicadores `GGXWDG_NGDP` e `GGXONLB_NGDP`; os anos 2000–2029; e as nove colunas definidas em [`CONTRATO.md`](../CONTRATO.md) v1.3. O validador confere schema, vintage, valores e chaves únicas. Leia também o [dicionário](dicionario-indicadores.md) e as [notas da edição](notas-vintage-2026-04.md).

`Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --consultar-api` tenta consultar a edição **corrente** pela função `imfapi::imf_get`. Ela não escolhe a edição histórica de abril/2026; por isso essa opção não grava o CSV. No teste de 22/09/2026, a consulta falhou ao interpretar um metadado da resposta SDMX (`dataflow$description[[1]]`). A falha é exibida e não altera o cache. A opção equivalente em Python tem a mesma proteção. Para reproduzir a apresentação, use o bruto congelado.

Os pacotes R necessários estão fixados em [`renv.lock`](../renv.lock). Em outra máquina, prepare o ambiente com `Rscript -e 'source("renv/activate.R"); renv::restore(prompt=FALSE)'`. A rota Python usa `uv sync --locked` e `uv run`.
