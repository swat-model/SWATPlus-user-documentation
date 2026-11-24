---
description: Organic carbon content of the soil layer
---

# carbon

**Code reference:** `soildb(isol)%ly(j)%cbn` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_data_module.f90#L51)).

Organic carbon content of the soil layer (`%` by weight of fine earth `< 2` mm; Fortran struct default: `2.0`). During initialization in [`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L43), SWAT+ enforces a floor of `0.001`% ($\text{cbn}_l = \max(0.001, \text{carbon}_l)$) and computes the initial total organic carbon mass $C_{\text{tot},l}$ (kg/ha) ([`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L114-L117)):

$$C_{\text{tot},l} = 10000 \cdot \Delta z_l \cdot \rho_{b,l} \cdot \frac{\text{cbn}_l}{100}$$

where $\Delta z_l$ is layer thickness (mm) and $\rho_{b,l}$ is layer bulk density ($\text{Mg/m}^3$). Layer `cbn` also drives denitrification ([`nut_nminrl.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/nut_nminrl.f90#L182)), pesticide sorption $K_d = K_{\text{oc}} \cdot \text{cbn}_l / 100$ ([`pest_lch.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_lch.f90#L44)), and dynamic phosphorus sorption ([`soil_nutcarb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_init.f90#L79)).
