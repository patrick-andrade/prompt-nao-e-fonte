"""Gera o portal e o painel autossuficientes a partir do derivado mundial em R.

Não altera a apresentação Reveal em ``outputs/revealjs-netlify/apresentacao``.
Os dados são incorporados ao HTML para que o site funcione sem fetch ou CDN.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA = ROOT / "02-dados-fiscal-monitor/data/processed/fm_global_2026_04.json"
DEFAULT_OUTPUT = ROOT / "outputs/revealjs-netlify"
SITE = ROOT / "site"
INDICATORS = {"GGXWDG_NGDP", "GGXONLB_NGDP"}
REQUIRED_ECONOMIES = {"BRA", "MEX", "CHL", "IND", "IDN", "CHN", "COL"}


def resolve_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def validate_data(data: object) -> dict:
    if not isinstance(data, dict):
        raise ValueError("O derivado mundial deve ser um objeto JSON.")
    if data.get("vintage") != "FM-2026-04":
        raise ValueError("Vintage diferente de FM-2026-04.")
    if data.get("unit") != "% do PIB":
        raise ValueError("Unidade diferente de % do PIB.")
    if not isinstance(data.get("source"), str) or not data["source"].strip():
        raise ValueError("Fonte ausente no derivado mundial.")
    rows = data.get("rows")
    if not isinstance(rows, list) or not rows:
        raise ValueError("O derivado mundial não contém linhas.")

    keys: set[tuple[str, int, str]] = set()
    names: dict[str, str] = {}
    for index, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            raise ValueError(f"Linha {index} não é um objeto.")
        iso = row.get("iso3")
        country = row.get("country")
        year = row.get("year")
        indicator = row.get("indicator_code")
        value = row.get("value")
        if not isinstance(iso, str) or not re.fullmatch(r"[A-Z]{3}", iso):
            raise ValueError(f"ISO3 inválido na linha {index}.")
        if not isinstance(country, str) or not country.strip():
            raise ValueError(f"País sem nome na linha {index}.")
        if not isinstance(year, int) or isinstance(year, bool) or year not in range(2000, 2030):
            raise ValueError(f"Ano fora de 2000–2029 na linha {index}.")
        if indicator not in INDICATORS:
            raise ValueError(f"Indicador fora do contrato na linha {index}.")
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(value)
        ):
            raise ValueError(f"Valor não numérico finito na linha {index}.")
        key = (iso, year, indicator)
        if key in keys:
            raise ValueError(f"Chave repetida: {key}.")
        keys.add(key)
        if iso in names and names[iso] != country:
            raise ValueError(f"Nome divergente para {iso}.")
        names[iso] = country

    missing = REQUIRED_ECONOMIES - names.keys()
    if missing:
        raise ValueError(f"Economias obrigatórias ausentes: {', '.join(sorted(missing))}.")
    return data


def replace_once(template: str, marker: str, replacement: str) -> str:
    if template.count(marker) != 1:
        raise ValueError(f"Marcador {marker!r} precisa ocorrer uma vez no template.")
    return template.replace(marker, replacement)


def render(data: dict) -> tuple[str, str]:
    base_css = (SITE / "base.css").read_text(encoding="utf-8")
    panel_css = (SITE / "painel.css").read_text(encoding="utf-8")
    panel_js = (SITE / "painel.js").read_text(encoding="utf-8")
    portal = (SITE / "portal.html").read_text(encoding="utf-8")
    panel = (SITE / "painel.html").read_text(encoding="utf-8")

    portal = replace_once(portal, "/* INLINE_BASE_CSS */", base_css)
    panel = replace_once(panel, "/* INLINE_BASE_CSS */", base_css)
    panel = replace_once(panel, "/* INLINE_PANEL_CSS */", panel_css)
    panel = replace_once(panel, "/* INLINE_PANEL_JS */", panel_js)

    embedded = json.dumps(data, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
    embedded = (
        embedded.replace("&", "\\u0026")
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("\u2028", "\\u2028")
        .replace("\u2029", "\\u2029")
    )
    panel = replace_once(panel, "/* INLINE_DATA_JSON */", embedded)
    return portal, panel


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", default=str(DEFAULT_DATA), help="JSON mundial preparado em R")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT), help="raiz publicada no Netlify")
    args = parser.parse_args()
    data_path = resolve_path(args.data)
    output = resolve_path(args.output_dir)
    data = validate_data(json.loads(data_path.read_text(encoding="utf-8-sig")))
    portal, panel = render(data)
    (output / "painel").mkdir(parents=True, exist_ok=True)
    (output / "index.html").write_text(portal, encoding="utf-8")
    (output / "painel/index.html").write_text(panel, encoding="utf-8")
    print(f"Portal: {output / 'index.html'}")
    print(f"Painel: {output / 'painel/index.html'} ({len(data['rows'])} linhas incorporadas)")


if __name__ == "__main__":
    main()
