---
description: Minimum nitrogen concentration for settling
---

# n\_min\_stl

**Code reference:** `res_nut(ires)%conc_nmin` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L121)).

Minimum nitrogen concentration (`ppm`, i.e., `mg/L`; default: `0.10`) below which particulate organic nitrogen and soluble inorganic nitrogen settling ceases. In [`res_nutrient.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_nutrient.f90#L50-L66), SWAT+ computes water-body concentrations as $C = 1000 \, M / V$ (with $M$ in kg and $V$ in $\text{m}^3$) and drives daily loss with $(C - C_{N,\min})$, clamping negative fractions to `0`:

$$f_N = \min\!\left(1,\; \max\!\left(0,\; (C - C_{N,\min}) \, k(T)\right)\right)$$

where $C_{N,\min}$ is `n_min_stl` (ppm) and $k(T)$ is the temperature-adjusted daily nitrogen loss rate.
