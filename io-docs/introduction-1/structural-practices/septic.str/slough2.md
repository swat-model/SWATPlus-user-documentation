---
description: Exponential coefficient for calculating the rate of biomass sloughing
---

# slough2

**Code reference:** `sep(isep)%slg2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/septic_data_module.f90#L43)).

Exponential coefficient used with [`slough1`](slough1.md) to calculate percolation-driven biomass sloughing from the biozone (`sep_biozone.f90`):

$$R_{\text{slg}} = s_1 \cdot q_{\text{perc}}^{s_2} \cdot B$$

where $R_{\text{slg}}$ is daily sloughed biomass (kg/ha), $s_1$ is `slough1`, $s_2$ is `slough2`, $q_{\text{perc}}$ is biozone percolation (mm/day), and $B$ is live biomass (kg/ha).
