---
description: Name of the atmospheric deposition station
---

# atmo\_dep

**Code reference:** `wst(i)%wco_c%atmodep` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/climate_module.f90#L124)).

The name of the atmospheric deposition station is a foreign key referencing the station names in [atmo.cli](../atmo.cli/).

{% hint style="info" %}
If no atmospheric deposition data are available, "null" should be entered instead of an atmospheric deposition station name.
{% endhint %}

The null token suppresses the unmatched-name warning and leaves index zero. Source reading indicates that monthly or yearly nitrogen deposition, and enabled salt or constituent deposition, can still access unallocated data at that index. See [cli_staread.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cli_staread.f90#L89-L95) and [nut_nrain.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/nut_nrain.f90#L38-L64).
