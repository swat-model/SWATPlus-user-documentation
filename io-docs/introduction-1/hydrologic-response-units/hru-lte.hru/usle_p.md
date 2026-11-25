---
description: USLE support practice factor P
---

# usle\_p

**Code reference:** `hlt_db(i)%uslep` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L49)).

USLE support practice factor P. It is one term of the MUSLE factor used for sediment yield ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L244-L245), [`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L359)):

$$
F = 11.8 \times K \times C \times P \times LS
$$
