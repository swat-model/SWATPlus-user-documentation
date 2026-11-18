---
description: "Average temperature of soil layer 2"
---

# sol_tmp

**Code reference:** `bpw_d%sol_tmp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L200)).

For full HRUs, the daily value is the temperature of soil layer 2. Longer periods use a daily mean. HRU-LTE writes zero, which is also the HRU-LTE contribution to LSU and basin values. [Full-HRU assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L853), [HRU-LTE assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L408).

**Unit:** deg C.

[Back to the plant and weather schema](plant-weather-output.md).
