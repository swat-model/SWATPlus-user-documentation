---
description: Maximum slope length
---

# slp\_len\_max

**Code reference:** `cons_prac(icp)%sl_len_mx` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_data_module.f90#L53), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cons_prac_read.f90#L45)).

Maximum slope length (`m`, default `1.0`; example `121.0 m`) associated with the conservation practice. In [`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L383-L385), SWAT+ computes `sl_len = amin1(hru(iihru)%topo%slope_len, cons_prac(icp)%sl_len_mx)`, but the `usle_ls` equation on line `384` uses `hru(iihru)%topo%slope_len` directly rather than `sl_len`. Consequently, `sl_len` is never read and `slp_len_max` has no effect on simulated erosion in SWAT+ main (`6f515368`).
