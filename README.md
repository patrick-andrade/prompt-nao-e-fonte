# Prompt não é fonte · Semana da Economia 2026

Minicurso sobre exploração e comunicação de projetos com IA, com uma análise de economia aplicada como caso. O percurso apresenta arquivos, documentação, versionamento e procedimentos para conferir e reproduzir resultados. A turma compara uma apresentação visualmente convincente, mas descuidada das fontes, com outra que pode ser refeita a partir de dados congelados. A fonte da verdade é o [`CONTRATO.md`](CONTRATO.md) **v1.5**.

| Dimensão | Pasta | Produto |
| --- | --- | --- |
| 1 · demanda simulada | [`01-demanda-simulada/`](01-demanda-simulada/) | E-mail da gestora, prompt plausível, HTML com falhas sutis de fonte e autópsia |
| 2 · dados | [`02-dados-fiscal-monitor/`](02-dados-fiscal-monitor/) | R reconstrói o CSV executivo e o derivado mundial de brutos congelados; Python é alternativa para o primeiro |
| 3 · apresentação | [`03-relatorio-qmd/`](03-relatorio-qmd/) | Um `.qmd` em R produz PPTX e Reveal.js a partir do CSV |

O roteiro do professor fica em [`aula/`](aula/). O [portal no Netlify](https://fiscal-monitor-2026.netlify.app/) abre o [Reveal.js executivo](https://fiscal-monitor-2026.netlify.app/apresentacao/) e o [painel mundial](https://fiscal-monitor-2026.netlify.app/painel/); a apresentação em PPTX fica em `outputs/pptx/`. O repositório da turma é [prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte).

## Reproduzir localmente

Na raiz do clone, com R, Quarto e Python disponíveis:

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

O professor fixa os pacotes R em [`renv.lock`](renv.lock); para preparar outra máquina, execute `Rscript -e 'source("renv/activate.R"); renv::restore(prompt=FALSE)'` antes do render. O `.Rprofile` usa a biblioteca local quando os pacotes centrais já estão restaurados. A rota Python usa `pyproject.toml` e `uv.lock`: `uv sync --locked` e `uv run python ...`. O script Python de validação usa só a biblioteca padrão e pode rodar com `python` do laboratório. O [`docs/requisitos-laboratorio.md`](docs/requisitos-laboratorio.md) explica os três níveis de participação.

`--offline` é o padrão das rotinas R: o CSV executivo usa dois JSONs recortados; o painel usa dois JSONs mundiais e o cadastro de economias do DataMapper FM, todos congelados em `data/raw/`. São 194 economias com ao menos uma observação dos dois indicadores entre 2000 e 2029; nem toda economia tem valor em todo ano. `--consultar-api` inspeciona a API corrente e **não** regrava o cache de abril/2026. O `.qmd` lê apenas `fm_weo_cache.csv`; o render e o navegador não chamam a API.

O portal, a apresentação e o painel são HTMLs autossuficientes e versionados em `outputs/revealjs-netlify/`. O Netlify publica esse diretório; seu build apenas verifica os três arquivos. O PPTX é saída local reproduzível. O deck da aula fica em `outputs/aula-expositiva/`, fora do Netlify.

Após renderizar os artefatos, `uv run python scripts/verificar_artefatos.py` confere recursos dos três HTMLs, dados embutidos do painel contra o CSV mundial, contagem de slides e números do Brasil no PPTX contra o CSV executivo. A leitura visual no projetor permanece no checklist.

## Começar pela leitura

- [`docs/ferramentas.md`](docs/ferramentas.md): ferramentas, extensões e quem lê cada arquivo.
- [Guias práticos de Patrick Andrade](https://patrick-andrade.github.io/guias.html): Codex, Git e GitHub, Quarto e skills, para leitura depois da aula.
- [`docs/plano-aula-2h.md`](docs/plano-aula-2h.md): 90 minutos de exposição e 30 minutos de discussão e folga.
- [`docs/checklist-instrutor.md`](docs/checklist-instrutor.md): inspeção final no projetor.
- [`docs/roteiro-netlify.md`](docs/roteiro-netlify.md): publicação do HTML estático.

Na aula, abrir o HTML simulado **antes** da [autópsia do instrutor](01-demanda-simulada/instrutor/autopsia.html), gerada de `01-demanda-simulada/instrutor/autopsia.qmd`.
