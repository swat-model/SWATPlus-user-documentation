---
description: Phosphorus enrichment ratio for loading with sediment
---

# orgp\_enrich

**Code reference:** `hyd_db(ithyd)%erorgp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrology_data_module.f90#L15)).

Dimensionless enrichment ratio for sediment-attached phosphorus, including organic and mineral forms. SWAT+ uses the input when it exceeds 0.001 and uses the calculated enrichment ratio otherwise. [`nut_psed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/nut_psed.f90#L63-L79) calculates $P_{\mathrm{sed}}=1000\,P_1 R Y/(M_1 A)$, where $P_1$ is the surface soil sediment-attached P pool per hectare, $R$ is the selected ratio, $Y$ is sediment yield in tonnes, $M_1$ is surface-layer soil mass per hectare, and $A$ is HRU area in hectares.
