---
description: Initial calibration parameter value in plant_parms.sft.
---

# init\_val

**Code reference:** `pl_prms(i)%prm(ilum)%init_val` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L156), [init](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_parms_cal.f90#L97-L103)).

Initial real value (struct default `0.`) assigned to `pcom(iihru)%plcur(ipl)` (`epco`, `pest_stress`, `lai_pot`, or `harv_idx`) in [`pl_read_parms_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_parms_cal.f90#L97-L103) and to `plcal%lum%prm%epco` in [`calsoft_plant.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_plant.f90#L97).

After plant soft calibration finishes, [`pl_write_parms_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_write_parms_cal.f90#L37-L54) updates `init_val`, clamps it to `[lo, up]`, and writes the calibrated records to `plant_parms.cal`.
