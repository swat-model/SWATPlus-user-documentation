---
description: "Seepage volume"
---

# seep

**Code reference:** `wet_wat_d(j)%seep` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_body_module.f90#L11)).

Seepage volume.

**Unit:** m3.

The wetland controller first calculates seepage from hydraulic conductivity, wetland area, and available storage, or gets it from the GWFlow exchange routine when active. Its soil saturation calculation can reduce the seepage before the volume is subtracted from wetland storage. [Seepage calculation and adjustment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wetland_control.f90#L99), [GWFlow seepage](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_wetland.f90#L139)

See the [reporting periods](README.md#how-to-read-the-reporting-periods) for how the writer combines daily values.

[Back to the output table](README.md).
