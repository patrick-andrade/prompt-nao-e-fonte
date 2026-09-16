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
import time
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


def _retry_fs(fn, *args, tries: int = 8, **kwargs):
    """OneDrive no Windows trava rmtree/unlink no meio do move do Quarto."""
    delay = 0.4
    last: OSError | None = None
    for _ in range(tries):
        try:
            return fn(*args, **kwargs)
        except OSError as exc:
            last = exc
            time.sleep(delay)
            delay = min(delay * 1.5, 3.0)
    assert last is not None
    raise last


def _chmod_writable(path: Path) -> None:
    try:
        path.chmod(path.stat().st_mode | 0o222)
    except OSError:
        pass


def _rmtree(path: Path) -> None:
    def onexc(func, p, _exc):
        _chmod_writable(Path(p))
        try:
            func(p)
        except OSError:
            pass

    shutil.rmtree(path, onexc=onexc)
    if path.exists():
        raise PermissionError(f"não removeu {path}")


def _remove(path: Path) -> None:
    if path.is_dir():
        _retry_fs(_rmtree, path)
    elif path.exists():
        _chmod_writable(path)
        _retry_fs(path.unlink)


def achatar(destino: Path, aninhada: str) -> None:
    origem = destino / aninhada
    if not origem.is_dir():
        return
    for item in origem.iterdir():
        alvo = destino / item.name
        if item.is_dir():
            if alvo.exists() and not alvo.is_dir():
                _remove(alvo)
            shutil.copytree(item, alvo, dirs_exist_ok=True)
        else:
            if alvo.exists() and alvo.is_dir():
                _remove(alvo)
            shutil.copy2(item, alvo)
    try:
        _remove(origem)
    except OSError as exc:
        print(
            f"AVISO: leftover {origem.relative_to(ROOT).as_posix()} ({exc}). "
            "O artefato na raiz do output-dir permanece válido.",
            file=sys.stderr,
        )
        return
    print(f"STATUS: achatado {origem.relative_to(ROOT).as_posix()} → {destino.relative_to(ROOT).as_posix()}")


def main() -> int:
    _utf8_stdio()
    for pasta, aninhada in ALVOS:
        achatar(pasta, aninhada)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
