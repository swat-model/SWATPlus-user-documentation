---
description: Oxygen production rate per unit of algal photosynthesis
---

# alg\_o2\_prod

**Code reference:** `ch_nut(ich)%ai3` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L141)).

Mass of oxygen produced per unit mass of algal photosynthesis (`mg O2/mg alg`, default `1.60`, range `1.40–1.80`). In [`ch_read_nut.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_nut.f90#L67), values `<= 0.` are replaced with `1.60`.

In [`ch_watqual4.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_watqual4.f90#L266), `ai3` enters `alg_m_o2 = ai4 * alg_m2 + ai3 * alg_m1`. However, from source reading at `6f515368`, [`ch_watqual4.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_watqual4.f90#L272-L274) omits `alg_m_o2` from the dissolved oxygen source/sink term `factm`, so `alg_o2_prod` does not affect simulated dissolved oxygen.
