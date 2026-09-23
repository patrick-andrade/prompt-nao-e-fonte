# Plano de aula · 80 minutos + até 40 opcionais

Público: graduação em economia e áreas próximas, do início ao fim do curso. A Diretoria de Pesquisa Aplicada é uma demanda simulada de estágio/trainee. A turma examina uma apresentação que convence visualmente, identifica o descuido com fontes e acompanha outra gerada de modo reproduzível. O [`CONTRATO.md`](../CONTRATO.md) distingue o recorte executivo de cinco países do universo mundial do painel.

Objetivos: reconhecer indicador e convenção de sinal; perguntar por documento, edição e ano; localizar no CSV a linha que gera o gráfico; entender por que conhecer R e Python ajuda a avaliar código produzido por IA.

## Núcleo de 80 minutos

| Tempo | Condução | Arquivos e atividade |
| ---: | --- | --- |
| 5 min | Cena da reunião e cartaz “Prompt não é fonte” | `aula/apresentacao-minicurso.qmd` |
| 7 min | Objetivos, extensões e regra “ler antes de rodar” | Atividade 0: abrir e executar `scripts/validar_contrato.py` |
| 17 min | E-mail da gestora → prompt do júnior → HTML, 60 s de observação → autópsia | Atividade 1: três perguntas de fonte, em duplas. Abrir `01-demanda-simulada/instrutor/autopsia.md` **após** o HTML. |
| 6 min | Cinco países, dois códigos, vintage, governo geral, saldo × NFSP | `CONTRATO.md` |
| 15 min | Professor abre `baixar_fm.R`, reconstrói offline e valida o CSV executivo | Atividade 2: localizar `BRA` · `2025` · `GGXONLB_NGDP`; alunos conferem sinal, edição e fonte. |
| 18 min | Professor mostra o `.qmd`, PPTX, Reveal.js, portal e painel | Cerca de 5 min no código/PPTX, 6 min nos slides executivos e 7 min de demonstração guiada: ano 2025 → Brasil na dispersão/tabela → trajetória → fonte e lacunas. |
| 7 min | O que travar num prompt; por que aprender R e Python | Atividade 3: escrever uma instrução verificável; comparar com `roteiro-ia-profissional.md`. |
| 5 min | Quiz das quatro perguntas e caminhos para continuar | Clone público, portal e duas rotas no Netlify |

O deck de aula **não lê** nenhum CSV. O produto executivo continua lendo só o CSV de cinco países; o painel usa outro derivado preparado em R da mesma edição, com as economias individuais do FMI. Números fiscais reais são mostrados ao abrir o CSV, a apresentação ou o painel. Os números do slop podem ser citados como parte da simulação. Cues de arquivo têm a forma `Abrir agora: caminho/relativo`; URLs públicos são links.

## Participação da turma

- **Navegador:** ler arquivos e CSV no GitHub, ver o portal, os slides e o painel no Netlify.
- **Editor + clone:** procurar país, ano, indicador e vintage no CSV.
- **Python do laboratório:** rodar o validador, que usa somente a biblioteca padrão. Nenhum pacote é instalado durante a aula.

R e Quarto ficam na máquina do professor para a demonstração. A rota Python alternativa de reconstrução está no clone. Para casa, `scripts/preparar_lab.py` prepara o ambiente Python do laboratório de lacunas, com `uv sync --locked`.

## Até 40 minutos opcionais

1. Reconstruir o CSV com R e com a rota Python e comparar as linhas.
2. Explicar o ano fiscal da Índia nas notas do FMI.
3. Tentar a consulta corrente com `Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --consultar-api`; se o serviço ou o pacote falhar, ler o erro sem substituir a edição congelada.
4. Ler `renv.lock`, `uv.lock` e os chunks do `lab-lacunas.qmd`.
5. Discutir o que seria necessário para uma afirmação de sustentabilidade da dívida.
6. Explorar outros anos e economias no painel e verificar como ausências alteram o universo comparável.

O checklist da projeção real fica em [`checklist-instrutor.md`](checklist-instrutor.md).
