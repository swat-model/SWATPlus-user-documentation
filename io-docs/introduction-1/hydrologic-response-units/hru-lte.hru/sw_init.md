---
description: Initial soil water (fraction of available water capacity)
---

# sw\_init

**Code reference:** `hlt_db(i)%sw` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L25)).

Initial soil water as a fraction of the profile available water capacity ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L261)):

$$SW_0 = f \times AWC$$

where $SW_0$ is initial soil water (`mm`), $f$ is `sw_init` (fraction), and $AWC$ is profile available water capacity (`mm`).
