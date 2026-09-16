# Autópsia do slop (somente instrutor)

Está no clone público; **não** entra no zip opcional. Abrir **depois** de projetar `entrega-slop/index.html` e **antes** de abrir o CSV.

O HTML é bonito de propósito. O erro não é estética; é **epistemologia do número**.

## O que o briefing pedia e o que chegou

| Pedido | Entrega slop |
| --- | --- |
| Cinco países canônicos, Chile no recorte | Colômbia no lugar do Chile |
| México como LatAm | México como América do Sul |
| Vintage abril/2026 (`FM-2026-04` / `WEO-2026-04`) | “dados atualizados” / “Live snapshot” |
| Dois indicadores com código | Dívida e “superávit” sem código, sem unidade explícita no insight |
| CSV-contrato | HTML único; rodapé admite que não usa planilha |
| Não inventar número | Números redondos, de memória / modelo |

O slop **não lê** `02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv`. Se lesse, o contraste didático cairia.

## Falhas para marcar na lousa

1. **Geografia:** México não é América do Sul. No material do minicurso, o núcleo é LatAm.
2. **Recorte:** Colômbia foi trocada pelo Chile no contrato. China continua fora (aqui o slop não a colocou; ainda assim a escala estaria distorcida se alguém “completasse o BRICS”).
3. **Vintage ausente:** sem edição, sem data de corte. “Recente” não é fonte.
4. **Sinal do primário:** o dashboard vende superávit brasileiro confortável. No CSV-contrato, o saldo primário do Brasil em 2025 é **déficit** (`GGXONLB_NGDP` negativo). Abrir a linha no cache; não ditá-la de memória.
5. **Nível da dívida:** o card do Brasil (78,2%) não reproduz a dívida bruta de 2025 no cache. Comparar `GGXWDG_NGDP` no CSV; o slop arredonda para o palco, não para o FMI.
6. **Critério de “sustentável”:** não há âncora (primário que estabiliza a dívida, r−g, cobertura do governo geral). Adjetivo no lugar de conta.
7. **Mistura realizado / projeção:** o snapshot trata um único número como fato corrente.
8. **Fonte teatral:** “FMI e web”. Qual publicação, qual tabela, qual vintage.
9. **Inglês cosmética:** título em inglês não adiciona rigor.
10. **Prompt preguiçoso in, slop out:** o junior autorizou inventar valor (“o importante é ficar apresentável”). A supervisão tinha proibido isso.

## Como usar na aula (3 minutos)

Não começar pelos números certos. Começar pelas **perguntas do checklist**: que indicador? que vintage? dá para rerodar? Só então abrir o CSV e o `.qmd`.

Números da autópsia = números do cache, nunca do modelo. Se o CSV mudar de vintage, esta página perde os exemplos numéricos — aí atualiza-se a autópsia a partir do CSV, não o contrário.
