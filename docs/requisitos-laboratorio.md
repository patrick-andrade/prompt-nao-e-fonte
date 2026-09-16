# Requisitos de laboratório

Máquina do aluno (Windows, macOS ou Linux). Sem conta Netlify. Sem chave de API. Sem instalar biblioteca durante a aula. O que é cada ferramenta e cada extensão de arquivo: [`ferramentas.md`](ferramentas.md).

## Quem fornece o quê

| Camada | Quem | O quê |
| --- | --- | --- |
| Laboratório (antes da aula) | Responsáveis pelo lab — checklist em [`pedido-laboratorio.md`](pedido-laboratorio.md) | VS Code, Python 3.10+, navegador; git e saída para GitHub desejáveis |
| Repositório (em sala) | O clone / zip de [prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte) | Contrato, dado (`data/raw/` + CSV), scripts de biblioteca padrão, `.qmd`, docs |
| Projeto (para casa) | O aluno, com `python scripts/preparar_lab.py` | `uv` no perfil do usuário, Python 3.13 do projeto, `pandas`, `matplotlib` — isolados em `<clone>/.venv` |
| Professor | Máquina do instrutor | Quarto (render), Netlify (deploy), autópsia |

O "clone" é a cópia do repositório na máquina: `git clone` ou **Code → Download ZIP** no GitHub. Sem ele, o aluno só olha os arquivos pelo site (degrau 1).

## Três degraus

Ninguém fica de fora por falta de instalação. Cada atividade da aula diz qual degrau basta.

| Degrau | Precisa de | Basta para |
| --- | --- | --- |
| 1 · navegador | Navegador | Ler briefing, prompt e CSV no GitHub; ver o produto no Netlify |
| 2 · VS Code + clone | VS Code (o laboratório tem) e a pasta do clone (git ou zip) | Abrir os arquivos, achar uma linha no CSV, ler o `.qmd` e os scripts |
| 3 · Python do laboratório | Qualquer Python 3.10+ | Rodar `scripts/validar_contrato.py` e `baixar_fm.py --offline` — só biblioteca padrão. **Cobre toda a aula.** |

Para casa (não é degrau da aula): `python scripts/preparar_lab.py` monta o `.venv` com `pandas` / `matplotlib` para completar `03-relatorio-qmd/lab-lacunas.qmd`.

## Atividade 0 · onboarding (em sala, 3 min)

Regra da aula: **ler antes de rodar**. Primeiro abre-se `scripts/validar_contrato.py` no VS Code e lê-se o que ele checa; só então:

```bash
git clone https://github.com/patrick-andrade/prompt-nao-e-fonte.git
cd prompt-nao-e-fonte
python scripts/validar_contrato.py
```

Sem git: **Code → Download ZIP** no GitHub, descompactar, abrir a pasta no VS Code e rodar a última linha no terminal integrado (ou `Terminal → Run Build Task`). Esperado:

```text
STATUS: esqueleto OK (pastas + cláusulas v1.2 em CONTRATO.md).
STATUS: CSV OK (02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv).
```

`FALHA:` diz o que faltou. Nada foi instalado.

## Para casa · `preparar_lab.py`

Também com a regra "ler antes de rodar": o arquivo tem cabeçalho e funções nomeadas (`degrau_2`, `localizar_uv`, `instalar_uv`, `sincronizar`, `validar`, `fechar`). Ele roda com o Python que existir (3.8+), instala **só o executável** `uv` para o usuário se faltar (`pip install --user uv`), faz `uv sync --locked` (o `uv` baixa o Python 3.13 do projeto, isolado no `.venv` do clone) e roda o validador. Sem admin. Pede rede uma vez (PyPI, GitHub). Esperado no fim: `DEGRAU: 3`. `--verificar` só relata o que a máquina tem.

O equivalente manual, para quem já tem `uv`:

```bash
uv sync --locked
uv run python scripts/validar_contrato.py
```

`uv` é o caminho do contrato para o render. Instalar apenas o executável `uv` por máquina; as dependências permanecem isoladas por projeto. Não instalar pacote global "no feeling". Quarto só quem for renderizar o `.qmd`: `uv run -- quarto check jupyter`.

## Rede

A aula **não depende** do DataMapper no horário do laboratório. O cache versionado (`data/raw/` + `fm_weo_cache.csv`) é a fonte do render e do `--offline`. Download ao vivo é extra, para quem quiser ver a rotina abril/outubro.

## Plano B só no navegador (degrau 1)

- CSV: abrir `02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv` no GitHub; a visualização mostra o arquivo como tabela com busca.
- Briefing, prompt do junior, contrato, scripts e `.qmd`: o GitHub renderiza o Markdown e mostra o código.
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
