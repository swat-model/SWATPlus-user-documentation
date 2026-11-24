---
description: "Record name"
---

# name

**Code reference:** `ctbl(ictbl)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_conditions_module.f90#L29)).

Primary key identifying each release condition table. In [`res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read.f90#L121-L125), SWAT+ matches `name` against [rel](../reservoir.res/rel.md) in [**reservoir.res**](../reservoir.res/) whenever `rel` begins with `ctbl_`.
