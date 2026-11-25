---
description: Plant residue decomposition coefficient
---

# plnt\_decomp

**Code reference:** `pldb(ic)%rsdco_pl` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L79)).

**Current use:** values below `1e-6` are replaced by the basin [rsd\_decomp](../../basin-1/parameters.bsn/rsd_decomp.md) value ([`plantparm_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plantparm_init.f90#L22)). It scales daily residue decomposition ([`rsd_decomp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/rsd_decomp.f90#L106)).

The plant residue decomposition coefficient is the fraction of residue that will decompose in a day assuming optimal moisture, temperature, C:N ratio, and C:P ratio.

{% hint style="info" %}
A default value of 0.05 is used for all plant species in the database, but users may vary decomposition by plant species.
{% endhint %}
