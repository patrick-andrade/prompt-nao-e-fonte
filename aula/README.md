# Deck de aula (instrutor)

Fonte: `aula/apresentacao-minicurso.qmd`. Reveal.js, `lang: pt-BR`, tema reutilizado de `03-relatorio-qmd/tema-slate-indigo-sky.scss`. **Não** lê o CSV. HTML gerado **não** entra no Netlify.

Saída: `outputs/aula-expositiva/`.

```bash
uv run -- quarto render aula/apresentacao-minicurso.qmd --profile aula --to revealjs
```

O Quarto aninha `aula/` no `--output-dir`; o script sobe o `index.html` para a raiz de `outputs/aula-expositiva/`. O `render:` padrão de `_quarto.yml` continua só o produto da Dimensão 3.

URL do produto: YAML `params.url_netlify` ([https://fiscal-monitor-2026.netlify.app](https://fiscal-monitor-2026.netlify.app)). Pacote da turma: `params.url_github`. Cue de arquivo = caminho relativo (`Abrir agora:`). Hiperlink só para URL público.

Memes em `aula/imagens/`: uso acadêmico, sem fins comerciais, minicurso PUC.
