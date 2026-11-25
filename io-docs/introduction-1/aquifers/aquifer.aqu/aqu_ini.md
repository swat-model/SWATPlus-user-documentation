---
description: Pointer to the aquifer constituent initialization record in initial.aqu_cs
---

# init

**Code reference:** `aqudb(i)%aqu_ini` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L7)).

Foreign key that matches the `name` field in [initial.aqu\_cs](../../initialization/initial.aqu_cs/). [`aqu_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L82) uses this match to initialize the aquifer's pesticide and pathogen constituent data. Although the source comment says it points to `initial.aqu`, it does not select a record from [initial.aqu](../initial.aqu/).
