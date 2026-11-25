---
description: "Record name"
---

# name

**Code reference:** `wtp(iwtp)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L152), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_treatment_read.f90#L45)).

25-character name of the water treatment plant (default: `""`). Compared against `wtp_name` in [`wallo_wtps_wuses.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_wtps_wuses.f90#L66) to set `db_num`; however, [`main.f90.in`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/main.f90.in#L104-L108) calls `wallo_wtps_wuses` before `water_treatment_read`, and `wtp%db_num` is not used in simulation.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
