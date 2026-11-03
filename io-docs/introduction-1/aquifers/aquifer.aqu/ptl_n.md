---
description: Organic carbon in aquifer (printed but not used in routing or constituent calculations)
---

# carbon

**Code reference:** `aqudb(i)%cbn` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L13)).

Organic carbon in aquifer (%). SWAT+ main (6f515368) copies this value into `aqu_d%cbn` and prints it in aquifer output, but it does not control aquifer routing or constituent calculations. The former pesticide-Kd explanation does not describe this version.

**Current use:** [initialization copy](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_initial.f90#L176); [aquifer output](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_output.f90#L22).
