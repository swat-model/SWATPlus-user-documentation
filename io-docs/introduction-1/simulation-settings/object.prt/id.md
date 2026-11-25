---
description: ID of the object print record
---

# id

**Code reference:** `ii` / `k` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/object_read_output.f90#L15-L16)).

Integer record index for each row in `object.prt`. During reading in [`object_read_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/object_read_output.f90#L34-L53), SWAT+ first scans the file to find `imax` (maximum `id`) and `mobj_out` (row count), allocates `ob_out(0:imax)`, and stores each row into `ob_out(ii)`.

Because the subsequent initialization loop processes `ob_out(i)` for `i = 1, mobj_out` ([`object_read_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/object_read_output.f90#L48-L118)), `id` values must be sequential integers starting at `1` (`1, 2, ..., mobj_out`).
