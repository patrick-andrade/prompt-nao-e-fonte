# Checklist do instrutor (Onda 3)

Inspeção humana. Sem número fiscal neste arquivo. O agente fecha código e esqueleto; **você** fecha o projetor. Fonte da verdade: [`CONTRATO.md`](../CONTRATO.md) v1.2.

Marcar na ordem. Cortar gordura se o relógio apertar.

## Antes da aula

- [ ] `python scripts/validar_contrato.py` passa (esqueleto + CSV).
- [ ] Briefing, prompt do junior e slop abrem no navegador (UTF-8, acentos).
- [ ] Autópsia em `01-demanda-simulada/instrutor/autopsia.md` conferida **na mão** contra o CSV (não copiar número para o deck).
- [ ] Deck de aula renderizado: `quarto render aula/apresentacao-minicurso.qmd --to revealjs --output-dir outputs/aula-expositiva` e `python scripts/achatar_saidas.py` (HTML na raiz de `outputs/aula-expositiva/`).
- [ ] Produto Reveal.js e PPTX renderizados (`outputs/revealjs-netlify/`, `outputs/pptx/`).
- [ ] Zip regenerado (`python scripts/empacotar_aluno.py`); conferir **sem** `aula/` e **sem** `instrutor/autopsia.md`.
- [ ] URL Netlify colado em `url_netlify` no deck — ou o placeholder `COLE-APOS-O-DROP` ainda visível de propósito, com cue para `outputs/revealjs-netlify/` + [Netlify Drop](https://app.netlify.com/drop).
- [ ] Notas de palestrante visíveis no modo apresentador; slides de gordura com selo **se sobrar tempo**.

## Dimensão 1 — slop

- [ ] Briefing da Diretoria lido em voz alta (`01-demanda-simulada/briefing-supervisao.md`).
- [ ] Prompt do colega no projetor (`01-demanda-simulada/prompt-do-junior.md`).
- [ ] Slop 60 s em silêncio: `Abrir agora: 01-demanda-simulada/entrega-slop/index.html`.
- [ ] Autópsia **depois** do HTML, pelas quatro perguntas de [`checklist-rigor.md`](checklist-rigor.md).
- [ ] Acusações da autópsia batem com o CSV (sinal do primário, recorte, geografia) — conferência na mão, sem ditar número certo.

## Dimensão 2 — rotina

- [ ] `python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline`.
- [ ] `python scripts/validar_contrato.py` de novo.
- [ ] Dicionário aberto **sem** série numérica no markdown.
- [ ] CSV aberto: colunas na ordem do contrato; nenhum número copiado para o deck.

## Dimensão 3 — produto

- [ ] Reveal.js do briefing no projetor (local ou Netlify).
- [ ] PPTX existe em `outputs/pptx/` e **não** está no site.
- [ ] Um gráfico + tabela do ano-foco; tema slate / indigo / sky.
- [ ] Cinco países; México como LatAm; **sem China**; vintage no rodapé.
- [ ] Adjetivo “sustentável” ausente sem critério.

## Publicação

- [ ] Drop só de `outputs/revealjs-netlify/` (não o slop, não o PPTX, não `outputs/aula-expositiva/`).
- [ ] URL `*.netlify.app` conferido no ar (5 países, sem China, vintage).
- [ ] Mesmo URL colado no YAML `url_netlify` e deck rerenderizado, se o drop já existia.

## Aula (80 + 40)

- [ ] Núcleo cronometrado em 80 min.
- [ ] Abertura: vocês são o trainee; isto é o e-mail da Diretoria; isto é o prompt do colega.
- [ ] Cues `Abrir agora:` com caminho relativo (sem OneDrive, sem `file://`).
- [ ] Memes: rodapé de uso acadêmico visível; cortar os que não funcionarem.
- [ ] Gordura só se sobrar tempo (rebuild, card vs CSV, lab, Drop ao vivo, r−g, quiz).
- [ ] UTF-8 no projetor (acentos, travessão, iso3).

## Zip

- [ ] `aluno/minicurso-prompt-nao-e-fonte.zip` sem `aula/` e sem `instrutor/autopsia.md`.
