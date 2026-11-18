---
description: "Surface-runoff run-on from upland landscape"
---

# surq_runon

**Code reference:** `bwb_d%surq_runon` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L29)).

Full HRUs add the incoming surface volume directly to the tile contribution converted to depth over the receiving HRU. The printed value therefore mixes m³ and mm where both terms contribute. The wetland inflow branch bypasses this diagnostic. HRU-LTE reports zero. [Calculation and reporting details](README.md#run-on-and-water-yield)

**Unit:** Printed as mm. The source combines m³ and mm.

[Back to the output table](README.md).
