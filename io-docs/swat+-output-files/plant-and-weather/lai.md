---
description: "Daily leaf area index, summed across plants in a full HRU"
---

# lai

**Code reference:** `bpw_d%lai` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L196)).

The daily full-HRU value sums leaf area index across plants before the day's growth calculation. HRU-LTE reads its current leaf area index after the growth or season-end action. Longer-period rows average the daily values. [Daily calculations](plant-weather-output.md#daily-plant-values)

**Unit:** m2/m2.

[Back to the plant and weather schema](plant-weather-output.md).
