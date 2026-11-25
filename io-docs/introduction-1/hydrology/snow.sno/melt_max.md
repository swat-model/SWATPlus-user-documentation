---
description: Snowmelt factor near June 21
---

# melt\_max

**Code reference:** `snodb(isno)%meltmx` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L76)).

Seasonal melt coefficient $b_J$ near June 21. The built-in snow record uses 4.5 mm water equivalent per day per °C. Use with [melt_min](melt_min.md).

The seasonal factor in [`sq_snom.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sq_snom.f90#L63-L67) is:

$$b(d) = \frac{b_J + b_D}{2} + \sin\left(\frac{d - 81}{58.09}\right) \frac{b_J - b_D}{2}$$

where $b(d)$ is the seasonal melt factor (mm water equivalent per day per °C), $b_J$ is `melt_max` (mm water equivalent per day per °C), $b_D$ is [melt\_min](melt_min.md) (mm water equivalent per day per °C), and $d$ is day of year. The equation uses the same calendar phase in both hemispheres.
