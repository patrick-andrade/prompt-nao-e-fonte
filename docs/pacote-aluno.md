# Pacote do aluno

Canal da turma: clone do repositório público [https://github.com/patrick-andrade/prompt-nao-e-fonte](https://github.com/patrick-andrade/prompt-nao-e-fonte). Sem conta Netlify. Sem chave de API.

A autópsia (`01-demanda-simulada/instrutor/autopsia.md`) **está no clone**. Na aula abre-se **depois** do slop. O deck de palco (`aula/`) também está no clone: é o projetor do professor, não o produto da Dimensão 3.

Zip opcional (máquina sem git): `uv run python scripts/empacotar_aluno.py` → `aluno/minicurso-prompt-nao-e-fonte.zip`. O zip **não** inclui `aula/` nem `instrutor/autopsia.md`.

## Entra no clone (e no zip, salvo nota)

- `README.md`, `CONTRATO.md` (v1.2), `AGENTS.md`
- `pyproject.toml`, `uv.lock`, `.python-version`, `_quarto.yml`
- `01-demanda-simulada/` — briefing, prompt do junior, `entrega-slop/`
  - no clone: também `instrutor/autopsia.md` (não abrir antes do slop)
  - no zip: **sem** `instrutor/`
- `02-dados-fiscal-monitor/`
  - scripts, dicionário, notas de vintage
  - `data/processed/fm_weo_cache.csv`
  - `data/raw/` recortado (cinco países; sem dump mundial)
- `03-relatorio-qmd/`
  - `mini-fiscal-monitor.qmd`, `lab-lacunas.qmd`, `roteiro-ia-profissional.md`
  - `tema-slate-indigo-sky.scss`, `template-referencia.pptx`
- `docs/plano-aula-2h.md`, `docs/requisitos-laboratorio.md`, `docs/ferramentas.md`, `docs/checklist-rigor.md`
- `scripts/validar_contrato.py`, `scripts/preparar_lab.py`, `scripts/achatar_saidas.py`
- `.vscode/tasks.json` (tarefas "Preparar laboratório" e "Validar contrato")
- `.cursor/rules/minicurso.mdc`

## Não entra no zip (e não se publica no Netlify)

- `aula/` (no clone sim; no zip não)
- `01-demanda-simulada/instrutor/autopsia.md` (no clone sim; no zip não)
- `docs/checklist-instrutor.md` (no zip não)
- Qualquer token, `.env`, credencial, `.venv`
- PPTX gerado, site Reveal.js do produto e HTML do deck (`outputs/`)
- `docs/roteiro-netlify.md` (no zip não)

## Comando de checagem (aluno)

```bash
git clone https://github.com/patrick-andrade/prompt-nao-e-fonte.git
cd prompt-nao-e-fonte
python scripts/validar_contrato.py
```

Esperado: `STATUS: esqueleto OK` e `STATUS: CSV OK`, com o Python do laboratório e nada instalado. Para casa, `python scripts/preparar_lab.py` monta o `.venv` (`uv`, `pandas`, `matplotlib`) para o lab de lacunas. Degraus e ferramentas: [`ferramentas.md`](ferramentas.md).

O zip opcional deste script **não** passa no validador de esqueleto (omite `aula/` e `instrutor/` de propósito). Para a Atividade 0 em máquina sem git, use o **Download ZIP do GitHub** (repositório completo).
