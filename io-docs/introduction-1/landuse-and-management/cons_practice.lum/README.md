---
description: >-
  This file lists the USLE P values and slope lengths for various conservation
  practices.
---

# cons\_practice.lum

This file defines conservation-practice USLE P factors and maximum slope lengths read by [`cons_prac_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cons_prac_read.f90#L25-L47). In SWAT+ main (`6f515368`), [slp\_len\_max](slp_len_max.md) is read and stored in a temporary variable `sl_len`, but does not alter the HRU USLE `LS` factor ([`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L383-L386)).

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [name](name_consp.md) | Name of the conservation practice | string | n/a | n/a | n/a |
| [usle\_p](usle_p.md) | USLE P factor | real | none | 1.0 | 0.0-1.0 |
| [slp\_len\_max](slp_len_max.md) | Maximum slope length (does not alter `usle_ls` in main 6f515368) | real | m | 1.0 |  |
