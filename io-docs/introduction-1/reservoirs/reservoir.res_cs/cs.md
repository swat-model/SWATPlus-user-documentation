---
description: "Name of the constituent input record (cs_res) linked to this reservoir"
---

# cs

**Code reference:** `res_dat_c_cs(ires)%cs` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L21)).

Foreign key referencing [name](../cs_res/name.md) in [**cs\_res**](../cs_res/). In [`res_read_salt_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_salt_cs.f90#L56-L57), SWAT+ matches this name to set `res_dat(ires)%cs`, which is used by [`res_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_initial.f90#L147-L157) to initialize constituent concentrations and by [`res_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L221) during daily constituent routing.
