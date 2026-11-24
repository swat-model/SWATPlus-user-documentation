---
description: Intended salt-initialization pointer (read but not used in initial.res in main 6f515368)
---

# salt

**Code reference:** `res_init_dat_c(ires)%salt` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L48)).

Intended salt-initialization pointer, parsed from `initial.res` by [`res_read_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_init.f90#L51). Active reservoir salt initialization instead uses the [salt](../reservoir.res_cs/salt.md) pointer in [**reservoir.res\_cs**](../reservoir.res_cs/), matched against [**salt\_res**](../salt_res/) in [`res_read_salt_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read_salt_cs.f90#L48-L49).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
