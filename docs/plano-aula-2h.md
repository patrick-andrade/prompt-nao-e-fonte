# Plano de aula — 80 min + gordura

Minicurso *Prompt não é fonte*. Público: graduação mista (calouro → formandos), laboratório. Núcleo **80 min** de propósito apertado; gordura **até 40 min** se a turma perguntar pouco. Sem números fiscais neste plano; eles só aparecem no CSV e no que o `.qmd` da Dimensão 3 lê. Números **do slop** podem aparecer no projetor porque são deliberadamente falsos.

Deck de palco (instrutor): `aula/apresentacao-minicurso.qmd` → `outputs/aula-expositiva/`. Não lê o CSV. Cue no slide: `Abrir agora:` + caminho relativo. Hiperlink só para URL público.

A Diretoria de Pesquisa Aplicada é a demanda realista (estágio / trainee / júnior). Vocês são o trainee; o briefing é o e-mail da chefia; o prompt do colega é o atalho preguiçoso.

## Objetivo

Sair da aula sabendo distinguir um HTML apresentável de uma rotina que se reroda: pergunta, indicador, fonte/vintage, artefato.

## Núcleo (80 min)

### 5 min — cartaz e cena

- Cartaz: “Wikipedia não é fonte” → “Prompt não é fonte”.
- “Vocês são o trainee.” Cena 17h42, reunião às 18h.
- As três dimensões em uma frase; ainda não abrir o contrato inteiro.

### 15 min — demanda, slop, autópsia

- Ler em voz alta o briefing da Diretoria (`01-demanda-simulada/briefing-supervisao.md`).
- Projetar o prompt do colega (`01-demanda-simulada/prompt-do-junior.md`).
- Abrir o slop. **60 segundos em silêncio.**
  - `Abrir agora: 01-demanda-simulada/entrega-slop/index.html`
- Autópsia pelas quatro perguntas (`docs/checklist-rigor.md`). Arquivo `instrutor/autopsia.md` **não** vai ao aluno; abrir **depois** do HTML.
- Transição: “o resultado bom não mora nesta pasta.”

### 8 min — contrato (sem ler o arquivo inteiro)

- Cinco países, dois códigos, vintage abril/2026.
- México = LatAm; China fora; Colômbia saiu (entrou o Chile).
- Calouros: governo geral ≠ central; primário ≠ nominal; vintage = edição, não “dados recentes”.
- `Abrir agora: CONTRATO.md` (só a tabela de recorte, se precisar).

### 12 min — rotina Python e CSV

- Pasta `02-dados-fiscal-monitor/`: dicionário (códigos, sem série) e notas de vintage.
- Caminho da aula: `baixar_fm.py --offline`.
- `python scripts/validar_contrato.py` — o CSV tem de passar, não só o esqueleto.
- Abrir o CSV: colunas na ordem do contrato. **Não** copiar número para o slide.

### 18 min — um `.qmd`, dois artefatos

- `03-relatorio-qmd/mini-fiscal-monitor.qmd` lê **somente** o CSV.
- Um gráfico + tabela do ano-foco no produto já renderizado (local ou Netlify).
- PPTX (reunião) e Reveal.js (navegador) saem do mesmo `.qmd`.
- `Abrir agora: outputs/revealjs-netlify/` — ou o URL em `url_netlify` se já houver drop.
- PPTX **não** vai ao Netlify.

### 12 min — dois prompts profissionais vs o junior

- Contraste com `03-relatorio-qmd/roteiro-ia-profissional.md`.
- Recolocar as quatro perguntas: `docs/checklist-rigor.md`.
- Prompt profissional não substitui o contrato.

### 10 min — zip, URL, o que levar

- Pacote: `aluno/minicurso-prompt-nao-e-fonte.zip` (sem autópsia, sem `aula/`).
- Netlify é demo do professor; aluno não cria conta.
- Fechar: o campeonato não é o título em inglês; é o CSV que reroda.

## Gordura (até 40 min; pular se houver debate)

Cada item abaixo é um slide com selo **se sobrar tempo** no deck:

- Rebuild ao vivo do CSV (`baixar_fm.py --offline`).
- Card do slop vs linha do CSV (abrir o arquivo, **não** ditar número).
- Chunks 2–3 de `03-relatorio-qmd/lab-lacunas.qmd` no projetor.
- Drop Netlify ao vivo ([Netlify Drop](https://app.netlify.com/drop)); colar o URL em `url_netlify`.
- Slide r−g: o que “sustentável” exigiria (primário que estabiliza, r − g) **sem calcular número**.
- Quiz das quatro perguntas.

## O que não cabe nestas 2 h

Paper, app Shinylive, conta Netlify da turma, incluir China “só para comparar”, laboratório completo de `lab-lacunas.qmd` (vira gordura / para casa).
