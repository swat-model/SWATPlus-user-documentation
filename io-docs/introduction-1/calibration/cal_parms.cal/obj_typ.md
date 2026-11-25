---
description: Object type impacted by a calibration parameter in cal_parms.cal.
---

# obj\_typ

**Code reference:** `cal_parms(i)%ob_typ` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L1-L12), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_read.f90#L42)).

Object type string (up to 25 characters, struct default `"plt"`). Determines the default element count when `obj_tot == 0` in [`cal_parmchg_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parmchg_read.f90#L108-L146), supporting `hru`, `rdt`, `plt`, `lyr`, `sol`, `hlt`, `ru`, `aqu`, `cha`, `swq`, `res`, `sdc`, `rte`, `bsn`, `pcp`, `tmp`, `gwf`, `gwf_riv`, and `gwf_sgl`.

In [`cal_conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_conditions.f90#L108-L112), `sol`, `rdt`, `plt`, and `cli` trigger specialized layer, decision-table action, plant-community, and climate time-window loops instead of direct single-parameter updates.
