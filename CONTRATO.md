# CONTRATO.md — v1.5

**Cartaz:** Prompt não é fonte: análise de dados e IA em economia aplicada.

Este é o contrato do minicurso. Agentes, scripts, apresentações e documentação devem concordar com ele. Não se infere país, coluna, indicador, vintage, formato ou número a partir de uma resposta de IA.

## Estrutura e produtos

A raiz é `2026/`. Há três pastas numeradas de produto; `docs/`, `scripts/`, `outputs/`, `aluno/` e `aula/` são infraestrutura sem prefixo.

| Dimensão | Pasta | Produto |
| --- | --- | --- |
| 1 — Demanda simulada | `01-demanda-simulada/` | E-mail da chefia, prompt plausível de trainee, HTML visualmente convincente com falhas de fonte e autópsia do instrutor. |
| 2 — Dados reais | `02-dados-fiscal-monitor/` | R reconstrói o CSV executivo e o derivado mundial a partir de brutos congelados; Python é alternativa apenas para o executivo. Consulta corrente à API não troca a vintage sem revisão. |
| 3 — Apresentação reprodutível | `03-relatorio-qmd/` | Um `mini-fiscal-monitor.qmd` em R lê só o CSV executivo e gera PPTX e Reveal.js. O painel é outro produto, alimentado pelo derivado mundial. |

A Diretoria de Pesquisa Aplicada é a demanda realista de estágio, trainee ou trabalho júnior. O e-mail e a apresentação para a reunião falam como produto profissional; o deck da aula fala com os estudantes.

- PPTX → `outputs/pptx/`, apresentação interna de cerca de 10–12 slides para a reunião simulada de 20 minutos. Não vai ao Netlify.
- Portal Netlify → `outputs/revealjs-netlify/index.html`, com acesso a `apresentacao/index.html` (Reveal.js autossuficiente) e `painel/index.html` (BI estático no navegador). Somente essa árvore é publicada.
- Template PPTX → `03-relatorio-qmd/template-referencia.pptx`, entrada do render, não saída.
- Aula → `aula/apresentacao-minicurso.qmd` e `outputs/aula-expositiva/`, fora do Netlify. O deck da aula não lê o CSV; a autópsia só é aberta depois do slop.
- Autópsia → `01-demanda-simulada/instrutor/autopsia.qmd`, renderizada em `01-demanda-simulada/instrutor/autopsia.html` para abrir no navegador. Os dois arquivos ficam fora do Netlify e do zip opcional do aluno.

## Schemas e recortes da versão

O v1.5 preserva o recorte executivo e o derivado mundial da v1.4; altera apenas o formato da autópsia do instrutor.

- **Vintage fixa:** Fiscal Monitor / WEO abril/2026; `FM-2026-04` ou `WEO-2026-04` quando a origem correspondente for comprovada. A edição do Fiscal Monitor é *Fiscal Policy under Pressure: High Debt, Rising Risks*.
- **Países executivos nesta ordem:** `BRA`, `MEX`, `CHL`, `IND`, `IDN`. Brasil, México e Chile formam o núcleo LatAm; México não é América do Sul. China (`CHN`) e Colômbia (`COL`) ficam fora desse CSV e da reunião simulada.
- **Universo do painel:** economias individuais listadas no catálogo `/countries` do DataMapper FM com pelo menos uma observação nos dois indicadores contratados, 2000–2029. `CHN` e `COL` entram quando a série existe. Agregados como `ADVEC` e `EURO` são excluídos.
- **Indicadores canônicos:** `GGXWDG_NGDP` (dívida bruta do governo geral, % do PIB) e `GGXONLB_NGDP` (saldo primário do governo geral, % do PIB). No saldo, positivo significa superávit.
- **Anos:** 2000–2029, incluindo observações e projeções conforme a edição. O CSV não contém classificação de status; não chamar 2025 ou 2026 de realizado sem conferência na nota metodológica.
- **CSV executivo:** `02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv`.
- **Derivado do painel:** `02-dados-fiscal-monitor/data/processed/fm_global_2026_04.csv` e `02-dados-fiscal-monitor/data/processed/fm_global_2026_04.json`, gerados por R offline. O CSV mundial usa as mesmas nove colunas do executivo; o JSON compacto contém `vintage`, `source`, `unit` e `rows` com `iso3`, `country`, `year`, `indicator_code`, `value` numérico. Uma observação indisponível não gera linha nem vira zero.
- **Colunas, nesta ordem:** `iso3`, `country`, `year`, `indicator_code`, `indicator_name`, `value`, `unit`, `vintage`, `source`.

