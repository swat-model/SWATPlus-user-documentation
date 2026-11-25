---
description: Plant growth soft-calibration switch.
---

# plt

**Code reference:** `cal_codes%plt` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_read_codes.f90#L34), [dispatch](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_control.f90#L94)).

Enables (`"y"`) or disables (`"n"`, struct default) plant-growth soft calibration. When `"y"`, SWAT+ accumulates harvested yield by plant name during management operations ([`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L552), [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L671), [`mgt_sched.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L199), [`mgt_sched.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L312)).

During soft calibration, [`calsoft_plant.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_plant.f90#L49-L516) adjusts `epco`, `pest_stress`, `lai_pot`, and `harv_idx` against targets in `plant_gro.sft` and [`calsoft_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_control.f90#L129) writes updated values via [`pl_write_parms_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_write_parms_cal.f90#L1-L62).
