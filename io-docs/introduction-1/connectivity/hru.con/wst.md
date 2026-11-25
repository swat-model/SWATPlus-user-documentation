---
description: Weather station name
---

# wst

**Code reference:** `ob(i)%wst_c` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L344)).

The wst value is a foreign key matching the name field in weather-sta.cli. SWAT+ uses that name to resolve the weather-station record for the object.

A name that matches no station, including `null`, [leaves the object on the first station](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L345) in weather-sta.cli with no warning.

{% hint style="warning" %}
SWAT+ looks the name up with a [binary search](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/search.f90#L18-L44) and [does not sort the station names](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cli_staread.f90#L64-L70). Keep weather-sta.cli sorted by name; otherwise a valid name can be missed.
{% endhint %}
