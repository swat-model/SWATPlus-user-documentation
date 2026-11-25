---
description: "Actual evapotranspiration"
---

# et

**Code reference:** `bwb_d%et` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L13)).

Full-HRU actual ET is the sum of canopy evaporation, plant transpiration, and the soil evaporation diagnostic. HRU-LTE calculates actual ET from its soil-water store and potential ET, with a cap on remaining soil water. [Calculation and reporting details](README.md#evapotranspiration-and-soil-water)

**Unit:** mm.

[Back to the output table](README.md).
