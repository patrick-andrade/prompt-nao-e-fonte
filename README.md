# Prompt não é fonte · Semana da Economia 2026

Minicurso sobre análise fiscal, IA e reprodutibilidade. A turma compara uma apresentação visualmente convincente, mas descuidada das fontes, com outra que pode ser refeita a partir do mesmo CSV. A fonte da verdade é o [`CONTRATO.md`](CONTRATO.md) **v1.3**.

| Dimensão | Pasta | Produto |
| --- | --- | --- |
| 1 · demanda simulada | [`01-demanda-simulada/`](01-demanda-simulada/) | E-mail da gestora, prompt plausível, HTML com falhas sutis de fonte e autópsia |
| 2 · dados | [`02-dados-fiscal-monitor/`](02-dados-fiscal-monitor/) | R reconstrói o CSV congelado; Python é alternativa |
| 3 · apresentação | [`03-relatorio-qmd/`](03-relatorio-qmd/) | Um `.qmd` em R produz PPTX e Reveal.js a partir do CSV |

O roteiro do professor fica em [`aula/`](aula/). O produto público é o [Reveal.js no Netlify](https://fiscal-monitor-2026.netlify.app); a apresentação em PPTX fica em `outputs/pptx/`. O repositório da turma é [prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte).

## Reproduzir localmente

Na raiz do clone, com R, Quarto e Python disponíveis:

```bash
Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline
python scripts/validar_contrato.py
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx
quarto render aula/apresentacao-minicurso.qmd --profile aula --to revealjs
```

O professor fixa os pacotes R em [`renv.lock`](renv.lock); para preparar outra máquina, execute `Rscript -e 'source("renv/activate.R"); renv::restore(prompt=FALSE)'` antes do render. O `.Rprofile` usa a biblioteca local quando os pacotes centrais já estão restaurados. A rota Python usa `pyproject.toml` e `uv.lock`: `uv sync --locked` e `uv run python ...`. O script Python de validação usa só a biblioteca padrão e pode rodar com `python` do laboratório. O [`docs/requisitos-laboratorio.md`](docs/requisitos-laboratorio.md) explica os três níveis de participação.

`--offline` é o padrão das rotinas R e Python e usa dois JSONs recortados, versionados em `data/raw/`. `--consultar-api` inspeciona a API corrente e **não** regrava o cache de abril/2026, pois a função documentada não seleciona essa vintage. O `.qmd` lê apenas `fm_weo_cache.csv`; o render não chama a API.

O `index.html` do produto é autossuficiente e versionado em `outputs/revealjs-netlify/`. O Netlify publica esse arquivo estático; seu build apenas verifica que ele existe. O PPTX é saída local reproduzível. O deck da aula fica em `outputs/aula-expositiva/`, fora do Netlify.

Após renderizar os três artefatos, `python scripts/verificar_artefatos.py` confere a contagem de slides, recursos do HTML, nomes de arquivos e números do Brasil contra o CSV. A leitura visual no projetor permanece no checklist.

## Começar pela leitura

- [`docs/ferramentas.md`](docs/ferramentas.md): ferramentas, extensões e quem lê cada arquivo.
- [`docs/plano-aula-2h.md`](docs/plano-aula-2h.md): núcleo de 80 minutos e atividades opcionais.
- [`docs/checklist-instrutor.md`](docs/checklist-instrutor.md): inspeção final no projetor.
- [`docs/roteiro-netlify.md`](docs/roteiro-netlify.md): publicação do HTML estático.

Na aula, abrir o HTML simulado **antes** de [`01-demanda-simulada/instrutor/autopsia.md`](01-demanda-simulada/instrutor/autopsia.md).
