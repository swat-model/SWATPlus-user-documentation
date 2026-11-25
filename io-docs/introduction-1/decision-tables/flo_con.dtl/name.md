---
description: "Record name"
---

# name

**Code reference:** `dtbl_flo(i)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L29)).

Name of the decision table, up to 40 characters. The reader matches this name against the connectivity `rule` field. SWAT+ main (6f515368) reads this file and matches connectivity `rule` names to table names. The matched table index has no downstream executable reads, so these rules have no effect on routed flow at this commit. [`dtbl_flocon_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_flocon_read.f90#L77-L87)
