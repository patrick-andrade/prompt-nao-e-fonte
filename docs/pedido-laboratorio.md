# Pedido ao laboratório de informática

Checklist para enviar aos responsáveis pelo laboratório antes de **24/09/2026** (manhã). Minicurso *Prompt não é fonte*, Semana da Economia. Nada aqui exige conta paga, chave de API, instalação de biblioteca ou privilégio de administrador para o aluno.

## Obrigatório nas máquinas

- [ ] **VS Code** (já confirmado) — editor e terminal integrado.
- [ ] **Python 3.10 ou mais recente**, no PATH como `python` (ou `py`). Os scripts da aula usam só a biblioteca padrão; nenhum pacote adicional é necessário.
- [ ] Navegador atualizado (Chrome, Edge ou Firefox).
- [ ] Usuário comum consegue **criar pastas e arquivos** na área de trabalho ou em Documentos (para descompactar / clonar o repositório da aula, ~alguns MB).

## Desejável

- [ ] **Git** — para `git clone`. Sem git, a turma baixa o zip do GitHub (**Code → Download ZIP**); não é bloqueante.
- [ ] Saída HTTPS para `github.com` (baixar o repositório) e `fiscal-monitor-2026.netlify.app` (produto publicado, só leitura). Sem rede, o professor distribui o zip por pendrive e o produto é projetado da máquina do instrutor.

## Não é necessário

- Instalar `pandas`, `matplotlib`, `uv`, Quarto ou R.
- Acesso à API do FMI (`imf.org`): a aula usa dado já versionado no repositório.
- Conta em qualquer serviço.

Quem quiser ir além (exercício para casa) instala o `uv` no próprio perfil de usuário com `python scripts/preparar_lab.py`; isso pede saída HTTPS para `pypi.org` e `github.com` e permissão de gravar em `%APPDATA%` / `%LOCALAPPDATA%`. Se o laboratório puder liberar, ótimo; se não, é dever de casa.

## Projetor e sala

- [ ] Projetor com resolução mínima 1280×720; navegador em tela cheia.
- [ ] Máquina do instrutor com os mesmos itens acima (ou notebook próprio + cabo).

## Teste que resolve tudo (1 minuto)

Numa máquina do laboratório, logado como aluno:

```bash
git clone https://github.com/patrick-andrade/prompt-nao-e-fonte.git
cd prompt-nao-e-fonte
python scripts/validar_contrato.py
```

(Sem git: baixar o zip do GitHub, descompactar, abrir o terminal na pasta e rodar a última linha.)

Esperado:

```text
STATUS: esqueleto OK (pastas + cláusulas v1.2 em CONTRATO.md).
STATUS: CSV OK (02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv).
```

Se isso aparecer, a máquina está pronta para toda a aula. `python scripts/preparar_lab.py --verificar` mostra, sem instalar nada, o que mais a máquina tem (pip, git, uv).

Contato e material: [`requisitos-laboratorio.md`](requisitos-laboratorio.md), [`ferramentas.md`](ferramentas.md).
