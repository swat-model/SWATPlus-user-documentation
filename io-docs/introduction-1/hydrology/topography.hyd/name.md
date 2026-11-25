---
description: Name of the topography record
---

# name (topography.hyd)

**Code reference:** `topo_db(ith)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/topography_data_module.f90#L6)).

Name of the topography record (up to 16 characters). Reference it from [hru-data.hru](../../hydrologic-response-units/hru-data.hru/topo.md) or [rout_unit.rtu](../../routing-units/untitled/topo.md). An unmatched HRU name is logged and selects the built-in topography record. [`hru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_read.f90#L132-L139) · [`topohyd_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/topohyd_init.f90#L25-L38) · [`ru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_read.f90#L233-L239)
