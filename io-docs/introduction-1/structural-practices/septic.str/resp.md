---
description: Respiration rate coefficient
---

# resp

**Code reference:** `sep(isep)%rsp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/septic_data_module.f90#L41)).

Daily bacterial respiration rate coefficient in the biozone (dimensionless; [`sep_biozone.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sep_biozone.f90#L208)):

$$R_{\text{resp}} = c_T \cdot k_r \cdot B$$

where $R_{\text{resp}}$ is daily biomass respiration loss (kg/ha), $k_r$ is `resp` (dimensionless), $B$ is live biomass (kg/ha), and $c_T$ is the temperature factor (`1.0` in SWAT+ main (`6f515368`)).
