---
description: Controls whether print object rows are identified by label or fixed order
---

# use_obj_lbls

**Code reference:** `pco%use_obj_labels` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L171)).

When `use_obj_lbls` is `"n"` (Fortran struct default), [`basin_print_codes_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_print_codes_read.f90#L57) reads the object rows in the fixed positional order expected by the reader and ignores the first-column label. For any other value, [`basin_print_codes_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_print_codes_read.f90#L177-L779) matches each row by the object label in the first column (which is required for per-family/LSU carbon rows and GWFlow rows) and halts with `error stop` on an unrecognized label ([`basin_print_codes_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_print_codes_read.f90#L770-L776)). This field does not control database-format output.
