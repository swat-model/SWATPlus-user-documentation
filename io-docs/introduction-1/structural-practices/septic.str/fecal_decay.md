---
description: Fecal coliform bacteria decay rate coefficient
---

# fecal\_decay

**Code reference:** `sep(isep)%fecal` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/septic_data_module.f90#L38)).

Biozone fecal coliform decay rate coefficient ($\text{m}^3/\text{day}$), normalized by live biomass concentration in the biozone pore volume (`sep_biozone.f90`):

$$k_{\text{fc}} = \max\!\left(0,\; K_{\text{fc}} \cdot \frac{B \, A_{\text{hru}}}{V_{\text{bz}} \, \phi}\right), \qquad \Delta N_{\text{fc}} = N_{\text{fc}} \left(1 - e^{-k_{\text{fc}}}\right)$$

where $k_{\text{fc}}$ is the effective daily decay rate ($\text{day}^{-1}$), $K_{\text{fc}}$ is `fecal_decay`, $B$ is live biomass (kg/ha), $A_{\text{hru}}$ is HRU area (ha), $V_{\text{bz}}$ is biozone volume ($\text{m}^3$), $\phi$ is porosity, and $N_{\text{fc}}$ is biozone fecal coliform count.
