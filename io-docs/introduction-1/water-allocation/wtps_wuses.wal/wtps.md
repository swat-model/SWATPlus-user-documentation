---
description: "Number of water treatment plant objects included in the simulation"
---

# wtps

**Code reference:** `wtps` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L6), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_wtps_wuses.f90#L32)).

Number of water treatment plant objects included in the simulation (default: `0`). Used in [`wallo_wtps_wuses.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_wtps_wuses.f90#L34-L43) to allocate `wtp_name`, `wtp_om_stor`, `wtp_cs_stor`, `wtp_om_out`, and `wal_tr_om{d,m,y,a}`, and in [`wallo_treat_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_treat_output.f90#L13) to bound output loops.
