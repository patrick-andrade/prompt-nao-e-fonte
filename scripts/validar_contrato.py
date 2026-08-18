#!/usr/bin/env python3
"""Valida o CONTRATO.md v1.2 e, se existir, o schema do CSV-contrato.

Uso (na raiz do repositório, pasta 2026/):

    python scripts/validar_contrato.py

Códigos de saída
----------------
0  Esqueleto OK. Se o CSV ainda não existe: Dimensão 2 pendente (Onda 0).
   Se o CSV existe e o schema bate com o contrato: OK.
1  Falha: CONTRATO/esqueleto incompleto, ou CSV presente com schema divergente.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


def _utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass


_utf8_stdio()

ROOT = Path(__file__).resolve().parents[1]
CONTRATO = ROOT / "CONTRATO.md"
CSV_PATH = ROOT / "02-dados-fiscal-monitor" / "data" / "processed" / "fm_weo_cache.csv"

VERSION = "v1.2"
ISO3_CANONICO = ("BRA", "MEX", "CHL", "IND", "IDN")
ISO3_PROIBIDOS = {"CHN", "COL"}
INDICADORES = ("GGXWDG_NGDP", "GGXONLB_NGDP")
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
ANO_MIN, ANO_MAX = 2000, 2029
ANOS_CHAVE = range(2023, 2027)
VINTAGE_OK = re.compile(r"(FM-2026-04|WEO-2026-04|2026-04)")

PASTAS_OBRIGATORIAS = (
    ROOT / "docs",
    ROOT / "scripts",
    ROOT / "aula",
    ROOT / "01-demanda-simulada",
    ROOT / "01-demanda-simulada" / "entrega-slop",
    ROOT / "01-demanda-simulada" / "instrutor",
    ROOT / "02-dados-fiscal-monitor",
    ROOT / "02-dados-fiscal-monitor" / "scripts",
    ROOT / "02-dados-fiscal-monitor" / "data" / "raw",
    ROOT / "02-dados-fiscal-monitor" / "data" / "processed",
    ROOT / "03-relatorio-qmd",
    ROOT / "outputs",
    ROOT / "outputs" / "pptx",
    ROOT / "outputs" / "revealjs-netlify",
    ROOT / "outputs" / "aula-expositiva",
    ROOT / "aluno",
    ROOT / ".cursor" / "rules",
)

ARQUIVOS_OBRIGATORIOS = (
    ROOT / "aula" / "apresentacao-minicurso.qmd",
)

CLAUSULAS_CONTRATO = (
    "v1.2",
    "BRA",
    "MEX",
    "CHL",
    "IND",
    "IDN",
    "GGXWDG_NGDP",
    "GGXONLB_NGDP",
    "fm_weo_cache.csv",
    "iso3",
    "indicator_code",
    "vintage",
    "outputs/pptx",
    "outputs/revealjs-netlify",
    "outputs/aula-expositiva",
    "aula/apresentacao-minicurso.qmd",
    "inspeção humana",
    "Abrir agora",
)


def _fail(msg: str) -> int:
    print(f"FALHA: {msg}", file=sys.stderr)
    return 1


def validar_esqueleto() -> list[str]:
    erros: list[str] = []
    if not CONTRATO.is_file():
        erros.append("CONTRATO.md ausente na raiz.")
        return erros
    texto = CONTRATO.read_text(encoding="utf-8")
    if VERSION not in texto:
        erros.append("CONTRATO.md não declara v1.2.")
    for trecho in CLAUSULAS_CONTRATO:
        if trecho not in texto:
            erros.append(f"CONTRATO.md não contém a cláusula '{trecho}'.")
    if "China" not in texto and "CHN" not in texto:
        erros.append("CONTRATO.md não registra a exclusão da China.")
    for pasta in PASTAS_OBRIGATORIAS:
        if not pasta.is_dir():
            erros.append(f"Pasta obrigatória ausente: {pasta.relative_to(ROOT).as_posix()}")
    for arquivo in ARQUIVOS_OBRIGATORIOS:
        if not arquivo.is_file():
            erros.append(f"Arquivo obrigatório ausente: {arquivo.relative_to(ROOT).as_posix()}")
    return erros


def validar_csv(path: Path) -> list[str]:
    erros: list[str] = []
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames is None:
            return ["CSV sem cabeçalho."]
        encontradas = tuple(h.strip() for h in reader.fieldnames)
        if encontradas != COLUNAS:
            erros.append(
                "Colunas divergem do contrato. "
                f"esperadas={list(COLUNAS)} encontradas={list(encontradas)}"
            )
            return erros
        linhas = list(reader)

    if not linhas:
        erros.append("CSV vazio.")
        return erros

    iso3_vistos: list[str] = []
    pares_chave: set[tuple[str, int, str]] = set()
    vintages: set[str] = set()

    for i, row in enumerate(linhas, start=2):
        iso3 = (row.get("iso3") or "").strip()
        indicador = (row.get("indicator_code") or "").strip()
        vintage = (row.get("vintage") or "").strip()
        valor = (row.get("value") or "").strip()
        year_raw = (row.get("year") or "").strip()

        if iso3 in ISO3_PROIBIDOS:
            erros.append(f"L{i}: iso3 proibido no contrato ({iso3}).")
        if iso3 and iso3 not in ISO3_CANONICO and iso3 not in ISO3_PROIBIDOS:
            erros.append(f"L{i}: iso3 fora do conjunto canônico ({iso3}).")
        if iso3 and iso3 not in iso3_vistos:
            iso3_vistos.append(iso3)
        if indicador and indicador not in INDICADORES:
            erros.append(f"L{i}: indicator_code fora do contrato ({indicador}).")
        vintages.add(vintage)

        try:
            year = int(year_raw)
        except ValueError:
            erros.append(f"L{i}: year inválido ({year_raw!r}).")
            continue
        if year < ANO_MIN or year > ANO_MAX:
            erros.append(f"L{i}: year {year} fora de {ANO_MIN}–{ANO_MAX}.")

        pares_chave.add((iso3, year, indicador))
        if iso3 in ISO3_CANONICO and year in ANOS_CHAVE and indicador in INDICADORES:
            if valor == "":
                erros.append(
                    f"L{i}: NA crítico em ano-chave {year} "
                    f"({iso3}, {indicador})."
                )

    ordem = tuple(c for c in iso3_vistos if c in ISO3_CANONICO)
    if ordem and ordem != tuple(c for c in ISO3_CANONICO if c in ordem):
        erros.append(
            f"Ordem de iso3 diverge da canônica {ISO3_CANONICO}. vista={ordem}"
        )

    faltando_paises = [c for c in ISO3_CANONICO if c not in iso3_vistos]
    if faltando_paises:
        erros.append(f"Países canônicos ausentes no CSV: {faltando_paises}")

    faltando_ind = [ind for ind in INDICADORES if not any(p[2] == ind for p in pares_chave)]
    if faltando_ind:
        erros.append(f"Indicadores ausentes no CSV: {faltando_ind}")

    if vintages and not any(VINTAGE_OK.search(v or "") for v in vintages):
        erros.append(
            "Nenhum vintage registra FM-2026-04, WEO-2026-04 ou 2026-04. "
            f"valores={sorted(vintages)}"
        )

    return erros


def main() -> int:
    print(f"Validador do contrato {VERSION}")
    print(f"Raiz: {ROOT}")

    erros_esqueleto = validar_esqueleto()
    if erros_esqueleto:
        for e in erros_esqueleto:
            print(f"FALHA: {e}", file=sys.stderr)
        return 1

    print("STATUS: esqueleto OK (pastas + cláusulas v1.2 em CONTRATO.md).")

    if not CSV_PATH.is_file():
        rel = CSV_PATH.relative_to(ROOT).as_posix()
        print(f"STATUS: SKIP — CSV ausente ({rel}).")
        print("STATUS: Onda 0 ok; Dimensão 2 pendente.")
        return 0

    erros_csv = validar_csv(CSV_PATH)
    if erros_csv:
        for e in erros_csv:
            print(f"FALHA: {e}", file=sys.stderr)
        return 1

    print(f"STATUS: CSV OK ({CSV_PATH.relative_to(ROOT).as_posix()}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
