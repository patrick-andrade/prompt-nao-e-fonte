#!/usr/bin/env python3
"""Confere estrutura do HTML estático e dos decks após o render local."""

from __future__ import annotations

import re
import sys
import zipfile
import csv
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PRODUTO = ROOT / "outputs/revealjs-netlify/index.html"
AULA = ROOT / "outputs/aula-expositiva/index.html"
PPTX = ROOT / "outputs/pptx/mini-fiscal-monitor.pptx"
CSV = ROOT / "02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv"


def _utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass


class AuditorHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.slides = 0
        self.recursos: list[str] = []
        self.links_locais: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        if tag == "section":
            self.slides += 1
        if tag in {"script", "img", "source", "iframe", "video", "audio"}:
            valor = a.get("src") or a.get("poster")
            if valor:
                self.recursos.append(valor)
        if tag == "link" and "stylesheet" in (a.get("rel") or ""):
            if a.get("href"):
                self.recursos.append(a["href"])
        if tag == "a" and (a.get("href") or "").startswith(("file:", "C:", "/C:")):
            self.links_locais.append(a["href"] or "")


def html(path: Path, *, estatico: bool) -> list[str]:
    erros: list[str] = []
    if not path.is_file():
        return [f"ausente: {path.relative_to(ROOT)}"]
    texto = path.read_text(encoding="utf-8")
    audit = AuditorHTML()
    audit.feed(texto)
    if audit.slides < 10:
        erros.append(f"poucos slides em {path.name}: {audit.slides}")
    if audit.links_locais:
        erros.append(f"links de arquivo no HTML: {audit.links_locais[:3]}")
    for recurso in audit.recursos:
        if recurso.startswith(("data:", "#")):
            continue
        if estatico:
            erros.append(f"recurso externo no produto: {recurso[:100]}")
        elif recurso.startswith(("https:", "http:")):
            continue
        elif not (path.parent / recurso.split("?", 1)[0]).is_file():
            erros.append(f"recurso da aula ausente: {recurso[:100]}")
    if "<U+" in texto or "\ufffd" in texto:
        erros.append(f"texto com erro de codificação em {path.name}")
    print(f"STATUS: {path.relative_to(ROOT).as_posix()} · {audit.slides} slides · {len(audit.recursos)} recursos")
    return erros


def pptx(path: Path) -> list[str]:
    if not path.is_file():
        return [f"ausente: {path.relative_to(ROOT)}"]
    erros: list[str] = []
    with zipfile.ZipFile(path) as zf:
        nomes = [n for n in zf.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)]
        textos = []
        for nome in nomes:
            root = ET.fromstring(zf.read(nome))
            textos.extend((el.text or "") for el in root.iter()
                          if el.tag.endswith("}t"))
    if not 10 <= len(nomes) <= 12:
        erros.append(f"PPTX tem {len(nomes)} slides; esperado 10–12")
    corpo = " ".join(textos)
    with CSV.open(encoding="utf-8", newline="") as fh:
        brasil = {row["indicator_code"]: float(row["value"])
                  for row in csv.DictReader(fh)
                  if row["iso3"] == "BRA" and row["year"] == "2025"}
    exibidos = [f"{brasil[codigo]:.1f}".replace(".", ",")
                for codigo in ("GGXWDG_NGDP", "GGXONLB_NGDP")]
    for trecho in (*exibidos, "OCDE", "2026"):
        if trecho not in corpo:
            erros.append(f"PPTX sem {trecho!r}")
    if "<U+" in corpo or "\ufffd" in corpo:
        erros.append("PPTX com texto mal codificado")
    print(f"STATUS: {path.relative_to(ROOT).as_posix()} · {len(nomes)} slides")
    return erros


def main() -> int:
    _utf8_stdio()
    erros = html(PRODUTO, estatico=True) + html(AULA, estatico=False) + pptx(PPTX)
    for erro in erros:
        print(f"FALHA: {erro}", file=sys.stderr)
    return int(bool(erros))


if __name__ == "__main__":
    raise SystemExit(main())
