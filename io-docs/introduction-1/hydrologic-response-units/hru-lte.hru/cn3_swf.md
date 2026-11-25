---
description: Soil water factor for CN3
---

# cn3\_swf

**Code reference:** `hlt_db(i)%cn3_swf` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L13)).

Sets the soil water content that corresponds to curve number condition III, as a position between field capacity (0) and saturation (1) ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L265-L268)):

$$
SW_3 = AWC + f \, (POR - AWC)
$$

Here *f* is cn3\_swf, and *AWC* and *POR* are the profile water contents in mm obtained from [soil\_text](soil_text.md) and [soil\_dp](soil_dp.md).
