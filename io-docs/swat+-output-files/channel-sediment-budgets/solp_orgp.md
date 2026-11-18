---
description: "Phosphorus transferred from soluble to organic phosphorus"
---

# solp_orgp

**Code reference:** `ch_sed_bud(ichan)%solp_orgp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L93)).

Phosphorus transferred from soluble to organic phosphorus.

**Unit:** kg.

The same printed heading can appear in daily, monthly, yearly, and average-annual variants of this family. The reporting interval changes the row period; this page does not infer a total-versus-average rule beyond what the family output and source establish.

The [channel transformation calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_control3.f90#L205) subtracts this mass from the dissolved pool and adds it to the organic pool when `qual2e == 1`. This field is a transfer amount, not the sum of both pools.

[Back to the channel nutrient and sediment budget schema](channel-nutrient-sediment-budget.md).
