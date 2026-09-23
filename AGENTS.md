# Regras para agentes

Leia e honre [`CONTRATO.md`](CONTRATO.md) **v1.3** antes de alterar o minicurso. Ele é a fonte da verdade para países, indicadores, vintage, CSV, artefatos e publicação. Esta é a instrução de repositório para o Codex; `.cursor/rules/minicurso.mdc` é apenas a ponte para o Cursor.

- Escreva em português UTF-8. Não invente número fiscal, país, indicador, coluna, formato ou fonte. Números deliberadamente enganosos da Dimensão 1 precisam de lastro documentado na autópsia.
- Países na ordem `BRA`, `MEX`, `CHL`, `IND`, `IDN`; sem China. México pertence à LatAm, não à América do Sul.
- A Dimensão 1 não lê o CSV. A rotina R da Dimensão 2 gera o CSV de um bruto congelado; consulta atual à API não o substitui. Python permanece alternativa. O `.qmd` da Dimensão 3 só lê o CSV e não chama API; o deck de aula não lê o CSV.
- Use `renv` para pacotes R e `pyproject.toml` + `uv sync --locked` / `uv run` para Python. Não instale dependências globalmente nem grave credenciais no repositório.
- PPTX em `outputs/pptx/`; somente `outputs/revealjs-netlify/index.html` é publicado no Netlify. `outputs/aula-expositiva/` fica fora do site.
- Cues no material: `Abrir agora: caminho/relativo`. Hiperlinks só para URLs públicos; nunca `file://` ou OneDrive. Abra a autópsia apenas depois do slop na aula.
- Mudanças de país, coluna, indicador, vintage ou formato exigem atualização explícita do contrato e de `scripts/validar_contrato.py`. A inspeção física no projetor permanece com o instrutor.
