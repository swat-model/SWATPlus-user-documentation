---
description: "Nitrogen added to plant biomass via fixation"
---

# fixn

**Code reference:** `bnb_d%fixn` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L88)).

The plant uptake routine calls `pl_nfix` when the plant fixation coefficient exceeds `1.e-6`. The calculation uses unmet N demand, soil water, soil nitrate, and plant growth stage, and caps the result at unmet demand and `nfixmx`. The printed diagnostic is the current value of the daily `fixn` variable. Each fixation call can replace it, and a non-fixing plant call can reuse the preceding value when adding fixation to uptake. [daily initialization](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/varinit.f90#L97-L101), [fixation calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_nfix.f90#L44-L87), [uptake call and addition](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_nup.f90#L90-L100).

**Unit:** kg/ha.

The same printed heading can appear in daily, monthly, yearly, and average-annual variants of this family. The reporting interval changes the row period; this page does not infer a total-versus-average rule beyond what the family output and source establish.

[Back to the output table](README.md).
