# Briefing da supervisão

**De:** Diretoria de Pesquisa Aplicada  
**Para:** equipe júnior (estágio / trainee)  
**Assunto:** Mini Fiscal Monitor — briefing interno + versão para o navegador  
**Quando:** rotina **abril / outubro** (acompanhar o Fiscal Monitor e o WEO)  
**Vintage desta rodada:** Fiscal Monitor / WEO **abril/2026**  
**Título da edição (referência, não número):** *Fiscal Policy under Pressure: High Debt, Rising Risks*

---

## O pedido

Precisamos de um **mini monitor fiscal** para uma reunião de 20 minutos com a coordenação e, em seguida, de uma versão HTML para projetar no laboratório. Não é um paper. É um produto curto, reproduzível, com números que dá para defender.

A demanda **não** é “um dashboard bonito”. A demanda é: **pergunta → indicador → fonte/vintage → gráfico que se reroda**.

## Recorte (não negociar no feeling)

Países, nesta ordem:

1. Brasil (`BRA`)
2. México (`MEX`)
3. Chile (`CHL`)
4. Índia (`IND`)
5. Indonésia (`IDN`)

Núcleo LatAm: Brasil, México e Chile. México **não** é América do Sul — no texto, dizer LatAm. Emergentes de destaque: Índia e Indonésia.

**Fora:** China (distorce escala e narrativa). Colômbia saiu do recorte (entrou o Chile).

Indicadores:

- `GGXWDG_NGDP` — dívida bruta do governo geral, % do PIB
- `GGXONLB_NGDP` — saldo primário do governo geral, % do PIB

Anos: 2000–2029 (realizado + projeção da vintage).

## Entregas

1. **Rotina em Python** que baixa (ou relê o cache) e grava o CSV canônico. Não colar número de memória, de slide antigo nem de “o que o modelo lembrar”.
2. **Um `.qmd`** que lê **somente** esse CSV e gera:
   - PPTX para a reunião interna
   - Reveal.js para o navegador (é o que se publica; o PPTX não vai para o site)
3. Dois slides de método: o que é governo geral, o que é primário, e qual é a vintage.

## O que não fazer

- Não inventar número do Brasil nem dos outros.
- Não chamar API na hora de renderizar a aula se o CSV já existe.
- Não misturar vintage (abril com outubro, WEO com GFS “que achei no Google”).
- Não tratar México como América do Sul.
- Não incluir China “só para comparar”.

Se a fonte oficial estiver fora do ar, use o cache da pasta de dados e registre isso. Cache com vintage explícita vale mais do que um HTML impecável com número solto.

## Prazo

Hoje, fim do expediente. Se não der para fechar o `.qmd`, pelo menos o CSV e uma tabela com os cinco países. Sem tabela com fonte, não há entrega.
