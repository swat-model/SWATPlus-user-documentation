---
description: ID of the element
---

# id (ls\_unit.ele)

**Code reference:** `k` / index `i` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_read_elements.f90#L21-L22), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_read_elements.f90#L124-L127)).

Unique sequential element index (`integer`, dimensionless, range `1..imax`). In [`lsu_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_read_elements.f90#L108-L127), SWAT+ first scans the column to find the maximum element index `imax` (saved as `db_mx%lsu_elem` at line 121, which gates `basin_output` in [`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L618)) and uses it as the primary key referenced by [`elements`](../ls_unit.def/elements.md) in [`ls_unit.def`](../ls_unit.def/README.md).
