# Prompt não é fonte

Minicurso da Semana da Economia da PUC-SP, em 24 de setembro de 2026, por Patrick Andrade. São 90 minutos de exposição, demonstrações e pequenas atividades, com 30 minutos de discussão e folga.

O curso acompanha a elaboração de uma análise de economia aplicada, desde o pedido de uma apresentação até a publicação dos resultados. O caso permite explorar como trabalhar com IA em um projeto: organizar arquivos, registrar escolhas, conferir fontes, revisar código e comunicar o que os dados permitem dizer.

O mote **“prompt não é fonte”** aparece em uma situação de trabalho: uma apresentação pode parecer pronta para a reunião e ainda misturar conceitos, anos e convenções de sinal. Para examinar esses problemas, o repositório reúne a demanda simulada, os dados de origem, os scripts e os documentos que geram os produtos finais.

## Primeiro passo no laboratório: clonar e abrir o projeto

No VS Code, abra **Terminal → Novo Terminal**. O VS Code sem extensões adicionais basta para esta etapa; para usar `git clone`, o computador também precisa ter o Git instalado. No terminal PowerShell integrado, execute os comandos abaixo, um por vez:

```powershell
cd $env:USERPROFILE
git clone https://github.com/patrick-andrade/prompt-nao-e-fonte.git
cd .\prompt-nao-e-fonte
code .
```

O que significa cada comando:

- `cd $env:USERPROFILE`: muda o diretório atual para a pasta do usuário conectado (`C:\Users\Usuario`).
- `git clone https://github.com/patrick-andrade/prompt-nao-e-fonte.git`: clona o repositório do GitHub para o diretório atual.
- `cd .\prompt-nao-e-fonte`: muda o diretório atual para a pasta `prompt-nao-e-fonte`.
- `code .`: abre a pasta atual como projeto no VS Code.

Não é preciso entrar em uma conta GitHub para clonar o repositório público.

*Recomendação:*

Confira no explorador de arquivos do editor se aparecem este `README.md` e as pastas `01-demanda-simulada/`, `02-dados-fiscal-monitor/` e `03-relatorio-qmd/`.

Se `code .` não abrir a pasta, use **Arquivo → Abrir Pasta** no VS Code e escolha `C:\Users\Usuario\prompt-nao-e-fonte`, trocando `Usuario` pelo login da máquina. Se `git` não estiver disponível, baixe o repositório completo no GitHub por **Code → Download ZIP**, extraia o ZIP na pasta do usuário e abra a pasta extraída pelo mesmo menu.

## Acessar os materiais

