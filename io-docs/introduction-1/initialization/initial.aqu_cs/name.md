---
description: "Record name"
---

# name

**Code reference:** `aqu_init_dat_c_cs(iaqu)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L87)).

Name of the aquifer constituent initialization record, read in [`aqu_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L63). It is matched against [init](../../aquifers/aquifer.aqu/aqu_ini.md) (`aqudb(iaq)%aqu_ini`) in [**aquifer.aqu**](../../aquifers/aquifer.aqu/) for `pest` ([`aqu_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L82)) and `path` ([`aqu_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L99)), whereas `salt` and `cs` index `aqu_init_dat_c_cs(iaq)` positionally by aquifer index `iaq` ([`aqu_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L115), [`#L133`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L133)).
