---
description: Soil water used for the plant uptake concentration
---

# resistance\_n

**Code reference:** `pestdb(ip)%resistance_n` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pesticide_data_module.f90#L22)).

The blended value is used in the uptake equation under [pl\_uptake](pl_uptake.md) ([`pest_pl_up.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_pl_up.f90#L71-L73)).

Sets which soil water content is used to compute the pesticide concentration for plant uptake:

* 0: use the actual soil water content
* 1 (default): use the field-capacity water content
* between 0 and 1: a linear blend, soil water = actual + resistance\_n × max(0, field capacity − actual)
