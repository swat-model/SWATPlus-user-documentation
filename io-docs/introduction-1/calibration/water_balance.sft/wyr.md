---
description: Target total water yield ratio for baseflow-mode soft calibration.
---

# wyr

**Code reference:** `lscal(ireg)%lum(ilum)%meas%wyr` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L89), [conversion](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L94-L95)).

Dimensionless target ratio of total water yield to precipitation ($\text{WYLD} / P$, struct default `0.`). Used when `hyd_hru /= "a"` (`b` or `y` mode) in [`lcu_read_softcal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L94-L95) to compute `srr` and `bfr`, and in [`calsoft_hyd_bfr_et.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd_bfr_et.f90#L45) and [`calsoft_hyd_bfr_pet.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd_bfr_pet.f90#L39) to calibrate `esco` and `pet_co`.
