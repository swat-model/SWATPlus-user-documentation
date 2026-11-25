---
description: Minimum value of the USLE C factor for water erosion
---

# usle\_c\_min

**Code reference:** `pldb(ic)%usle_c` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L69)).

{% hint style="warning" %}
**Current use:** values are limited to above 0 and at most 1 ([`plantparm_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plantparm_init.f90#L23-L24)). The daily HRU C factor does not use this value in SWAT+ main (`6f515368`), because [the method switch is fixed](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ero_cfactor.f90#L51-L55) to the residue and canopy cover method. Sub-daily overland erosion still uses it ([`ero_ovrsed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ero_ovrsed.f90#L165-L168)). This comes from source reading.
{% endhint %}

The minimum C factor can be estimated from a known average annual C factor using the following equation (Arnold and Williams, 1995):

$$C_{USLE,mn} = 1.463 * ln⁡[C_{USLE,aa}] + 0.1034$$

where $$C_{USLE,mn}$$ is the minimum C factor for the land cover and $$C_{USLE,aa}$$ is the average annual C factor for the land cover.

#### References

> Arnold and Williams (1995)
