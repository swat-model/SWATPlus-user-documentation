---
description: Grassed-waterway activation token
---

# flag

**Code reference:** `grwaterway_db(igrwwop)%grwat_i` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L49)).

This column is parsed from the input file, but [`structure_set_parms`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/structure_set_parms.f90#L68) unconditionally sets the HRU flag to 1 when the grassed-waterway record is applied. The user-supplied value is therefore ignored; the column serves as a positional placeholder in the file format.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but its value is overridden to 1 by `structure_set_parms` and is not used directly.)*
