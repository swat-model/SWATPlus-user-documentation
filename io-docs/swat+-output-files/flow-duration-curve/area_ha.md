---
description: "Contributing area"
---

# area_ha

**Code reference:** `ob(icmd)%area_ha` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L340)).

Channel object area stored in `ob(icmd)%area_ha` from the connectivity record. The duration-curve routine uses no area conversion or upstream-area sum in the active write. [Connectivity read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hyd_read_connect.f90#L220-L225), [report write](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/flow_dur_curve.f90#L145-L146).

**Unit:** ha.

This field belongs to a fixed or event-style report rather than the standard daily/monthly/yearly/average-annual series.

[Back to the output table](README.md).
