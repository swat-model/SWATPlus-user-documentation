---
description: Hydraulic conductivity of the wetland bottom
---

# k

**Code reference:** `wet_hyddb(ires)%k` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L88)).

This value supplies the hydraulic conductivity used for wetland seepage. In SWAT+ main (6f515368), a nonpositive input is replaced by `soil(ires)%phys(1)%k` during reading. Here `ires` is the wetland-hydrology reader index, not necessarily an individually matched HRU. See [the default assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_read_hyd.f90#L63).
