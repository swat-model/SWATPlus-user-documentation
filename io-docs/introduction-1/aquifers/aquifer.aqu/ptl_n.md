---
description: Organic carbon in aquifer (printed but not used in routing or constituent calculations)
---

# carbon

**Code reference:** `aqudb(i)%cbn` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L13)).

Organic carbon content of the aquifer (%). SWAT+ copies this value into `aqu_d%cbn` in [`aqu_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_initial.f90#L176) and writes it to [aquifer output](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_output.f90#L22). Calibration can also change it. No aquifer water, nutrient, or pesticide calculation reads it.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
