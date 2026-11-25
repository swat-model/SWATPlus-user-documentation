---
description: Fraction of phosphorus in channel bank and bed that is bioavailable
---

# p\_bio

**Code reference:** `sd_chd(idb)%p_bio` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L41)).

This fraction (default `0.30`) splits phosphorus associated with eroded bank sediment between particulate and soluble forms in [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L219-L221) (`solp` receives `p_bio`, and `sedp` receives `1 - p_bio`).
