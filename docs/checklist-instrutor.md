# Checklist do instrutor (Onda 3)

Inspeção humana. Sem número fiscal neste arquivo. O agente fecha código e esqueleto; **você** fecha o projetor. Fonte da verdade: [`CONTRATO.md`](../CONTRATO.md) v1.2. Aula: **24/09/2026**, manhã.

Marcar na ordem. Cortar gordura se o relógio apertar.

## Antes da aula

- [ ] `uv run python scripts/validar_contrato.py` passa (esqueleto + CSV).
- [ ] Enviar [`pedido-laboratorio.md`](pedido-laboratorio.md) aos responsáveis pelo laboratório (VS Code, Python 3.10+ com pip, git, rede para GitHub/PyPI/Netlify, gravação no perfil do usuário). Guardar a resposta.
- [ ] Numa máquina do lab, logado como aluno **sem admin**, rodar `python scripts/preparar_lab.py` e anotar em que degrau para (`DEGRAU: 2` ou `3`). Isso decide se a Atividade 0 chega ao degrau 3 e se a Atividade 2 pede o validador.
- [ ] `.vscode/tasks.json` aparece em `Terminal → Run Build Task` numa máquina do lab.
- [ ] Briefing, prompt do junior e slop abrem no navegador (UTF-8, acentos).
- [ ] Autópsia em `01-demanda-simulada/instrutor/autopsia.md` conferida **na mão** contra o CSV (não copiar número para o deck).
- [ ] Deck de aula renderizado: `uv run -- quarto render aula/apresentacao-minicurso.qmd --profile aula --to revealjs` (HTML na raiz de `outputs/aula-expositiva/` após o pós-render automático).
- [ ] Produto Reveal.js e PPTX renderizados (`outputs/revealjs-netlify/`, `outputs/pptx/`).
- [ ] Repositório público [prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte) abre no navegador; zip opcional só se alguém estiver sem git.
- [x] URL Netlify de produção colado em `url_netlify` no deck: [https://fiscal-monitor-2026.netlify.app](https://fiscal-monitor-2026.netlify.app).
- [ ] Notas de palestrante visíveis no modo apresentador; slides de gordura com selo **se sobrar tempo**.

## Dimensão 1 — slop

- [ ] Briefing da Diretoria lido em voz alta (`01-demanda-simulada/briefing-supervisao.md`).
- [ ] Prompt do colega no projetor (`01-demanda-simulada/prompt-do-junior.md`).
- [ ] Slop 60 s em silêncio: `Abrir agora: 01-demanda-simulada/entrega-slop/index.html`.
- [ ] Autópsia **depois** do HTML, pelas quatro perguntas de [`checklist-rigor.md`](checklist-rigor.md).
- [ ] Acusações da autópsia batem com o CSV (sinal do primário, recorte, geografia) — conferência na mão, sem ditar número certo.

## Dimensão 2 — rotina

- [ ] `uv run python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline`.
- [ ] `uv run python scripts/validar_contrato.py` de novo.
- [ ] Dicionário aberto **sem** série numérica no markdown.
- [ ] CSV aberto: colunas na ordem do contrato; nenhum número copiado para o deck.

## Dimensão 3 — produto

- [ ] Reveal.js do **produto** no projetor (local ou Netlify).
- [ ] PPTX (briefing interno) existe em `outputs/pptx/` e **não** está no site.
- [ ] Um gráfico + tabela do ano-foco; tema slate / indigo / sky.
- [ ] Cinco países; México como LatAm; **sem China**; vintage no rodapé.
- [ ] Adjetivo “sustentável” ausente sem critério.

## Publicação

- [x] Site `fiscal-monitor-2026` ligado ao git; publish só de `outputs/revealjs-netlify/` (não o slop, não o PPTX, não `outputs/aula-expositiva/`).
- [x] URL [https://fiscal-monitor-2026.netlify.app](https://fiscal-monitor-2026.netlify.app) conferido no ar (5 países, sem China, vintage no rodapé).
- [x] Mesmo URL colado no YAML `url_netlify` e deck rerenderizado.

## Aula (80 + 40)

- [ ] Núcleo cronometrado em 80 min (5 + 7 + 18 + 6 + 13 + 13 + 10 + 8).
- [ ] Abertura: vocês são o trainee; isto é o e-mail da Diretoria; isto é o prompt do colega.
- [ ] "Antes de começar": três objetivos ditos em voz alta; slides de extensões apontados, não lidos; Atividade 0 (onboarding *as is*) disparada e deixada rodar em segundo plano — dizer em voz alta o que o laboratório forneceu e o que o projeto puxa.
- [ ] Atividade 1 (3 min, duplas): três duplas falam; nada de número certo.
- [ ] Atividade 2 (5 min): a turma acha `BRA` · 2025 · `GGXONLB_NGDP`; contar mãos (positivo / negativo) sem ditar valor.
- [ ] Atividade 3 (3 min): três voluntários leem a trava; ligar ao `CONTRATO.md`.
- [ ] Quiz no fecho, em coro; voltar aos três verbos.
- [ ] Cues `Abrir agora:` com caminho relativo (sem OneDrive, sem `file://`).
- [ ] Memes: rodapé de uso acadêmico visível; cortar os que não funcionarem.
- [ ] Gordura só se sobrar tempo (rebuild, card vs CSV, lab, site no ar, r−g).
- [ ] UTF-8 no projetor (acentos, travessão, iso3).

## Pacote

- [ ] Clone público no projetor; pedir para **não** abrir a autópsia antes do slop.
- [ ] Se gerar zip: `aluno/minicurso-prompt-nao-e-fonte.zip` sem `aula/` e sem `instrutor/autopsia.md` (inclui `scripts/preparar_lab.py`, `docs/ferramentas.md`, `.vscode/tasks.json`).
