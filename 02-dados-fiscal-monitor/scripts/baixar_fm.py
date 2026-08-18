"""Baixa o Fiscal Monitor abril/2026 e grava o CSV-contrato.

Fonte pública: IMF DataMapper (dataset FM). Sem credencial.
Códigos da API FM são mapeados para os códigos canônicos do CONTRATO.md.

Uso (na raiz do repositório, pasta 2026/):

    python 02-dados-fiscal-monitor/scripts/baixar_fm.py
    python 02-dados-fiscal-monitor/scripts/baixar_fm.py --offline
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "02-dados-fiscal-monitor" / "data" / "raw"
PROCESSED_DIR = ROOT / "02-dados-fiscal-monitor" / "data" / "processed"
CSV_PATH = PROCESSED_DIR / "fm_weo_cache.csv"

DATAMAPPER = "https://www.imf.org/external/datamapper/api/v1/{code}"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)
ACCEPT = "application/json,text/plain,*/*"

ANO_MIN, ANO_MAX = 2000, 2029
VINTAGE = "FM-2026-04"
SOURCE = "IMF Fiscal Monitor April 2026 (DataMapper)"

PAISES: tuple[tuple[str, str], ...] = (
    ("BRA", "Brasil"),
    ("MEX", "México"),
    ("CHL", "Chile"),
    ("IND", "Índia"),
    ("IDN", "Indonésia"),
)

# Código-contrato → código DataMapper FM + metadados.
INDICADORES: dict[str, dict[str, str]] = {
    "GGXWDG_NGDP": {
        "fm_code": "G_XWDG_G01_GDP_PT",
        "name": "Dívida bruta do governo geral",
        "unit": "% do PIB",
    },
    "GGXONLB_NGDP": {
        "fm_code": "GGXONLB_G01_GDP_PT",
        "name": "Saldo primário do governo geral",
        "unit": "% do PIB",
    },
}

COLUNAS = (
    "iso3",
    "country",
    "year",
    "indicator_code",
    "indicator_name",
    "value",
    "unit",
    "vintage",
    "source",
)


def _utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass


def _raw_path(fm_code: str) -> Path:
    return RAW_DIR / f"datamapper_{fm_code}.json"


def recortar_payload(payload: dict, fm_code: str) -> dict:
    """Mantém só países canônicos e anos do contrato. China não entra no bruto versionado."""
    bloco = payload.get("values", {}).get(fm_code, {})
    recorte: dict[str, dict[str, float]] = {}
    for iso3, _nome in PAISES:
        serie = {}
        for ano_txt, valor in bloco.get(iso3, {}).items():
            try:
                ano = int(ano_txt)
            except (TypeError, ValueError):
                continue
            if ano < ANO_MIN or ano > ANO_MAX or valor is None or valor == "":
                continue
            serie[str(ano)] = float(valor)
        recorte[iso3] = serie
    return {
        "values": {fm_code: recorte},
        "meta": {
            "vintage": VINTAGE,
            "source": SOURCE,
            "datamapper_code": fm_code,
            "year_min": ANO_MIN,
            "year_max": ANO_MAX,
        },
    }


def baixar_indicador(fm_code: str) -> dict:
    url = DATAMAPPER.format(code=fm_code)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": ACCEPT,
            "Referer": "https://www.imf.org/external/datamapper/datasets/FM",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    if "values" not in payload:
        raise RuntimeError(f"DataMapper não devolveu 'values' para {fm_code}.")
    recorte = recortar_payload(payload, fm_code)
    _raw_path(fm_code).write_text(
        json.dumps(recorte, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return recorte


def carregar_indicador(fm_code: str, *, offline: bool) -> dict:
    cache = _raw_path(fm_code)
    if offline:
        if not cache.is_file():
            raise FileNotFoundError(
                f"Modo --offline sem bruto em {cache.relative_to(ROOT).as_posix()}."
            )
        return json.loads(cache.read_text(encoding="utf-8"))
    try:
        return baixar_indicador(fm_code)
    except (urllib.error.URLError, TimeoutError, RuntimeError) as exc:
        if cache.is_file():
            print(f"AVISO: download falhou ({exc}); usando bruto em disco.", file=sys.stderr)
            return json.loads(cache.read_text(encoding="utf-8"))
        raise


def serie_pais(payload: dict, fm_code: str, iso3: str) -> dict[str, float | None]:
    bloco = payload.get("values", {}).get(fm_code, {})
    bruto = bloco.get(iso3, {})
    saida: dict[str, float | None] = {}
    for ano_txt, valor in bruto.items():
        try:
            ano = int(ano_txt)
        except (TypeError, ValueError):
            continue
        if ano < ANO_MIN or ano > ANO_MAX:
            continue
        if valor is None or valor == "":
            continue
        saida[str(ano)] = float(valor)
    return saida


def montar_linhas(payloads: dict[str, dict]) -> list[dict[str, str]]:
    linhas: list[dict[str, str]] = []
    for iso3, country in PAISES:
        for codigo, meta in INDICADORES.items():
            serie = serie_pais(payloads[codigo], meta["fm_code"], iso3)
            for ano in range(ANO_MIN, ANO_MAX + 1):
                valor = serie.get(str(ano))
                if valor is None:
                    continue
                linhas.append(
                    {
                        "iso3": iso3,
                        "country": country,
                        "year": str(ano),
                        "indicator_code": codigo,
                        "indicator_name": meta["name"],
                        "value": f"{valor:.6f}".rstrip("0").rstrip("."),
                        "unit": meta["unit"],
                        "vintage": VINTAGE,
                        "source": SOURCE,
                    }
                )
    return linhas


def gravar_csv(linhas: list[dict[str, str]]) -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUNAS)
        writer.writeheader()
        writer.writerows(linhas)


def validar_minimo(linhas: list[dict[str, str]]) -> None:
    iso_vistos = {row["iso3"] for row in linhas}
    faltando = [c for c, _ in PAISES if c not in iso_vistos]
    if faltando:
        raise RuntimeError(f"Países canônicos ausentes no recorte: {faltando}")
    if any(row["iso3"] == "CHN" for row in linhas):
        raise RuntimeError("China entrou no CSV; isso viola o CONTRATO.md.")
    ind_vistos = {row["indicator_code"] for row in linhas}
    for codigo in INDICADORES:
        if codigo not in ind_vistos:
            raise RuntimeError(f"Indicador ausente no recorte: {codigo}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Grava fm_weo_cache.csv a partir do FM abril/2026.")
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Não chama a API; reconstrói o CSV a partir de data/raw/.",
    )
    return parser.parse_args()


def main() -> int:
    _utf8_stdio()
    args = parse_args()
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    payloads: dict[str, dict] = {}
    for codigo, meta in INDICADORES.items():
        print(f"Fonte: {meta['fm_code']} → {codigo} ({'offline' if args.offline else 'DataMapper'})")
        payloads[codigo] = carregar_indicador(meta["fm_code"], offline=args.offline)

    linhas = montar_linhas(payloads)
    validar_minimo(linhas)
    gravar_csv(linhas)
    rel = CSV_PATH.relative_to(ROOT).as_posix()
    print(f"STATUS: {len(linhas)} linhas em {rel}")
    print(f"STATUS: vintage={VINTAGE}; anos={ANO_MIN}–{ANO_MAX}; países={[c for c, _ in PAISES]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
