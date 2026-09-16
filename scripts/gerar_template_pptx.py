#!/usr/bin/env python3
"""Gera o template de referência PPTX (entrada da Dimensão 3).

Paleta slate / indigo / sky. Não contém números fiscais.
Uso (raiz 2026/):

    uv run python scripts/gerar_template_pptx.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DESTINO = ROOT / "03-relatorio-qmd" / "template-referencia.pptx"

A = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS = {"a": A}

# Office theme: dk/lt + 6 accents + hyperlinks
SCHEME = {
    "dk1": ("sys", "windowText", "1E293B"),  # slate-800
    "lt1": ("sys", "window", "F8FAFC"),  # slate-50
    "dk2": ("srgb", None, "334155"),  # slate-700
    "lt2": ("srgb", None, "E2E8F0"),  # slate-200
    "accent1": ("srgb", None, "4F46E5"),  # indigo-600
    "accent2": ("srgb", None, "0EA5E9"),  # sky-500
    "accent3": ("srgb", None, "6366F1"),  # indigo-500
    "accent4": ("srgb", None, "0284C7"),  # sky-600
    "accent5": ("srgb", None, "64748B"),  # slate-500
    "accent6": ("srgb", None, "38BDF8"),  # sky-400
    "hlink": ("srgb", None, "4F46E5"),
    "folHlink": ("srgb", None, "0284C7"),
}


def _utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass


def _quarto_pandoc() -> list[str]:
    quarto = shutil.which("quarto")
    if quarto:
        return [quarto, "pandoc"]
    return ["pandoc"]


def dump_reference_pptx(path: Path) -> None:
    cmd = _quarto_pandoc() + [
        "-o",
        str(path),
        "--print-default-data-file",
        "reference.pptx",
    ]
    subprocess.run(cmd, check=True, cwd=ROOT)


def _set_color(parent: ET.Element, kind: str, sys_val: str | None, hex_rgb: str) -> None:
    for child in list(parent):
        parent.remove(child)
    if kind == "sys":
        el = ET.SubElement(parent, f"{{{A}}}sysClr")
        el.set("val", sys_val or "windowText")
        el.set("lastClr", hex_rgb)
    else:
        el = ET.SubElement(parent, f"{{{A}}}srgbClr")
        el.set("val", hex_rgb)


def patch_theme(pptx_path: Path) -> None:
    with zipfile.ZipFile(pptx_path, "r") as zin:
        nomes = zin.namelist()
        temas = [n for n in nomes if n.startswith("ppt/theme/") and n.endswith(".xml")]
        if not temas:
            raise FileNotFoundError("Nenhum ppt/theme/*.xml no PPTX de referência.")
        dados = {n: zin.read(n) for n in nomes}

    for tema in temas:
        root = ET.fromstring(dados[tema])
        scheme = root.find(".//a:clrScheme", NS)
        if scheme is None:
            continue
        scheme.set("name", "SlateIndigoSky")
        for tag, (kind, sys_val, hex_rgb) in SCHEME.items():
            node = scheme.find(f"a:{tag}", NS)
            if node is None:
                node = ET.SubElement(scheme, f"{{{A}}}{tag}")
            _set_color(node, kind, sys_val, hex_rgb)
        dados[tema] = ET.tostring(root, encoding="utf-8", xml_declaration=True)

    tmp = pptx_path.with_suffix(".patched.pptx")
    with zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED) as zout:
        for nome in nomes:
            zout.writestr(nome, dados[nome])
    tmp.replace(pptx_path)


def main() -> int:
    _utf8_stdio()
    DESTINO.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as td:
        bruto = Path(td) / "reference.pptx"
        dump_reference_pptx(bruto)
        patch_theme(bruto)
        shutil.copyfile(bruto, DESTINO)
    print(f"STATUS: template PPTX em {DESTINO.relative_to(ROOT).as_posix()}")
    print("STATUS: paleta slate / indigo / sky (sem números fiscais).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
