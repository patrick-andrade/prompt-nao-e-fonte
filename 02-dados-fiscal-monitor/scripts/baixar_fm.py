#!/usr/bin/env python3
"""Rota Python alternativa para o bruto congelado de abril/2026.

Uso: python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline
     python 02-dados-fiscal-monitor/scripts/baixar_fm.py --consultar-api

Sem argumento, usa o modo offline. A consulta atual não grava bruto nem CSV.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "02-dados-fiscal-monitor" / "data" / "raw"
CSV_PATH = ROOT / "02-dados-fiscal-monitor" / "data" / "processed" / "fm_weo_cache.csv"
VINTAGE = "FM-2026-04"
SOURCE = "IMF Fiscal Monitor April 2026 (DataMapper)"
COUNTRIES = (
    ("BRA", "Brasil"),
    ("MEX", "México"),
    ("CHL", "Chile"),
    ("IND", "Índia"),
    ("IDN", "Indonésia"),
)
INDICATORS = {
    "GGXWDG_NGDP": ("G_XWDG_G01_GDP_PT", "Dívida bruta do governo geral"),
    "GGXONLB_NGDP": ("GGXONLB_G01_GDP_PT", "Saldo primário do governo geral"),
}
COLUMNS = (
    "iso3", "country", "year", "indicator_code", "indicator_name",
    "value", "unit", "vintage", "source",
)


def _utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass


def _raw_path(fm_code: str) -> Path:
    return RAW_DIR / f"datamapper_{fm_code}.json"


def _load_snapshot(fm_code: str) -> dict:
    path = _raw_path(fm_code)
    if not path.is_file():
        raise FileNotFoundError(f"Bruto ausente: {path.relative_to(ROOT).as_posix()}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    meta = payload.get("meta", {})
    expected = (VINTAGE, SOURCE, fm_code)
    found = (meta.get("vintage"), meta.get("source"), meta.get("datamapper_code"))
    if found != expected:
        raise ValueError(f"Metadados incompatíveis com abril/2026: {path.name}")
    return payload


def _consult_current(fm_code: str) -> dict:
    url = f"https://www.imf.org/external/datamapper/api/v1/{fm_code}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json,text/plain,*/*",
            "Referer": "https://www.imf.org/external/datamapper/datasets/FM",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = json.load(resp)
    if "values" not in payload:
        raise ValueError(f"API sem values para {fm_code}")
    return payload


def _rows(payloads: dict[str, dict]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for iso3, country in COUNTRIES:
        for code, (fm_code, name) in INDICATORS.items():
            serie = payloads[code]["values"][fm_code].get(iso3)
            if serie is None:
                raise ValueError(f"País ausente no bruto: {iso3} / {code}")
            for year in range(2000, 2030):
                value = serie.get(str(year))
                if value is None or value == "":
                    continue
                rows.append(
                    {
                        "iso3": iso3,
                        "country": country,
                        "year": str(year),
                        "indicator_code": code,
                        "indicator_name": name,
                        "value": f"{float(value):.6f}".rstrip("0").rstrip("."),
                        "unit": "% do PIB",
                        "vintage": VINTAGE,
                        "source": SOURCE,
                    }
                )
    return rows


def main() -> int:
    _utf8_stdio()
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--offline", action="store_true", help="Bruto congelado (padrão).")
    group.add_argument(
        "--consultar-api", action="store_true",
        help="Consulta atual somente para inspeção; não altera arquivos.",
    )
    args = parser.parse_args()

    if args.consultar_api:
        print("Consulta exploratória do FM corrente; nenhum arquivo será alterado.")
        for code, (fm_code, _name) in INDICATORS.items():
            payload = _consult_current(fm_code)
            bloco = payload["values"].get(fm_code, {})
            seen = [iso3 for iso3, _ in COUNTRIES if iso3 in bloco]
            print(f"{fm_code} → {code}: países disponíveis={seen}")
        print("A API não fixa abril/2026. Revise a vintage antes de atualizar o contrato.")
        return 0

    payloads = {
        code: _load_snapshot(fm_code)
        for code, (fm_code, _name) in INDICATORS.items()
    }
    rows = _rows(payloads)
    if len({row["iso3"] for row in rows}) != len(COUNTRIES):
        raise ValueError("Recorte de países incompleto.")
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"STATUS: {len(rows)} linhas em {CSV_PATH.relative_to(ROOT).as_posix()}")
    print(f"STATUS: bruto congelado {VINTAGE}; consulta de rede não realizada.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
