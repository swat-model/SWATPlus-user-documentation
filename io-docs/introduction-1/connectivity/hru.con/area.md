---
description: Area of the object
---

# area

**Code reference:** `ob(i)%area_ha` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L340)).

The table below gives an overview of what the area represents and what it is used for in the model.

{% hint style="warning" %}
Even though some objects don't have an area, a value has to be specified in the area column to make sure the file gets read correctly by the model.
{% endhint %}

| Object             | Area                           | Use                      |
| ------------------ | ------------------------------ | ------------------------ |
| HRU                | Area of the HRU                | Conversion from mm to m3 |
| Routing Unit       | Area of the Routing Unit       | Conversion from mm to m3 |
| Aquifer            | Area of the aquifer            | Conversion from mm to m3 |
| Channel            | Drainage area of the channel   | Conversion of flow to mm, peak-rate ratio, flood duration, and ordering of channels for aqu\_cha.lin |
| Reservoir          | Drainage area of the reservoir | n/a                      |
| Outlet             | Object does not have an area   | n/a                      |
| Recall             | Object does not have an area   | n/a                      |
| Export Coefficient | Reference area of the export-coefficient object | Scales per-area values by the routed element area divided by this area |
| Delivery Ratio     | Object does not have an area   | n/a                      |

A water depth $d$ (mm) over an area $A$ (ha) is converted to a volume as

$$V = 10 \times d \times A$$

with $V$ in m3. For SWAT-DEG channels, the area is used in the [inflow depth](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_control3.f90#L155), the [peak-rate ratio](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L87), the [flood duration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L189) and the [channel ordering](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu2d_init.f90#L36) for [aqu\_cha.lin](../aqu_cha.lin.md).

The `hru_fr_update` decision-table action [replaces HRU areas](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_fr_change.f90#L97-L100) during the simulation.
