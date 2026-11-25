---
description: Snowmelt factor near December 21
---

# melt\_min

**Code reference:** `snodb(isno)%meltmn` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L77)).

Seasonal melt coefficient $b_D$ near December 21. The built-in snow record uses 0.5 mm water equivalent per day per °C. Use with [melt_max](melt_max.md).

The seasonal factor in [`sq_snom.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sq_snom.f90#L63-L67) is $b(d)=(b_J+b_D)/2+\sin((d-81)/58.09)\,(b_J-b_D)/2$, where $d$ is day of year and the coefficients are in mm water equivalent per day per °C. The equation uses the same calendar phase in both hemispheres.
