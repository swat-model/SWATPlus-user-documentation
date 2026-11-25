---
description: Organic nitrogen enrichment ratio for loading with sediment
---

# orgn\_enrich

**Code reference:** `hyd_db(ithyd)%erorgn` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrology_data_module.f90#L13)).

Dimensionless enrichment ratio for organic nitrogen in eroded surface sediment. SWAT+ uses the input when it exceeds 0.001 and uses the calculated sediment enrichment ratio otherwise. In [`nut_orgn.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/nut_orgn.f90#L33-L48), the standard organic-N routine uses $N_{\mathrm{sed}}=1000\,N_1 R Y/(M_1 A)$, where $N_1$ is the surface soil organic N pool per hectare, $R$ is the selected ratio, $Y$ is sediment yield in tonnes, $M_1$ is the surface layer soil mass per hectare, and $A$ is HRU area in hectares.
