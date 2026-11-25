---
description: "Ground-surface elevation, m"
---

# elev

**Code reference:** `gw_state(i)%elev` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L50), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L449)).

Ground-surface elevation of the cell, in m. It is the top of the aquifer: the bottom is $z - b$, where $b$ is [thck](thck.md) ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L460)). It is also the reference surface for groundwater ET ([exdp](exdp.md)), saturation-excess flow, soil transfer, tile drain depth and floodplain stage. For reservoir exchange, the elevation of the reservoir's own cell is used as the reservoir head ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1153)).
