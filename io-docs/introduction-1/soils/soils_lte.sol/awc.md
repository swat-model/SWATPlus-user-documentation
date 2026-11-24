---
description: "Available water capacity value for the soil"
---

# awc

**Code reference:** `soil_lte(k)%awc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L7)).

Available water capacity of the soil ($\text{mm H}_2\text{O/mm soil}$; Fortran struct default: `0.`). During HRU-LTE initialization in [`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L258), SWAT+ scales it by the HRU-LTE soil profile depth $D_{\text{soil}}$ (mm):

$$\text{AWC}_{\text{mm}} = \text{awc} \cdot D_{\text{soil}}$$

The resulting depth-integrated storage $\text{AWC}_{\text{mm}}$ (mm) sets initial soil water ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L261)), percolation travel time ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L263)), evapotranspiration, and excess-water thresholds for lateral flow and percolation in [`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L180-L319).
