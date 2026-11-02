---
description: Intended daily dry biomass removal by trampling (fraction reset to zero)
---

# bm\_tramp

**Code reference:** `grazeop_db(igrazop)%tramp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L127)).

Intended daily dry biomass removal by trampling ((kg/ha)/day). SWAT+ main (6f515368) computes a trampling fraction from this input, then overwrites that fraction with zero before applying biomass changes.

For the intended trampling process, trampling becomes more significant as the number of grazing animals per hectare increases. The input has conventionally been set equal to [bm_eat](eat.md), assuming that animals trample as much as they eat. This guidance describes intended behavior, not a current calibration effect.

**Current use:** [trampling-fraction calculation and reset](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_graze.f90#L59).
