---
description: USLE soil erodibility factor K
---

# usle\_k

**Code reference:** `hlt_db(i)%uslek` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L47)).

USLE soil erodibility factor K. It is one term of the MUSLE factor used for sediment yield ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L244-L245), [`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L359)):

$$
F = 11.8 \times K \times C \times P \times LS
$$
