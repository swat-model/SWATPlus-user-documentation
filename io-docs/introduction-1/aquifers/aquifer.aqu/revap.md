---
description: Groundwater revap coefficient
---

# revap

**Code reference:** `aqudb(i)%revap_co` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L17)).

Water can move from the aquifer into the overlying unsaturated zone. This happens when capillary-fringe water evaporates and is replaced from below, or when deep-rooted plants take up water directly from the aquifer. The process matters most where the saturated zone is shallow or deep-rooted plants are present.

When the water table is shallower than [revap\_min](revap_min.md), [`aqu_1d_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L130-L135) calculates revap as:

$$
E_{\text{revap}} = \min\left(\text{PET} \times \beta_{\text{rev}},\; S\right)
$$

where PET is the daily potential evapotranspiration (mm), $\beta_{\text{rev}}$ is _revap_, and $S$ is aquifer storage (mm). As _revap_ approaches 0, revap is restricted. As it approaches 1, revap approaches PET.
