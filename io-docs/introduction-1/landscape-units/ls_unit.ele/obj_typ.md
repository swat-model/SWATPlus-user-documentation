---
description: Object type of the element
---

# obj\_typ

**Code reference:** `lsu_elem(i)%obtyp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L222), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_read_elements.f90#L127)).

3-character object type code (`character(len=3)`, default `""`). SWAT+ main (`6f515368`) supports `"hru"` for a standard Hydrologic Response Unit and `"hlt"` for an HRU-LTE in [`lsu_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_output.f90#L39-L50), [`basin_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_output.f90#L33-L49), and [`basin_sw_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_sw_init.f90#L39-L76), while carbon outputs, soil nutrient/carbon outputs, and HRU fraction updates check `"hru"` only ([`lsu_carbon_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lsu_carbon_output.f90#L48), [`soil_nutcarb_write.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soil_nutcarb_write.f90#L236), [`hru_fr_change.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_fr_change.f90#L95)).
