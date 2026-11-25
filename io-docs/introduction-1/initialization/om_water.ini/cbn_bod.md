---
description: Carbonaceous biological oxygen demand
---

# cbn\_bod

**Code reference:** `om_init_water(ichi)%cbod` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L41)).

Initial carbonaceous biological oxygen demand concentration in water (`ppm`, equivalent to `mg/L` or `g/m^3`; default `0`). SWAT+ converts this concentration to stored mass (`kg`) using the initialized water volume $V_{\text{init}}$ (`m^3`) in [`res_convert_mass`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1295) (reservoirs and wetlands) and [`hyd_convert_conc_to_mass`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1247) (SWAT-DEG channels):

$$M = \frac{C \cdot V_{\text{init}}}{1000}$$
