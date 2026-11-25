---
description: Time of concentration
---

# t\_conc

**Code reference:** `hlt_db(i)%tc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L15)).

Time of concentration in minutes. SWAT+ converts it to seconds ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L272)) and uses it for the surface runoff peak rate ([`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L354)), which affects sediment yield:

$$
q_{peak} = \frac{2 \, Q}{1.5 \, t_c}
$$

Here *Q* is the runoff volume in m³. Enter a positive value. The fallback for a value of 0 divides by a slope variable that is never set ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L247-L253)), so it does not give a usable time.
