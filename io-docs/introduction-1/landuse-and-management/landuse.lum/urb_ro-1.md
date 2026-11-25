---
description: Urban runoff simulation option
---

# urb\_ro

**Code reference:** `lum(ilu)%urb_ro` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_data_module.f90#L13), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L56)).

Character string (`len=40`, default `""`) selecting the urban runoff sediment and nutrient loading algorithm. Copied to `hru(iihru)%luse%urb_ro` in [`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L389) and evaluated in [`hru_urban.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_urban.f90#L91-L140); any other string (such as `"null"`) skips urban runoff loading calculations.

| Option             | Description                                                    |
| ------------------ | -------------------------------------------------------------- |
| `usgs_reg`         | USGS linear regression equations (Driver and Tasker, 1988)     |
| `buildup_washoff`  | SWMM-style build-up/wash-off algorithm (Huber and Dickinson, 1988) |

#### References

> Driver and Tasker (1988)
>
> Huber and Dickinson (1988)
