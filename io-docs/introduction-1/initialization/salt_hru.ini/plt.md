---
description: Intended initial plant salt values (read but not used in main 6f515368)
---

# plt

**Code reference:** `salt_soil_ini(isalti)%plt` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L292)).

Array of `cs_db%num_salts + 5` values allocated and read in [`salt_hru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_hru_read.f90#L51-L71). It is never read in [`salt_hru_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_hru_init.f90#L42-L67) or any simulation routine.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
