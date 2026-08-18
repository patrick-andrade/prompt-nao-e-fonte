# Regras para agentes

Honrar [`CONTRATO.md`](CONTRATO.md) **v1.2**. Não inventar país, coluna, indicador, vintage, formato nem número.

A raiz do minicurso é esta pasta (`2026/`). Pastas de infraestrutura (`docs/`, `scripts/`, `outputs/`, `aluno/`, `aula/`) **não** ganham prefixo numérico.

## Obrigatório

- UTF-8 e acentuação em português.
- Sem tokens, chaves, senhas ou credenciais em arquivos, configs ou relatórios.
- Python do projeto: `pyproject.toml` + `uv`. Não instalar dependências globalmente.
- Países na ordem canônica: `BRA`, `MEX`, `CHL`, `IND`, `IDN`.
- **Sem China** (`CHN` fora). México é LatAm, não América do Sul, no material.
- Não inventar número fiscal do Brasil nem dos outros países. Só cache, API ou PDF extraído com `doc_extract` (recorte, não o Fiscal Monitor inteiro no contexto). Números do slop podem aparecer no deck de aula porque são deliberadamente falsos e estão no HTML.
- Cue de arquivo = caminho relativo no repositório (`Abrir agora: …`). Hiperlink só para URL público. Sem `file://`, sem OneDrive.
- A Diretoria de Pesquisa Aplicada é a demanda realista (estágio / trainee / júnior), não um tom a substituir no produto da Dimensão 3.

## Dimensões

- **Slop (Dimensão 1, `01-demanda-simulada/`):** não lê `fm_weo_cache.csv`. HTML ilustrativo e impreciso de propósito.
- **Scripts (Dimensão 2, `02-dados-fiscal-monitor/`):** único lugar que baixa FM/WEO abril/2026 e grava o CSV-contrato.
- **Quarto (Dimensão 3, `03-relatorio-qmd/`):** só lê o CSV-contrato. Sem número inventado; render de aula não chama API. PPTX → `outputs/pptx/`; Reveal.js → `outputs/revealjs-netlify/`. Template PPTX é entrada em `03-relatorio-qmd/`.
- **Aula (infraestrutura, `aula/`):** `apresentacao-minicurso.qmd` não lê o CSV. Saída `outputs/aula-expositiva/`. Fora do zip e **fora** do Netlify.
- **Netlify:** somente o artefato Reveal.js em `outputs/revealjs-netlify/`. PPTX não se hospeda. Sem Shinylive neste contrato.

## Mudança de contrato

País, coluna ou formato novos = bump para **v1.3** em `CONTRATO.md` e em `scripts/validar_contrato.py`. Não ajustar no feeling.

## Onda atual

Ondas 0–2 feitas (produto). Onda 3 = inspeção humana no projetor (deck de aula, URL Netlify, zip, memes). CONTRATO **v1.2**. Ver [`docs/plano-implementacao.md`](docs/plano-implementacao.md) e [`docs/checklist-instrutor.md`](docs/checklist-instrutor.md).
