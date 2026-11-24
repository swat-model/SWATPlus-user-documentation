---
description: Temperature adjustment for nitrogen loss (settling)
---

# theta\_n

**Code reference:** `res_nut(ires)%theta_n` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L119)).

Dimensionless Arrhenius temperature adjustment factor for nitrogen settling and soluble nitrogen loss (default: `1.0`). SWAT+ calls [`theta.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/theta.f90#L17) from [`res_nutrient.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_nutrient.f90#L58) for particulate organic nitrogen and [`res_nutrient.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_nutrient.f90#L64) for soluble inorganic nitrogen:

$$k(T) = k_{20} \, \theta_N^{(T - 20)}$$

where $k_{20}$ is the daily loss rate at 20 °C (`1/day`), $\theta_N$ is `theta_n`, and $T$ is daily average air temperature (`deg C`). Setting `theta_n = 1.0` disables temperature adjustment.
