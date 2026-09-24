# Deck de aula do instrutor

[`apresentacao-minicurso.qmd`](apresentacao-minicurso.qmd) organiza 90 minutos de exposição, demonstrações e pequenas atividades, com 30 minutos de discussão e folga. Mostra e-mail, prompt, slop e **depois** autópsia; a demonstração principal usa R, e os alunos fazem validação simples em Python. A parte do site conduz portal → slides executivos → painel mundial por cerca de 7 minutos de exploração guiada. O caso também apresenta harness, documentação, Git, publicação e skills. Os quatro guias práticos do site de Patrick Andrade entram como leituras para depois, com aberturas breves durante a exposição. O deck não lê CSV e fica fora do Netlify.

```bash
uv run -- quarto render aula/apresentacao-minicurso.qmd --profile aula --to revealjs
```

O HTML fica em `outputs/aula-expositiva/index.html` após o pós-render. Tempos, orientações de condução e cues `Abrir agora:` ficam nas notas do apresentador, fora dos slides projetados. Os cues usam caminhos relativos ao clone. Hiperlinks levam apenas a URLs públicos. O YAML guarda a URL do [portal no Netlify](https://fiscal-monitor-2026.netlify.app/) e do [clone no GitHub](https://github.com/patrick-andrade/prompt-nao-e-fonte). A inspeção no projetor segue [`docs/checklist-instrutor.md`](../docs/checklist-instrutor.md).

A tipografia do deck usa Source Sans 3 de [Google Fonts](https://github.com/google/fonts/tree/main/ofl/sourcesans3), com arquivos locais e licença em `fontes/OFL.txt`. O meme Roll Safe vem do [template no Imgflip](https://imgflip.com/memetemplate/103240651/Roll-Safe-Black-Guy-Pointing-at-His-Head) e recebe crédito no slide.
