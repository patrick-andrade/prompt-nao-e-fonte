# Dimensão 1 · Demanda simulada

Uma gestora da Diretoria de Pesquisa Aplicada pede uma apresentação para a reunião. Um trainee recorre ao ChatGPT web gratuito e recebe um [HTML convincente](entrega-slop/index.html). O recorte de países está correto; os problemas são de **fonte, edição, ano, cobertura, sinal e inferência**.

Leia nesta ordem:

1. [E-mail da gestora](briefing-supervisao.md).
2. [Prompt do júnior](prompt-do-junior.md).
3. [HTML entregue](entrega-slop/index.html), em silêncio por um minuto.
4. [Autópsia do instrutor no navegador](instrutor/autopsia.html), depois da discussão; fonte em `instrutor/autopsia.qmd`.

Para atualizar o HTML local após editar a fonte: `quarto render 01-demanda-simulada/instrutor/autopsia.qmd --to html` na raiz do projeto. O arquivo gerado incorpora os recursos e não faz parte do site Netlify.

O HTML é uma peça estática da simulação e não lê `fm_weo_cache.csv`. Os valores do Brasil vêm do BCB, mas o título troca discretamente NFSP por “resultado”; os outros cards misturam anos e condições de observação sem aviso. A matriz da autópsia registra a fonte exata de cada valor. O contrato do projeto está em [`CONTRATO.md`](../CONTRATO.md) v1.5.
