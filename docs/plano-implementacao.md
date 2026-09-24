# Registro de implementação · contrato v1.5

O projeto foi construído em três dimensões. A revisão v1.5 mantém o CSV executivo contratado (cinco países, dois indicadores, nove colunas, anos 2000–2029 e abril/2026), o derivado mundial, o portal e o painel; a autópsia do instrutor passa a ter fonte Quarto e saída HTML local.

| Etapa | Estado no repositório | Evidência |
| --- | --- | --- |
| Estrutura | Três pastas de produto e infraestrutura sem número | `AGENTS.md`, `CONTRATO.md`, `scripts/validar_contrato.py` |
| Demanda simulada | E-mail visual, prompt plausível e HTML com falhas sutis de fonte | `01-demanda-simulada/` e matriz da autópsia |
| Dados | R offline principal para os dois derivados; consulta `imfapi` somente exploratória; Python alternativo para o CSV executivo | `baixar_fm.R`, `gerar_painel.R`, brutos e derivados versionados |
| Produto | `.qmd` R/knitr com PPTX e Reveal.js executivo; novo tema de alto contraste | `mini-fiscal-monitor.qmd`, template, tema, `outputs/revealjs-netlify/apresentacao/index.html` |
| Painel | HTML estático, filtros no navegador e dados embutidos do derivado mundial | `site/`, `scripts/gerar_site.py`, `outputs/revealjs-netlify/painel/index.html` |
| Aula | 90 min de exposição + 30 de discussão e folga; arquivos, harness, Git, skills e comunicação integrados ao caso; slop antes da autópsia; 7 min de painel | `aula/apresentacao-minicurso.qmd`, [`plano-aula-2h.md`](plano-aula-2h.md) |
| Publicação | Portal, apresentação e painel já renderizados; sem instalação no build | `netlify.toml`, `scripts/netlify_build.sh`, [`roteiro-netlify.md`](roteiro-netlify.md) |

## Verificação reprodutível

```bash
Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline
Rscript 02-dados-fiscal-monitor/scripts/gerar_painel.R --offline
uv run python scripts/validar_contrato.py
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify/apresentacao
quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to pptx --output-dir outputs/pptx
uv run python scripts/gerar_site.py
quarto render aula/apresentacao-minicurso.qmd --profile aula --to revealjs
uv run python scripts/verificar_artefatos.py
```

Comparar os dois derivados reconstruídos com os versionados, conferir reconciliação dos cinco países, dados embutidos do painel, número de slides e os dois formatos do produto. Antes da aula, completar a inspeção em [`checklist-instrutor.md`](checklist-instrutor.md). Após a publicação, conferir commit no GitHub e as três rotas ao vivo no Netlify. A inspeção em projetor continua sendo uma tarefa humana.

## Histórico breve

- **v1.1:** estrutura em três pastas numeradas.
- **v1.2:** deck de aula separado, cues relativos e inspeção humana.
- **v1.3:** R principal, Python alternativo, slop com fonte mal tratada, apresentação executiva com referência visual e HTML estático versionado.
- **v1.5:** autópsia do instrutor em Quarto com HTML autossuficiente, fontes revisitadas e cues de aula atualizados; dados e Netlify preservados.
- **v1.4:** portal, Reveal executivo redesenhado, painel mundial estático e roteiro de aula atualizado; CSV executivo preservado.
