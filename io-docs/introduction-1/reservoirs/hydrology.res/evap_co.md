---
description: Reservoir evaporation coefficient
---

# evap\_co

**Code reference:** `res_hyddb(ires)%evrsv` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L75)).

Dimensionless lake evaporation coefficient applied to potential evapotranspiration over the reservoir surface (historical table default: `0.60`, range `0.0–1.0`; Fortran struct default: `0.7`). If `evap_co` $\le 0$ when SWAT+ reads `hydrology.res` ([`res_read_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_hyd.f90#L60)), the model resets it to `0.6`.

Each day, SWAT+ computes reservoir evaporation volume in [`res_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L160):

$$V_{\text{evap}} = 10 \cdot \eta_{\text{ev}} \cdot E_0 \cdot A$$

where $V_{\text{evap}}$ is daily evaporation volume ($\text{m}^3$), $\eta_{\text{ev}}$ is `evap_co`, $E_0$ is potential evapotranspiration (mm), and $A$ is reservoir surface area (ha), capped at remaining reservoir storage in [`res_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L179-L183).
