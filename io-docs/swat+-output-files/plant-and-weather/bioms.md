---
description: "Daily plant biomass"
---

# bioms

**Code reference:** `bpw_d%bioms` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L197)).

The daily full-HRU value copies the plant-community biomass record before the controller clamps any negative biomass to zero. HRU-LTE reports its current dry matter, which the season-end action can reset to zero before output. Longer-period rows average the daily values. [Daily calculations](plant-weather-output.md#daily-plant-values)

**Unit:** kg/ha.

[Back to the plant and weather schema](plant-weather-output.md).
