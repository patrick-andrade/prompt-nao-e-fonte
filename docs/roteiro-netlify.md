# Publicar o Reveal.js no Netlify

Demo do **professor**. Alunos **não** criam conta. PPTX **não** se hospeda. Sem Shinylive neste contrato.

Artefato publicado = conteúdo de `outputs/revealjs-netlify/` (HTML Reveal.js gerado a partir de `03-relatorio-qmd/mini-fiscal-monitor.qmd`). O CSV-contrato já foi lido no render local; o site não chama API.

## 1. Render local (antes do drop)

Na raiz `2026/`, com o `.venv` do projeto e Quarto no PATH:

```bash
python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline
python scripts/validar_contrato.py
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify
```

O `netlify.toml` declara `publish = "outputs/revealjs-netlify"`. O HTML de entrada deve ser `index.html` na raiz dessa pasta (o Quarto aninha a subpasta da fonte; `scripts/achatar_saidas.py` sobe o arquivo). Leve também a pasta `*_files/` se o Quarto a gerar ao lado do HTML.

Não publique `outputs/pptx/`. Reunião interna fica no arquivo PowerPoint, não no site.

## 2. Caminho da aula: Netlify Drop

1. Abrir [Netlify Drop](https://app.netlify.com/drop) na conta **do professor**.
2. Arrastar a pasta `outputs/revealjs-netlify/` (ou o conteúdo dela, se o drop pedir os arquivos na raiz do site).
3. Esperar o URL `*.netlify.app`.
4. Projetar em tela cheia. Não pedir login aos alunos.

Se o Drop pedir autenticação, é da conta do professor — a turma só assiste o URL.

## 3. Caminho opcional: site ligado ao git

`netlify.toml` na raiz:

```toml
[build]
  publish = "outputs/revealjs-netlify"
  command = "quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify"
```

Só funciona se a imagem de build tiver **Quarto + Python** com pandas/matplotlib/ipykernel e o CSV versionado. A pasta `outputs/revealjs-netlify/` está no `.gitignore` (esqueleto via `.gitkeep`); por isso o Drop do artefato já renderizado é o caminho da demo de 2 horas.

Não ligar o repositório na conta de aluno. Não publicar o PPTX. Não publicar o HTML slop da Dimensão 1 como se fosse o produto.

## 4. O que conferir no ar

- Título e vintage da edição (abril/2026), sem “dados recentes”.
- Cinco países; México como LatAm; **sem China**.
- Gráficos iguais aos do render local (são o mesmo HTML).
- Rodapé / método apontando para o CSV, não para uma API no browser.

## 5. Fora desta demo

- Conta Netlify da turma
- Token, `.env`, chave FMI
- Hospedar `outputs/pptx/`
- Tratar o slop (`01-demanda-simulada/entrega-slop/`) como site oficial
