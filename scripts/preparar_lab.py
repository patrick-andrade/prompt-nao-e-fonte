#!/usr/bin/env python3
"""Prepara a máquina do laboratório para o degrau 3 (uv + validador).

Roda com o Python que já existir na máquina (3.8+), sem exigir `uv` no PATH:

    python scripts/preparar_lab.py

O que faz, nesta ordem:

1. Confere o clone (degrau 2): CONTRATO.md, pyproject.toml, uv.lock e o CSV-contrato.
2. Procura `uv` no PATH ou como módulo (`python -m uv`). Se faltar, instala só o
   executável para o usuário (`pip install --user uv`). Nenhuma dependência do
   projeto é instalada globalmente: elas ficam no `.venv` do clone.
3. `uv sync --locked` (baixa o Python 3.13 do projeto se a máquina não tiver).
4. `uv run python scripts/validar_contrato.py`.

Ao final imprime o degrau alcançado (1, 2 ou 3) e a próxima ação em uma linha.
Falha de rede ou de instalação não vira traceback: a aula segue no degrau 2.

Opções:
    --so-validar     pula instalação e sync; só roda o validador com o uv encontrado
    --sem-instalar   nunca tenta `pip install --user uv`

Códigos de saída: 0 = degrau 3; 2 = parou no degrau 2; 1 = clone incompleto.
Sem token, sem `.env`, sem credencial.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_REL = "02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv"
OBRIGATORIOS = ("CONTRATO.md", "pyproject.toml", "uv.lock", CSV_REL)
TIMEOUT_SYNC = 900  # s; primeiro sync baixa Python 3.13 + pandas + matplotlib


def _utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, OSError):
            pass


def _rodar(cmd: list[str], timeout: int = 300) -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env.setdefault("UV_LINK_MODE", "copy")  # evita aviso de hardlink em disco de rede
    env.setdefault("PYTHONIOENCODING", "utf-8")
    env.pop("VIRTUAL_ENV", None)  # o alvo é sempre o .venv do clone, não um venv ativo
    return subprocess.run(
        cmd,
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
    )


def _funciona(cmd: list[str]) -> bool:
    try:
        return _rodar(cmd + ["--version"], timeout=60).returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


def localizar_uv() -> list[str] | None:
    """Devolve o prefixo de comando do uv (`["uv"]` ou `[python, "-m", "uv"]`)."""
    exe = shutil.which("uv")
    if exe and _funciona([exe]):
        return [exe]
    modulo = [sys.executable, "-m", "uv"]
    if _funciona(modulo):
        return modulo
    return None


def instalar_uv() -> list[str] | None:
    print("uv ausente. Instalando só o executável para o usuário (pip install --user uv)…")
    try:
        r = _rodar(
            [sys.executable, "-m", "pip", "install", "--user", "--quiet", "uv"],
            timeout=600,
        )
    except (OSError, subprocess.TimeoutExpired) as e:
        print(f"  pip não respondeu: {e}")
        return None
    if r.returncode != 0:
        ultima = (r.stderr or r.stdout).strip().splitlines()[-1:] or ["sem detalhe"]
        print(f"  pip falhou: {ultima[0]}")
        return None
    return localizar_uv()


def degrau_2() -> bool:
    faltando = [rel for rel in OBRIGATORIOS if not (ROOT / rel).is_file()]
    if faltando:
        for rel in faltando:
            print(f"FALHA: ausente no clone: {rel}")
        return False
    return True


def sincronizar(uv: list[str]) -> bool:
    print("uv sync --locked (primeira vez pode levar alguns minutos)…")
    try:
        r = _rodar(uv + ["sync", "--locked"], timeout=TIMEOUT_SYNC)
    except subprocess.TimeoutExpired:
        print("  sync demorou demais (rede lenta?).")
        return False
    except OSError as e:
        print(f"  não foi possível executar o uv: {e}")
        return False
    if r.returncode != 0:
        ultima = (r.stderr or r.stdout).strip().splitlines()[-1:] or ["sem detalhe"]
        print(f"  sync falhou: {ultima[0]}")
        return False
    return True


def validar(uv: list[str]) -> bool:
    print("uv run python scripts/validar_contrato.py")
    try:
        r = _rodar(uv + ["run", "python", "scripts/validar_contrato.py"], timeout=300)
    except (OSError, subprocess.TimeoutExpired) as e:
        print(f"  validador não rodou: {e}")
        return False
    saida = (r.stdout or "") + (r.stderr or "")
    for linha in saida.strip().splitlines():
        print(f"  {linha}")
    return r.returncode == 0 and "CSV OK" in saida


def fechar(degrau: int, proximo: str) -> int:
    print()
    print(f"DEGRAU: {degrau}")
    print(f"PRÓXIMO: {proximo}")
    return {3: 0, 2: 2}.get(degrau, 1)


def main(argv: list[str]) -> int:
    _utf8_stdio()
    so_validar = "--so-validar" in argv
    sem_instalar = "--sem-instalar" in argv

    print(f"Raiz do clone: {ROOT}")
    print(f"Python em uso: {sys.executable} ({sys.version.split()[0]})")

    if not degrau_2():
        return fechar(
            1,
            "clone incompleto; refaça git clone https://github.com/patrick-andrade/prompt-nao-e-fonte",
        )
    print("Degrau 2 OK: contrato, pyproject, uv.lock e CSV-contrato presentes.")

    uv = localizar_uv()
    if uv is None and not (so_validar or sem_instalar):
        uv = instalar_uv()
    if uv is None:
        return fechar(
            2,
            "sem uv nesta máquina; abra os arquivos no VS Code e acompanhe pelo projetor "
            "(o CSV abre como texto).",
        )
    print(f"uv encontrado: {' '.join(uv)}")

    if not so_validar and not sincronizar(uv):
        return fechar(
            2,
            "sem rede para o sync; abra o CSV no VS Code e siga no degrau 2.",
        )

    if not validar(uv):
        return fechar(
            2,
            "validador não passou; confira a saída acima e siga no degrau 2.",
        )

    return fechar(
        3,
        "uv run python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline",
    )


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
