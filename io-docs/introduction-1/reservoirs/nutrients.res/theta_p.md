---
description: Temperature adjustment for phosphorus loss (settling)
---

# theta\_p

**Code reference:** `res_nut(ires)%theta_p` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L120)).

Dimensionless Arrhenius temperature adjustment factor for phosphorus settling and soluble phosphorus loss (default: `1.0`). SWAT+ calls [`theta.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/theta.f90#L17) from [`res_nutrient.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_nutrient.f90#L61) for particulate phosphorus and [`res_nutrient.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_nutrient.f90#L67) for soluble phosphorus:

$$k(T) = k_{20} \, \theta_P^{(T - 20)}$$

where $k_{20}$ is the daily loss rate at 20 °C (`1/day`), $\theta_P$ is `theta_p`, and $T$ is daily average air temperature (`deg C`). Setting `theta_p = 1.0` disables temperature adjustment.
