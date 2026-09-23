# Publicar o portal, a apresentação e o painel no Netlify

O projeto Netlify `fiscal-monitor-2026` publica o diretório `outputs/revealjs-netlify/` do repositório [prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte). As rotas são:

| Rota pública | Artefato versionado | Função |
| --- | --- | --- |
| `/` | `index.html` | Portal com escolha entre apresentação e painel |
| `/apresentacao/` | `apresentacao/index.html` | Reveal.js executivo, autossuficiente, cinco países |
| `/painel/` | `painel/index.html` | Exploração mundial, autossuficiente, dados preparados em R |

O build do Netlify apenas verifica os três HTMLs já versionados. A transformação em R do snapshot oficial, o Quarto e o gerador do site são executados **localmente antes do commit**, não no servidor. O navegador não chama a API do FMI; o painel usa dados embutidos de uma edição fixa. O PPTX e o deck do instrutor continuam fora do site.

## Antes do push

1. Reconstruir e validar o CSV executivo e o derivado mundial pelos comandos do [`README.md`](../README.md). Conferir URL, hash e edição do snapshot bruto; não trocá-lo por consulta corrente à API.
2. Renderizar Reveal.js para `outputs/revealjs-netlify/apresentacao/` e PPTX para `outputs/pptx/`, gerar o portal/painel e renderizar a aula.
3. Rodar `python scripts/verificar_artefatos.py` e `bash scripts/netlify_build.sh`. Conferir offline as três páginas, seus links, filtros, gráficos, fontes e ausências; examinar todos os slides. Os recursos executáveis da página devem estar embutidos.
4. Registrar no Git o contrato, os códigos, o snapshot bruto usado, os dados derivados e os três HTMLs. O PDF integral do relatório e a planilha de figuras/tabelas ficam apenas como referência local, fora do commit e do site. Conferir que arquivos não rastreados do usuário não entraram no commit.

## Depois do push

1. Conferir o hash do commit em `main` no GitHub e o deploy correspondente no Netlify.
2. Abrir [o portal](https://fiscal-monitor-2026.netlify.app/), [os slides](https://fiscal-monitor-2026.netlify.app/apresentacao/) e [o painel](https://fiscal-monitor-2026.netlify.app/painel/).
3. No painel, selecionar 2025, localizar os cinco países do recorte executivo, testar outro ano, uma economia sem dado e as duas trajetórias. Confirmar vintage, unidade, convenção de sinal e N válido.
4. Na apresentação, conferir capa, gráficos, conclusão, fontes e crédito visual; comparar o HTML público ao arquivo local. O instrutor ainda deve completar a inspeção física no projetor.

Se o deploy não refletir o commit, guardar o identificador do deploy e revisar a ligação do site ao Git. A configuração atual não exige credenciais Netlify para a geração local; acesso ao painel Netlify pode ser necessário para investigar falha do deploy.
