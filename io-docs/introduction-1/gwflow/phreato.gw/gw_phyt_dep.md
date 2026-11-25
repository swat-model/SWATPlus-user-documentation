---
description: "Water-table depth below ground, m"
---

# gw_phyt_dep

**Code reference:** `gw_phyt_dep(i)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L432), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1431)).

Depth of the water table below the ground surface, in m, at which the rate on the same line applies. List depths in increasing order. For a depth between two points the rate is interpolated linearly ([`gwflow_phreatophyte.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_phreatophyte.f90#L31-L37)):

$$r = r_{k} - \frac{w - w_{k}}{w_{k+1} - w_{k}} \, (r_{k} - r_{k+1})$$

where $w = z - h$ is the water-table depth. Shallower than the first depth or deeper than the last, the rate is 0.
