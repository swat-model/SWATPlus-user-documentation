---
description: Moist bulk density of the soil layer
---

# bd

**Code reference:** `soildb(isol)%ly(j)%bd` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L48)).

Moist bulk density of the soil layer ($\text{Mg/m}^3$, equivalent to $\text{g/cm}^3$; Fortran struct default: `1.3`), expressing the ratio of the mass of oven-dry solid particles to the total soil volume at or near field capacity, $\rho_b = M_s / V_t$. During initialization in [`soil_phys_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_phys_init.f90#L76-L77), values $\le 10^{-6}$ are reset to `1.3` and values $> 2.0$ are clamped to `2.0`.

SWAT+ uses layer bulk density $\rho_{b,l}$ to compute total porosity $\phi_l$ ([`soil_phys_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_phys_init.f90#L94)), wilting-point water content $\theta_{\text{wp},l}$ ([`soil_phys_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_phys_init.f90#L91)), and the concentration-to-mass conversion factor `conv_wt` ([`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L50)):

$$\phi_l = 1 - \frac{\rho_{b,l}}{2.65}, \qquad \theta_{\text{wp},l} = \frac{0.4 \cdot \text{clay}_l \cdot \rho_{b,l}}{100}, \qquad w_{\text{conv},l} = \frac{\rho_{b,l} \cdot \Delta z_l}{100}$$

where $\text{clay}_l$ is layer clay percentage and $\Delta z_l$ is layer thickness (mm).
