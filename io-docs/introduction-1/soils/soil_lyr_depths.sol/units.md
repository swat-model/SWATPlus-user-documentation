---
description: "Units text token read before the depth values"
---

# units

**Code reference:** `units` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L52)).

16-character units text token read on line 3 of `soil_lyr_depths.sol` ([`soils_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L171), [second pass](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L206)), before the depth values. All [`csld`](csld.md) depth values are treated directly as millimeters regardless of this token.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
