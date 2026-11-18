---
description: "Dissolved oxygen entering the reservoir"
---

# dox_in

**Code reference:** `res_in_d(j)%dox` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L42)).

Dissolved oxygen measured as mass in the routed incoming hydrograph for an operating reservoir. Water delivered directly by allocation enters storage through a separate record. [Inflow and storage](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L38-L63), [Reported inflow](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_control.f90#L243-L254), [Allocation delivery](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_deliv.f90#L88-L96)

**Unit:** kg.

Monthly and yearly records sum the daily loads. The average-annual record divides the accumulated loads by the number of printed years. See [oxygen and temperature values](README.md#oxygen-and-temperature-values).

[Back to the output table](README.md).
