---
description: Weir discharge linear coefficient
---

# linear\_c

**Code reference:** `res_weir(ires)%c` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L139)).

Dimensionless linear coefficient in the weir-release equation (Fortran struct default: `1.84`). SWAT+ calculates weir discharge in [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L199-L208) and [`res_weir_release.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_weir_release.f90#L84-L104) as:

$$Q = 0.45 \, A \cdot c \cdot w \cdot h_{\text{above}}^{k}$$

where $A$ is surface area (ha), $c$ is `linear_c`, $w$ is [width](weir_wd.md) (m), $k$ is [exp\_k](energy_co.md), $h_{\text{above}} = \max(0,\, d - h_{\text{weir}})$ is water depth above the weir crest (m), and $Q$ is the discharge rate (`m3/s` in source comments, integrated over the sub-daily/hourly step to $\text{m}^3$).
