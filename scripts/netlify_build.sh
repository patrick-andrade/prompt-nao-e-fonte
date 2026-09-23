#!/usr/bin/env bash
# O Netlify publica o HTML autossuficiente já versionado.
set -euo pipefail
test -s outputs/revealjs-netlify/index.html
printf 'Reveal.js estático pronto para publicação.\n'
