# Plano de aula · 90 minutos de exposição + 30 de discussão e folga

Público: graduação em economia e áreas próximas, com diferentes experiências em programação e IA. O caso da Diretoria de Pesquisa Aplicada liga uma demanda de estágio/trainee à exploração e à comunicação de projetos com IA. A turma examina uma apresentação convincente, confere suas fontes e acompanha a produção de outra com dados e procedimentos documentados.

Objetivos: reconhecer indicador e convenção de sinal; localizar a origem de um resultado; entender como arquivos, código, documentação e ambiente permitem refazer o trabalho; conhecer o uso de harness, Git, Quarto e skills no projeto. O [`CONTRATO.md`](../CONTRATO.md) distingue o recorte executivo de cinco países do universo mundial do painel.

## Exposição de 90 minutos

Os tempos incluem demonstrações e pequenas atividades. A apresentação da reunião simulada dura cerca de 20 minutos, mas a aula mostra apenas trechos desse produto.

| Tempo | Condução | Demonstração e atividade |
| ---: | --- | --- |
| 35 min | Introdução, demanda, prompt, HTML, autópsia e passagem do prompt ao projeto | Atividade 1 depois do slop; autópsia somente depois do HTML. Explicar o recorte do contrato antes da Atividade 2, que localiza as escolhas no contrato e no validador. |
| 18 min | ETL, script, harness, pacotes, reconstrução e conferência | 13 min para abrir a rotina R, localizar entrada e saída, explicar harness e pacotes, reconstruir e validar; 5 min para a Atividade 3: localizar `BRA` · `2025` · `GGXONLB_NGDP`. Apresentar a API depois como consulta exploratória. |
| 20 min | Quarto, comunicação, Git, publicação, portal e painel | 7 min para `.qmd`, gráfico e saídas; 4 min para histórico, diff, commit e push; 2 min para portal e materiais; 7 min para o painel em 2025, Brasil, trajetórias, linhas de origem e lacunas. |
| 12 min | Repertório com IA, skills e instrução verificável | 3 min para linguagens e outros projetos; 4 min para skill e função dos arquivos de instruções; 3 min de Atividade 4; 2 min para comparar com o roteiro profissional. |
| 5 min | Encerramento e materiais | Retomar pergunta, fontes, possibilidade de conferir/refazer e comunicação; indicar clone, portal, guias e exercício para casa. |
| **90 min** | **Total de exposição, demonstrações e pequenas atividades** | |

Os guias práticos de [Codex](https://patrick-andrade.github.io/guias/codex-na-pratica.html), [Git e GitHub](https://patrick-andrade.github.io/guias/git-na-pratica.html), [Quarto](https://patrick-andrade.github.io/guias/quarto-na-pratica.html) e [Skills](https://patrick-andrade.github.io/guias/skills-na-pratica.html) entram nos respectivos blocos. Abrir brevemente para mostrar um exemplo e deixar a leitura integral para depois. Não instalar ferramentas nem depender de geração ao vivo pela IA.

O deck de aula não lê CSV. O produto executivo lê apenas o CSV de cinco países; o painel usa o derivado mundial da mesma edição. Números reais são mostrados ao abrir os dados e os produtos. Cues de arquivo têm a forma `Abrir agora: caminho/relativo`; links levam a URLs públicos.

## Participação da turma

- Navegador: ler arquivos e CSV no GitHub, ver os produtos no Netlify e consultar os guias.
- Editor e clone: procurar país, ano, indicador e edição no CSV; ler os scripts.
- Python do laboratório: a Atividade 2 pede leitura do validador. Sua execução é opcional, usa somente a biblioteca padrão e exige o clone ou Download ZIP completo.

R, Quarto e o ambiente Python do professor estarão preparados antes da aula. Nas demonstrações do professor, usar `uv run python` para a rota Python. Para casa, com `uv` instalado, preparar o ambiente com `uv sync --locked`. As skills mostradas pertencem ao ambiente do instrutor; o clone não as instala.

## Discussão e folga de 30 minutos

Reservar esse período para perguntas, comentários e atrasos nas transições. Os slides “se sobrar tempo” são complementos, escolhidos conforme a discussão; não constituem um segundo bloco obrigatório de exposição.

- Comparar a reconstrução em R e Python com os mesmos brutos.
- Retomar o calendário fiscal da Índia e os limites de comparabilidade.
- Examinar os arquivos de versões e a preparação do ambiente.
- Discutir o que seria necessário para avaliar sustentabilidade da dívida.
- Explorar outro ano e uma economia com valor ausente no painel.

Se a rede falhar, abrir os HTMLs locais; guias externos ficam para consulta posterior. A inspeção física e o cronômetro ficam no [`checklist-instrutor.md`](checklist-instrutor.md).
