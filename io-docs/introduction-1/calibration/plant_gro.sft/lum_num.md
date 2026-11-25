---
description: Number of plant target rows in a plant_gro.sft region.
---

# lum\_num

**Code reference:** `plcal(i)%lum_num` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L274), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_regions_cal.f90#L49)).

Integer count (struct default `0`) of plant-growth target rows following the region line. [`pl_read_regions_cal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_read_regions_cal.f90#L80-L86) allocates `plcal(i)%lum` to `lum_num` and reads one plant target record per entry.
