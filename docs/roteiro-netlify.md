# Publicar o Reveal.js no Netlify

Demo do **professor**. Alunos **não** criam conta. PPTX **não** se hospeda. Sem Shinylive neste contrato.

Artefato publicado = conteúdo de `outputs/revealjs-netlify/` (HTML Reveal.js gerado a partir de `03-relatorio-qmd/mini-fiscal-monitor.qmd`). O CSV-contrato já foi lido no render; o site não chama API.

Site ligado ao git: repositório [prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte), projeto Netlify `fiscal-monitor-2026`, owner `patrick-andrade`. Colar o URL de produção (`*.netlify.app`) em `params.url_netlify` no deck de aula depois do primeiro deploy verde.

## 1. Render local (projetor e conferência)

Na raiz `2026/`, com `uv` e Quarto no PATH:

```bash
uv sync --locked
uv run python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline
uv run python scripts/validar_contrato.py
uv run -- quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify
```

O `netlify.toml` declara `publish = "outputs/revealjs-netlify"`. O HTML de entrada deve ser `index.html` na raiz dessa pasta (o Quarto aninha a subpasta da fonte; `scripts/achatar_saidas.py` sobe o arquivo).

Não publique `outputs/pptx/`. Reunião interna fica no arquivo PowerPoint, não no site.

## 2. Caminho da aula: git → Netlify

O build remoto está em `scripts/netlify_build.sh` (instala `uv` + Quarto 1.9.37, `uv sync --locked`, render Reveal.js, achata a saída). Um `git push` em `main` dispara o deploy. Alunos só assistem o URL; não pedem login.

Enquanto o URL de produção não estiver no YAML do deck, projetar `outputs/revealjs-netlify/index.html`.

Drop avulso ([Netlify Drop](https://app.netlify.com/drop)) fica como plano B se o build da imagem falhar. Arrastar só `outputs/revealjs-netlify/`.

## 3. O que conferir no ar

- Título e vintage da edição (abril/2026), sem “dados recentes”.
- Cinco países; México como LatAm; **sem China**.
- Gráficos iguais aos do render local (são o mesmo HTML).
- Rodapé / método apontando para o CSV, não para uma API no browser.

## 4. Fora desta demo

- Conta Netlify da turma
- Token, `.env`, chave FMI
- Hospedar `outputs/pptx/`
- Publicar `outputs/aula-expositiva/`
- Tratar o slop (`01-demanda-simulada/entrega-slop/`) como site oficial
