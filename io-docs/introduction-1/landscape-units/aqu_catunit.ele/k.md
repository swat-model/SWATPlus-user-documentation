---
description: "Record number"
---

# k

**Code reference:** `k` / index `i` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_elements.f90#L20-L21), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_elements.f90#L171-L174)).

Sequential element index (`integer`, dimensionless, range `1..imax`) indexing `acu_elem(i)` and referenced by [`elem_cnt`](../aqu_catunit.def/elem_cnt.md) in [`aqu_catunit.def`](../aqu_catunit.def/README.md). In [`aqu_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_elements.f90#L169), the maximum index `imax` is stored in `db_mx%aqu_elem`, which must be `> 0` for [`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L621) to call [`basin_aquifer_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_aquifer_output.f90#L19-L22).
