---
description: Maximum canopy storage
---

# can\_max

**Code reference:** `hyd_db(ithyd)%canmx` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrology_data_module.f90#L10)).

Maximum canopy water storage, in mm, at maximum leaf area. For daily and subdaily rainfall, [`sq_canopyint.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sq_canopyint.f90#L45-L53) scales the storage capacity as $C=C_{\max}\operatorname{LAI}/\operatorname{LAI}_{\max}$. The routine skips interception if either leaf-area index total is below 0.001. Daily precipitation first fills available canopy storage. [`sq_canopyint.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sq_canopyint.f90#L80-L88)
