---
description: "Type of action performed (e.g. reservoir release, irrigate, fertilize)"
---

# typ

**Code reference:** `dtbl_scen(i)%act(iac)%typ` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L17)).

The scenario reader resolves record names for `lu_change` and `snow_change`. The general action routine also contains scenario-related actions such as `hru_fr_update` and `p_factor`. Use action types appropriate to the scenario, since this reader does not perform the management operation lookups provided by `lum.dtl`. [`dtbl_scen_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_scen_read.f90#L78-L97) · [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L978-L999) · [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L1032-L1055)
