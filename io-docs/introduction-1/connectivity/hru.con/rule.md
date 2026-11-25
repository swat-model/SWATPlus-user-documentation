---
description: Intended flow-control decision table in flo_con.dtl (does not change outflow in main 6f515368)
---

# rule

**Code reference:** `ob(i)%ruleset` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L348)).

Name of a flow-control decision table in flo\_con.dtl. SWAT+ main (6f515368) [matches the name to a table](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_flocon_read.f90#L77-L87), but no routing calculation uses the match, so it does not change the outflow of the object. A name that matches no table gives no warning. Use null.
