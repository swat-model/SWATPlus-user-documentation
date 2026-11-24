---
description: Minimum phosphorus concentration for settling
---

# p\_min\_stl

**Code reference:** `res_nut(ires)%conc_pmin` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L122)).

Minimum phosphorus concentration (`ppm`, i.e., `mg/L`; default: `0.01`) below which particulate phosphorus and soluble phosphorus settling ceases. In [`res_nutrient.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_nutrient.f90#L51-L69), SWAT+ computes water-body concentrations as $C = 1000 \, M / V$ (with $M$ in kg and $V$ in $\text{m}^3$) and drives daily loss with $(C - C_{P,\min})$, clamping negative fractions to `0`:

$$f_P = \min\!\left(1,\; \max\!\left(0,\; (C - C_{P,\min}) \, k(T)\right)\right)$$

where $C_{P,\min}$ is `p_min_stl` (ppm) and $k(T)$ is the temperature-adjusted daily phosphorus loss rate.
