# Roteiro de IA profissional

Depois de observar o [prompt do júnior](../01-demanda-simulada/prompt-do-junior.md) e abrir a autópsia, use estes pedidos como exercício. O [`CONTRATO.md`](../CONTRATO.md) v1.5 continua sendo a referência; a resposta do modelo precisa passar pelo código e pelo CSV.

## Prompt 1 · Reconstruir dados

```text
Leia CONTRATO.md, 02-dados-fiscal-monitor/notas-vintage-2026-04.md e o dicionário.
Em R, faça uma rotina que reconstrua o CSV-contrato a partir dos dois JSONs recortados
e versionados em data/raw/. Use --offline como padrão, valide metadados, países,
indicadores, anos, colunas e chaves; não preencha células ausentes.

Se mostrar uma consulta com imfapi, deixe-a em --consultar-api e informe que a função
documentada não seleciona a vintage abril/2026. Essa consulta não pode regravar nem
rotular o CSV contratado. Entregue comandos de validação e explique o que verificam.
Não inclua dados mundiais, valores fiscais no Markdown ou credenciais.
```

## Prompt 2 · Apresentação da reunião

```text
Leia CONTRATO.md e o CSV em 02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv.
Crie um único mini-fiscal-monitor.qmd em R/knitr que apenas leia esse CSV e gere
PPTX e Reveal.js com cerca de 10–12 slides para uma reunião de 20 minutos.

Mostre pergunta, método, comparação dos cinco países, trajetórias, leitura do Brasil,
limites de status e ano fiscal, e síntese. Use os dois códigos contratados e indique
ano, setor, unidade, convenção de sinal e vintage. Não chame API durante o render,
não invente número e não declare sustentabilidade sem critério.

Use o template PPTX e o tema Reveal.js do repositório; credite no último slide a
inspiração visual OECD Economic Outlook 2026/1. O Reveal.js deve gerar um index.html
autossuficiente para publicação estática. Valide os valores contra o CSV.
```

Peça ao grupo que acrescente **uma instrução verificável** ao prompt inicial: fonte ou arquivo a consultar, resultado esperado e forma de conferência. Por exemplo: conferir `indicator_code`, `vintage` e o sinal da célula usada no gráfico. Em outros projetos, o mesmo procedimento pode ser aplicado a uma citação num fichamento ou à tabela de um relatório.
