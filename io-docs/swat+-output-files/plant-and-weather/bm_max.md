---
description: "Maximum total plant biomass"
---

# bm_max

**Code reference:** `bpw_d%bm_max` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L218)).

Daily full-HRU rows use the current biomass. Monthly and yearly rows use the highest daily biomass in that period. The average-annual writer restores the running peak saved before the final day’s update, so a new peak on that day can be omitted. [Daily updates](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L45-L53), [average-annual write](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L289-L298).

HRU-LTE leaves this field at zero. LSU and basin daily rows use weighted sums of their contributing daily values. Longer LSU and basin periods average those daily values.

**Unit:** kg/ha.

[Back to the plant and weather schema](plant-weather-output.md).
