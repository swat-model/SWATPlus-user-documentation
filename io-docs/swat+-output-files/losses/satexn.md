---
description: "Saturation-excess nitrate field left at zero by the source"
---

# satexn

**Code reference:** `bls_d%satexn` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L163)).

The heading denotes nitrate nitrogen in saturation-excess surface runoff. At source revision `6f515368`, the daily losses record starts at zero and no active producer assigns this field. A printed zero therefore gives no measurement of the nitrate transported by saturation excess. [field default](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/output_landscape_module.f90#L151-L164), [daily HRU assignments](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L875-L889).

**Unit:** kg N/ha.

The loss aggregation carries the zero through LSU, basin, monthly, yearly, and average-annual output.

[Back to the output table](README.md).
