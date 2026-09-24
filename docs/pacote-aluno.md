# Pacote do aluno

Canal principal: clone do [repositório público](https://github.com/patrick-andrade/prompt-nao-e-fonte), com contrato v1.5, brutos congelados, CSV executivo, derivado mundial, scripts, `.qmd`, docs e deck de aula. No curso, a autópsia em `01-demanda-simulada/instrutor/autopsia.html` só deve ser aberta **depois** do HTML simulado.

Na Atividade 2, leia `CONTRATO.md` e `scripts/validar_contrato.py`. Para executar o validador integralmente, use clone ou **Code → Download ZIP** do GitHub, ambos completos. Na raiz:

```bash
python scripts/validar_contrato.py
```

O zip opcional produzido por `python scripts/empacotar_aluno.py` omite `aula/`, `instrutor/` e saídas; serve para a leitura da Atividade 2 se o acesso ao clone falhar. Como o validador exige essas pastas, **não** use esse zip reduzido para executá-lo integralmente.

O pacote inclui `baixar_fm.R`, a rota alternativa `baixar_fm.py`, `renv.lock`, `pyproject.toml` e `uv.lock`. R/Quarto são usados pelo professor; o aluno precisa apenas de navegador, editor e Python básico. O [portal](https://fiscal-monitor-2026.netlify.app/) oferece a [apresentação](https://fiscal-monitor-2026.netlify.app/apresentacao/) e o [painel](https://fiscal-monitor-2026.netlify.app/painel/); os HTMLs também ficam no clone completo, mas não no zip opcional reduzido.
