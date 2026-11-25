---
description: Code for printing daily output
---

# daily

**Code reference:** `pco%<obj>%d` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L141)).

Character flag (`"y"` = yes, `"n"` = no; Fortran struct default: `"n"`) controlling daily output for each object row in `print.prt`. Daily printing is additionally gated by `nyskip`, `day_start`, `yrc_start`, `day_end`, `yrc_end`, and `interval`.

For the legacy carbon rows `hru_cb` and `hru_cb_vars`, `"l"` enables diagnostic daily output ([`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L530)). For `gwflow_pump` and `gwflow_flux`, this column acts as part of a group switch rather than an independent daily toggle ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L286-L311)).
