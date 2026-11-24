---
description: Available water capacity of the soil layer
---

# awc

**Code reference:** `soildb(isol)%ly(j)%awc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L49)).

Plant available water capacity of the soil layer ($\text{mm H}_2\text{O/mm soil}$; Fortran struct default: `0.2`), defined as the difference between volumetric water content at field capacity ($-0.033\text{ MPa}$) and permanent wilting point ($-1.5\text{ MPa}$), $\text{AWC} = \theta_{\text{fc}} - \theta_{\text{wp}}$. During initialization in [`soil_phys_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_phys_init.f90#L78-L79) (and [`soil_awc_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_awc_init.f90#L45-L46)), values $\le 10^{-6}$ are replaced with `0.005` and values $\ge 0.8$ are clamped to `0.8`.

SWAT+ computes field-capacity water content $\theta_{\text{fc},l}$ and plant-available water storage $\text{FC}_l$ (mm) in [`soil_phys_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_phys_init.f90#L93-L100) and [`soil_phys_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_phys_init.f90#L149):

$$\theta_{\text{fc},l} = \theta_{\text{wp},l} + \text{AWC}_l, \qquad \text{FC}_l = \Delta z_l \left(\theta_{\text{fc},l} - \theta_{\text{wp},l}\right)$$

where $\Delta z_l$ is layer thickness (mm). If $\theta_{\text{fc},l} \ge \phi_l$ (porosity), SWAT+ resets $\theta_{\text{fc},l} = \phi_l - 0.05$ and $\theta_{\text{wp},l} = \theta_{\text{fc},l} - \text{AWC}_l$, falling back to $\theta_{\text{fc},l} = 0.75\,\phi_l$ and $\theta_{\text{wp},l} = 0.25\,\phi_l$ if $\theta_{\text{wp},l} \le 0$.
