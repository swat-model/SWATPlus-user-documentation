---
description: Molecular weight to calculate mixing velocity
---

# mol\_wt

**Code reference:** `pestdb(ip)%mol_wt` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pesticide_data_module.f90#L14)).

**Current use:** sets the water–sediment mixing velocity in channels, proportional to `mol_wt^(−0.6666)` ([`sd_hydsed_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L267)), and converts parent mass to metabolite mass ([`pest_decay.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_decay.f90#L62-L63)). Do not leave it at 0 for a pesticide that is simulated.

{% hint style="warning" %}
Suspected defect (source reading): reservoirs set the mixing velocity to `mol_wt × porosity` ([`res_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_initial.f90#L112)), which increases with molecular weight, unlike the channel formula.
{% endhint %}
