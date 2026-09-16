# Pedido ao laboratório de informática

Checklist para enviar aos responsáveis pelo laboratório antes de **24/09/2026** (manhã). Minicurso *Prompt não é fonte*, Semana da Economia. Nada aqui exige conta paga, chave de API ou instalação por aluno: o que a turma precisa puxar em sala ela puxa sozinha, como exercício.

## Instalado nas máquinas (pedir)

- [ ] **VS Code** (já confirmado) — editor e terminal integrado.
- [ ] **Python 3.10 ou mais recente**, com `pip`, disponível no PATH como `python` (ou `py`). Serve para rodar o script de preparação; a versão exata do projeto (3.13) é baixada pelo `uv` para dentro da pasta do clone, sem afetar a máquina.
- [ ] **Git** — para `git clone`. Se não for possível, a turma baixa o zip do GitHub; não é bloqueante.
- [ ] Navegador atualizado (Chrome, Edge ou Firefox).

Não é necessário instalar: `uv`, pandas, matplotlib, Quarto, R. O `uv` é instalado pelo próprio aluno **no perfil do usuário** durante a aula; as bibliotecas ficam isoladas na pasta do projeto.

## Permissões (confirmar)

- [ ] Usuário sem privilégio de administrador consegue **gravar no próprio perfil** (`%APPDATA%`, `%LOCALAPPDATA%`, pasta de documentos). O `pip install --user` e o cache do `uv` escrevem ali.
- [ ] Usuário consegue **executar scripts Python e executáveis** baixados para o perfil (sem política que bloqueie `.exe` fora de `Program Files`).
- [ ] Criar pastas e arquivos dentro do clone (o `.venv` fica em `<clone>/.venv`).

## Rede (liberar saída HTTPS)

- [ ] `github.com` e `raw.githubusercontent.com` — clone / download do repositório e dos binários de Python que o `uv` usa (`github.com/astral-sh/python-build-standalone`).
- [ ] `pypi.org` e `files.pythonhosted.org` — `pip install --user uv` e dependências.
- [ ] `fiscal-monitor-2026.netlify.app` — produto publicado, só leitura.
- [ ] Proxy: se houver, que as variáveis `HTTPS_PROXY` / `HTTP_PROXY` estejam definidas para o usuário; `pip` e `uv` as respeitam.

Não é necessário liberar a API do FMI (`imf.org`): a aula usa o cache versionado no repositório.

## Projetor e sala

- [ ] Projetor com resolução mínima 1280×720; navegador em tela cheia.
- [ ] Uma máquina do instrutor com os mesmos itens acima (ou notebook próprio + cabo).

## Teste que resolve tudo

Numa máquina do laboratório, logado como aluno (sem admin):

```bash
git clone https://github.com/patrick-andrade/prompt-nao-e-fonte.git
cd prompt-nao-e-fonte
python scripts/preparar_lab.py
```

Se a última linha for `DEGRAU: 3`, a máquina está pronta. Se for `DEGRAU: 2`, a mensagem acima dela diz o que faltou (rede, pip, permissão) — e a aula funciona mesmo assim, só no editor. Um `python scripts/preparar_lab.py --verificar` mostra o que a máquina tem sem instalar nada.

Contato e material: [`requisitos-laboratorio.md`](requisitos-laboratorio.md), [`ferramentas.md`](ferramentas.md).
