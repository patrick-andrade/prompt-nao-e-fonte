# CONTRATO.md — v1.0

**Cartaz:** Prompt não é fonte: análise de dados e IA em economia aplicada

Este arquivo é a fonte da verdade do minicurso. Depois da Onda 0, agentes **não** inventam país, coluna, indicador, vintage nem formato. Qualquer dúvida sobre o produto lê-se aqui, não no prompt da sessão.

---

## As três dimensões

A árvore de 5 pastas agrupa-se em **3 dimensões de produto**. Cada dimensão tem README, entradas, saídas e teste de validação.

| Dimensão | Pastas | Papel |
| --- | --- | --- |
| 1 — Demanda simulada e resultados | `01-demanda-simulada/` | Pedido da supervisão, prompt preguiçoso do trainee, HTML slop (bonito, ilustrativo, impreciso). Autópsia só em `instrutor/`. |
| 2 — Análise real em Python | `02-dados-fiscal-monitor/` | Scripts que baixam, empilham, validam e gravam o CSV-contrato. Motor da rotina (abril/outubro). |
| 3 — Do `.qmd` ao PPTX e ao Reveal.js | `03-relatorio-qmd/`, `04-pptx/`, `05-revealjs-netlify/` | Um único `mini-fiscal-monitor.qmd` (Python) gera PPTX e Reveal.js. No Netlify entra **só** o Reveal.js. |

O resultado *bom* da demanda **não** vive na Dimensão 1: é o HTML Reveal.js / PPTX da Dimensão 3, gerado a partir do CSV.

---

## Cláusulas travadas (v1.0)

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

- **Quarto, PPTX e Reveal.js só leem esse CSV.** Render de aula **não** chama API.
- **O slop (Dimensão 1) não usa esse CSV.** Se o HTML slop ler `fm_weo_cache.csv`, o contraste didático cai.
- **Não inventar número do Brasil (nem dos outros) em README, AGENTS, docs ou slides stub.** Só cache, API ou PDF extraído com `doc_extract`.
- **Netlify:** demo do professor; alunos não criam conta. Artefato publicado = Reveal.js. PPTX não se hospeda. Não há app Shinylive nesta versão.
- **Python:** `pyproject.toml` + `uv`. R só como menção de ecossistema.
- **UTF-8;** sem credenciais, tokens ou senhas no git.

---

## Validação

```bash
python scripts/validar_contrato.py
```

- Onda 0 (CSV ainda ausente): o validador confirma o esqueleto e imprime que a Dimensão 2 está pendente (exit 0).
- Com CSV presente: passa só se colunas, países, indicadores, vintage e ausência de NA crítico nos anos-chave baterem com este contrato (exit 1 se houver desvio).

---

## Versionamento

Mudança de **país**, **coluna** ou **formato** = bump para **v1.1** neste arquivo **e** no validador. Agentes não “ajustam no feeling”.
