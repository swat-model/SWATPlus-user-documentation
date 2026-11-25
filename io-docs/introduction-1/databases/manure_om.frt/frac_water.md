---
description: "Mass fraction of the manure that is water"
---

# frac_water

**Code reference:** `manure_om(it)%frac_water` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/fertilizer_data_module.f90#L38)).

Water fraction $w$ of the wet manure. The application amount $m$ (kg/ha) is treated as solids, and water is added to the soil on top of it ([`pl_manure.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_manure.f90#L66-L81)):

$$W = \frac{m}{1 - w} - m$$

$W$ is kg of water per ha (0.0001 mm per kg/ha). Do not enter 1.
