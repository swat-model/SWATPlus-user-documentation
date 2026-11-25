---
description: >-
  Plant uptake factor for pesticide
---

# pl\_uptake

**Code reference:** `pestdb(ip)%pl_uptake` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pesticide_data_module.f90#L20)).

Plant uptake factor (a transpiration-stream concentration factor) used for root uptake by growing plants. By default the mass taken from a soil layer is ([`pest_pl_up.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_pl_up.f90#L94-L97)):

$$U = f\,\frac{W}{S + W + K}\,M$$

$U$ is uptake (kg/ha), $f$ is `pl_uptake`, $W$ the water taken up from the layer (mm), $S$ the effective soil water (see [resistance\_n](resistance_n.md)), $K$ the sorption capacity from [soil\_ads](soil_ads.md), and $M$ the pesticide mass in the layer.
