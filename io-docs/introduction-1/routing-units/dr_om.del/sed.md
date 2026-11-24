---
description: "Sediment delivery ratio for this named record"
---

# sed

**Code reference:** `dr(ii)%sed` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L33), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dr_read_om.f90#L60)).

Dimensionless delivery-ratio multiplier (`fraction`; Fortran struct default: `0.`) for total sediment mass. During hydrograph scaling in [`hydout_mult`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1393), SWAT+ computes:

$$H_{\text{out}} = H_{\text{in}} \cdot r_{\text{sed}}$$

where $H_{\text{in}}$ is the incoming sediment load (`metric tons`), $r_{\text{sed}}$ is `dr(ii)%sed`, and $H_{\text{out}}$ is the delivered sediment load (`metric tons`). This ratio is applied to Routing Unit elements in [`ru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_control.f90#L100) ([elements](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_control.f90#L123), excluding recharge at `#L135`) and to standalone `dr` spatial objects in [`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L361).
