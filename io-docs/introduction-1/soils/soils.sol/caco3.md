---
description: Calcium carbonate (CaCO3) content of the soil layer
---

# caco3

**Code reference:** `soildb(isol)%ly(j)%cal` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L59)).

Calcium carbonate ($\text{CaCO}_3$) content of the soil layer (`%` by weight; Fortran struct default: `0.0`). During initialization in [`soil_phys_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_phys_init.f90#L83), values $\le 10^{-6}$ are replaced with `2.8`%.

When the dynamic soil phosphorus routine is active (`soil_p = 1` in `codes.bsn`), `caco3` sets the active-to-stable inorganic phosphorus transfer coefficient in [`nut_pminrl2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/nut_pminrl2.f90#L124-L126), which scales the transfer rate ([`nut_pminrl2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/nut_pminrl2.f90#L141)):

$$k_{\text{as}} = \min\!\left(0.05,\; \max\!\left(0.002,\; 0.0023 \cdot \text{CaCO}_3 + 0.005\right)\right)$$

where $\text{CaCO}_3$ is layer calcium carbonate content (%).
