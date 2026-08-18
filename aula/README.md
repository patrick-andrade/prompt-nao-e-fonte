# Deck de aula (instrutor)

Fonte: `aula/apresentacao-minicurso.qmd`. Reveal.js, `lang: pt-BR`, tema reutilizado de `03-relatorio-qmd/tema-slate-indigo-sky.scss`. **Não** lê o CSV. **Não** entra no zip do aluno nem no Netlify.

Saída: `outputs/aula-expositiva/`.

```bash
quarto render aula/apresentacao-minicurso.qmd --to revealjs --output-dir outputs/aula-expositiva
python scripts/achatar_saidas.py
```

O Quarto aninha `aula/` no `--output-dir`; o script sobe o `index.html` para a raiz de `outputs/aula-expositiva/`. O `render:` padrão de `_quarto.yml` continua só o briefing da Dimensão 3.

URL do produto: YAML `params.url_netlify` (placeholder `COLE-APOS-O-DROP` até o drop). Cue de arquivo = caminho relativo (`Abrir agora:`). Hiperlink só para URL público.

Memes em `aula/imagens/`: uso acadêmico, sem fins comerciais, minicurso PUC.
