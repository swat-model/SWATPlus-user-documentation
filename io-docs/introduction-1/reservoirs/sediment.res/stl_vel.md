---
description: Sediment settling velocity input (read but not used by the model)
---

# stl\_vel

**Code reference:** `res_sed(ires)%velsetlr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L105)).

Sediment settling velocity input (`m/d`; historical table default: `1.0`; Fortran struct default: `0.`), read from `sediment.res` by [`res_read_sed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_sed.f90#L55). Although [`cal_parm_select.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L848) can adjust the stored field, active reservoir and wetland settling in [`res_sediment.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_sediment.f90#L37) instead uses `sed_stlr_co = exp(-0.184 * d50)` computed in [`res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read.f90#L143).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
