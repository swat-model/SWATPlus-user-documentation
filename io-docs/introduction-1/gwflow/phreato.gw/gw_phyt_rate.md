---
description: "Transpiration rate at that depth, m/day"
---

# gw_phyt_rate

**Code reference:** `gw_phyt_rate(i)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L433), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1431)).

Transpiration rate, in m/day, at the depth on the same line. The daily uptake from a cell is the interpolated rate times the cell's phreatophyte area, limited to the water stored in the cell ([`gwflow_phreatophyte.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_phreatophyte.f90#L36-L43)).