- [Portal do minicurso](https://fiscal-monitor-2026.netlify.app/): produtos publicados e leituras complementares.
- [Apresentação executiva](https://fiscal-monitor-2026.netlify.app/apresentacao/): comparação fiscal de Brasil, México, Chile, Índia e Indonésia, preparada para a reunião simulada de 20 minutos.
- [Painel fiscal](https://fiscal-monitor-2026.netlify.app/painel/): exploração por economia e ano, com trajetórias, linhas de origem e indicação de valores ausentes.
- [Slides da aula e instruções para gerar o HTML](aula/): explicações, atividades e notas do apresentador.

É possível acompanhar a leitura dos arquivos no GitHub e explorar os produtos no navegador. Para executar os scripts ou gerar as apresentações, use uma cópia completa deste repositório, obtida por `git clone` ou **Code → Download ZIP**. Os [requisitos de participação](docs/requisitos-laboratorio.md) distinguem a leitura no navegador, o uso de editor e a execução de código.

## O que se aprende

O material foi preparado para estudantes de economia e áreas próximas, inclusive quem ainda não conhece os ambientes e as ferramentas usados em projetos com IA. Ao longo do caso, as atividades propõem:

- Conferir indicador, fonte, edição, ano e convenção de sinal antes de interpretar um número ou comparar países.
- Localizar o dado usado em um gráfico e acompanhar sua transformação, do arquivo original à tabela de análise.
- Entender o papel de arquivos como `.md`, `.R`, `.py`, `.json`, `.csv` e `.qmd`, e como eles se relacionam em um projeto.
- Trabalhar com um agente de IA em um *harness*, o ambiente que conecta a conversa aos arquivos e às ferramentas, com instruções sobre a tarefa e a conferência do resultado.
- Ler diferenças entre versões, registrar alterações com Git e compartilhar o trabalho pelo GitHub.
- Escrever uma instrução verificável para a IA e conhecer *skills*: procedimentos reutilizáveis descritos em arquivos `SKILL.md`.

Documentação registra as escolhas e os procedimentos. Auditabilidade permite conferir a origem e o tratamento de um resultado. Reprodutibilidade permite refazer sua produção com os dados, o código e o ambiente disponíveis. Essas práticas também se aplicam a fichamentos, relatórios e outros projetos com IA; reproduzir uma saída ainda exige avaliar sua interpretação.

## O caso e os arquivos

A Diretoria de Pesquisa Aplicada pede uma apresentação sobre dívida pública e resultado fiscal. Um pedido ao ChatGPT leva a um HTML convincente, com falhas deliberadas de cuidado com as fontes. A leitura começa pelo e-mail, pelo prompt e por essa entrega; a matriz de auditoria apresenta depois as fontes e os problemas de cada afirmação.

A sequência passa à reconstrução dos dados em R, à validação dos arquivos e à elaboração de uma apresentação em Quarto. O mesmo `.qmd`, que reúne texto e código, gera slides no navegador com Reveal.js e um arquivo PowerPoint. O painel permite explorar a base mundial da mesma edição, além dos cinco países escolhidos para a reunião.

| Pasta | Conteúdo |
| --- | --- |
| [`01-demanda-simulada/`](01-demanda-simulada/) | E-mail, prompt, HTML da simulação e matriz de auditoria das fontes, chamada de autópsia |
| [`02-dados-fiscal-monitor/`](02-dados-fiscal-monitor/) | Dados brutos e tabelas derivadas, scripts R e Python, dicionário dos indicadores e notas da edição |
| [`03-relatorio-qmd/`](03-relatorio-qmd/) | Arquivo Quarto da apresentação executiva, estilos, modelo PowerPoint e exercício para continuar o estudo |
| [`aula/`](aula/) | Apresentação do minicurso, imagens e notas de condução |
| [`site/`](site/) | Fontes do portal e do painel: HTML, estilos e código de interação |
| [`docs/`](docs/) | Explicações das ferramentas, critérios de revisão, roteiro da aula e instruções de publicação |

As escolhas de países, indicadores, edição dos dados e entregas estão registradas no [`CONTRATO.md`](CONTRATO.md), versão 1.5. O [`AGENTS.md`](AGENTS.md) orienta o agente de IA que trabalha na pasta. O [guia de ferramentas e extensões](docs/ferramentas.md) explica a função dos demais arquivos. As skills `humanizer` e `apresentacao-bullets`, usadas na revisão dos textos e slides, são exemplos discutidos na aula; elas não são instaladas pelo clone.

## Dados e reprodução

A análise usa dívida bruta e saldo primário, em porcentagem do PIB, da edição de abril de 2026 do Fiscal Monitor do FMI. Os arquivos originais estão guardados em `02-dados-fiscal-monitor/data/raw/`, para que a reconstrução use a mesma edição. O CSV executivo contém Brasil, México, Chile, Índia e Indonésia. O painel usa uma base separada, com 194 economias individuais e anos de 2000 a 2029; a disponibilidade varia entre indicadores, economias e anos.

As rotinas R reconstroem as tabelas a partir desses arquivos com `--offline`. Há também uma alternativa em Python para o CSV executivo. Uma API permite que um programa peça dados a um serviço; aqui, `--consultar-api` permite explorar a edição corrente sem substituir a base de abril de 2026. O arquivo Quarto executivo lê apenas `fm_weo_cache.csv`. A geração das apresentações e o navegador não consultam a API.

A edição reúne observações, estimativas e projeções, e os dados exigem atenção às diferenças de cobertura e de ano fiscal. O CSV não classifica cada ponto como observado ou projetado. As [notas da edição](02-dados-fiscal-monitor/notas-vintage-2026-04.md) e o [dicionário dos indicadores](02-dados-fiscal-monitor/dicionario-indicadores.md) documentam esses limites. Valores ausentes permanecem ausentes, sem virar zero.

<details>
<summary>Preparar o ambiente e reproduzir os produtos localmente</summary>

Use o clone completo, com R, Quarto, Python e `uv` disponíveis. Na raiz do projeto, prepare os ambientes:

```bash
uv sync --locked
Rscript -e 'source("renv/activate.R"); renv::restore(prompt=FALSE)'
```

O [`renv.lock`](renv.lock) registra os pacotes R. O `.Rprofile` usa a biblioteca local quando os pacotes centrais estão restaurados. Para Python, `pyproject.toml` e `uv.lock` definem as dependências e suas versões. A preparação inicial pode precisar de internet para obter os pacotes; a reconstrução dos dados usa os arquivos locais.

Em seguida, reconstrua as bases, valide os dados e gere os produtos:

```bash
Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline
Rscript 02-dados-fiscal-monitor/scripts/gerar_painel.R --offline
uv run python scripts/validar_contrato.py
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify/apresentacao
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx
uv run python scripts/gerar_site.py
quarto render aula/apresentacao-minicurso.qmd --profile aula --to revealjs
uv run python scripts/verificar_artefatos.py
```

O validador do contrato confere estrutura, indicadores, países, edição e consistência entre as bases. A verificação dos artefatos compara os dados embutidos no painel com a base mundial, confere recursos dos HTMLs, contagem de slides e valores do Brasil no PowerPoint. A revisão dos gráficos, das fontes e da interpretação segue o [checklist de rigor](docs/checklist-rigor.md).

As saídas ficam em `outputs/revealjs-netlify/` (portal, apresentação executiva e painel), `outputs/pptx/` (PowerPoint) e `outputs/aula-expositiva/` (slides da aula). Os HTMLs gerados abrem localmente sem rede; links para guias e outras páginas externas exigem conexão.

Para conferir somente a estrutura e os dados, `scripts/validar_contrato.py` usa a biblioteca padrão e pode rodar com o Python do laboratório. O [pacote opcional do aluno](aluno/) é reduzido e exclui a aula e a autópsia; a validação completa da estrutura requer o clone ou o Download ZIP do repositório.

</details>

## GitHub, Netlify e publicação

O Git registra o histórico das alterações. No [GitHub](https://github.com/patrick-andrade/prompt-nao-e-fonte), ficam os arquivos do projeto e os commits enviados por *push*, que permitem examinar o que mudou entre versões.

O Netlify publica apenas `outputs/revealjs-netlify/`, com as três páginas acessíveis nos links do início deste README. Os HTMLs já estão gerados e versionados; a etapa de publicação confere sua presença. O painel funciona no navegador com os dados incorporados ao próprio arquivo. O PowerPoint, os slides da aula e a autópsia ficam fora do site. Os detalhes estão no [roteiro de publicação](docs/roteiro-netlify.md).

## Para continuar

Os [guias práticos de Patrick Andrade](https://patrick-andrade.github.io/guias.html) retomam recursos apresentados no minicurso:

- [Codex na Prática](https://patrick-andrade.github.io/guias/codex-na-pratica.html): trabalhar com um agente de IA nos arquivos de um projeto.
- [Quarto na Prática](https://patrick-andrade.github.io/guias/quarto-na-pratica.html): reunir texto e análise no arquivo que gera a entrega.
- [Git e GitHub na Prática](https://patrick-andrade.github.io/guias/git-na-pratica.html): conferir alterações, registrar versões e compartilhar o trabalho.
- [Skills na Prática](https://patrick-andrade.github.io/guias/skills-na-pratica.html): guardar instruções para tarefas recorrentes.

Para praticar, o repositório inclui um [laboratório de lacunas em Quarto](03-relatorio-qmd/lab-lacunas.qmd) e um [roteiro de trabalho com IA](03-relatorio-qmd/roteiro-ia-profissional.md). Para reutilizar o material em aula, estão disponíveis o [plano de duas horas](docs/plano-aula-2h.md) e o [checklist de preparação](docs/checklist-instrutor.md).
