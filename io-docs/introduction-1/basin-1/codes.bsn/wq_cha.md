---
description: Legacy channel water quality code (read but not used in main 6f515368)
---

# wq\_cha

**Code reference:** `bsn_cc%wq` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L37), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_cc.f90#L24)).

Legacy integer control code for channel water quality (struct default `0`). Instream nutrient routing is instead controlled by [qual2e](qual2e.md).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
