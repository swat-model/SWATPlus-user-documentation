---
description: Humus C:N ratio
---

# hum\_c\_n

**Code reference:** `solt_db(isolt)%hum_c_n` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L19)).

Humus carbon-to-nitrogen ratio (`ratio`, typical range `8–12`; Fortran struct default: `10.0`) used to initialize nitrogen in the active and stable humus pools (kg/ha) in [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L132) and [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L138):

$$N_{\text{act},l} = \frac{C_{\text{act},l}}{R_{\text{CN}}}, \qquad N_{\text{sta},l} = \frac{C_{\text{sta},l}}{R_{\text{CN}}}$$

where $R_{\text{CN}}$ is `hum_c_n`, and $C_{\text{act},l}$ and $C_{\text{sta},l}$ are active and stable humus carbon (kg/ha). A positive value must be supplied because SWAT+ divides by `hum_c_n` without a zero-guard.
