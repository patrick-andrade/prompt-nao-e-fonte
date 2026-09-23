#!/usr/bin/env bash
# O Netlify publica três HTMLs autossuficientes já versionados.
set -euo pipefail
test -s outputs/revealjs-netlify/index.html
test -s outputs/revealjs-netlify/apresentacao/index.html
test -s outputs/revealjs-netlify/painel/index.html
printf 'Portal, Reveal.js e painel estáticos prontos para publicação.\n'
