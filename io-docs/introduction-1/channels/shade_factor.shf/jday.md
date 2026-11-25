---
description: "Day of year"
---

# jday

**Code reference:** `shf_db(idlsu)%jday` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1196)).

Day-of-year value matched together with the channel number in [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L352-L362) (read by [`shade_factor_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/shade_factor_read.f90#L50)). In the file-based shading branch, day `366` sets `ssff = 0.5` rather than performing a row lookup. Because `w_temp(0)%sf_on` remains `0`, source reading indicates this branch is not reached at `6f515368`.
