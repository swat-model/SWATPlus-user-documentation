---
description: Concentration of nitrate in irrigation water
---

# no3\_ppm

**Code reference:** `irrop_db(irr_op)%no3` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L12), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_irrops.f90#L48)).

Concentration of nitrate in irrigation water (`mg/kg`; default `0.0`).

During paddy irrigation setup in [`mgt_sched.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L534), SWAT+ copies `irrop_db%no3` into `irrig(j)%no3` and adds the resulting nitrate mass (`kg N`) to ponded wetland or paddy water storage in [`wetland_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wetland_control.f90#L81):

$$\Delta N_{\text{wet,NO3}} = 0.001\, C_{\text{NO3}} \cdot I_{\text{app}} \cdot A_{\text{wsa1}}$$

where $C_{\text{NO3}}$ is `no3_ppm` (`mg/kg`), $I_{\text{app}}$ is applied irrigation depth (`mm`), and $A_{\text{wsa1}}$ is `hru(j)%area_ha * 10` (`m^3/mm`). This concentration is not applied to upland soil irrigation outside the wetland/paddy pathway.
