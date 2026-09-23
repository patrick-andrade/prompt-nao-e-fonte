# A ativação completa do renv pode demorar no checkout sincronizado.
# Usamos a biblioteca local se os pacotes centrais já foram restaurados.
invisible(local({
  if (!requireNamespace("renv", quietly = TRUE)) return()
  biblioteca <- renv::paths$library(project = getwd())
  pacotes <- c("jsonlite", "imfapi", "ggplot2", "knitr", "rmarkdown")
  if (all(file.exists(file.path(biblioteca, pacotes, "DESCRIPTION")))) {
    .libPaths(c(biblioteca, .libPaths()))
  }
}))
