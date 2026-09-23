# CONTRATO.md — v1.3

**Cartaz:** Prompt não é fonte: análise de dados e IA em economia aplicada.

Este é o contrato do minicurso. Agentes, scripts, apresentações e documentação devem concordar com ele. Não se infere país, coluna, indicador, vintage, formato ou número a partir de uma resposta de IA.

## Estrutura e produtos

A raiz é `2026/`. Há três pastas numeradas de produto; `docs/`, `scripts/`, `outputs/`, `aluno/` e `aula/` são infraestrutura sem prefixo.

| Dimensão | Pasta | Produto |
| --- | --- | --- |
| 1 — Demanda simulada | `01-demanda-simulada/` | E-mail da chefia, prompt plausível de trainee, HTML visualmente convincente com falhas de fonte e autópsia do instrutor. |
| 2 — Dados reais | `02-dados-fiscal-monitor/` | R reconstrói o CSV-contrato a partir do bruto congelado; Python é alternativa. Consulta à API é explícita e não troca a vintage sem revisão. |
| 3 — Apresentação reprodutível | `03-relatorio-qmd/` | Um `mini-fiscal-monitor.qmd` em R lê só o CSV-contrato e gera PPTX e Reveal.js. |

A Diretoria de Pesquisa Aplicada é a demanda realista de estágio, trainee ou trabalho júnior. O e-mail e a apresentação para a reunião falam como produto profissional; o deck da aula fala com os estudantes.

- PPTX → `outputs/pptx/`, apresentação interna de cerca de 10–12 slides para a reunião simulada de 20 minutos. Não vai ao Netlify.
- Reveal.js → `outputs/revealjs-netlify/index.html`, HTML autossuficiente e versionado. Este é o único artefato publicado no Netlify.
- Template PPTX → `03-relatorio-qmd/template-referencia.pptx`, entrada do render, não saída.
- Aula → `aula/apresentacao-minicurso.qmd` e `outputs/aula-expositiva/`, fora do Netlify. O deck da aula não lê o CSV; a autópsia só é aberta depois do slop.

## Schema e recorte imutáveis nesta versão

O v1.3 muda o fluxo de produção e apresentação, **não** os dados contratados.

- **Vintage fixa:** Fiscal Monitor / WEO abril/2026; `FM-2026-04` ou `WEO-2026-04` quando a origem correspondente for comprovada. A edição do Fiscal Monitor é *Fiscal Policy under Pressure: High Debt, Rising Risks*.
- **Países nesta ordem:** `BRA`, `MEX`, `CHL`, `IND`, `IDN`. Brasil, México e Chile formam o núcleo LatAm; México não é América do Sul. China (`CHN`) fica fora; Colômbia não integra o recorte.
- **Indicadores canônicos:** `GGXWDG_NGDP` (dívida bruta do governo geral, % do PIB) e `GGXONLB_NGDP` (saldo primário do governo geral, % do PIB). No saldo, positivo significa superávit.
- **Anos:** 2000–2029, incluindo observações e projeções conforme a edição. O CSV não contém classificação de status; não chamar 2025 ou 2026 de realizado sem conferência na nota metodológica.
- **CSV:** `02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv`.
- **Colunas, nesta ordem:** `iso3`, `country`, `year`, `indicator_code`, `indicator_name`, `value`, `unit`, `vintage`, `source`.

## Origem, execução e separação didática

- A Dimensão 1 não lê `fm_weo_cache.csv`. Seus números são escolhidos manualmente para a simulação e auditados na autópsia com fonte, data, cobertura e convenção de sinal. Ela pode mostrar a NFSP nominal do BCB como parte da falha intencional; **isso não acrescenta indicador ao CSV ou à Dimensão 3**.
- A Dimensão 2 é o único lugar que consulta FM/WEO ou escreve o CSV. `baixar_fm.R --offline` reconstrói o CSV do JSON recortado e versionado de abril/2026. `--consultar-api` usa `imfapi` para consulta exploratória da edição corrente, sem escrever o CSV-contrato: a função não fixa vintage histórica. O script Python oferece rota alternativa com a mesma proteção.
- O `.qmd`, o PPTX e o Reveal.js da Dimensão 3 **só leem o CSV**. O render não consulta a API. O HTML publicado não busca dados em tempo de execução.
- Números fiscais verdadeiros em relatórios e slides vêm apenas do cache, da API verificada ou de PDF extraído em recorte com `doc_extract`. Não inventar número em Markdown. Números do slop podem aparecer no deck da aula porque são citações do HTML simulado.
- Pacotes R do professor ficam no ambiente local do projeto controlado por `renv.lock`. Python permanece em `pyproject.toml` + `uv`; usar `uv sync --locked` e `uv run`, sem instalação global. Não versionar segredos.
- Netlify é demo do professor, projeto `fiscal-monitor-2026`, conectado ao Git. Publica apenas o Reveal.js pronto. Sem Shinylive; alunos não criam conta.
- Pacote do aluno: clone de https://github.com/patrick-andrade/prompt-nao-e-fonte. Zip opcional de `scripts/empacotar_aluno.py`, sem `aula/` nem a autópsia.
- Cue de arquivo em slide: `Abrir agora: caminho/relativo`. Hiperlink apenas para URL público; sem `file://` ou caminho OneDrive.

## Comandos e verificação

```bash
Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline
uv run python scripts/validar_contrato.py
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx
uv run -- quarto render aula/apresentacao-minicurso.qmd --profile aula --to revealjs
```

O validador exige as pastas, o schema, os países, os indicadores e a vintage, além de chaves únicas e valores numéricos. O HTML do produto deve ser autossuficiente e estar versionado antes do push. Inspeção humana no projetor, cronômetro, memes, URL e clone continuam no `docs/checklist-instrutor.md`.

## Versionamento

**v1.3:** R principal com bruto congelado, Python alternativo, apresentação executiva concisa com referência visual creditada, Reveal.js estático versionado, slop com erros sutis de fonte e aula ajustada. Países, indicadores, anos, colunas e vintage permanecem os de v1.2.

**v1.2:** deck de aula, saída fora do Netlify, inspeção humana e cues relativos. **v1.1:** três pastas de produto e infraestrutura sem número.

Qualquer mudança futura de país, coluna, indicador, vintage ou formato exige nova versão neste arquivo **e** em `scripts/validar_contrato.py`. Não ajustar no feeling.
