---
description: Initial pesticide mass on plant foliage
---

# plt

**Code reference:** `pest_soil_ini(ipesti)%plt(ipest)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L292)).

Initial pesticide mass on plant foliage (`kg/ha`), read in [`pest_hru_aqu_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_hru_aqu_read.f90#L58). Note that despite the generic struct comment (`ppm or #cfu/m^2`), [`pesticide_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pesticide_init.f90#L59-L68) assigns `plt` directly to the HRU plant pesticide balance (`hpestb_d(ihru)%pest(ipest)%plant`) and distributes it across active plants in the community by leaf-area-index (LAI) fraction:

$$M_{\text{pl},i} = f_{\text{pl},i} \cdot M_{\text{plt}}, \qquad f_{\text{pl},i} = \min\!\left(\frac{\text{LAI}_{i}}{\text{LAI}_{\text{sum}}},\, 1\right)$$

with $f_{\text{pl},i} = 0$ when total community LAI (`pcom(ihru)%lai_sum`) is zero.
