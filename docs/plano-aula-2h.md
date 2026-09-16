# Plano de aula — 80 min + gordura

Minicurso *Prompt não é fonte*. Público: graduação mista em economia e ciências sociais aplicadas (calouro → formandos), laboratório de informática com VS Code. Núcleo **80 min** de propósito apertado; gordura **até 40 min** se a turma perguntar pouco. Sem números fiscais neste plano; eles só aparecem no CSV e no que o `.qmd` da Dimensão 3 lê. Números **do slop** podem aparecer no projetor porque são deliberadamente falsos.

Deck de palco (instrutor): `aula/apresentacao-minicurso.qmd` → `outputs/aula-expositiva/`. Não lê o CSV. Cue no slide: `Abrir agora:` + caminho relativo. Hiperlink só para URL público.

A Diretoria de Pesquisa Aplicada é a demanda realista (estágio / trainee / júnior). Vocês são o trainee; o briefing é o e-mail da chefia; o prompt do colega é o atalho preguiçoso.

## Objetivos de aprendizado

Ao sair, o aluno consegue:

1. **Distinguir** um HTML apresentável de uma rotina que se reroda.
2. **Aplicar** as quatro perguntas (pergunta, indicador, fonte/vintage, reroda?) a qualquer número que chegue por chat.
3. **Ler** um CSV-contrato — `iso3`, código do indicador, vintage — e localizar uma célula sem perguntar ao modelo.

O quiz do fecho verifica os três. Nenhum exige programar.

## Três degraus de participação

Cada atividade diz qual degrau basta ([`ferramentas.md`](ferramentas.md), [`requisitos-laboratorio.md`](requisitos-laboratorio.md)):

- **1 · navegador** — GitHub (CSV como tabela) + Netlify.
- **2 · VS Code + clone** — abrir arquivos e procurar no CSV. **Basta para toda a aula.**
- **3 · `uv`** — `python scripts/preparar_lab.py`; validador e `--offline`.

## Núcleo (80 min)

### 5 min — cartaz e cena

- Cartaz: "Wikipedia não é fonte" → "Prompt não é fonte".
- "Vocês são o trainee." Cena 17h42, reunião às 18h.
- As três dimensões em uma frase; ainda não abrir o contrato inteiro.

### 9 min — antes de começar

- Três objetivos (distinguir, aplicar, ler) e a **regra da aula: ler antes de rodar**. Nenhum comando "cola e roda": antes de executar um arquivo, abre-se o arquivo, diz-se o que ele faz e por que vamos rodá-lo. Vale para `preparar_lab.py`, `baixar_fm.py`, `validar_contrato.py` e o `.qmd`.
- Crash course de extensões em dois slides: o que cada arquivo é (`.md`, `.py`, `.csv`, `.qmd`, `.html`, `.pptx`, `.toml`/`.yml`/`.lock`, `.json`, `.scss`) e **quem lê o quê** (humano, Python, Quarto, navegador, IA). Ponto: o `.md` é referência para pessoa e para modelo; o `.csv` é a única fonte de número; o `.html` é saída.
- Ferramentas na mesa e quem usa hoje (aluno / professor). Dizer a divisão: o laboratório forneceu VS Code, Python e rede ([`pedido-laboratorio.md`](pedido-laboratorio.md)); o resto o projeto puxa.
  - `Abrir agora: docs/ferramentas.md`
- **Leitura guiada de `scripts/preparar_lab.py`** (3 min): projetar o arquivo; docstring do topo e os `def` na ordem — `degrau_2` (confere o clone), `localizar_uv`/`instalar_uv` (só o executável, no perfil do usuário), `sincronizar` (`uv sync --locked`: mesmas versões em toda máquina), `validar`, `fechar`. Ler nomes, não linhas.
- **Atividade 0 · Onboarding as is** (4 min, individual, dispara e segue): clonar ou baixar o zip, abrir no VS Code, `python scripts/preparar_lab.py` — agora sabendo o que vai aparecer. O repositório instala `uv`, o Python do projeto e as bibliotecas no `.venv` e roda o validador. Esperado `DEGRAU: 3`; `DEGRAU: 2` não trava a aula. É a primeira lição de projeto real: ninguém instala pacote à mão.

### 17 min — demanda, slop, autópsia

- Ler em voz alta o briefing da Diretoria (`01-demanda-simulada/briefing-supervisao.md`).
- Projetar o prompt do colega (`01-demanda-simulada/prompt-do-junior.md`).
- Abrir o slop. **60 segundos em silêncio.**
  - `Abrir agora: 01-demanda-simulada/entrega-slop/index.html`
