---
description: "Last day of year of the pumping period"
---

# pe_dy_e

**Code reference:** `pe_dy_e` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L139), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L984)).

Day of year (1–365) on which the period ends; that day is included ([`gwflow_pump_ext.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_pump_ext.f90#L39-L41)). It is ignored when [pe_yr_e](pe_yr_e.md) is before the first simulation year.
