---
description: Plant uptake compensation factor
---

# epco

**Code reference:** `hyd_db(ithyd)%epco` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrology_data_module.f90#L12)).

Dimensionless plant water uptake compensation factor. [`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L372-L377) copies the HRU value to each crop. A larger value lets deeper layers compensate more for unmet uptake in upper layers. For layers other than the second layer, [`pl_waterup.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_waterup.f90#L122-L138) computes $U=U_{\mathrm{cum}}-U_{\mathrm{prev}}(1-c)$, where $c$ is `epco` and $U_{\mathrm{prev}}$ is the previous cumulative potential uptake. The second layer uses $U_{\mathrm{cum}}$, equivalent to $c=1$ for this calculation. Soil water availability limits uptake.
