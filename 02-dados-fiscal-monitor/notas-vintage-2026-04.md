# Notas de vintage — abril/2026

Sem séries numéricas neste arquivo. Números ficam nos CSVs processados.

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

## Como o cache executivo foi montado

1. IMF DataMapper, dataset **FM** (não o recorte WEO do DataMapper: lá não há `GGXONLB_NGDP`).
2. Recorte: cinco iso3 canônicos, anos 2000–2029, dois indicadores.
3. China e demais países do dump mundial **não** entram nos JSONs recortados nem no CSV executivo.
4. Uma lacuna conhecida: o DataMapper FM não devolve o primário do Brasil em **2000**. A linha não é inventada; simplesmente não existe no cache. Anos-chave 2023–2026 estão completos.

## Fonte congelada do painel mundial

Em 23/09/2026, a [página oficial do DataMapper FM](https://www.imf.org/external/datamapper/datasets/FM) identificava o conjunto como **Fiscal Monitor (April 2026)**. O [relatório](https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/text.pdf), apêndice metodológico p. 43 e Tabela A p. 51, remete explicitamente a essa página para as economias além das tabelas impressas. Foram congelados **uma única vez** os seguintes retornos oficiais da API; os hashes impedem troca silenciosa por edição corrente:

| Bruto versionado em `data/raw/` | URL oficial | SHA-256 |
| --- | --- | --- |
| `datamapper_full_G_XWDG_G01_GDP_PT.json` | [Dívida bruta](https://www.imf.org/external/datamapper/api/v1/G_XWDG_G01_GDP_PT) | `F96749538A5CFB8D31141438865A21D7BAB9B0DE0466FDB2DBEB37650C59E500` |
| `datamapper_full_GGXONLB_G01_GDP_PT.json` | [Saldo primário](https://www.imf.org/external/datamapper/api/v1/GGXONLB_G01_GDP_PT) | `22B35875344767733C4BA6F46632A417858EC22771F167E9860EDF83EB7C3D06` |
| `datamapper_countries_2026-04.json` | [Catálogo de economias](https://www.imf.org/external/datamapper/api/v1/countries) | `F74B5BC5EEB69F3DA3EDCD19CAAAB95D94F02A476C1382590A77024164D3B836` |

`gerar_painel.R --offline` faz a interseção dos códigos das séries com `/countries`. Códigos encontrados só nas séries, como `ADVEC` e `EURO`, são agregados e ficam de fora. As 194 economias com observações em 2000–2029 geram 11.118 linhas para os dois indicadores; `CHN` e `COL` estão presentes. O arquivo não cria linhas para ausências e não imputa zero. O CSV mundial preserva as nove colunas do executivo; o JSON entrega `vintage`, `source`, `unit` e linhas numéricas compactas para o painel estático.

As 299 linhas do CSV executivo coincidiam com o snapshot mundial na precisão de seis casas decimais em 23/09/2026, sem chaves extras nos cinco países. Os nomes no executivo são em português; no mundial vêm do catálogo oficial em inglês. O validador reexecuta essa conciliação e compara cada linha mundial ao bruto congelado.

## Referências locais fora do Git

O [XLSX oficial chamado `fmdatabase.xlsx`](https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/data/fmdatabase.xlsx) foi baixado como `data/raw/fmdatabase-2026-04.xlsx` (SHA-256 `80896D2FC2048D2511EDA11326C8925EF3DD9375F6D76420523EC479F9CC1802`). Suas 64 abas são dados de figuras e tabelas do relatório; **ele não é a origem do painel mundial**. Fica local e ignorado pelo Git.

O [PDF integral oficial](https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/text.pdf) está localmente em `data/raw/fiscal-monitor-2026-04.pdf` (SHA-256 `FAB582DBF2D00FF71284204550E2CA882D5C7F081745F8F76C2BDA4B6824836F`). Páginas consultadas: vi (convenções), 43–44 (origem, cobertura, anos fiscais e padrões contábeis) e 51–57 (grupos e cobertura por economia); no visualizador PDF, são aproximadamente páginas 8, 57–58 e 65–71. O PDF não será versionado nem publicado.

A ressalva de cobertura é material: o MSA informa que, para algumas economias emergentes e em desenvolvimento, os dados fiscais podem referir-se ao governo central ou orçamentário, mesmo em comparações agrupadas do Fiscal Monitor. O painel apresenta o nome do indicador e remete a essas notas; não trata os países como perfeitamente harmonizados. Alguns países usam ano fiscal em vez de ano calendário. O recorte mistura estimativas e projeções da equipe do FMI, sem coluna de status por observação.

## Rede e aula

Algumas redes devolvem HTTP 403 no DataMapper para clientes script. Por isso o bruto recortado vive em `data/raw/` e a aula reconstrói com R:

```bash
Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline
```

Consulta exploratória à API corrente (quando a rede responder):

```bash
Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --consultar-api
```

`imfapi::imf_get()` não seleciona a vintage histórica; `--consultar-api` não substitui o cache de abril/2026. A rota Python alternativa tem o mesmo bloqueio. O `.qmd` do produto só lê o CSV, e o deck de aula não o lê.
