# Autópsia do HTML · uso do instrutor

Abra este arquivo **depois** de projetar `01-demanda-simulada/entrega-slop/index.html` e ouvir a turma. O HTML respeita o recorte de países e não comete erro geográfico evidente. A falha está na **proveniência, no status dos anos e na interpretação das séries**.

## Matriz de auditoria

| Valor exibido | Fonte exata | Ano | Cobertura | Convenção de sinal | Inferência indevida ou informação ausente |
| --- | --- | --- | --- | --- | --- |
| Brasil: dívida **78,7% do PIB** | [BCB, Estatísticas fiscais, janeiro/2026](https://www.bcb.gov.br/content/estatisticas/hist_estatisticasfiscais/202601_Texto_de_estatisticas_fiscais.pdf), DBGG | Fechamento de 2025 | Dívida bruta do governo geral na definição do BCB | Estoque positivo | Posta ao lado da dívida FMI dos demais países sem avisar que as definições e coberturas podem divergir. No CSV FM, Brasil 2025 é **93,329176%**, outro conceito/recorte. |
| Brasil: “resultado primário” **+0,43% do PIB** | Mesmo informe do BCB, **NFSP primária**; [metodologia do BCB](https://www.bcb.gov.br/content/estatisticas/Documents/notas_metodologicas/estatisticas-fiscais/estatisticasfiscais.pdf) | 2025 | Setor público consolidado | **NFSP positiva = déficit** | O título “resultado” e o sinal `+` sugerem saldo positivo; o conceito e a convenção da fonte foram ocultados. O saldo do FMI para Brasil 2025 é **−0,388479%** no governo geral. |
| Brasil: “resultado nominal” **+8,34% do PIB** | Mesmo informe do BCB, **NFSP nominal** | 2025 | Setor público consolidado | **NFSP positiva = déficit** | A mesma troca de conceito ocorre no nominal; ele nem integra o CSV contratado de dois indicadores. |
| México: dívida **62,7**; primário **+1,6** | [`fm_weo_cache.csv`](../../02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv), `MEX`, `GGXWDG_NGDP` e `GGXONLB_NGDP`, `FM-2026-04`; valores 62,680153 e 1,602886 arredondados | 2026 | Governo geral, % do PIB | Saldo primário positivo = superávit | “Mais recente” não diz que 2026 é projeção da edição publicada antes do fim do ano. |
| Chile: dívida **41,8**; primário **−2,0** | Mesmo CSV, `CHL`, mesmos códigos e vintage; 41,774031 e −1,993155 arredondados | 2025 | Governo geral, % do PIB | Saldo negativo = déficit | Edição, código e status do ponto não aparecem no HTML. |
| Índia: dívida **84,8**; primário **−3,0** | Mesmo CSV, `IND`; 84,781769 e −2,958179 arredondados. [Notas metodológicas do FMI, abril/2026](https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/msa.pdf) | 2024 no FMI | Governo geral; ano fiscal indiano | Saldo negativo = déficit | O rótulo 2024 parece ano civil. O FMI registra como 2024 o exercício fiscal encerrado antes de 30 de junho de 2025; o painel não explica essa diferença. |
| Indonésia: dívida **41,0**; primário **−0,8** | Mesmo CSV, `IDN`; 41,021123 e −0,757286 arredondados | 2025 | Governo geral, % do PIB | Saldo negativo = déficit | Edição, status do ponto e arredondamento não são documentados. |

O HTML não lê o CSV: os valores foram selecionados e colados manualmente para a simulação. No produto da Dimensão 3, o `.qmd` lê o CSV **em cada render**. O CSV registra a vintage, mas não tem coluna que marque cada ponto como observado ou estimado; não atribua esse status a 2025 sem conferir a fonte. México 2026 pertence ao horizonte projetado. A Índia segue o ano fiscal indicado no MSA.

## Quatro perguntas para a discussão

1. “Mais recente” é a mesma coisa que **mesmo ano, edição e status**? Aqui há 2024, 2025 e 2026 no mesmo painel.
2. “FMI e estatísticas fiscais nacionais” permite localizar documento, tabela, indicador e cobertura de cada card?
3. O sinal `+` significa o mesmo na **NFSP do BCB** e no **saldo primário do FMI**?
4. Que cálculo ou hipótese sustenta a frase “trajetória sustentável”? O HTML não apresenta nenhum.

**Sequência de palco:** 60 segundos no HTML → hipóteses da turma → esta matriz → CSV e `.qmd`. O contraste ensina a cuidar das fontes, e não a melhorar a aparência do slop.
