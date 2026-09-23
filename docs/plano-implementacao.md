# Registro de implementação · contrato v1.3

O projeto foi construído em três dimensões; a revisão v1.3 preserva o CSV contratado (cinco países, dois indicadores, nove colunas, anos 2000–2029 e abril/2026) e altera fluxo, apresentação e aula.

| Etapa | Estado no repositório | Evidência |
| --- | --- | --- |
| Estrutura | Três pastas de produto e infraestrutura sem número | `AGENTS.md`, `CONTRATO.md`, `scripts/validar_contrato.py` |
| Demanda simulada | E-mail visual, prompt plausível e HTML com falhas sutis de fonte | `01-demanda-simulada/` e matriz da autópsia |
| Dados | R offline principal; `imfapi` somente exploratório; Python alternativo | `baixar_fm.R`, `baixar_fm.py`, bruto e CSV versionados |
| Produto | `.qmd` R/knitr com PPTX e Reveal.js; referência visual OCDE creditada | `mini-fiscal-monitor.qmd`, template, tema, `outputs/revealjs-netlify/index.html` |
| Aula | 80 min + até 40 opcionais; slop antes da autópsia; R pelo professor, Python para validar | `aula/apresentacao-minicurso.qmd`, [`plano-aula-2h.md`](plano-aula-2h.md) |
| Publicação | Netlify serve só HTML pronto, sem instalação no build | `netlify.toml`, `scripts/netlify_build.sh`, [`roteiro-netlify.md`](roteiro-netlify.md) |

## Verificação reprodutível

```bash
Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline
python scripts/validar_contrato.py
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx
quarto render aula/apresentacao-minicurso.qmd --profile aula --to revealjs
python scripts/verificar_artefatos.py
```

Comparar o CSV reconstruído com o versionado, conferir o número de slides e abrir os dois formatos. Antes da aula, completar a inspeção em [`checklist-instrutor.md`](checklist-instrutor.md). Após a publicação, conferir commit no GitHub e versão ao vivo no Netlify. A inspeção em projetor continua sendo uma tarefa humana.

## Histórico breve

- **v1.1:** estrutura em três pastas numeradas.
- **v1.2:** deck de aula separado, cues relativos e inspeção humana.
- **v1.3:** R principal, Python alternativo, slop com fonte mal tratada, apresentação executiva com referência visual e HTML estático versionado.
