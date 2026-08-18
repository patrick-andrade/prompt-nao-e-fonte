# Plano de implementação



Alinhado ao as-built e ao [`CONTRATO.md`](../CONTRATO.md) v1.2. Raiz = `2026/`. Não inventar números fiscais neste plano.



## Onda 0 (feita)



Esta onda fecha o esqueleto e o realinhamento da árvore. Não implementa slop real, download nem análise.



Já construído:



- Três pastas numeradas de produto (`01-demanda-simulada/`, `02-dados-fiscal-monitor/`, `03-relatorio-qmd/`) e infraestrutura sem número (`docs/`, `scripts/`, `outputs/`, `aluno/`; `aula/` entra na Onda 3).

- `CONTRATO.md` v1.1 e `scripts/validar_contrato.py` (nesta onda o CSV ainda não existia: esqueleto OK, Dimensão 2 pendente, exit 0).

- Stubs: `02-dados-fiscal-monitor/scripts/baixar_fm.py`, `03-relatorio-qmd/mini-fiscal-monitor.qmd`, HTML slop placeholder, `lab-lacunas.qmd` e roteiro de IA como placeholder.

- `pyproject.toml` + `uv`; `_quarto.yml`; `netlify.toml` stub com `publish = "outputs/revealjs-netlify"`.

- Saídas da Dimensão 3 mapeadas: `outputs/pptx/` e `outputs/revealjs-netlify/` (com `.gitkeep`). Template PPTX (Onda 2) será entrada em `03-relatorio-qmd/`.

- Documentação de organização: [`arquitetura.md`](arquitetura.md), [`proposta-organizacao.md`](proposta-organizacao.md), este plano.



Validar:



```bash

python scripts/validar_contrato.py

```



## Onda 1 (feita)



Conteúdo didático e o CSV-contrato.



- Briefing da supervisão, prompt do junior, HTML slop e autópsia do instrutor (`01-demanda-simulada/`).

- Recorte FM abril/2026 em `data/raw/` e CSV-contrato em `data/processed/fm_weo_cache.csv` (script `baixar_fm.py`; aula usa `--offline` se o DataMapper responder 403).

- Dicionário de indicadores e notas de vintage (sem séries numéricas nos markdowns: os números só no CSV).

- `.qmd` lendo o CSV-contrato (sem chamar API no render de aula).

- Docs de aula: `plano-aula-2h.md`, requisitos de laboratório, checklist de rigor, pacote do aluno (lista; o zip sai na Onda 2).



Validar:



```bash

python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline

python scripts/validar_contrato.py

```



Esperado: esqueleto OK **e** CSV OK.



## Onda 2 (feita)



Produto final e publicação.



- Análise completa em `03-relatorio-qmd/mini-fiscal-monitor.qmd` (briefing interno; números só via código que lê o CSV).

- `lab-lacunas.qmd` e `roteiro-ia-profissional.md`.

- Template de referência PPTX em `03-relatorio-qmd/template-referencia.pptx` (entrada, paleta slate/indigo/sky; gerador: `scripts/gerar_template_pptx.py`).

- Render para as pastas de saída:



```bash

quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify

quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx

```



- Drop/publish Netlify (somente Reveal.js; demo do professor; ver [`roteiro-netlify.md`](roteiro-netlify.md)).

- Zip do aluno em `aluno/minicurso-prompt-nao-e-fonte.zip` (sem `instrutor/autopsia.md`; lista em [`pacote-aluno.md`](pacote-aluno.md)). Regenerar com `python scripts/empacotar_aluno.py`.
- O Quarto aninha a subpasta da fonte no `--output-dir`; `scripts/achatar_saidas.py` (post-render) deixa `index.html` e o PPTX na raiz de cada pasta de saída.

CONTRATO nesta onda ainda era **v1.1** (país, coluna e formato não mudaram). O bump v1.2 é da Onda 3 (aula + inspeção humana), sem mexer no schema.

## Onda 3 (código feito; inspeção humana pendente)

Deck de exposição, contrato v1.2 e o que **só você** fecha no projetor. Ondas 0–2 permanecem feitas (produto). Onda 3 = você no projetor.

Já no repositório:

- `CONTRATO.md` **v1.2**: pasta `aula/`, `aula/apresentacao-minicurso.qmd`, saída `outputs/aula-expositiva/` (fora do Netlify e do zip), cláusula de inspeção humana, Diretoria como demanda de estágio/trainee, cues = caminho relativo.
- Deck Reveal.js (núcleo 80 min + gordura; não lê o CSV; tema reutilizado de `03-relatorio-qmd/tema-slate-indigo-sky.scss`).
- [`plano-aula-2h.md`](plano-aula-2h.md) em 80+40; este plano; [`checklist-instrutor.md`](checklist-instrutor.md).
- Zip **sem** `aula/` e **sem** autópsia (`scripts/empacotar_aluno.py`).
- `scripts/achatar_saidas.py` também achata `aula/` aninhado em `outputs/aula-expositiva/`. `netlify.toml` **não** muda: publish continua `outputs/revealjs-netlify/`.

Render do deck (explícito; fora do `render:` padrão de `_quarto.yml`):

```bash
quarto render aula/apresentacao-minicurso.qmd --to revealjs --output-dir outputs/aula-expositiva
python scripts/achatar_saidas.py
```

O que o agente **não** fecha (marcar em [`checklist-instrutor.md`](checklist-instrutor.md)):

- Render local do briefing e contraste visual slop vs Reveal.js.
- Drop Netlify; colar o `*.netlify.app` em `url_netlify` no deck e rerenderizar.
- Assistir o deck como aluno: ritmo, memes (nota de uso acadêmico), cues `Abrir agora:`, simulação Diretoria → trainee.
- Conferir o zip na mão.
- Ajustes de texto/tom que só o professor decide.
- Cronometrar o núcleo de 80 min; cortar gordura/memes que não funcionarem; UTF-8 no projetor.

