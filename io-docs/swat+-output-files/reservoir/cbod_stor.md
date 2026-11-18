---
description: "Carbonaceous Biochemical Oxygen Demand storage in the reservoir"
---

# cbod_stor

**Code reference:** `res(j)%cbod` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L41)).

Carbonaceous biochemical oxygen demand mass in storage comes from initialization and incoming water. An allocation withdrawal can remove some of the mass, and a low-volume reset can clear the storage record. [Mass conversion](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1282-L1303), [Allocation withdrawal](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L99-L108), [Low-volume reset](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_nutrient.f90#L31-L36)

**Unit:** kg.

Storage values are snapshots on the reporting date. See [oxygen and temperature values](README.md#oxygen-and-temperature-values).

[Back to the output table](README.md).
