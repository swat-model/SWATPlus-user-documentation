---
description: Hydraulic conductivity of the reservoir bottom
---

# k

**Code reference:** `res_hyddb(ires)%k` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L74)).

Saturated hydraulic conductivity of the reservoir bottom (`mm/hr`; historical table default: `0.0`, range `0.0–1.0`; Fortran struct default: `0.01`). If seepage occurs in the reservoir, `k` must be set greater than `0`.

When the basin groundwater-flow option (`bsn_cc%gwflow == 0`) is off, SWAT+ computes daily seepage in [`res_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L162-L166):

$$V_{\text{seep}} = 240 \cdot K_{\text{sat}} \cdot A$$

where $V_{\text{seep}}$ is daily seepage volume ($\text{m}^3$), $K_{\text{sat}}$ is `k` (mm/hr), $A$ is reservoir surface area (ha), and $240 = 24 \times 10$ converts mm/hr over ha to $\text{m}^3\text{/day}$ (capped at remaining reservoir storage in [`res_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L186-L190)). When groundwater-flow mode is active (`gwflow == 1`), reservoir seepage is calculated by `gwflow_reservoir` instead.
