# Pedido ao laboratório de informática

Minicurso *Prompt não é fonte*, Semana da Economia, manhã de **24/09/2026**. Solicitamos um teste com o login de aluno antes da aula.

## Máquinas dos alunos

- [ ] Navegador atualizado e VS Code com terminal integrado.
- [ ] Python 3.10+ acessível como `python` ou `py`.
- [ ] Permissão para clonar ou descompactar o [repositório público](https://github.com/patrick-andrade/prompt-nao-e-fonte) em uma pasta do usuário.
- [ ] Acesso HTTPS ao GitHub e a [fiscal-monitor-2026.netlify.app](https://fiscal-monitor-2026.netlify.app), se a política de rede permitir.
- [ ] Git é desejável; sem ele, **Code → Download ZIP** do repositório completo funciona.

Teste no clone completo, sem instalar bibliotecas:

```bash
python scripts/validar_contrato.py
```

Esperado: `STATUS: esqueleto OK (pastas + cláusulas v1.5 em CONTRATO.md).`, além da validação dos dados executivos e mundiais. A aula do aluno não exige R, Quarto, `uv`, acesso à API do FMI nem conta em serviço externo.

## Projetor e professor

- [ ] Projetor ao menos 1280×720; testar navegador em tela cheia, tamanho de fonte e acentos.
- [ ] Notebook do professor pode executar R e Quarto e abrir o PPTX local; portal, apresentação e painel públicos têm fallback nos HTMLs locais.

O professor leva o bruto e o CSV versionados, portanto a demonstração principal funciona sem DataMapper. O [checklist do instrutor](checklist-instrutor.md) cobre a inspeção de slides e do site.
