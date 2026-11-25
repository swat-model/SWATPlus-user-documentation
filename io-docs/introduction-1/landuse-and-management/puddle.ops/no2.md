---
description: "Nitrite concentration (read but not used in main 6f515368)"
---

# no2

**Code reference:** `pudl_db(ic)%no2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L26), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_puddle.f90#L42)).

Nitrite concentration (`ppm`, struct default `0.0`) intended for standing paddy water after puddling. Keep the column in each row so subsequent fields remain aligned.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
