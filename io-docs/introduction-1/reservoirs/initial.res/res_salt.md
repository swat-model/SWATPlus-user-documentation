---
description: Intended salt-initialization pointer (read but not used in initial.res in main 6f515368)
---

# salt

**Code reference:** `res_init_dat_c(ires)%salt` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L48)).

Intended salt-initialization pointer. SWAT+ main (6f515368) reads this `initial.res` field but does not use its value afterward. Active reservoir salt initialization uses the salt pointer in `reservoir.res_cs`.
