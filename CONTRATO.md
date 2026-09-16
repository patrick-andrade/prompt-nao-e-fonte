# CONTRATO.md — v1.2

**Cartaz:** Prompt não é fonte: análise de dados e IA em economia aplicada

Este arquivo é a fonte da verdade do minicurso. Depois da Onda 0, agentes **não** inventam país, coluna, indicador, vintage nem formato. Qualquer dúvida sobre o produto lê-se aqui, não no prompt da sessão.

---

## As três dimensões

A árvore tem **3 pastas numeradas de produto** mais pastas de **infraestrutura** sem prefixo (`docs/`, `scripts/`, `outputs/`, `aluno/`, `aula/`). Cada dimensão de produto tem README, entradas, saídas e teste de validação.

| Dimensão | Pasta | Papel |
| --- | --- | --- |
| 1 — Demanda simulada e resultados | `01-demanda-simulada/` | Pedido da supervisão, prompt preguiçoso do trainee, HTML slop (bonito, ilustrativo, impreciso). Autópsia só em `instrutor/`. |
| 2 — Análise real em Python | `02-dados-fiscal-monitor/` | Scripts que baixam, empilham, validam e gravam o CSV-contrato. Motor da rotina (abril/outubro). |
| 3 — Do `.qmd` ao PPTX e ao Reveal.js | `03-relatorio-qmd/` | Um único `mini-fiscal-monitor.qmd` (Python) lê o CSV e gera PPTX e Reveal.js. No Netlify entra **só** o Reveal.js. |

A **Diretoria de Pesquisa Aplicada** é a demanda realista de trabalho (estágio / trainee / júnior): e-mail da chefia, recorte travado, reunião no fim do expediente. Não é um tom a substituir no produto da Dimensão 3. O briefing e o `mini-fiscal-monitor.qmd` falam *como* a Diretoria; o deck de aula fala *com* o estudante (“vocês são o trainee”).

Saídas da Dimensão 3 (infraestrutura, não pastas numeradas):

- PPTX → `outputs/pptx/` (reunião interna; **não** vai ao Netlify)
- Reveal.js → `outputs/revealjs-netlify/` (único artefato publicado)
- Template de referência PPTX (Onda 2) é **entrada** em `03-relatorio-qmd/`, não em `outputs/`

Artefato de **aula** (instrutor; não é produto da Dimensão 3):

- Fonte: `aula/apresentacao-minicurso.qmd` (Reveal.js; **não** lê o CSV)
- Saída: `outputs/aula-expositiva/`
- HTML gerado **fora** do Netlify. A fonte `aula/` e a autópsia vivem no repositório público; na aula a autópsia abre-se **depois** do slop.

O resultado *bom* da demanda **não** vive na Dimensão 1: é o HTML Reveal.js / PPTX da Dimensão 3, gerado a partir do CSV.

---

## Cláusulas travadas (schema; vigentes em v1.2)

Países, indicadores, vintage e caminho do CSV **não mudam** em relação ao v1.0. O bump v1.2 não altera o schema: entra o artefato de aula, a inspeção humana e as regras de cue.

### Vintage e edição

- **Vintage:** Fiscal Monitor / WEO **abril/2026**.
- O script registra `FM-2026-04` ou `WEO-2026-04` (ou ambos, na coluna `vintage` / `source` conforme o caso).
- Título da edição: *Fiscal Policy under Pressure: High Debt, Rising Risks*.

### Países (iso3, ordem canônica)

`BRA`, `MEX`, `CHL`, `IND`, `IDN`

- Núcleo: Brasil, México, Chile (LatAm; México **não** é América do Sul — no material dizer LatAm).
- Emergentes de destaque: Índia e Indonésia.
- **Fora:** China (distorce escala e narrativa); Colômbia (trocada pelo Chile).

Não incluir `CHN` em dado, gráfico, tabela ou texto de produto.

### Indicadores

- `GGXWDG_NGDP` — dívida bruta do governo geral, % do PIB
- `GGXONLB_NGDP` — saldo primário do governo geral, % do PIB

### Anos

2000–2029 (realizado + projeção).

### CSV canônico

Caminho: `02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv`

Colunas (nesta ordem):

`iso3`, `country`, `year`, `indicator_code`, `indicator_name`, `value`, `unit`, `vintage`, `source`

