---
description: Percolation coefficient from shallow to deep aquifer
---

# rchg\_dp

**Code reference:** `hlt_db(i)%percc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L24)).

Fraction of the day's soil percolation that moves from the shallow aquifer to the deep aquifer, limited to the shallow storage remaining ([`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L335), [`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L343-L346)):

$$
w_{deep} = w_{perc} \times f
$$

Here *f* is rchg\_dp.
