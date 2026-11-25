---
description: "Number of regions"
---

# mreg

**Code reference:** `mreg` -> `db_mx%cha_reg` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L19), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L88), [stored](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L121)).

Total number of channel regions defined in [`ch_reg.def`](README.md) (`integer`, dimensionless, default `0`). In [`ch_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L121), `mreg` is stored in `db_mx%cha_reg`, which controls channel soft-calibration region loops in [`calsoft_sed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_sed.f90#L42) (`#L42`, `#L93`, `#L128`, `#L172`) and gates element mapping in [`ch_read_orders_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_orders_cal.f90#L126).
