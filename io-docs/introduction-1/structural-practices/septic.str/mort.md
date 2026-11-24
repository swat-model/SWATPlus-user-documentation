---
description: Mortality rate coefficient
---

# mort

**Code reference:** `sep(isep)%mrt` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/septic_data_module.f90#L40)).

Daily bacterial mortality rate coefficient in the biozone (dimensionless; [`sep_biozone.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sep_biozone.f90#L211)):

$$R_{\text{mort}} = c_T \cdot k_m \cdot B$$

where $R_{\text{mort}}$ is daily mortality (kg/ha), $k_m$ is `mort`, $B$ is live biomass (kg/ha), and $c_T = 1.0$ in SWAT+ main (`6f515368`). Dead biomass transfers to the biozone plaque pool.
