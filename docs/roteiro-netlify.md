# Publicar o Reveal.js estático no Netlify

O projeto Netlify `fiscal-monitor-2026` publica **somente** `outputs/revealjs-netlify/index.html` do repositório [prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte). O HTML já está renderizado com `embed-resources: true` e versionado. O site não instala R, Python ou Quarto; `scripts/netlify_build.sh` apenas verifica que o arquivo existe.

## Antes do push

```bash
Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline
python scripts/validar_contrato.py
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify
```

Abrir `outputs/revealjs-netlify/index.html` sem rede e conferir todos os slides. Registrar o HTML no Git junto com o `.qmd`, o CSV e o contrato. `netlify.toml` usa `publish = "outputs/revealjs-netlify"` e um comando de checagem estática. O PPTX local e `outputs/aula-expositiva/` não entram no publish.

## Depois do push

1. Conferir o commit em `main` no GitHub e o deploy correspondente no painel Netlify.
2. Abrir [https://fiscal-monitor-2026.netlify.app](https://fiscal-monitor-2026.netlify.app) e recarregar a página.
3. Conferir capa, cinco países, vintage abril/2026, gráficos, slide de limites e crédito visual à OCDE.
4. Comparar o site com o `index.html` local. O navegador não deve buscar CSV ou API em tempo de execução.

Se o deploy não refletir o commit, guardar o identificador do deploy e revisar a ligação do site ao repositório. Não publicar o slop como produto. Os alunos apenas acessam a URL; não precisam de conta.
