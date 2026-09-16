# Requisitos de laboratório

Máquina do aluno (Windows, macOS ou Linux). Sem conta Netlify. Sem chave de API. O que é cada ferramenta e cada extensão de arquivo: [`ferramentas.md`](ferramentas.md).

## Três degraus

Ninguém fica de fora por falta de instalação. Cada atividade da aula diz qual degrau basta.

| Degrau | Precisa de | Basta para |
| --- | --- | --- |
| 1 · navegador | Navegador | Ler briefing, prompt e CSV no GitHub; ver o produto no Netlify |
| 2 · VS Code + clone | VS Code (o laboratório tem) e a pasta do clone (git ou zip) | **Toda a aula**: abrir os arquivos, achar uma linha no CSV, ler o `.qmd` |
| 3 · `uv` | Um Python qualquer na máquina + rede | Rodar o validador, `baixar_fm.py --offline`, o lab de lacunas |

## Antes de quinta (opcional, 5 min)

Na máquina que você vai usar:

```bash
git clone https://github.com/patrick-andrade/prompt-nao-e-fonte.git
cd prompt-nao-e-fonte
python scripts/preparar_lab.py
```

Se não tiver git: no GitHub, `Code → Download ZIP`, descompactar e abrir a pasta no VS Code. O comando final é o mesmo.

`preparar_lab.py` roda com o Python que já existir (3.8+). Ele confere o clone, instala **só o executável** `uv` para o usuário se faltar (`pip install --user uv`), faz `uv sync --locked` (o `uv` baixa o Python 3.13 do projeto, isolado no `.venv` do clone) e roda o validador. Sem admin. Esperado no fim:

```text
STATUS: CSV OK (02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv).
DEGRAU: 3
```

Se imprimir `DEGRAU: 2`, a aula segue igual: você acompanha no VS Code. No VS Code, `Terminal → Run Build Task` roda o mesmo script; a tarefa `Validar contrato` roda só o validador.

## Obrigatório para o degrau 3

- Python **3.13+** gerenciado pelo `uv` (o `uv` baixa se não houver)
- Git e editor (VS Code ou Cursor); clone de [https://github.com/patrick-andrade/prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte)
- Navegador para o HTML slop e para o Reveal.js
- Quarto CLI só se o aluno for renderizar o `.qmd` (o professor renderiza na demo)

## Python do projeto

Na raiz do clone, o equivalente manual do `preparar_lab.py`:

```bash
uv sync --locked
uv run python scripts/validar_contrato.py
uv run python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline
```

`uv` é o caminho do contrato. Instalar apenas o executável `uv` por máquina; as dependências permanecem isoladas por projeto. Não instalar pacote global "no feeling".

Para confirmar que o Quarto encontrou o Python do projeto (só quem for renderizar):

```bash
uv run -- quarto check jupyter
```

## Rede

A aula **não depende** do DataMapper no horário do laboratório. O cache versionado (`data/raw/` + `fm_weo_cache.csv`) é a fonte do render. Download ao vivo é extra, para quem quiser ver a rotina abril/outubro.

O degrau 3 precisa de rede uma vez (baixar `uv`, Python 3.13 e as dependências). Sem rede, fica-se no degrau 2.

## Plano B só no navegador (degrau 1)

- CSV: abrir `02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv` no GitHub; a visualização mostra o arquivo como tabela com busca.
- Briefing, prompt do junior, contrato e `.qmd`: o GitHub renderiza o Markdown e mostra o código.
- Produto: [https://fiscal-monitor-2026.netlify.app](https://fiscal-monitor-2026.netlify.app).
- Slop: só no projetor (HTML não renderiza na visualização do GitHub).

## Não pedir ao aluno

- Conta no Netlify (demo do professor; ver [`roteiro-netlify.md`](roteiro-netlify.md))
- Zip obrigatório (o canal é o GitHub; zip só se a máquina não tiver git)
- Token FMI, `.env`, scrape autenticado
- China no recorte
- Shinylive
- Instalar R: RStudio existe no laboratório, mas o minicurso não o usa

## Acessibilidade mínima

UTF-8 em todos os arquivos. Projetor: o slop e o Reveal.js em tela cheia; o CSV em fonte grande só o suficiente para ver **colunas**, não para transcrever número.
