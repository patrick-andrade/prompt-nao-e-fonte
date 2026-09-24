# Dicionário de indicadores (contrato v1.5)

Códigos travados. Séries numéricas **não** vivem neste arquivo: estão no CSV executivo e no derivado mundial separado.

| Código-contrato | Nome | Unidade | Código DataMapper (FM) |
| --- | --- | --- | --- |
| `GGXWDG_NGDP` | Dívida bruta do governo geral | % do PIB | `G_XWDG_G01_GDP_PT` |
| `GGXONLB_NGDP` | Saldo primário do governo geral | % do PIB | `GGXONLB_G01_GDP_PT` |

Países do CSV executivo (iso3, ordem canônica): `BRA`, `MEX`, `CHL`, `IND`, `IDN`. O painel usa economias individuais do catálogo DataMapper FM, incluindo `CHN` e `COL`; agregados não entram.

## Notas metodológicas (sem série)

- **Setor:** os códigos selecionados referem-se ao governo geral, mas o apêndice metodológico do Fiscal Monitor registra cobertura distinta para algumas economias, inclusive governo central/orçamentário. Verificar notas por país nas Tabelas B–D antes de comparar níveis.
- **Dívida bruta:** estoque de passivos brutos, % do PIB. Não é dívida líquida (`GGXWDN` existe no FM e **não** entra neste recorte).
- **Saldo primário:** net lending/borrowing primário (também chamado primary balance). É o resultado global **antes** de juros. Sinal FMI: positivo = superávit primário; negativo = déficit primário.
- **Não confundir** com `GGXCNL_NGDP` / `GGXCNL_G01_GDP_PT` (resultado nominal / overall balance), que inclui juros e **não** está no CSV-contrato.
- **Cobertura e GFSM:** o MSA do Fiscal Monitor adverte que países misturam GFSM 2014, GFSM 2001 e, em alguns casos, GFSM 1986. Comparação entre países é do FMI, não uma conta nacional harmonizada por nós.
- **Projeção:** anos à frente da vintage são projeções da equipe do FMI, não realizado. O CSV não traz uma coluna `obs_status`; o recorte 2000–2029 mistura os dois de propósito — o `.qmd` deve dizer isso.

Mapeamento bruto → contrato: `scripts/baixar_fm.R` reconstrói offline os códigos canônicos `GGXWDG_NGDP` e `GGXONLB_NGDP`; `scripts/baixar_fm.py` é a rota alternativa. A consulta corrente à API é separada e não troca a edição do cache.

O painel usa o mesmo mapeamento em `scripts/gerar_painel.R`, com snapshots completos e congelados do DataMapper FM abril/2026. Sua execução offline não altera o CSV executivo.
