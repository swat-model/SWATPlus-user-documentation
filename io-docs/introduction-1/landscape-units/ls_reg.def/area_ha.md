---
description: "Region area"
---

# area\_ha

**Code reference:** `lsu_reg(i)%area_ha` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L195), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L106)).

Landscape region area in hectares (`real`, `ha`, struct default `0.0`). Note that [`reg_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reg_read_elements.f90#L1-L205) is never called in SWAT+ main (`6f515368`).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
