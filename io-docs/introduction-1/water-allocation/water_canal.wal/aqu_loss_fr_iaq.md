---
description: "Seepage fraction assigned to each aquifer"
---

# aqu_loss_fr(iaq)

**Code reference:** `canal(ic)%aqu_loss_fr(iaq)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L211), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_canal_read.f90#L56)).

Array of `num_aqu` seepage fractions (`fraction`) distributing total canal seepage across aquifers `1..num_aqu`. In [`wallo_canal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_canal.f90#L40-L52), the fraction of current canal storage lost to aquifer `iaq` is:

$$f_{\text{aqu},k} = \frac{V_{\text{seep}} \cdot f_{\text{loss},k}}{V_{\text{stor}}}$$

where $V_{\text{seep}}$ is `seep_tot`, $f_{\text{loss},k}$ is `aqu_loss_fr(iaq)`, and $V_{\text{stor}}$ is `canal_om_stor(ican)%flo`. Each aquifer receives seepage water, `no3`, `solp`, and `cs_aqu` constituents, and canal storage is scaled by $(1 - \sum_k f_{\text{aqu},k})$.
