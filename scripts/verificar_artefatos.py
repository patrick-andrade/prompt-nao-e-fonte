#!/usr/bin/env python3
"""Confere estrutura do HTML estático e dos decks após o render local."""

from __future__ import annotations

import re
import sys
import zipfile
import csv
import json
import math
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PORTAL = ROOT / "outputs/revealjs-netlify/index.html"
PRODUTO = ROOT / "outputs/revealjs-netlify/apresentacao/index.html"
PAINEL = ROOT / "outputs/revealjs-netlify/painel/index.html"
AULA = ROOT / "outputs/aula-expositiva/index.html"
PPTX = ROOT / "outputs/pptx/mini-fiscal-monitor.pptx"
CSV = ROOT / "02-dados-fiscal-monitor/data/processed/fm_weo_cache.csv"
CSV_MUNDIAL = ROOT / "02-dados-fiscal-monitor/data/processed/fm_global_2026_04.csv"


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
        self.links: list[str] = []

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
        if tag == "a" and a.get("href"):
            self.links.append(a["href"] or "")
            if a["href"].startswith(("file:", "C:", "/C:")):
                self.links_locais.append(a["href"] or "")


def html(path: Path, *, estatico: bool, min_slides: int = 0) -> list[str]:
    erros: list[str] = []
    if not path.is_file():
        return [f"ausente: {path.relative_to(ROOT)}"]
    texto = path.read_text(encoding="utf-8")
    audit = AuditorHTML()
    audit.feed(texto)
    if audit.slides < min_slides:
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


def site() -> list[str]:
    erros = html(PORTAL, estatico=True) + html(PRODUTO, estatico=True, min_slides=10)
    erros += html(PAINEL, estatico=True)
    if PORTAL.is_file():
        audit = AuditorHTML()
        audit.feed(PORTAL.read_text(encoding="utf-8"))
        for rota in ("apresentacao/", "painel/"):
            if not any(rota in link for link in audit.links):
                erros.append(f"portal sem link para {rota}")
    if PAINEL.is_file():
        texto = PAINEL.read_text(encoding="utf-8")
        if re.search(r"\b(fetch|XMLHttpRequest)\s*\(", texto):
            erros.append("painel faz requisição de dados em tempo de execução")
        match = re.search(
            r'<script\s+type="application/json"\s+id="fm-data"\s*>(.*?)</script>',
            texto, flags=re.DOTALL,
        )
        if not match:
            erros.append("painel sem dados embutidos em fm-data")
        elif CSV_MUNDIAL.is_file():
            try:
                payload = json.loads(match.group(1))
                linhas = payload["rows"]
                with CSV_MUNDIAL.open(encoding="utf-8", newline="") as fh:
                    esperado = {
                        (r["iso3"], int(r["year"]), r["indicator_code"]): float(r["value"])
                        for r in csv.DictReader(fh)
                    }
                obtido = {
                    (r["iso3"], int(r["year"]), r["indicator_code"]): float(r["value"])
                    for r in linhas
                }
                if len(linhas) != len(esperado) or set(obtido) != set(esperado):
                    erros.append("dados embutidos no painel divergem das chaves do CSV mundial")
                elif any(not math.isclose(obtido[k], v, rel_tol=0, abs_tol=1e-6)
                         for k, v in esperado.items()):
                    erros.append("valores embutidos no painel divergem do CSV mundial")
                else:
                    print(f"STATUS: painel · {len(linhas)} registros conferidos com CSV mundial")
            except (ValueError, TypeError, KeyError) as exc:
                erros.append(f"JSON embutido inválido: {exc}")
        else:
            erros.append("CSV mundial ausente para conferir o painel")
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
    erros = site() + html(AULA, estatico=False, min_slides=10) + pptx(PPTX)
    for erro in erros:
        print(f"FALHA: {erro}", file=sys.stderr)
    return int(bool(erros))


if __name__ == "__main__":
    raise SystemExit(main())
