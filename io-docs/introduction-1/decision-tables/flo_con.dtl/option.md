---
description: "Action-specific option whose meaning depends on the action type (e.g. rate input"
---

# option

**Code reference:** `dtbl_flo(i)%act(iac)%option` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L21)).

Action option token in the parsed flow-control record. SWAT+ main (6f515368) reads this file and matches connectivity `rule` names to table names. The matched table index has no downstream executable reads, so these rules have no effect on routed flow at this commit. [`dtbl_flocon_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_flocon_read.f90#L77-L87)
