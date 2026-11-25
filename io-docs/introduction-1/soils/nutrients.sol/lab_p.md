---
description: Labile P in soil surface
---

# lab\_p

**Code reference:** `solt_db(isolt)%lab_p` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L16)).

Initial labile phosphorus concentration at the soil surface (`ppm`; Fortran struct default: `5.0`). During initialization in [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L50) and [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L64-L69), values $\le 10^{-9}$ are replaced with `5.0` ppm ([fallback](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L63-L67)), and SWAT+ initializes each layer's labile phosphorus mass (kg/ha) as:

$$P_{\text{lab},l} = C_{P,0} \cdot f_{\text{dep},l} \cdot \frac{\rho_{b,l} \cdot \Delta z_l}{100}$$

where $C_{P,0}$ is `lab_p` (ppm), $f_{\text{dep},l}$ is the depth attenuation factor, $\rho_{b,l}$ is layer bulk density ($\text{Mg/m}^3$), and $\Delta z_l$ is layer thickness (mm).
