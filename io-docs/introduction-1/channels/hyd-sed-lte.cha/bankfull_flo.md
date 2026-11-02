---
description: Bankfull flow factor
---

# bankfull\_flo

**Code reference:** `sd_chd(idb)%bankfull_flo` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L36)).

Factor applied to the channel's flow at bankfull depth (from the channel rating curve) to get the flow above which water spills onto the floodplain.

{% hint style="warning" %}
In SWAT+ main (6f515368), the channel sediment routine overwrites this factor with 1.5 before multiplying it by the rating-curve bankfull flow. The entered factor therefore does not control this sediment-routing path.
{% endhint %}
