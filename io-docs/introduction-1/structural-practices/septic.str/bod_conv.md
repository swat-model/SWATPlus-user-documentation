---
description: >-
  Conversion factor representing the proportion of mass bacterial growth and
  mass BOD degraded in the septic system
---

# bod\_conv

**Code reference:** `sep(isep)%bod_conv` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/septic_data_module.f90#L34)).

Dimensionless biomass yield conversion factor relating degraded BOD mass to live bacterial growth in the biozone (`sep_biozone.f90`):

$$\Delta B = c_T \, Y_{\text{bod}} \, \frac{Q_{\text{in}} C_{\text{in}} - Q_{\text{out}} C_{\text{out}}}{1000 \, A_{\text{hru}}} - (R_{\text{resp}} + R_{\text{mort}} + R_{\text{slg}})$$

where $\Delta B$ is daily net change in live biomass (kg/ha), $Y_{\text{bod}}$ is `bod_conv`, $Q_{\text{in}} C_{\text{in}} - Q_{\text{out}} C_{\text{out}}$ is daily BOD mass degraded in the biozone, $A_{\text{hru}}$ is HRU area (ha), $R_{\text{resp}}$, $R_{\text{mort}}$, and $R_{\text{slg}}$ are daily respiration, mortality, and sloughing losses (kg/ha), and $c_T = 1.0$ in SWAT+ main (`6f515368`).
