---
description: Percolation coefficient
---

# perco

**Code reference:** `hyd_db(ithyd)%perco` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrology_data_module.f90#L21)).

Dimensionless input $p$ that controls the multiplier for seepage from the bottom soil layer. For HRUs with a tile drain, [`topohyd_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/topohyd_init.f90#L54-L66) sets $p=0.1$ before converting it. For $p>10^{-9}$, the initialization uses

$$F=\min(1,\exp[-1.0052\ln(-\ln(p-10^{-6}))-5.6862]).$$

For smaller inputs it sets $F=0$. The nested logarithms have a domain problem when $10^{-9}<p\leq10^{-6}$, flagged as a suspected model issue. [`swr_percmicro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/swr_percmicro.f90#L104-L107) multiplies bottom-layer seepage by $F$.