---

## Quem lê o quê

- **Quarto, PPTX e Reveal.js da Dimensão 3 só leem esse CSV.** Render de aula do produto **não** chama API.
- **O slop (Dimensão 1) não usa esse CSV.** Se o HTML slop ler `fm_weo_cache.csv`, o contraste didático cai.
- **O deck de aula (`aula/apresentacao-minicurso.qmd`) não lê o CSV.** Aponta para caminhos no repositório e, quando houver, para o URL público do produto.
- **Não inventar número do Brasil (nem dos outros) em README, AGENTS, docs ou slides stub.** Números **do slop** podem aparecer no deck de aula porque são deliberadamente falsos e estão no HTML. Número fiscal verdadeiro só vem do cache, da API ou de PDF extraído com `doc_extract`.
- **Netlify:** demo do professor; alunos não criam conta. Site ligado ao git (projeto `fiscal-monitor-2026`). Artefato publicado = Reveal.js em `outputs/revealjs-netlify/`. PPTX não se hospeda. Deck de aula em `outputs/aula-expositiva/` **não** se publica. Não há app Shinylive nesta versão.
- **Pacote do aluno:** clone de [https://github.com/patrick-andrade/prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte). Zip opcional (`scripts/empacotar_aluno.py`) só para máquina sem git; se gerado, sem `aula/` e sem `instrutor/autopsia.md`.
- **Python:** `pyproject.toml` + `uv`. R só como menção de ecossistema.
- **UTF-8;** sem credenciais, tokens ou senhas no git.
- **Cue de arquivo:** caminho relativo no repositório, no projetor como `Abrir agora: 01-demanda-simulada/entrega-slop/index.html`. Sem `file://`, sem OneDrive. Hiperlink só para URL público (GitHub, Netlify).

Render do deck de aula (explícito; **não** entra no `render:` padrão de `_quarto.yml`):

```bash
uv run -- quarto render aula/apresentacao-minicurso.qmd --profile aula --to revealjs
```

---

## Inspeção humana (Onda 3)

O agente fecha o código e o esqueleto. **Não** fecha o que só o instrutor vê no projetor. Ver [`docs/checklist-instrutor.md`](docs/checklist-instrutor.md). A cláusula de inspeção humana cobre, sem número fiscal neste arquivo:

- Dimensão 1: slop legível no projetor; prompt e briefing; autópsia **depois** do HTML; conferir na mão as acusações da autópsia contra o CSV (não copiar número para o deck de aula).
- Dimensão 2: `baixar_fm.py --offline` + `validar_contrato.py`; dicionário sem série.
- Dimensão 3: `quarto render` Reveal.js **e** PPTX; gráficos e tabela; tema; “sustentável” ausente sem critério.
- Publicação: deploy Netlify do git; colar o URL de produção no parâmetro `url_netlify` do deck; conferir no ar (5 países, sem China, vintage no rodapé).
- Aula: cronometrar o núcleo de 80 min; cortar gordura e memes que não funcionarem; UTF-8 no projetor.
- Pacote: clone do GitHub; autópsia só **depois** do slop. Zip opcional, se existir: sem `aula/`, sem `instrutor/autopsia.md`.

---

## Validação

```bash
uv run python scripts/validar_contrato.py
```

- Onda 0 (CSV ainda ausente): o validador confirma o esqueleto e imprime que a Dimensão 2 está pendente (exit 0).
- Com CSV presente: passa só se colunas, países, indicadores, vintage e ausência de NA crítico nos anos-chave baterem com este contrato (exit 1 se houver desvio).

---

## Versionamento

**v1.2** (esta versão): pasta `aula/`, artefato `aula/apresentacao-minicurso.qmd`, saída `outputs/aula-expositiva/` (fora do Netlify), cláusula de inspeção humana (Onda 3), Diretoria como demanda realista de estágio/trainee, cues de arquivo = caminho relativo. Pacote do aluno = repositório público (zip opcional). Países, colunas, indicadores, vintage e CSV permanecem os do v1.1 / v1.0.

**v1.1:** a árvore deixa de ser cinco pastas numeradas e passa a ser três pastas de produto + infraestrutura.

Mudança de **país**, **coluna** ou **formato** = bump para **v1.3** neste arquivo **e** no validador. Agentes não “ajustam no feeling”.
