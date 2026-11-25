---
description: Application efficiency
---

# app\_eff

**Code reference:** `chemapp_db(ichemapp)%app_eff` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L101), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_chemapp.f90#L45)).

Dimensionless application efficiency (`0.0–1.0`, default `0.0`). In SWAT+ main (`6f515368`), `app_eff` is applied only to pesticide applications in [`mgt_sched.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L430) and [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L741):

$$M_{\text{pest}} = M_{\text{sched}} \cdot E_{\text{app}}$$

where $M_{\text{sched}}$ is the scheduled pesticide rate (`kg/ha`), $E_{\text{app}}$ is `app_eff`, and $M_{\text{pest}}$ is the mass passed to [`pest_apply.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_apply.f90#L49-L60). Fertilizer and manure operations take the scheduled rate directly ([`mgt_sched.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L378), [`#L405`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_sched.f90#L405); [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L351), [`#L384`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L384)) without multiplying by `app_eff`.
