# Ferramentas e extensões

O projeto separa **fonte**, **código**, **contrato** e **apresentação**.

Elementos:

- O [`CONTRATO.md`](../CONTRATO.md) v1.5 distingue o recorte executivo do universo mundial do painel, mantendo indicadores, vintage e schema
- [`AGENTS.md`](../AGENTS.md) orienta o Codex, e `.cursor/rules/minicurso.mdc` mantém compatibilidade com Cursor
  - A extensão `.mdc` não registra o contrato para o Codex

| Ferramenta | O que é | Função |
| --- | --- | --- |
| GitHub | Site que guarda e compartilha os arquivos e o histórico de versões do projeto | Acessar o briefing, o código e os dados do minicurso |
| VS Code ou outro editor | Programa para abrir e editar arquivos de texto e código | Procurar país, ano, indicador e edição dos dados (vintage) |
| R + `jsonlite` + `imfapi` | Linguagem de análise de dados com pacotes para ler JSON e consultar dados do FMI | Reconstruir o CSV executivo a partir dos dados guardados no projeto e demonstrar uma consulta atual |
| R + dados brutos do FMI guardados no projeto | Linguagem de análise de dados aplicada aos arquivos originais da edição escolhida | Preparar os dados mundiais usados pelo painel |
| Quarto + R/knitr + `ggplot2` | Ferramentas para combinar texto, cálculos e gráficos em uma apresentação | Gerar PowerPoint (PPTX) e apresentação para a web (Reveal.js) a partir do mesmo `.qmd` |
| Python | Linguagem de programação | Conferir se os arquivos seguem o contrato; também oferece uma rota alternativa para preparar o CSV executivo |
| Netlify | Serviço que publica sites na web | Disponibilizar o portal, a apresentação e o painel já gerados |

Extensões de arquivo:

| Extensão | O que é | Função | Exemplo |
| --- | --- | --- | --- |
| `.md` / `.mdc` | `.md` vem de *Markdown*; `.mdc` identifica um arquivo de regras do Cursor baseado em Markdown | Guardar textos e instruções; `.mdc` é usado pelo Cursor | `CONTRATO.md`, `AGENTS.md`, `minicurso.mdc` |
| `.R` / `.py` | Código escrito em R / Python | Guardar programas executáveis | `baixar_fm.R`, `baixar_fm.py`, `validar_contrato.py` |
| `.json` / `.csv` | *JavaScript Object Notation* (formato de dados) / *Comma-Separated Values* (valores separados por vírgula) | Guardar dados originais congelados / tabelas derivadas | `data/raw/`, `fm_weo_cache.csv`, derivado mundial |
| `.qmd` | *Quarto Markdown*, documento que combina texto e código | Guardar texto e trechos de código R para gerar relatórios e apresentações | `mini-fiscal-monitor.qmd` |
| `.scss` / `.pptx` | *Sassy CSS* (linguagem de estilos) / *PowerPoint Open XML Presentation* (arquivo de apresentação) | Definir o tema do Reveal.js / guardar um modelo ou uma apresentação PowerPoint | `tema-executivo-escuro.scss`, `template-referencia.pptx` |
| `.html` | *HyperText Markup Language* (linguagem de marcação de páginas web) | Exibir apresentações e páginas interativas | slop, portal, Reveal.js e painel |
| `.lock` | Arquivo de bloqueio de versões (*lockfile*) | Registrar as versões dos pacotes usados no projeto | `renv.lock`, `uv.lock` |

O `.qmd` do produto **só lê o CSV executivo**. O HTML do slop não lê CSV. O painel mundial usa outro derivado preparado em R da edição FMI abril/2026. As páginas públicas são saídas prontas, não consultas vivas. O PDF do BCB sustenta a autópsia da simulação; a comparação executiva usa o cache dos cinco países.

## Trabalhar com IA na pasta do projeto

O harness é o ambiente que liga o modelo à conversa, aos arquivos e às ferramentas. Conforme as permissões disponíveis, o agente pode ler o contrato, propor uma alteração e executar um comando. O pedido deve indicar o arquivo de referência, a entrega esperada e como conferir o resultado. O professor demonstra arquivos preparados; a aula não depende de geração ao vivo.

| Recurso | Uso no projeto |
| --- | --- |
| `CONTRATO.md` | Registrar escolhas sobre dados, recortes e entregas |
| `AGENTS.md` | Orientar o agente que trabalha na pasta |
| `README.md` | Apresentar o projeto e explicar como começar |
| `SKILL.md` | Descrever um procedimento reutilizável, com nome, descrição e instruções |
| Git | Conferir diferenças entre arquivos e registrar versões selecionadas em commits |
| GitHub | Receber os commits enviados por push e permitir obter uma cópia por clone |

As skills `humanizer` e `apresentacao-bullets` foram usadas na revisão da aula. A primeira orienta a revisão da prosa; a segunda organiza a hierarquia do texto nos slides. Elas pertencem ao ambiente do instrutor, e não são instaladas pelo clone do minicurso.

Documentação registra escolhas e instruções. Auditabilidade permite conferir a origem e o tratamento de um resultado. Reprodutibilidade permite repetir a produção com dados, código e ambiente disponíveis. Um resultado reproduzido ainda precisa de avaliação conceitual e revisão de sua interpretação.

## Leituras curtas

- [Codex na Prática](https://patrick-andrade.github.io/guias/codex-na-pratica.html): trabalhar com arquivos no projeto.
- [Git e GitHub na Prática](https://patrick-andrade.github.io/guias/git-na-pratica.html): registrar alterações e compartilhar quando necessário.
- [Quarto na Prática](https://patrick-andrade.github.io/guias/quarto-na-pratica.html): gerar a entrega a partir de texto e código.
- [Skills na Prática](https://patrick-andrade.github.io/guias/skills-na-pratica.html): guardar instruções de tarefas recorrentes.

As leituras são de Patrick Andrade. A aula abre exemplos breves; a leitura integral fica para depois. Para referência técnica: [skills no Codex](https://developers.openai.com/codex/skills/), [instruções em AGENTS.md](https://developers.openai.com/codex/guides/agents-md/), [fundamentos do Git](https://docs.github.com/en/get-started/using-git/about-git) e [computações no Quarto](https://quarto.org/docs/computations/r.html).
