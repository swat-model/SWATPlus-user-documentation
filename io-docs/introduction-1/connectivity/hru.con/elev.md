---
description: Elevation of the object
---

# elev

**Code reference:** `ob(i)%elev` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L337)).

The elevation of HRUs is used to adjust precipitation and temperature when lapse adjustments are enabled in [**codes.bsn**](../../basin-1/codes.bsn/baseflo.md), using the lapse rates in [**parameters.bsn**](../../basin-1/parameters.bsn/) ([plaps](../../basin-1/parameters.bsn/s_max.md) and [tlaps](../../basin-1/parameters.bsn/n_fix.md)). SWAT+ main (6f515368) computes lapse coefficients for all objects, but applies them to weather in the HRU routine. HRU elevation also supplies wetland stage for GWFlow. See [lapse-coefficient calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cli_lapse.f90#L18), [HRU weather adjustment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L127), and [GWFlow wetland stage](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_wetland.f90#L62).

{% hint style="warning" %}
Even though the elevation of most objects is not used by the model, a value has to be specified in the elevation column to make sure the file gets read correctly.&#x20;
{% endhint %}
