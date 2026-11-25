---
description: "POR receiving object type"
---

# typ (POR)

**Code reference:** `pou(ipou)%por(ipor)%typ` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L38), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L102)).

10-character receiving object type code (default: `""`). Dispatched in [`wallo_return.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_return.f90#L30-L68) to route return flows to `cha` (`ob%trans`), `res`, `aqu`, `wtp` (`wtp_om_stor`), `use` (`wuse_om_stor`), `wtow` (`wtow_om_stor`), `can` (`canal_om_stor`), `orcv` (`orcv_om`), or `hru` (no-op in `6f515368`).
