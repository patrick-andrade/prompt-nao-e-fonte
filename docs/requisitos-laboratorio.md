# Requisitos de laboratório

Máquina do aluno (Windows, macOS ou Linux). Sem conta Netlify. Sem chave de API.

## Obrigatório

- Python **3.13+** gerenciado pelo `uv`
- Git e editor (Cursor ou VS Code); clone de [https://github.com/patrick-andrade/prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte)
- Navegador para o HTML slop e para o Reveal.js
- Quarto CLI se o aluno for renderizar o `.qmd` (o professor renderiza na demo)

## Python do projeto

Na raiz do clone:

```bash
git clone https://github.com/patrick-andrade/prompt-nao-e-fonte.git
cd prompt-nao-e-fonte
uv sync --locked
uv run python scripts/validar_contrato.py
uv run python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline
```

`uv` é o caminho do contrato. Instalar apenas o executável `uv` por máquina; as dependências permanecem isoladas por projeto. Não instalar pacote global “no feeling”.

Para confirmar que o Quarto encontrou o Python do projeto:

```bash
uv run -- quarto check jupyter
```

## Rede

A aula **não depende** do DataMapper no horário do laboratório. O cache versionado (`data/raw/` + `fm_weo_cache.csv`) é a fonte do render. Download ao vivo é extra, para quem quiser ver a rotina abril/outubro.

## Não pedir ao aluno

- Conta no Netlify (demo do professor; ver [`roteiro-netlify.md`](roteiro-netlify.md))
- Zip obrigatório (o canal é o GitHub; zip só se a máquina não tiver git)
- Token FMI, `.env`, scrape autenticado
- China no recorte
- Shinylive

## Acessibilidade mínima

UTF-8 em todos os arquivos. Projetor: o slop e o Reveal.js em tela cheia; o CSV em fonte grande só o suficiente para ver **colunas**, não para transcrever número.
