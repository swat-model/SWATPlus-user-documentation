---
description: Organic phosphorus concentration in lateral flow
---

# lat\_orgp

**Code reference:** `hyd_db(ithyd)%lat_orgp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrology_data_module.f90#L23)).

Organic phosphorus concentration $C$ in lateral flow, in mg/L. The built-in value is 0. [`swr_latsed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/swr_latsed.f90#L49-L52) adds $q_{\ell}C/10^4$ to the sediment-associated organic P load, where $q_{\ell}$ is lateral flow depth in mm. The calculation excludes tile flow.

The source uses a divisor of $10^4$, which is 100 times larger than the divisor for a direct conversion from mm and mg/L to kg/ha. This is flagged as a suspected unit-conversion issue.
