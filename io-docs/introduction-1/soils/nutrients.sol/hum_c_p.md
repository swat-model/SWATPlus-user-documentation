---
description: Humus C:P ratio
---

# hum\_c\_p

**Code reference:** `solt_db(isolt)%hum_c_p` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L20)).

Humus carbon-to-phosphorus ratio (`ratio`, typical range `70–90`; Fortran struct default: `80.0`) used to initialize phosphorus in the active and stable humus pools (kg/ha) in [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L133) and [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L139):

$$P_{\text{act},l} = \frac{C_{\text{act},l}}{R_{\text{CP}}}, \qquad P_{\text{sta},l} = \frac{C_{\text{sta},l}}{R_{\text{CP}}}$$

where $R_{\text{CP}}$ is `hum_c_p`, and $C_{\text{act},l}$ and $C_{\text{sta},l}$ are active and stable humus carbon (kg/ha). A positive value must be supplied because SWAT+ divides by `hum_c_p` without a zero-guard.
