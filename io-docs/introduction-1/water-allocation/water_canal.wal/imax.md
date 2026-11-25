---
description: "Number of canal records"
---

# imax

**Code reference:** `imax / db_mx%canal` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_canal_read.f90#L15), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_canal_read.f90#L33,L35)).

Number of canal records in `water_canal.wal` (stored in `db_mx%canal`). Allocates `canal`, `canal_om_stor`, `canal_om_out`, and `canal_cs_stor` in [`water_canal_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_canal_read.f90#L38-L41), and sets `gw_ncanal` in [`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1243).
