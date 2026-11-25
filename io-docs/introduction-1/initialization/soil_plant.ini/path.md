---
description: Pointer to the pathogen initialization file
---

# path

**Code reference:** `sol_plt_ini(ii)%pathc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L133)).

Foreign key referencing [name](../path_hru.ini/name.md) in [**path\_hru.ini**](../path_hru.ini/). During setup, [`hru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_read.f90#L102-L103) resolves `pathc` into `sol_plt_ini(isp_ini)%path`, which is used to initialize and simulate HRU soil pathogens in [`pathogen_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pathogen_init.f90#L67), [`path_ls_process.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_process.f90#L35), [`path_ls_runoff.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_runoff.f90#L22), and [`path_ls_swrouting.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_swrouting.f90#L21).
