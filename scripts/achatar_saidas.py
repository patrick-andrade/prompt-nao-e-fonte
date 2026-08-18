#!/usr/bin/env python3
"""Sobe o HTML/PPTX que o Quarto aninha na subpasta da fonte para a raiz do output-dir.

O projeto tem fontes em subpasta; o publish Netlify, a reunião e o deck de aula
esperam o artefato na raiz de cada pasta de saída:

- outputs/revealjs-netlify/index.html  (aninhado: 03-relatorio-qmd/)
- outputs/pptx/*.pptx                  (aninhado: 03-relatorio-qmd/)
- outputs/aula-expositiva/index.html   (aninhado: aula/)
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALVOS = (
    (ROOT / "outputs" / "revealjs-netlify", "03-relatorio-qmd"),
    (ROOT / "outputs" / "pptx", "03-relatorio-qmd"),
    (ROOT / "outputs" / "aula-expositiva", "aula"),
)


def _utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass


def achatar(destino: Path, aninhada: str) -> None:
    origem = destino / aninhada
    if not origem.is_dir():
        return
    for item in origem.iterdir():
        alvo = destino / item.name
        if alvo.exists():
            if alvo.is_dir():
                shutil.rmtree(alvo)
            else:
                alvo.unlink()
        shutil.move(str(item), str(alvo))
    origem.rmdir()
    print(f"STATUS: achatado {origem.relative_to(ROOT).as_posix()} → {destino.relative_to(ROOT).as_posix()}")


def main() -> int:
    _utf8_stdio()
    for pasta, aninhada in ALVOS:
        achatar(pasta, aninhada)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
