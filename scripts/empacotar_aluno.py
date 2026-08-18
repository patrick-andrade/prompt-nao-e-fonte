#!/usr/bin/env python3
"""Empacota o zip do aluno (sem autópsia nem deck de aula).

Uso (raiz 2026/):

    python scripts/empacotar_aluno.py
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESTINO = ROOT / "aluno" / "minicurso-prompt-nao-e-fonte.zip"

ARQUIVOS = [
    "README.md",
    "CONTRATO.md",
    "AGENTS.md",
    "pyproject.toml",
    "uv.lock",
    "_quarto.yml",
    "01-demanda-simulada/README.md",
    "01-demanda-simulada/briefing-supervisao.md",
    "01-demanda-simulada/prompt-do-junior.md",
    "01-demanda-simulada/entrega-slop/index.html",
    "02-dados-fiscal-monitor/README.md",
    "02-dados-fiscal-monitor/dicionario-indicadores.md",
    "02-dados-fiscal-monitor/notas-vintage-2026-04.md",
    "02-dados-fiscal-monitor/scripts/baixar_fm.py",
    "02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv",
    "02-dados-fiscal-monitor/data/raw/datamapper_GGXONLB_G01_GDP_PT.json",
    "02-dados-fiscal-monitor/data/raw/datamapper_G_XWDG_G01_GDP_PT.json",
    "03-relatorio-qmd/README.md",
    "03-relatorio-qmd/mini-fiscal-monitor.qmd",
    "03-relatorio-qmd/lab-lacunas.qmd",
    "03-relatorio-qmd/roteiro-ia-profissional.md",
    "03-relatorio-qmd/tema-slate-indigo-sky.scss",
    "03-relatorio-qmd/template-referencia.pptx",
    "docs/plano-aula-2h.md",
    "docs/requisitos-laboratorio.md",
    "docs/checklist-rigor.md",
    "scripts/validar_contrato.py",
    "scripts/achatar_saidas.py",
    ".cursor/rules/minicurso.mdc",
]

PROIBIDOS_NO_ZIP = (
    "instrutor/autopsia.md",
    "01-demanda-simulada/instrutor/",
    "aula/",
    "outputs/aula-expositiva/",
    ".venv/",
    ".env",
    "outputs/pptx/",
    "outputs/revealjs-netlify/",
)


def _utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass


def main() -> int:
    _utf8_stdio()
    faltando = [rel for rel in ARQUIVOS if not (ROOT / rel).is_file()]
    if faltando:
        for rel in faltando:
            print(f"FALHA: ausente para o zip: {rel}", file=sys.stderr)
        return 1

    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    if DESTINO.exists():
        DESTINO.unlink()

    with zipfile.ZipFile(DESTINO, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for rel in ARQUIVOS:
            zf.write(ROOT / rel, arcname=rel)

        internos = zf.namelist()
        for trecho in PROIBIDOS_NO_ZIP:
            hits = [n for n in internos if trecho.replace("\\", "/") in n.replace("\\", "/")]
            if hits:
                print(f"FALHA: zip contém trecho proibido {trecho}: {hits}", file=sys.stderr)
                return 1

    print(f"STATUS: zip em {DESTINO.relative_to(ROOT).as_posix()}")
    print(f"STATUS: {len(ARQUIVOS)} arquivos; sem instrutor/autopsia.md nem aula/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
