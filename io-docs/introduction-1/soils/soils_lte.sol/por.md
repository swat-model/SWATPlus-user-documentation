---
description: "Porosity value for the soil, scaled by the soil layer thickness when assigned to the HRU LTE state"
---

# por

**Code reference:** `soil_lte(k)%por` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L8)).

Total porosity of the soil (`mm/mm`, fraction; Fortran struct default: `0.`). During HRU-LTE initialization in [`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L259), SWAT+ scales it by the HRU-LTE soil profile depth $D_{\text{soil}}$ (mm):

$$\text{UL}_{\text{mm}} = \text{por} \cdot D_{\text{soil}}$$

The resulting total pore-water capacity $\text{UL}_{\text{mm}}$ (mm) sets saturation storage ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L265)), percolation travel time ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L263)), and the saturation fraction in [`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L231) and [`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L299).
