---
description: Bank erosion exponent (currently not used)
---

# erod\_fact

**Code reference:** `sd_chd(idb)%bank_exp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L27)).

This input is intended to be an exponent in a bank-erosion equation. In SWAT+ main (6f515368) that equation is commented out in [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L195) (and `erod_fact` is not referenced in executable calculations), so from source reading changing `erod_fact` has no effect on simulation results.
