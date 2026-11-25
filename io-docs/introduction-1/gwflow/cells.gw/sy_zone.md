---
description: "Zone for specific yield"
---

# Sy_zone

**Code reference:** `Sy_zone` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L89), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L452)).

Zone number, that is the line position in [zones.gw](../zones.gw/README.md). The cell takes `aquifer_Sy` from this zone ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L462)). It can differ from `K_zone`. A number larger than the number of zones is not checked.
