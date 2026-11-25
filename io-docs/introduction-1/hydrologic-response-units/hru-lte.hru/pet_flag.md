---
description: Potential ET method
---

# pet\_flag

**Code reference:** `hlt_db(i)%ipet` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L43)).

Potential ET method ([`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L162-L175)):

* `harg`: Hargreaves method
* `p_t`: Priestley-Taylor method

Only the exact value `harg` selects Hargreaves. Any other value uses Priestley-Taylor.
