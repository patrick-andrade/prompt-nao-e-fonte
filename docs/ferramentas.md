# Ferramentas, arquivos e degraus

Material de apoio do minicurso *Prompt não é fonte*. Para quem chega sem saber o que é `uv`, `.qmd` ou iso3. Sem número fiscal neste arquivo: números só no CSV-contrato. Fonte da verdade do produto: [`CONTRATO.md`](../CONTRATO.md) v1.2.

Você **não** precisa instalar tudo isto para acompanhar a aula. A tabela de degraus, no fim, diz o que basta.

## Ferramentas

| Ferramenta | O que é | Para que serve aqui | Quem usa | Como conferir | Plano B |
| --- | --- | --- | --- | --- | --- |
| Navegador | Chrome, Edge, Firefox | Ver o repositório no GitHub, o CSV como tabela e o produto publicado | Todos | Abrir [o repositório](https://github.com/patrick-andrade/prompt-nao-e-fonte) e [o produto](https://fiscal-monitor-2026.netlify.app) | — |
| GitHub | Site que hospeda o repositório público da turma | Clonar ou só ler os arquivos; o CSV abre como tabela na visualização web | Todos | O repositório abre sem login | Zip opcional (`aluno/`) se a máquina não tiver git |
| git | Controle de versão | `git clone` do repositório; o Netlify rebuilda a cada `push` do professor | Quem tiver instalado | `git --version` | Baixar o zip do GitHub ("Code → Download ZIP") |
| VS Code | Editor que o laboratório já tem | Abrir o clone; ler `.md`, `.csv`, `.py`, `.qmd`; terminal integrado; tarefas prontas em `.vscode/tasks.json` | Todos | Abrir a pasta do clone: `File → Open Folder` | Qualquer editor de texto |
| Python 3.13 | Linguagem dos scripts | Rodar `baixar_fm.py` e `validar_contrato.py` | Quem chegar ao degrau 3 | `uv` baixa o 3.13 do projeto se a máquina tiver outro Python | Acompanhar no degrau 2 |
| `uv` | Gerenciador de ambiente e dependências Python | `uv sync --locked` cria o `.venv` do clone com `pandas`, `matplotlib` etc., isolado da máquina | Quem chegar ao degrau 3 | `python scripts/preparar_lab.py` instala só o executável (`pip install --user uv`) se faltar | Acompanhar no degrau 2 |
| pandas / matplotlib | Bibliotecas Python de tabela e gráfico | O `.qmd` lê o CSV com pandas e desenha com matplotlib | O `.qmd`, o lab de lacunas | Ficam no `.venv`; nada global | — |
| Quarto | Compila `.qmd` (texto + código) em HTML, PPTX e outros | `mini-fiscal-monitor.qmd` → Reveal.js e PPTX; o deck de aula também | Professor, na demo | `uv run -- quarto check jupyter` | Aluno não precisa: o render já está no ar |
| Reveal.js | Slides em HTML para o navegador | Formato do produto publicado e do deck de aula | Todos veem; professor gera | Abrir o URL do produto | HTML local em `outputs/revealjs-netlify/` |
| PowerPoint (`.pptx`) | Apresentação de escritório | Briefing interno da reunião, gerado pelo mesmo `.qmd` | Diretoria (ficção) e professor | `outputs/pptx/` depois do render | Não se hospeda; não é para o aluno |
| Netlify | Hospedagem de sites estáticos ligada ao git | Publica **só** o Reveal.js do produto (`outputs/revealjs-netlify/`) | Professor | URL público do produto | HTML local |
| DataMapper (FMI) | API pública de onde vem o Fiscal Monitor / WEO | Só `02-dados-fiscal-monitor/scripts/baixar_fm.py` fala com ela; na aula usamos o cache (`--offline`) | Ninguém na aula | `data/raw/` tem o recorte já baixado | O cache é o plano A |
| R / RStudio | Ecossistema irmão do Python para dados | Menção. O laboratório tem RStudio; este minicurso não usa | — | — | — |

Ninguém cria conta em nada. Sem token, sem `.env`, sem chave de API.

## Extensões de arquivo

A extensão diz **o que o arquivo é** e, por consequência, **quem consegue lê-lo**.

| Extensão | O que é | Quem lê | Exemplo no clone |
| --- | --- | --- | --- |
| `.md` (Markdown) | Texto legível com marcação leve (`#` título, `**negrito**`, tabelas) | Pessoas, o GitHub (renderiza), o Quarto e **ferramentas de IA**, que tratam `README.md`, `AGENTS.md` e `CONTRATO.md` como referência e regra | `README.md`, `CONTRATO.md`, `AGENTS.md`, `01-demanda-simulada/briefing-supervisao.md` |
| `.py` | Script Python | O interpretador Python executa; pessoas e IA leem e escrevem | `02-dados-fiscal-monitor/scripts/baixar_fm.py`, `scripts/validar_contrato.py`, `scripts/preparar_lab.py` |
| `.csv` | Tabela em texto puro, uma linha por registro, colunas separadas por vírgula | Python (pandas), planilhas, o GitHub (como tabela), qualquer editor. **Única fonte de número** deste minicurso | `02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv` |
| `.qmd` (Quarto) | Markdown com blocos de código (chunks) que rodam no render | O Quarto renderiza; pessoas e IA leem e escrevem | `03-relatorio-qmd/mini-fiscal-monitor.qmd`, `03-relatorio-qmd/lab-lacunas.qmd`, `aula/apresentacao-minicurso.qmd` |
| `.html` | Página para o navegador | O navegador exibe. É **saída**, nunca fonte de número | `01-demanda-simulada/entrega-slop/index.html` (o slop); o Reveal.js em `outputs/` |
| `.pptx` | PowerPoint | PowerPoint / LibreOffice | `outputs/pptx/` (gerado; não versionado) |
| `.toml` | Configuração legível | `uv` lê `pyproject.toml` (dependências), Netlify lê `netlify.toml` | `pyproject.toml`, `netlify.toml` |
| `.yml` / `.yaml` | Configuração legível | Quarto lê `_quarto.yml`; o cabeçalho dos `.qmd` também é YAML | `_quarto.yml`, `_quarto-aula.yml` |
| `.lock` | Versões exatas das dependências, geradas pela ferramenta | `uv` (`uv sync --locked` exige que bata com o `pyproject.toml`) | `uv.lock` |
| `.json` | Dado estruturado em texto (chaves e valores) | Python, navegador; é como a API devolve o dado bruto | `02-dados-fiscal-monitor/data/raw/*.json`, `.vscode/tasks.json` |
| `.scss` / `.css` | Aparência (cores, fontes) | Quarto compila o `.scss`; o navegador aplica o `.css` | `03-relatorio-qmd/tema-slate-indigo-sky.scss`, `aula/estilos-aula.css` |
| `.mdc` | Regra para o agente de IA do Cursor (Markdown com cabeçalho) | Ferramenta de IA | `.cursor/rules/minicurso.mdc` |

### Quem lê o quê

| Arquivo | Humano | Python | Quarto | Navegador | Ferramenta de IA |
| --- | --- | --- | --- | --- | --- |
| `.md` | lê | — | lê como texto | via GitHub | **lê como referência e regra** |
| `.csv` | lê | **lê** (pandas) | via Python no chunk | via GitHub, como tabela | só se você anexar; não "lembra" o número |
| `.py` | lê | **executa** | executa no chunk | — | lê e escreve |
| `.qmd` | lê | — | **renderiza** | — | lê e escreve |
| `.html` | — | — | gera | **exibe** | — |

O chat **não** está nesta tabela como fonte. O `.md` diz ao modelo o que ele **pode** fazer (país, coluna, vintage, o que não inventar); o `.csv` diz **qual** número existe. Por isso `CONTRATO.md` e `AGENTS.md` não contêm nenhum número fiscal.

## Três degraus de participação

Cada atividade da aula diz qual degrau basta. Ninguém fica de fora por falta de instalação.

| Degrau | O que você tem | O que consegue fazer | Como chegar |
| --- | --- | --- | --- |
| 1 · navegador | Só um navegador | Ler o briefing, o prompt e o CSV no GitHub; ver o produto no Netlify | Abrir [o repositório](https://github.com/patrick-andrade/prompt-nao-e-fonte) |
| 2 · VS Code + clone | VS Code com a pasta do clone aberta | Tudo do degrau 1 **e** abrir os arquivos localmente, procurar uma linha no CSV, ler o `.qmd`. **Basta para toda a aula.** | `git clone` (ou zip) e `File → Open Folder` |
| 3 · `uv` | `.venv` do projeto sincronizado | Rodar o validador, `baixar_fm.py --offline`, completar `lab-lacunas.qmd` | No terminal do VS Code: `python scripts/preparar_lab.py` (ou `Terminal → Run Build Task`) |

O que `scripts/preparar_lab.py` faz: confere o clone; procura `uv`; se faltar, instala só o executável para o usuário; `uv sync --locked`; roda o validador; imprime `DEGRAU: 2` ou `DEGRAU: 3` e a próxima ação. Sem admin. Se a rede falhar, a mensagem diz para ficar no degrau 2 — sem traceback.

## Glossário

- **CSV-contrato:** o único arquivo de número do minicurso, `02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv`, com as colunas e países fixados em `CONTRATO.md`.
- **iso3:** código de três letras por país (`BRA`, `MEX`, `CHL`, `IND`, `IDN`). Evita ambiguidade de nome e ordem.
- **Código do indicador:** identificador da série (`GGXWDG_NGDP` = dívida bruta do governo geral, % do PIB; `GGXONLB_NGDP` = saldo primário do governo geral, % do PIB). Ver `02-dados-fiscal-monitor/dicionario-indicadores.md`.
- **Vintage:** a edição da publicação (aqui, Fiscal Monitor / WEO abril/2026). "Dados recentes" não é vintage.
- **Governo geral:** cobertura que inclui governo central, estados e municípios (e, conforme o país, mais). Não é o mesmo que governo central.
- **Saldo primário:** resultado fiscal antes dos juros. Positivo = superávit primário; negativo = déficit primário.
- **Projeção:** anos à frente da vintage são estimativa da equipe do FMI, não realizado. O gráfico marca o ano da vintage com linha tracejada.
- **Render:** o Quarto executar o `.qmd` e gerar HTML / PPTX. O render do produto lê o CSV; não chama API.
- **Cache / `--offline`:** reconstruir o CSV a partir do JSON já baixado em `data/raw/`, sem rede.
- **Slop:** saída bonita e imprecisa de um prompt preguiçoso. O HTML de `01-demanda-simulada/entrega-slop/` é slop de propósito.
- **Validador:** `scripts/validar_contrato.py`; confere pastas, cláusulas do contrato e o schema do CSV. Esperado: `STATUS: esqueleto OK` e `STATUS: CSV OK`.

## Ver também

- [`requisitos-laboratorio.md`](requisitos-laboratorio.md) — o que a máquina precisa, por degrau.
- [`checklist-rigor.md`](checklist-rigor.md) — as quatro perguntas.
- [`plano-aula-2h.md`](plano-aula-2h.md) — grade dos 80 min e atividades.
