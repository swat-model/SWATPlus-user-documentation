---
description: "Organic-phosphorus delivery ratio for this named record"
---

# sedp

**Code reference:** `dr(ii)%sedp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L35), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dr_read_om.f90#L60)).

Dimensionless delivery-ratio multiplier (`fraction`; Fortran struct default: `0.`) for organic phosphorus mass. During hydrograph scaling in [`hydout_mult`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1395), SWAT+ computes:

$$H_{\text{out}} = H_{\text{in}} \cdot r_{\text{sedp}}$$

where $H_{\text{in}}$ is the incoming organic phosphorus load (`kg P`), $r_{\text{sedp}}$ is `dr(ii)%sedp`, and $H_{\text{out}}$ is the delivered load (`kg P`). This ratio is applied to Routing Unit elements in [`ru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_control.f90#L100) ([elements](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_control.f90#L123), excluding recharge at `#L135`) and to standalone `dr` spatial objects in [`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L361).
