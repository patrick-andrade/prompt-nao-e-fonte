# Regras para agentes

Honrar [`CONTRATO.md`](CONTRATO.md) **v1.0**. Não inventar país, coluna, indicador, vintage, formato nem número.

## Obrigatório

- UTF-8 e acentuação em português.
- Sem tokens, chaves, senhas ou credenciais em arquivos, configs ou relatórios.
- Python do projeto: `pyproject.toml` + `uv`. Não instalar dependências globalmente.
- Países na ordem canônica: `BRA`, `MEX`, `CHL`, `IND`, `IDN`.
- **Sem China** (`CHN` fora). México é LatAm, não América do Sul, no material.
- Não inventar número fiscal do Brasil nem dos outros países. Só cache, API ou PDF extraído com `doc_extract` (recorte, não o Fiscal Monitor inteiro no contexto).

## Dimensões

- **Slop (Dimensão 1):** não lê `fm_weo_cache.csv`. HTML ilustrativo e impreciso de propósito.
- **Scripts (Dimensão 2):** único lugar que baixa FM/WEO abril/2026 e grava o CSV-contrato.
- **Quarto / PPTX / Reveal.js (Dimensão 3):** só leem o CSV-contrato. Sem número inventado; render de aula não chama API.
- **Netlify:** somente o artefato Reveal.js. PPTX não se hospeda. Sem Shinylive neste contrato.

## Mudança de contrato

País, coluna ou formato novos = bump para v1.1 em `CONTRATO.md` e em `scripts/validar_contrato.py`. Não ajustar no feeling.

## Onda atual

Onda 0 = esqueleto. Dimensão 1 (slop), Dimensão 2 (download) e análise Quarto completa **não** se implementam até a onda correspondente.
