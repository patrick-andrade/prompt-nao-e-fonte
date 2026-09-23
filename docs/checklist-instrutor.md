# Checklist do instrutor · contrato v1.4

Aula de 24/09/2026. O render técnico foi preparado no projeto; a inspeção final no projetor, no laboratório e no site deve ser feita antes da aula. Marque somente o que observou.

## Preparação técnica

- [ ] `Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline` reconstrói o CSV executivo. A rotina R do painel reconstrói o derivado mundial do bruto congelado. `python scripts/validar_contrato.py` confirma os dois schemas, países/economias, indicadores, edição, cobertura e chaves únicas.
- [ ] O R do professor encontra os pacotes fixados em `renv.lock`; Quarto renderiza PPTX e Reveal.js do produto e o deck de aula.
- [ ] Portal, apresentação e painel em `outputs/revealjs-netlify/` abrem sem internet e sem recurso externo; o PPTX está em `outputs/pptx/`.
- [ ] `python scripts/verificar_artefatos.py` confirma os três HTMLs, os slides e os recursos depois do render.
- [ ] Todos os slides de ambos os formatos do produto foram projetados: sem cortes, gráficos e fontes legíveis, anos e unidade visíveis; o crédito à OCDE aparece no final.
- [ ] O deck de aula abre em `outputs/aula-expositiva/index.html`; cues de arquivo são relativos, links levam apenas a páginas públicas, memes e notas do apresentador são legíveis.
- [ ] O [clone público](https://github.com/patrick-andrade/prompt-nao-e-fonte) mostra o contrato v1.4 e os três HTMLs; o [portal](https://fiscal-monitor-2026.netlify.app/), os [slides](https://fiscal-monitor-2026.netlify.app/apresentacao/) e o [painel](https://fiscal-monitor-2026.netlify.app/painel/) exibem o mesmo commit.

## Laboratório e material

- [ ] Enviar [`pedido-laboratorio.md`](pedido-laboratorio.md); testar navegador, VS Code e Python 3.10+ no login de aluno.
- [ ] No clone/Download ZIP completo, `python scripts/validar_contrato.py` imprime `esqueleto OK` e `CSV OK`. Testar o acesso ao GitHub e ao Netlify; levar cópia local caso a rede falhe.
- [ ] Abrir `briefing-supervisao.md`, `prompt-do-junior.md` e o HTML simulado com acentos corretos.
- [ ] Conferir a [matriz da autópsia](../01-demanda-simulada/instrutor/autopsia.md) contra os PDFs do BCB e as notas do FMI. No Brasil, NFSP positiva significa déficit; não chamar esses valores de saldo do FMI.
- [ ] Se usar o zip opcional, conferir que exclui `aula/` e `instrutor/autopsia.md`. Para a Atividade 0, usar clone ou Download ZIP completo, pois o validador verifica essas pastas.

## Condução dos 80 minutos

- [ ] Mostrar e-mail → prompt → HTML, com 60 segundos de observação antes da autópsia.
- [ ] Atividade 1 (3 min): perguntar por documento, ano, cobertura e sinal, sem caça a erro de geografia.
- [ ] Abrir a autópsia depois do HTML; discutir vintage ausente, NFSP e mistura de anos/status, incluindo o ano fiscal indiano.
- [ ] Abrir `baixar_fm.R` antes de executar; mostrar entrada JSON, metadados e saída CSV. Rodar offline e validar em Python.
- [ ] Atividade 2 (5 min): alunos localizam a linha `BRA` · 2025 · `GGXONLB_NGDP` e distinguem o saldo do FMI da NFSP do BCB.
- [ ] Mostrar o `.qmd`, o Reveal.js e o PPTX. Explicar que o site publica HTMLs prontos; a API não roda no render nem no navegador.
- [ ] Demonstrar portal → painel em 2025 → Brasil na dispersão/tabela → trajetória → fonte e lacuna. Explicar que o universo mundial é outro derivado da mesma edição e inclui China/Colômbia, enquanto os slides executivos mantêm cinco países.
- [ ] Atividade 3 (3 min): cada aluno escreve uma trava verificável. Discutir por que conhecer R e Python ajuda a revisar código de IA.
- [ ] Encerrar com pergunta, indicador, fonte/edição e possibilidade de refazer. Cortar atividades opcionais se o relógio apertar.
- [ ] Verificar contraste, tamanhos, tooltips e seleção por teclado do painel no projetor; não marcar como concluído antes de observar na sala.

O plano com tempos está em [`plano-aula-2h.md`](plano-aula-2h.md). O público não precisa criar conta Netlify.
