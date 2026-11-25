---
description: Linear coefficient for calculation of field capacity in the biozone
---

# fc\_lin

**Code reference:** `sep(isep)%fc1` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/septic_data_module.f90#L36)).

Linear coefficient used with [`fc_exp`](fc_exp.md) to update biozone field capacity ($FC$, mm) in response to daily bacterial biomass growth $\Delta B$ ([`sep_biozone.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sep_biozone.f90#L192)):

$$FC_{\text{new}} = FC + c_1 \, (UL - FC)^{c_2} \, \frac{\Delta B}{10 \, \rho_b}$$

where $c_1$ is `fc_lin`, $c_2$ is `fc_exp`, $UL$ is saturated water capacity of the biozone (mm), $\Delta B$ is daily biomass change (kg/ha), and $\rho_b$ is [`bm_dens`](bm_dens.md) ($\text{kg/m}^3$).
