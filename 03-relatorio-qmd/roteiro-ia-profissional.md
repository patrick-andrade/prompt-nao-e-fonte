# Roteiro de IA profissional

Dois prompts para contrastar com o [prompt preguiçoso da Dimensão 1](../01-demanda-simulada/prompt-do-junior.md). **Não colar número fiscal neste arquivo.** País, indicador, vintage e caminho do CSV vêm do [`CONTRATO.md`](../CONTRATO.md) v1.2.

O junior autorizou inventar valor para “ficar apresentável”. Estes prompts fazem o contrário: travam recorte, fonte e artefato.

Use-os no laboratório (Bloco 4) depois da autópsia do slop. Cole no chat **depois** de abrir o contrato, não no lugar dele.

---

## Prompt 1 — rotina Python (Dimensão 2)

```text
Quero uma rotina reproduzível em Python (pyproject.toml + uv, UTF-8, sem credenciais)
que baixe o Fiscal Monitor / WEO de abril/2026 e grave UM csv canônico.

Contrato (não negociar no feeling):
- Países, nesta ordem: BRA, MEX, CHL, IND, IDN.
- Fora: China (CHN) e Colômbia. México é LatAm, não América do Sul — nos comentários e no README, dizer LatAm.
- Indicadores: GGXWDG_NGDP (dívida bruta do governo geral, % do PIB) e GGXONLB_NGDP (saldo primário do governo geral, % do PIB). Não trocar por dívida líquida nem por resultado nominal.
- Anos: 2000–2029 (realizado + projeção da vintage).
- Vintage no arquivo: FM-2026-04 e/ou WEO-2026-04.
- Caminho: 02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv
- Colunas nesta ordem: iso3, country, year, indicator_code, indicator_name, value, unit, vintage, source.

Regras:
- Não inventar número. Se a API falhar (por exemplo HTTP 403), reler o JSON recortado em data/raw/ e reconstruir o CSV (--offline). Não interpolar lacuna: se o DataMapper não devolver uma célula, a linha não existe.
- Não incluir dump mundial. Não incluir CHN.
- Render de aula e o .qmd NÃO chamam esta API; só este script fala com a rede.
- Documente códigos DataMapper → códigos-contrato, sem colar série numérica no markdown.
```

O que este prompt trava: recorte, schema, vintage, falha de rede, lacuna. O que ele recusa: “pode inventar se não achar a tabela”.

---

## Prompt 2 — análise Quarto (Dimensão 3)

```text
Escreva um único mini-fiscal-monitor.qmd (Python, lang: pt-BR) com dois artefatos:
PPTX = briefing interno da reunião de 20 minutos; Reveal.js = produto publicado (slide-level: 2).
O Netlify recebe só o Reveal.js. O PPTX não se hospeda.

Fonte: SOMENTE 02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv.
Render de aula NÃO chama API. Números só via código que lê o CSV — nunca hardcode no markdown.

Conteúdo:
- Comparar os cinco países do contrato (BRA, MEX, CHL, IND, IDN).
- Dívida bruta vs saldo primário; realizado vs projeção (marcar o ano da vintage 2026).
- México = LatAm, não América do Sul. Sem China. Sem Colômbia.
- Dois slides de método: governo geral; primário ≠ nominal.
- Paleta slate / indigo / sky nos gráficos (e no tema, se houver).
- Template PPTX de referência, se existir, como reference-doc; saídas: PPTX em outputs/pptx/ (não publicar) e Reveal.js em outputs/revealjs-netlify/ (único publish).

Não escreva “sustentável” sem critério. Não copie valor para card estático. Não invente país, coluna, indicador, vintage, formato nem número.
```

O que este prompt trava: um arquivo, duas saídas, CSV como única fonte, geografia, paleta, destinos. O que ele recusa: dashboard único em HTML com insight inventado.

---

## Como usar o contraste na aula

1. Projetar o [prompt do junior](../01-demanda-simulada/prompt-do-junior.md) (América do Sul, Colômbia, “pode inventar”, HTML único).
2. Abrir o slop.
3. Colar **um** dos prompts acima no mesmo modelo.
4. Checklist: [`docs/checklist-rigor.md`](../docs/checklist-rigor.md).

Prompt profissional não substitui o contrato. Se o modelo ainda inventar país ou número, o validador e o CSV é que mandam — não o chat.