## Origem, execução e separação didática

- A Dimensão 1 não lê `fm_weo_cache.csv`. Seus números são escolhidos manualmente para a simulação e auditados na autópsia com fonte, data, cobertura e convenção de sinal. Ela pode mostrar a NFSP nominal do BCB como parte da falha intencional; **isso não acrescenta indicador ao CSV ou à Dimensão 3**.
- A Dimensão 2 é o único lugar que consulta FM/WEO ou escreve bases processadas. `baixar_fm.R --offline` reconstrói o CSV executivo de JSONs recortados de abril/2026. `gerar_painel.R --offline` reconstrói o CSV/JSON mundiais de dois snapshots completos do DataMapper FM e do catálogo oficial de economias, todos congelados em `data/raw/`. `--consultar-api` do script executivo usa `imfapi` apenas para exploração da edição corrente e não escreve o contrato; a rota Python mantém a mesma proteção.
- O `.qmd`, o PPTX e o Reveal.js executivos **só leem o CSV executivo**. O painel usa apenas o derivado mundial preparado em R. Nenhum HTML publicado consulta a API em tempo de execução.
- Números fiscais verdadeiros em relatórios e slides vêm apenas do cache, da API verificada ou de PDF extraído em recorte com `doc_extract`. Não inventar número em Markdown. Números do slop podem aparecer no deck da aula porque são citações do HTML simulado.
- Pacotes R do professor ficam no ambiente local do projeto controlado por `renv.lock`. Python permanece em `pyproject.toml` + `uv`; usar `uv sync --locked` e `uv run`, sem instalação global. Não versionar segredos.
- Netlify é demo do professor, projeto `fiscal-monitor-2026`, conectado ao Git. Publica portal, apresentação e painel estáticos na árvore `outputs/revealjs-netlify/`. Não há servidor Shiny nem conta de aluno.
- Pacote do aluno: clone de https://github.com/patrick-andrade/prompt-nao-e-fonte. Zip opcional de `scripts/empacotar_aluno.py`, sem `aula/` nem a autópsia.
- Cue de arquivo em slide: `Abrir agora: caminho/relativo`. Hiperlink apenas para URL público; sem `file://` ou caminho OneDrive.

## Comandos e verificação

```bash
Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline
Rscript 02-dados-fiscal-monitor/scripts/gerar_painel.R --offline
uv run python scripts/validar_contrato.py
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify/apresentacao
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx
uv run -- quarto render aula/apresentacao-minicurso.qmd --profile aula --to revealjs
quarto render 01-demanda-simulada/instrutor/autopsia.qmd --to html
```

O validador exige o schema das duas bases, bruto congelado com SHA-256, economias individuais no mundial, indicadores/vintage/chaves únicas/valores finitos, equivalência CSV–JSON e conciliação da sobreposição dos cinco países. O portal e o Reveal.js devem estar versionados antes do push. Inspeção humana no projetor, cronômetro, memes, URL e clone continuam no `docs/checklist-instrutor.md`.

## Versionamento

**v1.5:** a autópsia da Dimensão 1 passa de Markdown a Quarto HTML autossuficiente, com matriz de fontes revisada; o deck da aula aponta para o HTML local. Países, indicadores, vintage, CSV executivo, derivado mundial e publicação no Netlify permanecem os da v1.4.

**v1.4:** mantém o CSV executivo de cinco países e cria derivado mundial separado para o painel, a partir de snapshots oficiais do DataMapper FM de abril/2026; portal estático passa a publicar apresentação e painel. `fmdatabase.xlsx` da página do relatório contém dados de figuras/tabelas, não as séries mundiais completas; fica como referência local, sem entrar no Git. O PDF integral também fica local e fora do site.

**v1.3:** R principal com bruto congelado, Python alternativo, apresentação executiva concisa com referência visual creditada, Reveal.js estático versionado, slop com erros sutis de fonte e aula ajustada. Países, indicadores, anos, colunas e vintage do CSV executivo permanecem os de v1.2.

**v1.2:** deck de aula, saída fora do Netlify, inspeção humana e cues relativos. **v1.1:** três pastas de produto e infraestrutura sem número.

Qualquer mudança futura de país, coluna, indicador, vintage ou formato exige nova versão neste arquivo **e** em `scripts/validar_contrato.py`. Não ajustar no feeling.
