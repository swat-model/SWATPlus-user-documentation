---
description: "Weir input name linked to this reservoir (not used)"
---

# weir

**Code reference:** `res_dat_c_cs(ires)%weir` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L19)).

Character name parsed into `res_dat_c_cs(ires)%weir` by [`res_read_salt_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_salt_cs.f90#L43). `res_dat%weir` is never assigned or read during simulation; reservoir weir releases are instead linked through [**res\_rel.dtl**](../../decision-tables/res_rel.dtl/).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
