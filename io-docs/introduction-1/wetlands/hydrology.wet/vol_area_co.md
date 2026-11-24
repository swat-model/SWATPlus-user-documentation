---
description: Volume surface area coefficient for HRU impoundment
---

# vol\_area\_co

**Code reference:** `wet_hyddb(ires)%acoef` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L90)).

A linear coefficient (default `1.0`) controlling how surface area fraction responds to changes in water depth $h$:

$$\text{wet\_fr} = 1 + \text{vol\_area\_co} \cdot h \quad (\text{clipped to } [0.01, 1.0])$$

Higher values cause the wetland surface area to expand and contract more rapidly as depth fluctuates relative to principal storage. Depth $h$ is determined each time step by the quadratic interaction of [`vol_dp_a`](vol_dp_a.md) and [`vol_dp_b`](vol_dp_b.md).
