---
description: "Record number"
---

# k

**Code reference:** `k` / index `i` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/rec_read_elements.f90#L19-L20), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/rec_read_elements.f90#L159-L162)).

Element index (`integer`, dimensionless, range `1..imax`) indexing `pcu_elem(i)` and referenced by [`elem_cnt`](../rec_catunit.def/elem_cnt.md) in [`rec_catunit.def`](../rec_catunit.def/README.md) and [`rec_reg.def`](../rec_reg.def/README.md).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory and used only to index `pcu_elem` for unused `pcu_out` and unread `pcu_cal` arrays).*
