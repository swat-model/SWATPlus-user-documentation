---
description: "Selector or referenced record name"
---

# file_pointer

**Code reference:** `dtbl_scen(i)%act(iac)%file_pointer` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L25)).

For `lu_change`, enter a record name from [landuse.lum](../../landuse-and-management/landuse.lum/). For `snow_change`, enter a record name from [snow.sno](../../hydrology/snow.sno/). For `hru_fr_update`, enter the filename of the updated routing-unit element table. [`dtbl_scen_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_scen_read.f90#L78-L97) · [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L978-L984)
