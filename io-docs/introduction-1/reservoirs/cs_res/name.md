---
description: "Name of the reservoir and wetland constituent record"
---

# name (cs\_res)

**Code reference:** `res_cs_data(ires)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_cs_module.f90#L40)).

Primary key identifying each general-constituent parameter record for reservoirs and wetlands. It is referenced by [cs](../reservoir.res_cs/cs.md) in [**reservoir.res\_cs**](../reservoir.res_cs/) (matched in [`res_read_salt_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_salt_cs.f90#L56)) and by wetland constituent links in [`wet_read_salt_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_read_salt_cs.f90#L56).
