---
description: Calibration group
---

# cal\_group

**Code reference:** `lum(ilu)%cal_group` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_data_module.f90#L7), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/landuse_read.f90#L56)).

User-defined character string (`len=40`, default `""`) grouping HRUs for calibration and conditional logic. Although the source declaration comment says `(not currently used)`, SWAT+ main (`6f515368`) copies `lum(ilu)%cal_group` to `hru(ihru)%cal_group` in [`hrudb_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hrudb_init.f90#L29) and to `hru(iihru)%lum_group_c` in [`hru_lum_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lum_init.f90#L23).

The copied value is tested as a target condition in [**calibration.cal**](../../calibration/calibration.cal/README.md) ([`cal_conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_conditions.f90#L100)), in `cal_group` decision-table conditions ([`conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditions.f90#L666)), and when matching HRUs to regional soft-calibration land-use groups.
