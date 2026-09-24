# Regras para agentes

Leia e honre [`CONTRATO.md`](CONTRATO.md) **v1.5** antes de alterar o minicurso. Ele é a fonte da verdade para países, indicadores, vintage, CSV, artefatos e publicação. Esta é a instrução de repositório para o Codex; `.cursor/rules/minicurso.mdc` é apenas a ponte para o Cursor.

- Escreva em português UTF-8. Não invente número fiscal, país, indicador, coluna, formato ou fonte. Números deliberadamente enganosos da Dimensão 1 precisam de lastro documentado na autópsia.
- CSV executivo: países na ordem `BRA`, `MEX`, `CHL`, `IND`, `IDN`; `CHN` e `COL` ficam fora. México pertence à LatAm, não à América do Sul. O painel tem derivado mundial separado, com economias individuais do catálogo FM, incluindo `CHN` e `COL` quando disponíveis; sem agregados.
- A Dimensão 1 não lê CSV fiscal. A rotina R da Dimensão 2 gera CSV executivo e derivado mundial de brutos congelados; consulta atual à API não os substitui. Python permanece alternativa para o executivo. O `.qmd` da Dimensão 3 só lê o CSV executivo e não chama API; o painel só lê o derivado mundial; o deck de aula não lê o CSV.
- Use `renv` para pacotes R e `pyproject.toml` + `uv sync --locked` / `uv run` para Python. Não instale dependências globalmente nem grave credenciais no repositório.
- PPTX em `outputs/pptx/`; o Netlify publica apenas a árvore `outputs/revealjs-netlify/`, com portal `index.html`, Reveal em `apresentacao/index.html` e painel em `painel/index.html`. `outputs/aula-expositiva/` fica fora do site.
- Cues no material: `Abrir agora: caminho/relativo`. Hiperlinks só para URLs públicos; nunca `file://` ou OneDrive. Abra a autópsia apenas depois do slop na aula.
- Mudanças de país, coluna, indicador, vintage ou formato exigem atualização explícita do contrato e de `scripts/validar_contrato.py`. A inspeção física no projetor permanece com o instrutor.
