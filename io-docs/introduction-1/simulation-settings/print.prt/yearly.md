---
description: Code for printing yearly output
---

# yearly

**Code reference:** `pco%<obj>%y` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L143)).

Character flag (`"y"` = yes, `"n"` = no; Fortran struct default: `"n"`) controlling yearly output for each object row in `print.prt` (after `nyskip` warm-up years).

For the legacy carbon rows `hru_cb` and `hru_cb_vars`, `"l"` enables diagnostic yearly output ([`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L534)). For `gwflow_pump` and `gwflow_flux`, this column contributes to the group switch rather than selecting yearly output independently ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L286-L311)).
