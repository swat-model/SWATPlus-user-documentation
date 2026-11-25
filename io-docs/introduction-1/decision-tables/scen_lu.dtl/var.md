---
description: "Keyword naming the quantity tested"
---

# var

**Code reference:** `dtbl_scen(i)%cond(ic)%var` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L8)).

Keyword naming the quantity tested for each HRU, for example `year_cal`, `jday`, `land_use`, `hyd_soil_group`, or `slope`. All keywords are listed on the [lum.dtl var page](../lum.dtl/var.md). Do not use `days_act`, `prob_unif`, or `prob_unif_lu` here: the scenario reader does not fill the action index, application fraction, or land-use count they need. An unrecognized keyword is ignored without a warning. [`dtbl_scen_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_scen_read.f90#L63-L66) · [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L227-L235)
