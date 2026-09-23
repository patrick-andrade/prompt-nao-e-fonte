#!/usr/bin/env Rscript
# Gera, sem rede, o recorte mundial do painel a partir de snapshots FM congelados.
# Uso: Rscript 02-dados-fiscal-monitor/scripts/gerar_painel.R --offline

if (.Platform$OS.type == "windows" && !l10n_info()[["UTF-8"]]) {
  invisible(Sys.setlocale("LC_CTYPE", "Portuguese_Brazil.utf8"))
}

argumentos <- commandArgs(trailingOnly = TRUE)
if (length(setdiff(argumentos, "--offline")) > 0L) {
  stop("Este script só aceita --offline; a consulta corrente não substitui o snapshot.",
       call. = FALSE)
}
if (!requireNamespace("jsonlite", quietly = TRUE)) {
  stop("jsonlite ausente. Restaure o ambiente local com renv antes de gerar os dados.",
       call. = FALSE)
}

arquivo_script <- sub("^--file=", "", grep("^--file=", commandArgs(), value = TRUE)[1])
raiz <- normalizePath(file.path(dirname(arquivo_script), "..", ".."), mustWork = TRUE)
base <- file.path(raiz, "02-dados-fiscal-monitor", "data")
bruto <- file.path(base, "raw")
processado <- file.path(base, "processed")
csv_executivo <- file.path(processado, "fm_weo_cache.csv")
csv_mundial <- file.path(processado, "fm_global_2026_04.csv")
json_mundial <- file.path(processado, "fm_global_2026_04.json")

codigos <- c(GGXWDG_NGDP = "G_XWDG_G01_GDP_PT",
             GGXONLB_NGDP = "GGXONLB_G01_GDP_PT")
nomes <- c(GGXWDG_NGDP = "Dívida bruta do governo geral",
           GGXONLB_NGDP = "Saldo primário do governo geral")
colunas <- c("iso3", "country", "year", "indicator_code", "indicator_name",
             "value", "unit", "vintage", "source")
vintage <- "FM-2026-04"
fonte <- "IMF Fiscal Monitor April 2026 (DataMapper)"
unidade <- "% do PIB"

ler_json <- function(nome) {
  caminho <- file.path(bruto, nome)
  if (!file.exists(caminho)) stop("Snapshot bruto ausente: ", caminho, call. = FALSE)
  jsonlite::fromJSON(caminho, simplifyVector = FALSE)
}

catalogo <- ler_json("datamapper_countries_2026-04.json")$countries
if (length(catalogo) < 200L || is.null(catalogo$BRA) || is.null(catalogo$CHN) ||
    is.null(catalogo$COL)) {
  stop("Catálogo de economias do DataMapper incompleto.", call. = FALSE)
}
series <- lapply(unname(codigos), function(codigo) {
  resposta <- ler_json(paste0("datamapper_full_", codigo, ".json"))
  valores <- resposta$values[[codigo]]
  if (is.null(valores) || length(valores) < 150L) {
    stop("Série mundial incompleta para ", codigo, call. = FALSE)
  }
  valores
})
names(series) <- names(codigos)

# O catálogo /countries nomeia economias individuais. Códigos presentes apenas
# nas séries, como ADVEC e EURO, são agregados e ficam fora do derivado.
economias <- sort(intersect(names(catalogo), union(names(series[[1]]), names(series[[2]]))))
linhas <- vector("list", 0L)
for (iso in economias) {
  pais <- catalogo[[iso]]$label
  if (is.null(pais) || !nzchar(pais)) stop("Economia sem nome: ", iso, call. = FALSE)
  for (indicador in names(codigos)) {
    serie <- series[[indicador]][[iso]]
    if (is.null(serie)) next
    for (ano in 2000:2029) {
      valor <- serie[[as.character(ano)]]
      if (is.null(valor)) next  # ausência continua ausência; nunca zero
      numero <- suppressWarnings(as.numeric(valor))
      if (length(numero) != 1L || !is.finite(numero)) {
        stop("Valor inválido em ", iso, "/", ano, "/", indicador, call. = FALSE)
      }
      linhas[[length(linhas) + 1L]] <- list(
        iso3 = iso, country = pais, year = ano, indicator_code = indicador,
        indicator_name = nomes[[indicador]], value = round(numero, 6),
        unit = unidade, vintage = vintage, source = fonte
      )
    }
  }
}
if (!length(linhas)) stop("Nenhuma linha gerada.", call. = FALSE)
dados <- do.call(rbind, lapply(linhas, as.data.frame, stringsAsFactors = FALSE))
rownames(dados) <- NULL
dados <- dados[colunas]
chave <- paste(dados$iso3, dados$year, dados$indicator_code, sep = "|")
if (anyDuplicated(chave) || !all(c("BRA", "MEX", "CHL", "IND", "IDN", "CHN", "COL") %in%
                                dados$iso3)) {
  stop("Chave duplicada ou economia necessária ausente.", call. = FALSE)
}

# As duas bases têm públicos diferentes. Antes de gravar, exige-se que o recorte
# comum coincida numericamente na precisão contratada do CSV executivo.
executivo <- utils::read.csv(csv_executivo, stringsAsFactors = FALSE,
                             fileEncoding = "UTF-8", check.names = FALSE)
chave_exec <- paste(executivo$iso3, executivo$year, executivo$indicator_code, sep = "|")
indices <- match(chave_exec, chave)
if (anyNA(indices) || any(abs(as.numeric(executivo$value) - dados$value[indices]) > 0.00000051)) {
  stop("O snapshot mundial diverge do CSV executivo: investigue antes de publicar.",
       call. = FALSE)
}
if (any(dados$iso3 %in% c("BRA", "MEX", "CHL", "IND", "IDN") &
        !(chave %in% chave_exec))) {
  stop("O snapshot mundial possui chaves extras nos cinco países executivos.",
       call. = FALSE)
}

dir.create(processado, recursive = TRUE, showWarnings = FALSE)
utils::write.csv(dados, csv_mundial, row.names = FALSE, na = "", fileEncoding = "UTF-8")
linhas_json <- dados[c("iso3", "country", "year", "indicator_code", "value")]
payload <- list(vintage = vintage, source = fonte, unit = unidade, rows = linhas_json)
jsonlite::write_json(payload, json_mundial, auto_unbox = TRUE, dataframe = "rows",
                     digits = 6, pretty = FALSE, na = "null")
cat("STATUS:", nrow(dados), "linhas,", length(unique(dados$iso3)),
    "economias individuais;", nrow(executivo), "linhas executivas conciliadas.\n")
cat("STATUS: CSV e JSON mundiais gerados sem consulta à rede.\n")
