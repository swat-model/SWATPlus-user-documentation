---
description: Soil evaporation compensation factor
---

# esco

**Code reference:** `hyd_db(ithyd)%esco` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrology_data_module.f90#L11)).

Dimensionless soil evaporation compensation factor. Larger values allow more evaporation to be drawn from deeper layers. In [`et_act.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/et_act.f90#L215-L224), potential extraction from a layer is $E=E_z-E_{\mathrm{prev}}(1-c)$, where $E_z$ and $E_{\mathrm{prev}}$ are cumulative evaporative demands to the current and previous layer depths and $c$ is `esco`. The model then reduces the demand for dry soil.
