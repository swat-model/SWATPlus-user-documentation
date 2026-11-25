---
description: "Number of regions"
---

# mreg

**Code reference:** `mreg` -> `db_mx%rec_reg` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/rec_read_elements.f90#L18), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/rec_read_elements.f90#L86), [stored](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/rec_read_elements.f90#L119)).

Total number of point-source regions defined in [`rec_reg.def`](README.md) (`integer`, dimensionless, default `0`), stored in `db_mx%rec_reg`.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