- **Atividade 1 · Três violações** (3 min, duplas, sem teclado): apontar três pontos em que o HTML viola o briefing. Não vale "o número está errado" — o CSV ainda não abriu. Três duplas falam; anotar sem corrigir.
- Autópsia pelas quatro perguntas (`docs/checklist-rigor.md`), cruzando com o que a turma apontou. `instrutor/autopsia.md` está no clone; abrir **depois** do HTML.
- Transição: "o resultado bom não mora nesta pasta."

### 6 min — contrato (sem ler o arquivo inteiro)

- Cinco países, dois códigos, vintage abril/2026.
- México = LatAm; China fora; Colômbia saiu (entrou o Chile).
- Calouros: governo geral ≠ central; primário ≠ nominal; vintage = edição, não "dados recentes".
- `Abrir agora: CONTRATO.md` (só a tabela de recorte, se precisar).

### 13 min — rotina Python e CSV

- Pasta `02-dados-fiscal-monitor/`: dicionário (códigos, sem série) e notas de vintage.
- Caminho da aula: abrir `baixar_fm.py` (onde está o `--offline`, o que lê em `data/raw/`, o que grava) e só então rodar no projetor; validador passa.
- **Atividade 2 · Achem a linha** (5 min, individual, degrau 2; degrau 3 opcional): abrir `fm_weo_cache.csv` no VS Code ou no GitHub, localizar `BRA` · `2025` · `GGXONLB_NGDP`, ler o **sinal** de `value` e comparar com o card do slop. Ninguém diz o número: mão levantada, positivo ou negativo. Degrau 3: `python scripts/preparar_lab.py --so-validar`.
- Abrir o CSV no projetor: colunas na ordem do contrato, a linha que a turma achou. **Não** copiar número para o slide.

### 12 min — um `.qmd`, dois artefatos

- `03-relatorio-qmd/mini-fiscal-monitor.qmd` lê **somente** o CSV. Mostrar o YAML e um chunk que lê o arquivo.
- Produto no ar ou local: gráficos, tabela do ano-foco. Perguntar: "a linha da Atividade 2 está neste gráfico?"
- PPTX (briefing interno da reunião) e Reveal.js (produto no navegador) saem do mesmo `.qmd`.
- `Abrir agora: outputs/revealjs-netlify/` — ou o URL em `url_netlify`.
- PPTX **não** vai ao Netlify.

### 10 min — IA com contrato

- **Atividade 3 · Uma trava** (3 min, individual, sem teclado): escrever uma linha que faltou no prompt das 17h42. Três voluntários leem.
- Contraste com `03-relatorio-qmd/roteiro-ia-profissional.md`: a trava boa aponta para um arquivo (`CONTRATO.md`, o CSV), não para "seja preciso".
- Prompt profissional não substitui o contrato. Colar um dos prompts no modelo só se rede e relógio deixarem.

### 8 min — quiz, clone, URL

- Quiz das quatro perguntas (3 min, oral, em coro): cinco afirmações, todas caem. Voltar aos três verbos.
- Pacote: [https://github.com/patrick-andrade/prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte). Autópsia só depois do slop.
- Netlify é demo do professor; aluno não cria conta.
- Para casa: `lab-lacunas.qmd` (degrau 3) ou as cinco perguntas de interpretação no fim dele (degrau 2).
- Fechar: o campeonato não é o título em inglês; é o CSV que reroda. Três frases.

## Gordura (até 40 min; pular se houver debate)

Cada item abaixo é um slide com selo **se sobrar tempo** no deck:

- Rebuild ao vivo do CSV (`baixar_fm.py --offline`).
- Card do slop vs linha do CSV — agora a dívida também (abrir o arquivo, **não** ditar número).
- Chunks 2–3 de `03-relatorio-qmd/lab-lacunas.qmd` no projetor.
- Site Netlify no ar: [https://fiscal-monitor-2026.netlify.app](https://fiscal-monitor-2026.netlify.app).
- Slide r−g: o que "sustentável" exigiria (primário que estabiliza, r − g) **sem calcular número**.

## O que não cabe nestas 2 h

Paper, app Shinylive, conta Netlify da turma, incluir China "só para comparar", fase em R (RStudio existe no laboratório; o contrato mantém R como menção), laboratório completo de `lab-lacunas.qmd` (vira gordura / para casa).
