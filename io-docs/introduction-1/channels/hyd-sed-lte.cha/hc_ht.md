---
description: Phosphorus concentration in channel bank and bed
---

# p\_conc

**Code reference:** `sd_chd(idb)%p_conc` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L40)).

Phosphorus concentration in channel bank and bed material, entered in mg/kg (default `0.30`). SWAT+ uses it in [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L219-L221) to calculate particulate and soluble phosphorus associated with eroded bank sediment. (The bed-erosion addition at [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L266-L272) is commented out.)
