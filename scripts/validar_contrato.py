#!/usr/bin/env python3
"""Valida o CONTRATO.md v1.5 e as duas bases fiscais congeladas.

Uso (na raiz do repositório, pasta 2026/):

    uv run python scripts/validar_contrato.py

Códigos de saída
----------------
0  Esqueleto OK. Se o CSV ainda não existe: Dimensão 2 pendente (Onda 0).
   Se o CSV existe e o schema bate com o contrato: OK.
1  Falha: CONTRATO/esqueleto incompleto, ou CSV presente com schema divergente.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
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
DATA_DIR = ROOT / "02-dados-fiscal-monitor" / "data"
GLOBAL_CSV = DATA_DIR / "processed" / "fm_global_2026_04.csv"
GLOBAL_JSON = DATA_DIR / "processed" / "fm_global_2026_04.json"
COUNTRIES_RAW = DATA_DIR / "raw" / "datamapper_countries_2026-04.json"
GLOBAL_CODES = {
    "GGXWDG_NGDP": "G_XWDG_G01_GDP_PT",
    "GGXONLB_NGDP": "GGXONLB_G01_GDP_PT",
}
SOURCE = "IMF Fiscal Monitor April 2026 (DataMapper)"
RAW_SHA256 = {
    "datamapper_full_G_XWDG_G01_GDP_PT.json": "f96749538a5cfb8d31141438865a21d7bab9b0de0466fdb2dbeb37650c59e500",
    "datamapper_full_GGXONLB_G01_GDP_PT.json": "22b35875344767733c4ba6f46632a417858ec22771f167e9860edf83eb7c3d06",
    "datamapper_countries_2026-04.json": "f74b5bc5eeb69f3da3edcd19caaab95d94f02a476c1382590a77024164d3b836",
}

VERSION = "v1.5"
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
    ROOT / "AGENTS.md",
    ROOT / "aula" / "apresentacao-minicurso.qmd",
    ROOT / "01-demanda-simulada" / "instrutor" / "autopsia.qmd",
    ROOT / "01-demanda-simulada" / "instrutor" / "autopsia.html",
    ROOT / "02-dados-fiscal-monitor" / "scripts" / "baixar_fm.R",
    ROOT / "03-relatorio-qmd" / "mini-fiscal-monitor.qmd",
)

CLAUSULAS_CONTRATO = (
    "v1.5",
    "01-demanda-simulada/instrutor/autopsia.qmd",
    "01-demanda-simulada/instrutor/autopsia.html",
    "BRA",
    "MEX",
    "CHL",
    "IND",
    "IDN",
    "GGXWDG_NGDP",
    "GGXONLB_NGDP",
    "fm_weo_cache.csv",
    "fm_global_2026_04.csv",
    "fm_global_2026_04.json",
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
        erros.append(f"CONTRATO.md não declara {VERSION}.")
    for trecho in CLAUSULAS_CONTRATO:
        if trecho not in texto:
            erros.append(f"CONTRATO.md não contém a cláusula '{trecho}'.")
    if "CHN" not in texto or "COL" not in texto:
        erros.append("CONTRATO.md não distingue China e Colômbia no painel mundial.")
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

        chave = (iso3, year, indicador)
        if chave in pares_chave:
            erros.append(f"L{i}: chave duplicada {chave}.")
        pares_chave.add(chave)
        try:
            numero = float(valor)
            if not math.isfinite(numero):
                erros.append(f"L{i}: value não finito ({valor!r}).")
        except ValueError:
            erros.append(f"L{i}: value não numérico ({valor!r}).")
        if not VINTAGE_OK.fullmatch(vintage):
            erros.append(f"L{i}: vintage fora do contrato ({vintage!r}).")
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

    if len(vintages) > 1:
        erros.append(f"CSV mistura vintages: {sorted(vintages)}")

    return erros


def _carregar_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def _carregar_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if tuple(reader.fieldnames or ()) != COLUNAS:
            raise ValueError(f"Schema divergente em {path.name}: {reader.fieldnames}")
        return list(reader)


def validar_mundial() -> tuple[list[str], int, int]:
    """Confronta derivado CSV/JSON com snapshots FM e CSV executivo."""
    erros: list[str] = []
    for nome, esperado in RAW_SHA256.items():
        caminho = DATA_DIR / "raw" / nome
        if not caminho.is_file():
            erros.append(f"Bruto oficial ausente: {nome}.")
            continue
        obtido = hashlib.sha256(caminho.read_bytes()).hexdigest()
        if obtido != esperado:
            erros.append(f"SHA-256 divergente no bruto {nome}: {obtido}.")
    if erros:
        return erros, 0, 0

    try:
        catalogo = _carregar_json(COUNTRIES_RAW)["countries"]
        series = {
            codigo: _carregar_json(DATA_DIR / "raw" / f"datamapper_full_{api}.json")
            ["values"][api]
            for codigo, api in GLOBAL_CODES.items()
        }
        linhas = _carregar_csv(GLOBAL_CSV)
        executivo = _carregar_csv(CSV_PATH)
        payload = _carregar_json(GLOBAL_JSON)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        return [f"Não foi possível ler as bases mundiais: {exc}"], 0, 0

    if not linhas:
        return ["CSV mundial vazio."], 0, 0
    esperado: dict[tuple[str, int, str], tuple[str, float]] = {}
    for codigo, conjunto in series.items():
        for iso, anos in conjunto.items():
            if iso not in catalogo:  # agregados ficam fora, mesmo que tenham série
                continue
            for ano_txt, valor in anos.items():
                if not ano_txt.isdecimal() or not ANO_MIN <= int(ano_txt) <= ANO_MAX:
                    continue
                try:
                    numero = float(valor)
                except (TypeError, ValueError):
                    erros.append(f"Bruto não numérico: {iso}/{ano_txt}/{codigo}.")
                    continue
                if not math.isfinite(numero):
                    erros.append(f"Bruto não finito: {iso}/{ano_txt}/{codigo}.")
                    continue
                esperado[(iso, int(ano_txt), codigo)] = (catalogo[iso]["label"], numero)

    visto: dict[tuple[str, int, str], float] = {}
    for numero_linha, linha in enumerate(linhas, start=2):
        iso = linha["iso3"]
        codigo = linha["indicator_code"]
        ano_txt = linha["year"]
        try:
            ano = int(ano_txt)
            valor = float(linha["value"])
        except ValueError:
            erros.append(f"Mundial L{numero_linha}: year/value não numérico.")
            continue
        chave = (iso, ano, codigo)
        if chave in visto:
            erros.append(f"Mundial L{numero_linha}: chave duplicada {chave}.")
        visto[chave] = valor
        if not math.isfinite(valor):
            erros.append(f"Mundial L{numero_linha}: valor não finito.")
        if codigo not in INDICADORES or not ANO_MIN <= ano <= ANO_MAX:
            erros.append(f"Mundial L{numero_linha}: indicador/ano fora do contrato.")
        if iso not in catalogo:
            erros.append(f"Mundial L{numero_linha}: agregado ou código desconhecido ({iso}).")
        elif linha["country"] != catalogo[iso]["label"]:
            erros.append(f"Mundial L{numero_linha}: nome diverge do catálogo ({iso}).")
        if not linha["indicator_name"] or linha["unit"] != "% do PIB":
            erros.append(f"Mundial L{numero_linha}: nome/unidade inválidos.")
        if linha["vintage"] != "FM-2026-04" or linha["source"] != SOURCE:
            erros.append(f"Mundial L{numero_linha}: vintage/fonte incompatível.")
        if chave in esperado and abs(valor - esperado[chave][1]) > 0.00000051:
            erros.append(f"Mundial L{numero_linha}: difere do snapshot oficial {chave}.")

    faltantes = esperado.keys() - visto.keys()
    extras = visto.keys() - esperado.keys()
    if faltantes:
        erros.append(f"Mundial omite {len(faltantes)} observações presentes no bruto.")
    if extras:
        erros.append(f"Mundial acrescenta {len(extras)} observações ausentes no bruto.")
    economias = {chave[0] for chave in visto}
    if len(economias) < 150 or not {"CHN", "COL"}.issubset(economias):
        erros.append("Cobertura mundial insuficiente ou CHN/COL ausentes.")
    if not {2025, 2029}.issubset({chave[1] for chave in visto}):
        erros.append("Anos de referência 2025/2029 ausentes.")

    chaves_exec: set[tuple[str, int, str]] = set()
    divergencias = 0
    for linha in executivo:
        chave = (linha["iso3"], int(linha["year"]), linha["indicator_code"])
        chaves_exec.add(chave)
        if chave not in visto or abs(float(linha["value"]) - visto[chave]) > 0.00000051:
            divergencias += 1
    extras_exec = {chave for chave in visto if chave[0] in ISO3_CANONICO} - chaves_exec
    if divergencias or extras_exec:
        erros.append(f"Duas bases divergem: {divergencias} linhas executivas e "
                     f"{len(extras_exec)} chaves extras no mundial.")

    if (payload.get("vintage"), payload.get("source"), payload.get("unit")) != (
        "FM-2026-04", SOURCE, "% do PIB"
    ):
        erros.append("JSON mundial: metadados divergentes.")
    linhas_json = payload.get("rows")
    if not isinstance(linhas_json, list) or len(linhas_json) != len(linhas):
        erros.append("JSON mundial: quantidade de linhas divergente.")
    else:
        for posicao, (registro, linha) in enumerate(zip(linhas_json, linhas), start=1):
            if not isinstance(registro, dict) or set(registro) != {
                "iso3", "country", "year", "indicator_code", "value"
            }:
                erros.append(f"JSON mundial: schema inválido na linha {posicao}.")
                break
            if (not isinstance(registro["value"], (int, float))
                    or isinstance(registro["value"], bool)
                    or not math.isfinite(registro["value"])):
                erros.append(f"JSON mundial: value não é número finito na linha {posicao}.")
                break
            if (registro["iso3"], registro["country"], registro["year"],
                registro["indicator_code"]) != (
                    linha["iso3"], linha["country"], int(linha["year"]), linha["indicator_code"]
                ) or abs(registro["value"] - float(linha["value"])) > 0.00000051:
                erros.append(f"JSON mundial: difere do CSV na linha {posicao}.")
                break

    return erros, len(linhas), len(economias)


def main() -> int:
    print(f"Validador do contrato {VERSION}")
    print(f"Raiz: {ROOT}")

    erros_esqueleto = validar_esqueleto()
    if erros_esqueleto:
        for e in erros_esqueleto:
            print(f"FALHA: {e}", file=sys.stderr)
        return 1

    print(f"STATUS: esqueleto OK (pastas + cláusulas {VERSION} em CONTRATO.md).")

    faltantes = [p for p in (CSV_PATH, GLOBAL_CSV, GLOBAL_JSON) if not p.is_file()]
    if faltantes:
        for caminho in faltantes:
            print(f"FALHA: base obrigatória ausente: {caminho.relative_to(ROOT)}", file=sys.stderr)
        return 1

    erros_csv = validar_csv(CSV_PATH)
    if erros_csv:
        for e in erros_csv:
            print(f"FALHA: {e}", file=sys.stderr)
        return 1

    print(f"STATUS: CSV OK ({CSV_PATH.relative_to(ROOT).as_posix()}).")
    erros_mundial, quantidade, economias = validar_mundial()
    if erros_mundial:
        for erro in erros_mundial[:30]:
            print(f"FALHA: {erro}", file=sys.stderr)
        if len(erros_mundial) > 30:
            print(f"FALHA: mais {len(erros_mundial) - 30} problemas omitidos.", file=sys.stderr)
        return 1
    print(f"STATUS: mundial OK ({quantidade} linhas, {economias} economias individuais).")
    print("STATUS: CSV executivo e mundial conciliados; JSON equivale ao CSV mundial.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
