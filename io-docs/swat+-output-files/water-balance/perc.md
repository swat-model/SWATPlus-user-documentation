---
description: "Water percolating below the soil profile"
---

# perc

**Code reference:** `bwb_d%perc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L12)).

In full HRUs, the field reads water leaving the bottom soil layer, including crack flow when enabled. HRU-LTE reports water drained from its single soil-water store above the percolation threshold and adds it to shallow groundwater. [Calculation and reporting details](README.md#evapotranspiration-and-soil-water)

**Unit:** mm.

[Back to the output table](README.md).
