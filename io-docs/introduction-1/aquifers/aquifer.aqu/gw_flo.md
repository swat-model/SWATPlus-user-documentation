---
description: Initial groundwater flow
---

# gw\_flo

**Code reference:** `aqudb(i)%flo` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L8)).

Groundwater flow (mm) from the aquifer at the start of the simulation. [`aqu_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_initial.f90#L170) copies it into the daily state `aqu_d%flo`, which is the starting value of the baseflow recession (see [alpha\_bf](alpha_bf.md)).

SWAT+ also uses this value to set the initial aquifer nutrient masses, [`aqu_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_initial.f90#L174-L175):

$$
M_{0} = \frac{10 \times Q_{0} \times A \times c}{1000}
$$

where $Q_{0}$ is _gw\_flo_ (mm), $A$ is the aquifer area (ha), and $c$ is [no3\_n](no3_n.md) or [sol\_p](sol_p.md) (mg/L). After the first day, `aqu_d%flo` is recomputed every time step, so _gw\_flo_ only affects the start-up period.
