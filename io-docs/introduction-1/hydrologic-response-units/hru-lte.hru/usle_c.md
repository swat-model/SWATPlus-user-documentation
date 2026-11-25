---
description: USLE cover factor C
---

# usle\_c

**Code reference:** `hlt_db(i)%uslec` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L48)).

USLE cover and management factor C, held constant through the simulation. It is one term of the MUSLE factor used for sediment yield ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L244-L245), [`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L359)):

$$
F = 11.8 \times K \times C \times P \times LS
$$
