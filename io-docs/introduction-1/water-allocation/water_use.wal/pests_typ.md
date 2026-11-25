---
description: "Source type for pesticide concentrations (`const`, `dtbl`, or `recall`)"
---

# pests_typ

**Code reference:** `wuse(iwuse)%conc(lev)%pests_typ` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L130), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_use_read.f90#L50-L53)).

6-character source type for pesticide concentrations (`const`, `dtbl`, or `recall`) for the water-use object (default: `""`). Only `org_min_typ` and `org_min_name` are crosswalked and evaluated in `6f515368`.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
