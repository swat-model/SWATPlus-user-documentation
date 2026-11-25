---
description: Object ID of the element
---

# obj\_typ\_no

**Code reference:** `lsu_elem(i)%obtypno` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L223), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_read_elements.f90#L127)).

Sequential integer object ID within the object type specified by [`obj_typ`](obj_typ.md) (`integer`, dimensionless, default `0`). It resolves the HRU index (when `obj_typ = "hru"`) or HRU-LTE index (when `obj_typ = "hlt"`) during basin output aggregation, initialization, soil nutrient/carbon output, and HRU fraction updates ([`basin_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_output.f90#L30-L46), [`basin_sw_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_sw_init.f90#L36-L54), [`basin_ls_pest_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_ls_pest_output.f90#L31), [`soil_nutcarb_write.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_write.f90#L233), [`hru_fr_change.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_fr_change.f90#L96)).
