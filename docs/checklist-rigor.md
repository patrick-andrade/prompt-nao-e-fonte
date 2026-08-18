# Checklist de rigor

Quatro perguntas, nesta ordem. Se alguma falhar, o gráfico não entra no briefing.

## 1. Qual é a pergunta?

Não “fazer um dashboard”. Uma frase: o que se quer comparar, em quais países, em qual horizonte. Exemplo de forma (sem número): dívida bruta e saldo primário dos cinco países do contrato, vintage abril/2026, 2000–2029.

## 2. Qual é o indicador?

Código, setor, unidade. Neste minicurso só existem dois: `GGXWDG_NGDP` e `GGXONLB_NGDP`, governo geral, % do PIB. Primário não é resultado nominal. Dívida bruta não é dívida líquida.

## 3. Qual é a fonte / vintage?

Publicação + edição + corte. Aqui: Fiscal Monitor abril/2026 (`FM-2026-04`), projeções alinhadas ao WEO abril/2026. “FMI” ou “dados recentes” não passa.

## 4. Dá para rerodar?

O número no slide tem de sair de `02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv` (ou de um render que só lê esse CSV). HTML com valor colado, mesmo bonito, não reroda.

## Anti-padrões (os do slop)

- Autorizar o modelo a inventar valor para “ficar apresentável”
- México como América do Sul
- País fora do recorte (Colômbia, China)
- Adjetivo (“sustentável”) no lugar da conta
- Render de aula chamando API
