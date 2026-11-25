---
description: USLE slope length and slope factor LS
---

# usle\_ls

**Code reference:** `hlt_db(i)%uslels` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L50)).

SWAT+ main (6f515368) calculates the LS factor from [slp](slp.md) and [slp\_len](slp_len.md) when it reads the HRU-lte data ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L237-L242)). That calculation overwrites the entered usle\_ls value, so changing this input currently has no effect.

$$
m = 0.6 \left( 1 - e^{-35.835 \, s} \right)
$$

$$
LS = \left( \frac{L}{22.128} \right)^{m} \left( 65.41 \sin^2 a + 4.56 \sin a + 0.065 \right)
$$

Here *s* is the slope in m/m, *L* is the slope length in m and *a* is the slope angle, arctan *s*.
