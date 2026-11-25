---
description: "Number of regions"
---

# mreg

**Code reference:** `mreg` -> `db_mx%cha_reg` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L19), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L39), [stored](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L77)).

Total number of channel cataloging units defined in [`ch_catunit.def`](README.md) (`integer`, dimensionless, default `0`). In [`ch_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_elements.f90#L77), `mreg` is written to `db_mx%cha_reg` (overwritten at line 121 if [`ch_reg.def`](../ch_reg.def/README.md) exists); `db_mx%cha_reg` is used as a loop bound in [`calsoft_sed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_sed.f90#L42) and checked in [`ch_read_orders_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_orders_cal.f90#L126).
