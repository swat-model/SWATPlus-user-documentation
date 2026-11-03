---
description: Intended overbank-flooding pointer (printed in connectivity output)
---

# ovfl

**Code reference:** `ob(i)%props2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L347)).

Intended overbank-flooding pointer. This HRU connectivity value does not control HRU flooding calculations in SWAT+ main (6f515368), but it is printed as `props2` in connectivity output when `hydcon` is enabled. Other object types can use `props2` differently.

**Current use:** [connectivity output](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hyd_connect_out.f90#L19).
