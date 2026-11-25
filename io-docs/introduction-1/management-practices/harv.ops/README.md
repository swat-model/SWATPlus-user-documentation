---
description: This file contains pre-defined harvest operations.
---

# harv.ops

This file defines pre-defined harvest operations read by [`mgt_read_harvops.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_harvops.f90#L25-L51). Each operation is referenced for both harvest (`harv`/`harvest`) and harvest-and-kill (`hvkl`/`harvest_kill`) actions to harvest plant yield or residue while leaving or terminating the stand according to the scheduled operation.

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [name](name_harvops.md) | Harvest operation name | string | n/a | n/a | n/a |
| [harv\_typ](harv_typ.md) | Harvest type | string | n/a | n/a | n/a |
| [harv\_idx](harv_idx.md) | Harvest index target specified at harvest | real | fraction | 0.0 | 0.0-1.0 |
| [harv\_eff](harv_eff.md) | Harvest efficiency | real | fraction | 0.0 | 0.0-1.0 |
| [harv\_bm\_min](harv_bm_min.md) | Minimum biomass to allow harvest | real | kg/ha | 0.0 | |
