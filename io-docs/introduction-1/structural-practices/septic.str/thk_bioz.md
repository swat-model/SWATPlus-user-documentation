---
description: Thickness of biozone layer
---

# thk\_bioz

**Code reference:** `sep(isep)%thk` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/septic_data_module.f90#L29)).

The biozone layer is a thin soil layer underneath the septic tank effluent (STE) distribution chamber where pollutants are degraded by naturally existing live biomass bacteria. In `sep_biozone.f90`, `thk_bioz` (mm) determines the biozone volume ($V_{\text{bz}}$, $\text{m}^3$) and the plaque-adjusted saturated storage capacity ($UL$, mm):

$$V_{\text{bz}} = h_{\text{bz}} \cdot A_{\text{hru}} \cdot 10, \qquad UL = \phi \cdot h_{\text{bz}} - \frac{M_{\text{plq}}}{10 \, \rho_b}$$

where $h_{\text{bz}}$ is `thk_bioz` (mm), $A_{\text{hru}}$ is HRU area (ha), $\phi$ is soil porosity, $M_{\text{plq}}$ is plaque mass (kg/ha), and $\rho_b$ is [`bm_dens`](bm_dens.md) ($\text{kg/m}^3$).
