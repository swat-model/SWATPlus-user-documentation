---
description: "Number of demand objects receiving manure from this allocation object"
---

# trn\_obs

**Code reference:** `mallo(imro)%trn_obs` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_allocation_module.f90#L61), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_allocation_read.f90#L52)).

Integer count (default `0`) of manure demand (receiving) objects in the allocation block. It allocates `mallo(imro)%trn` and controls receiver row reading in [`manure_allocation_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_allocation_read.f90#L58-L83), daily demand evaluation and application in [`mallo_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mallo_control.f90#L39-L51), and demand reporting in [`manure_demand_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_demand_output.f90#L14).
