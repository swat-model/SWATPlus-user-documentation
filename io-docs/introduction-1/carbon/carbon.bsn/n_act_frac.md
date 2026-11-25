---
description: "Fraction of humus organic nitrogen in the active pool (not used when carbon = 2)"
---

# n\_act\_frac

**Code reference:** `n_act_frac` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L13), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L80), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L492-L493)).

Fraction of humus organic nitrogen kept in the active pool by the static-carbon mineralization routine ([`nut_nminrl.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/nut_nminrl.f90#L107)).

*(Note: In SWAT+ main (`6f515368`), this column is parsed into memory but is not used in simulation calculations.)* `nut_nminrl` runs only when carbon `= 0` ([`hru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L385-L391)), while this file is read only when carbon `= 2` ([`carbon_bsn_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L46)). The `n_act_frac` calibration parameter does affect carbon `= 0` runs.

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `n_act_frac` and uses 0.02. The calibration parameter is `n_act_frac`.
