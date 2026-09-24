# Checklist do instrutor · contrato v1.5

Aula de 24/09/2026. O render técnico foi preparado no projeto; a inspeção final no projetor, no laboratório e no site deve ser feita antes da aula. Marque somente o que observou.

## Preparação técnica

- [ ] `Rscript 02-dados-fiscal-monitor/scripts/baixar_fm.R --offline` reconstrói o CSV executivo. A rotina R do painel reconstrói o derivado mundial do bruto congelado. `python scripts/validar_contrato.py` confirma os dois schemas, países/economias, indicadores, edição, cobertura e chaves únicas.
- [ ] O R do professor encontra os pacotes fixados em `renv.lock`; Quarto renderiza PPTX e Reveal.js do produto e o deck de aula.
- [ ] `quarto render 01-demanda-simulada/instrutor/autopsia.qmd --to html` gera `autopsia.html`; abrir no navegador e conferir matriz, acentos e largura da tabela no projetor.
- [ ] Portal, apresentação e painel em `outputs/revealjs-netlify/` abrem sem internet e sem recurso externo; o PPTX está em `outputs/pptx/`.
- [ ] `python scripts/verificar_artefatos.py` confirma os três HTMLs, os slides e os recursos depois do render.
- [ ] Todos os slides de ambos os formatos do produto foram projetados: sem cortes, gráficos e fontes legíveis, anos e unidade visíveis; o crédito à OCDE aparece no final.
- [ ] O deck de aula abre em `outputs/aula-expositiva/index.html`; cues de arquivo são relativos, links levam apenas a páginas públicas, memes e notas do apresentador são legíveis.
- [ ] O [clone público](https://github.com/patrick-andrade/prompt-nao-e-fonte) mostra o contrato v1.5 e os três HTMLs; o [portal](https://fiscal-monitor-2026.netlify.app/), os [slides](https://fiscal-monitor-2026.netlify.app/apresentacao/) e o [painel](https://fiscal-monitor-2026.netlify.app/painel/) correspondem aos HTMLs desse commit; conferir a referência remota e o deploy, pois as páginas não exibem o hash.

## Laboratório e material

- [ ] Enviar [`pedido-laboratorio.md`](pedido-laboratorio.md); testar navegador, VS Code e Python 3.10+ no login de aluno.
- [ ] No clone/Download ZIP completo, `python scripts/validar_contrato.py` imprime `esqueleto OK` e `CSV OK`. Testar o acesso ao GitHub e ao Netlify; levar cópia local caso a rede falhe.
- [ ] Abrir `briefing-supervisao.md`, `prompt-do-junior.md` e o HTML simulado com acentos corretos.
- [ ] Conferir a [matriz da autópsia](../01-demanda-simulada/instrutor/autopsia.html) contra os PDFs do BCB e as notas do FMI. No Brasil, NFSP positiva significa déficit; não chamar esses valores de saldo do FMI.
- [ ] Se usar o zip opcional, conferir que exclui `aula/` e `instrutor/` (inclusive o `.qmd` e o HTML da autópsia). A leitura da Atividade 2 cabe nesse zip; para executar o validador integralmente, usar clone ou Download ZIP completo.

## Condução dos 90 minutos e discussão de 30 minutos

- [ ] Mostrar e-mail → prompt → HTML, com 60 segundos de observação antes da autópsia.
- [ ] Atividade 1 (3 min): perguntar por documento, ano, cobertura e sinal, sem caça a erro de geografia.
- [ ] Abrir a autópsia depois do HTML; discutir vintage ausente, NFSP e mistura de anos/status, incluindo o ano fiscal indiano.
- [ ] Explicar o recorte do contrato e conduzir a Atividade 2: localizar países, indicadores e versão no contrato e no validador.
- [ ] Distinguir documentação, auditabilidade e reprodutibilidade. Apresentar o ETL e abrir `baixar_fm.R` para mostrar entrada JSON, metadados e saída CSV; retomar harness e pacotes antes da execução.
- [ ] Rodar a rotina offline e validar com `uv run python scripts/validar_contrato.py` no ambiente preparado do professor.
- [ ] Atividade 3 (5 min): alunos localizam a linha `BRA` · 2025 · `GGXONLB_NGDP` e distinguem o saldo do FMI da NFSP do BCB. Depois, apresentar a API como consulta exploratória.
- [ ] Mostrar o `.qmd`, o Reveal.js e o PPTX. Explicar que o site publica HTMLs prontos; a API não roda no render nem no navegador.
- [ ] Demonstrar portal → painel em 2025 → Brasil na dispersão/tabela → trajetória → fonte e lacuna. Explicar que o universo mundial é outro derivado da mesma edição e inclui China/Colômbia, enquanto os slides executivos mantêm cinco países.
- [ ] Para mostrar ausência em 2025, selecionar Eritrea (`ERI`): os dois indicadores aparecem como “—”. Voltar a Brazil (`BRA`) para a trajetória com valores.
- [ ] Mostrar um diff e o histórico do projeto em modo de leitura; explicar commit, GitHub, push e o que foi publicado.
- [ ] Abrir brevemente os guias de Codex, Git e GitHub, Quarto e Skills. Mostrar o exemplo de `SKILL.md`, sem instalar nem depender de geração ao vivo.
- [ ] Atividade 4 (3 min): cada aluno escreve uma instrução com fonte/arquivo, resultado esperado e forma de conferência. Discutir por que conhecer R e Python ajuda a revisar código de IA.
- [ ] Encerrar a exposição em 90 min com pergunta, fonte/edição, possibilidade de refazer e comunicação. Reservar 30 min para discussão e folga; usar complementos apenas se houver tempo.
- [ ] Manter os HTMLs locais prontos para a falta de rede; os guias externos podem ser consultados depois.
- [ ] Verificar contraste, tamanhos, tooltips e seleção por teclado do painel no projetor; não marcar como concluído antes de observar na sala.

O plano com tempos está em [`plano-aula-2h.md`](plano-aula-2h.md). O público não precisa criar conta Netlify.
