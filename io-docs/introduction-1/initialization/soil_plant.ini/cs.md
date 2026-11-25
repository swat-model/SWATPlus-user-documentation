---
description: Pointer to the constituent soil initialization
---

# cs

**Code reference:** `sol_plt_ini(ii)%csc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L136)).

Foreign key referencing [name](../cs_hru.ini/name.md) in [**cs\_hru.ini**](../cs_hru.ini/) that sets initial dissolved and sorbed general-constituent concentrations in soil. This column is read only when [event](../../basin-1/codes.bsn/event.md) (`bsn_cc%nam1`) in [**codes.bsn**](../../basin-1/codes.bsn/) is nonzero ([`soil_plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_plant_init.f90#L46-L52)). During setup, [`hru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_read.f90#L123-L124) resolves `csc` into `sol_plt_ini(isp_ini)%cs`, which [`cs_hru_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_hru_init.f90#L43) uses to initialize HRU soil constituent pools.
