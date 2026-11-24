---
description: Depth to the top of the biozone layer from the ground surface
---

# dp\_bioz

**Code reference:** `sep(isep)%z` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/septic_data_module.f90#L28)).

The depth (mm) includes the top soil layer and septic tank effluent (STE) distribution chamber, including perforated pipe. During soil initialization (`soils_init.f90`), soil layers are adjusted around `dp_bioz` and `dp_bioz + thk_bioz` to represent the biozone layer.

In `sep_biozone.f90`, `dp_bioz` also sets the sub-biozone soil volume ($V_p$, $\text{m}^3$) available for phosphorus sorption:

$$V_p = (z_{\text{max}} - z_{\text{bz}}) \cdot A_{\text{hru}} \cdot 10$$

where $z_{\text{max}}$ is total soil profile depth (mm), $z_{\text{bz}}$ is `dp_bioz` (mm), and $A_{\text{hru}}$ is HRU area (ha).
