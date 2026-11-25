---
description: "Secondary action value"
---

# const2

**Code reference:** `dtbl_scen(i)%act(iac)%const2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L24)).

Second numeric action parameter where the action uses it. The implementation does not enforce a change-count limit from this field for `lu_change` or `snow_change`. Both branches increment their counters, and the land-use limit check is commented out. [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L986-L998) · [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L1032-L1045)
