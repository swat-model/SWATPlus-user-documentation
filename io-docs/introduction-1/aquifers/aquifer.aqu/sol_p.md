---
description: Mineral P concentration in aquifer
---

# sol\_p

**Code reference:** `aqudb(i)%minp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L12)).

Concentration of soluble mineral phosphorus in the aquifer (mg P/L). Unlike nitrate, this concentration stays fixed for the whole simulation. The daily soluble P load leaving the aquifer is set in [`aqu_1d_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L171-L172):

$$
P_{\text{out}} = \frac{V_{\text{in}} \times c_{P}}{1000}
$$

where $P_{\text{out}}$ is the soluble P load (kg), $V_{\text{in}}$ is the water entering the aquifer that day (recharge inflow, m³), and $c_{P}$ is _sol\_p_. In SWAT+ main (6f515368), the groundwater P load therefore scales with the day's recharge inflow volume, not with the computed groundwater flow.
