---
description: "Water remaining in the saturation-excess routing store"
---

# lagsatex

**Code reference:** `bwb_d%lagsatex` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L44)).

Daily full-HRU rows read the water left in the saturation-excess store after subtracting the daily release. HRU-LTE reports zero. Monthly and yearly rows sum daily store depths. The average-annual row divides those sums by the reporting-year count. [Calculation and reporting details](README.md#water-held-in-routing-stores)

**Unit:** mm.

[Back to the output table](README.md).
