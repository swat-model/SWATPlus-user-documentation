---
description: Intended daily dry biomass removal by trampling (fraction reset to zero)
---

# bm\_tramp

**Code reference:** `grazeop_db(igrazop)%tramp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L127), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_grazeops.f90#L49)).

Intended daily dry biomass removal by trampling (`(kg/ha)/day`; default `0.0`, valid range `0.0–500.0`). In SWAT+ main (`6f515368`), [`pl_graze.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_graze.f90#L59-L60) computes `tramp_plant = graze%tramp / pl_mass(j)%ab_gr_com%m` and immediately overwrites it with `tramp_plant = 0.`, leaving no active simulation effect.

For the intended trampling process, trampling becomes more significant as the number of grazing animals per hectare increases. The input has conventionally been set equal to [bm\_eat](eat.md), assuming that animals trample as much as they eat. This guidance describes intended behavior, not a current calibration effect.
