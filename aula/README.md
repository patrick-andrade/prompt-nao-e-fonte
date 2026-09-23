# Deck de aula do instrutor

[`apresentacao-minicurso.qmd`](apresentacao-minicurso.qmd) organiza 80 minutos e até 40 minutos opcionais. Mostra e-mail, prompt, slop e **depois** autópsia; a demonstração principal usa R, e os alunos fazem validação simples em Python. A parte do site conduz portal → slides executivos → painel mundial por cerca de 7 minutos de exploração guiada. O deck não lê CSV e fica fora do Netlify.

```bash
quarto render aula/apresentacao-minicurso.qmd --profile aula --to revealjs
```

O HTML fica em `outputs/aula-expositiva/index.html` após o pós-render. Cues `Abrir agora:` são caminhos relativos ao clone. Hiperlinks levam apenas a URLs públicos. O YAML guarda a URL do [portal no Netlify](https://fiscal-monitor-2026.netlify.app/) e do [clone no GitHub](https://github.com/patrick-andrade/prompt-nao-e-fonte). A inspeção no projetor segue [`docs/checklist-instrutor.md`](../docs/checklist-instrutor.md).
