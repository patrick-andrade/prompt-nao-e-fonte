#!/usr/bin/env bash
# Build do Reveal.js da Dimensão 3 na imagem Linux do Netlify.
# Não publica PPTX, slop nem o deck de aula.
set -euo pipefail

curl -LsSf https://astral.sh/uv/install.sh | sh
# shellcheck disable=SC1091
if [ -f "$HOME/.local/bin/env" ]; then
  # uv installer (Linux)
  . "$HOME/.local/bin/env"
fi
export PATH="${HOME}/.local/bin:${PATH}"

QUARTO_VER="1.9.37"
curl -fsSL -o /tmp/quarto.tar.gz \
  "https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VER}/quarto-${QUARTO_VER}-linux-amd64.tar.gz"
tar -xzf /tmp/quarto.tar.gz -C /tmp
export PATH="/tmp/quarto-${QUARTO_VER}/bin:${PATH}"

uv python install 3.13
uv sync --locked
uv run -- quarto render 03-relatorio-qmd/mini-fiscal-monitor.qmd --to revealjs --output-dir outputs/revealjs-netlify
uv run python scripts/achatar_saidas.py
