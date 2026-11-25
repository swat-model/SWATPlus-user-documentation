---
description: Code for printing monthly output
---

# monthly

**Code reference:** `pco%<obj>%m` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L142)).

Character flag (`"y"` = yes, `"n"` = no; Fortran struct default: `"n"`) controlling monthly output for each object row in `print.prt` (after `nyskip` warm-up years).

For the legacy carbon rows `hru_cb` and `hru_cb_vars`, `"l"` enables diagnostic monthly output ([`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L532)). In GWFlow overrides, `gwflow_heat` and `gwflow_flux` do not enable output via the monthly column ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L292-L311)).
