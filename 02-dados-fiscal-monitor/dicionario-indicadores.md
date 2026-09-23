# Dicionário de indicadores (contrato v1.3)

Códigos travados. Séries numéricas **não** vivem neste arquivo: só no CSV-contrato.

| Código-contrato | Nome | Unidade | Código DataMapper (FM) |
| --- | --- | --- | --- |
| `GGXWDG_NGDP` | Dívida bruta do governo geral | % do PIB | `G_XWDG_G01_GDP_PT` |
| `GGXONLB_NGDP` | Saldo primário do governo geral | % do PIB | `GGXONLB_G01_GDP_PT` |

Países (iso3, ordem canônica): `BRA`, `MEX`, `CHL`, `IND`, `IDN`. China fora.

## Notas metodológicas (sem série)

- **Setor:** governo geral, salvo nota de país no Fiscal Monitor. Não é necessariamente o governo central.
- **Dívida bruta:** estoque de passivos brutos, % do PIB. Não é dívida líquida (`GGXWDN` existe no FM e **não** entra neste recorte).
- **Saldo primário:** net lending/borrowing primário (também chamado primary balance). É o resultado global **antes** de juros. Sinal FMI: positivo = superávit primário; negativo = déficit primário.
- **Não confundir** com `GGXCNL_NGDP` / `GGXCNL_G01_GDP_PT` (resultado nominal / overall balance), que inclui juros e **não** está no CSV-contrato.
- **Cobertura e GFSM:** o MSA do Fiscal Monitor adverte que países misturam GFSM 2014, GFSM 2001 e, em alguns casos, GFSM 1986. Comparação entre países é do FMI, não uma conta nacional harmonizada por nós.
- **Projeção:** anos à frente da vintage são projeções da equipe do FMI, não realizado. O CSV não traz uma coluna `obs_status`; o recorte 2000–2029 mistura os dois de propósito — o `.qmd` deve dizer isso.

Mapeamento bruto → contrato: `scripts/baixar_fm.R` reconstrói offline os códigos canônicos `GGXWDG_NGDP` e `GGXONLB_NGDP`; `scripts/baixar_fm.py` é a rota alternativa. A consulta corrente à API é separada e não troca a edição do cache.
