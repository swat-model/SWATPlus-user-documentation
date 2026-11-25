---
description: "Exponential coefficient controlling bed erosion rate for the channel reach"
---

# bed_exp

**Code reference:** `sd_chd1(idb)%bed_exp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L57)).

Exponential coefficient $\beta$ controlling bed erosion rate in [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L258) ($e_{\text{btm}} = 0.0001\,(v / v_{\text{cr}})^{\beta}$, struct default `1.5`).

{% hint style="warning" %}
In SWAT+ main (`6f515368`), [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L81) resets `sd_ch(ich)%bed_exp = 1.0` on every call before bed erosion is evaluated (and the resulting `bed_ero` addition to `ht1` at [`sd_channel_sediment3.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L272) is commented out). Based on source reading, values entered in `sed_nut.cha` do not affect simulation results.
{% endhint %}
