# Pacote do aluno

O zip está em `aluno/minicurso-prompt-nao-e-fonte.zip`. Regenerar: `python scripts/empacotar_aluno.py`. A autópsia do instrutor **não** entra. O deck de aula (`aula/`) **não** entra.

## Entra

- `README.md`, `CONTRATO.md` (v1.2), `AGENTS.md`
- `pyproject.toml`, `uv.lock`, `_quarto.yml`
- `01-demanda-simulada/` **sem** `instrutor/`
  - briefing, prompt do junior, `entrega-slop/`
- `02-dados-fiscal-monitor/`
  - scripts, dicionário, notas de vintage
  - `data/processed/fm_weo_cache.csv`
  - `data/raw/` recortado (cinco países; sem dump mundial)
- `03-relatorio-qmd/`
  - `mini-fiscal-monitor.qmd`, `lab-lacunas.qmd`, `roteiro-ia-profissional.md`
  - `tema-slate-indigo-sky.scss`, `template-referencia.pptx`
- `docs/plano-aula-2h.md`, `docs/requisitos-laboratorio.md`, `docs/checklist-rigor.md`
- `scripts/validar_contrato.py`, `scripts/achatar_saidas.py`
- `.cursor/rules/minicurso.mdc`

## Não entra

- `01-demanda-simulada/instrutor/autopsia.md`
- `aula/` (deck de palco, memes e notas do professor)
- `docs/checklist-instrutor.md` (inspeção humana do professor)
- Qualquer token, `.env`, credencial, `.venv`
- PPTX gerado, site Reveal.js do produto e deck de aula (saídas em `outputs/`; o aluno gera o produto se tiver Quarto)
- `docs/roteiro-netlify.md` (demo do professor; aluno não cria conta)

## Comando de checagem (aluno)

```bash
python scripts/validar_contrato.py
```

Esperado: esqueleto OK **e** CSV OK.

## Zip

Nome: `aluno/minicurso-prompt-nao-e-fonte.zip`. Conferir que `instrutor/autopsia.md` e `aula/` não estão dentro.
