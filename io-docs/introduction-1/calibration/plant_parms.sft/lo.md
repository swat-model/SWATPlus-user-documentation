---
description: Ultimate lower limit enforced on a plant soft-calibration parameter.
---

# lo

**Code reference:** `pl_prms(i)%prm(ilum)%lo` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L160), [clamp](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_plant.f90#L146-L516)).

Absolute minimum parameter value (real, struct default `0.`) enforced via $p = \max(p, l)$ on `pcom%plcur` fields in [`calsoft_plant.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_plant.f90#L146-L516) and on the final `init_val` written by [`pl_write_parms_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_write_parms_cal.f90#L39-L51), where $l$ is `lo`.
