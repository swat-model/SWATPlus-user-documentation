---
description: Pesticide percolation coefficient
---

# pest\_perc

**Code reference:** `bsn_prm%percop` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L99), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_prm.f90#L24)).

Controls the concentration of soluble pesticide removed from the top soil layer in surface runoff and layer-1 lateral flow relative to the concentration in percolate ($\beta_{\text{pest}}$, default `0.5`, range `0–1`; values `< 1.e-6` are reset to `0.5` in [`basin_prm_default.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_prm_default.f90#L24)).

In [`pest_lch.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_lch.f90#L59-L82), layer-1 surface runoff and lateral flow use $C_{\text{surf}} = \beta_{\text{pest}}\,C_0$, where $C_0$ is the solubility-capped mobile-water pesticide concentration (`kg/ha/mm`). This parameter is only important if pesticide transport is simulated.

{% hint style="info" %}
The lower *pest\_perc*, the lower the concentration of pesticide in surface runoff and layer-1 lateral flow. If *pest\_perc* = 1.0, surface runoff will have the same pesticide concentration as percolate.
{% endhint %}
