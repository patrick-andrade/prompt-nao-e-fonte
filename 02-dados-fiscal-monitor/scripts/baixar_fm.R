#!/usr/bin/env Rscript
# Reconstrói o CSV do Fiscal Monitor abril/2026 a partir do bruto versionado.
# --consultar-api mostra a edição corrente pela API SDMX; nunca grava o CSV.
# Uso, a partir de qualquer pasta: Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline

if (.Platform$OS.type == "windows" && !l10n_info()[["UTF-8"]]) {
  invisible(Sys.setlocale("LC_CTYPE", "Portuguese_Brazil.utf8"))
}

argumentos <- commandArgs(trailingOnly = TRUE)
if (length(setdiff(argumentos, c("--offline", "--consultar-api"))) > 0L ||
    ("--offline" %in% argumentos && "--consultar-api" %in% argumentos)) {
  stop("Use --offline (padrão) ou --consultar-api.", call. = FALSE)
}

arquivo_script <- sub("^--file=", "", grep("^--file=", commandArgs(), value = TRUE)[1])
raiz <- normalizePath(file.path(dirname(arquivo_script), "..", ".."), mustWork = TRUE)
raw_dir <- file.path(raiz, "02-dados-fiscal-monitor", "data", "raw")
csv_path <- file.path(raiz, "02-dados-fiscal-monitor", "data", "processed", "fm_weo_cache.csv")

paises <- c(BRA = "Brasil", MEX = "México", CHL = "Chile", IND = "Índia", IDN = "Indonésia")
indicadores <- c(GGXWDG_NGDP = "G_XWDG_G01_GDP_PT",
                 GGXONLB_NGDP = "GGXONLB_G01_GDP_PT")
nomes <- c(GGXWDG_NGDP = "Dívida bruta do governo geral",
           GGXONLB_NGDP = "Saldo primário do governo geral")
colunas <- c("iso3", "country", "year", "indicator_code", "indicator_name",
             "value", "unit", "vintage", "source")
vintage <- "FM-2026-04"
fonte <- "IMF Fiscal Monitor April 2026 (DataMapper)"

if ("--consultar-api" %in% argumentos) {
  if (!requireNamespace("imfapi", quietly = TRUE)) {
    stop("Pacote imfapi ausente. Restaure o ambiente local com renv::restore().", call. = FALSE)
  }
  cat("Consulta exploratória do FM corrente; nenhum arquivo do contrato será alterado.\n")
  atual <- tryCatch(
    imfapi::imf_get(
      dataflow_id = "FM",
      dimensions = list(COUNTRY = names(paises), INDICATOR = unname(indicadores),
                        FREQUENCY = "A"),
      start_period = "2000", end_period = "2029", max_tries = 2L
    ),
    error = function(e) stop(
      "Consulta corrente indisponível via imfapi/SDMX. O CSV de abril/2026 permanece intacto. ",
      "Detalhe: ", conditionMessage(e), call. = FALSE
    )
  )
  cat("Linhas recebidas:", nrow(atual), "\n")
  cat("Códigos recebidos:", paste(unique(atual$INDICATOR), collapse = ", "), "\n")
  cat("A API não fixa a edição abril/2026. Revise fonte e vintage antes de qualquer atualização.\n")
  quit(save = "no", status = 0L)
}

if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("Pacote jsonlite ausente. Restaure o ambiente local com renv::restore().", call. = FALSE)
}

formatar_valor <- function(valor) {
  texto <- sprintf("%.6f", as.numeric(valor))
  sub("\\.$", "", sub("0+$", "", texto))
}

linhas <- vector("list", 0L)
for (iso in names(paises)) {
  for (codigo in names(indicadores)) {
    fm_code <- indicadores[[codigo]]
    caminho <- file.path(raw_dir, paste0("datamapper_", fm_code, ".json"))
    if (!file.exists(caminho)) stop("Bruto ausente: ", caminho, call. = FALSE)
    bruto <- jsonlite::fromJSON(caminho, simplifyVector = FALSE)
    if (!identical(bruto$meta$vintage, vintage) ||
        !identical(bruto$meta$source, fonte) ||
        !identical(bruto$meta$datamapper_code, fm_code)) {
      stop("Metadados incompatíveis com abril/2026: ", caminho, call. = FALSE)
    }
    serie <- bruto$values[[fm_code]][[iso]]
    if (is.null(serie)) stop("País ausente no bruto: ", iso, call. = FALSE)
    for (ano in 2000:2029) {
      valor <- serie[[as.character(ano)]]
      if (is.null(valor) || !is.finite(as.numeric(valor))) next
      linhas[[length(linhas) + 1L]] <- c(
        iso, paises[[iso]], as.character(ano), codigo, nomes[[codigo]],
        formatar_valor(valor), "% do PIB", vintage, fonte
      )
    }
  }
}

dados <- as.data.frame(do.call(rbind, linhas), stringsAsFactors = FALSE)
names(dados) <- colunas
if (!identical(unique(dados$iso3), names(paises)) ||
    !identical(unique(dados$indicator_code), names(indicadores)) ||
    anyDuplicated(dados[c("iso3", "year", "indicator_code")])) {
  stop("Recorte ou chave incompatível com o contrato.", call. = FALSE)
}

dir.create(dirname(csv_path), recursive = TRUE, showWarnings = FALSE)
texto <- c(paste(colunas, collapse = ","),
           apply(dados, 1L, paste, collapse = ","))
con <- file(csv_path, open = "wb")
on.exit(close(con), add = TRUE)
writeLines(enc2utf8(texto), con = con, sep = "\n", useBytes = TRUE)
cat("STATUS:", nrow(dados), "linhas em",
    file.path("02-dados-fiscal-monitor", "data", "processed", "fm_weo_cache.csv"), "\n")
cat("STATUS: bruto congelado", vintage, "; consulta de rede não realizada.\n")
