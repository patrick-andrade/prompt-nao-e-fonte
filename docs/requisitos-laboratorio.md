# Requisitos de laboratório

Máquina do aluno (Windows, macOS ou Linux). Sem conta Netlify. Sem chave de API.

## Obrigatório

- Python **3.11+**
- Git e editor (Cursor ou VS Code)
- Navegador para o HTML slop e para o Reveal.js
- Quarto CLI se o aluno for renderizar o `.qmd` (o professor renderiza na demo)

## Python do projeto

Na raiz `2026/`:

```bash
uv sync
python scripts/validar_contrato.py
python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline
```

`uv` é o caminho do contrato. Se a máquina da sala não tiver `uv`, `python` 3.11+ com as dependências do `pyproject.toml` resolve o validador e o `.qmd`. Não instalar pacote global “no feeling”.

Se o Quarto achar o Python do sistema sem Jupyter, na raiz:

```bash
export QUARTO_PYTHON=".venv/Scripts/python.exe"   # Windows
# export QUARTO_PYTHON=".venv/bin/python"         # macOS / Linux
```

## Rede

A aula **não depende** do DataMapper no horário do laboratório. O cache versionado (`data/raw/` + `fm_weo_cache.csv`) é a fonte do render. Download ao vivo é extra, para quem quiser ver a rotina abril/outubro.

## Não pedir ao aluno

- Conta no Netlify (demo do professor; ver [`roteiro-netlify.md`](roteiro-netlify.md))
- Token FMI, `.env`, scrape autenticado
- China no recorte
- Shinylive

## Acessibilidade mínima

UTF-8 em todos os arquivos. Projetor: o slop e o Reveal.js em tela cheia; o CSV em fonte grande só o suficiente para ver **colunas**, não para transcrever número.
