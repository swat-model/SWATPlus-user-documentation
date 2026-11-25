---
description: Annual nitrogen loss-rate coefficient used during the mid-year nutrient period
---

# mid\_n\_stl

**Code reference:** `res_nut(ires)%nsetlr1` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L113)).

Annual particulate nitrogen loss-rate coefficient (`1/year`; historical table default: `5.50`, range `1.0–15.0`; Fortran struct default: `0.`) applied when the current month is between [mid\_start](mid_start.md) and [mid\_end](mid_end.md). SWAT+ divides the annual value by `365` in [`res_read_nut.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_nut.f90#L67) and applies it to organic nitrogen (`orgn`) in [`res_nutrient.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_nutrient.f90#L39-L75):

$$f_N = \min\!\left(1,\; \max\!\left(0,\; (C_N - C_{N,\min}) \, \frac{k_{N,1}}{365} \, \theta_N^{(T - 20)}\right)\right), \qquad M_{\text{orgN,new}} = M_{\text{orgN}} (1 - f_N)$$

where $C_N$ is organic nitrogen concentration (ppm), $C_{N,\min}$ is [n\_min\_stl](n_min_stl.md) (ppm), $k_{N,1}$ is `mid_n_stl` (`1/year`), $\theta_N$ is [theta\_n](theta_n.md), and $T$ is daily average air temperature (`deg C`).
