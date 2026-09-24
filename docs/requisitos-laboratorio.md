# Requisitos de laboratório

O aluno participa com navegador, VS Code e Python 3.10+; nenhuma biblioteca precisa ser instalada durante a aula. O professor usa R e Quarto em sua máquina para demonstrar a reconstrução e abrir as apresentações. O [pedido aos responsáveis pelo laboratório](pedido-laboratorio.md) contém o teste prático.

| Nível | Recursos | Ação |
| --- | --- | --- |
| Navegador | GitHub e Netlify | Ler briefing, prompt, CSV, slides e painel |
| Editor + clone | VS Code e cópia do repositório | Buscar país, ano, indicador e vintage |
| Python básico | Python 3.10+ | `python scripts/validar_contrato.py` |

Antes de executar, a turma abre o script e lê seu cabeçalho, constantes e checagens. O validador usa só a biblioteca padrão. Esperado no clone completo:

```text
STATUS: esqueleto OK (pastas + cláusulas v1.5 em CONTRATO.md).
STATUS: CSV OK (02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv).
```

O clone completo pode ser obtido por `git clone` ou **Code → Download ZIP** no GitHub. O zip opcional em `aluno/` exclui o deck e a autópsia; por isso não serve para a validação de esqueleto da Atividade 0.

Na máquina do professor: R com pacotes conforme `renv.lock`, Quarto, um navegador e acesso aos arquivos locais. O professor usa `baixar_fm.R --offline`, que não depende da rede, e prepara o painel mundial a partir do bruto congelado. A consulta `--consultar-api` é opcional e não altera o cache. O Netlify recebe os HTMLs já prontos.

Para casa, com `uv` instalado, o aluno pode executar `uv sync --locked` na raiz do clone para criar o `.venv` com o Python e os pacotes fixados pelo projeto. O laboratório de lacunas usa `pandas` e `matplotlib` desse ambiente; R e Quarto não são exigidos do aluno. Sem credenciais ou conta Netlify.
