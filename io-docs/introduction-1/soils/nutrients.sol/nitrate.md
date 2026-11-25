---
description: Nitrate N in soil surface
---

# nitrate

**Code reference:** `solt_db(isolt)%nitrate` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L17)).

Initial nitrate-nitrogen concentration at the soil surface (`ppm`; Fortran struct default: `7.0`). During initialization in [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L50) and [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L56-L60), values $\le 10^{-9}$ are replaced with `7.0` ppm ([fallback](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L55-L58)), and SWAT+ initializes each layer's nitrate-N mass (kg/ha) as:

$$N_{\text{NO3},l} = C_{N,0} \cdot f_{\text{dep},l} \cdot \frac{\rho_{b,l} \cdot \Delta z_l}{100}$$

where $C_{N,0}$ is `nitrate` (ppm), $f_{\text{dep},l}$ is the depth attenuation factor, $\rho_{b,l}$ is layer bulk density ($\text{Mg/m}^3$), and $\Delta z_l$ is layer thickness (mm).
