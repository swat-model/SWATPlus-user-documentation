---
description: Code for printing average annual output
---

# avann

**Code reference:** `pco%<obj>%a` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L144)).

Character flag (`"y"` = yes, `"n"` = no; Fortran struct default: `"n"`) controlling average-annual output at the end of the simulation (averaged over `time%yrs_prt` after `nyskip` warm-up years).

Legacy carbon rows `hru_cb` and `hru_cb_vars` have no average-annual writer call in [`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L529-L545), though any non-`"n"` value on `hru_cb` triggers the legacy end-of-simulation soil snapshot in [`hru_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_output.f90#L315-L318).
