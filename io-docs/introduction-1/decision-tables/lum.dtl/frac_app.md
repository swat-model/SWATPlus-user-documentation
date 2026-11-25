---
description: Probability of a scheduled application within the window
---

# frac\_app

**Code reference:** `dtbl_lum(i)%frac_app` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L50)).

For a `prob_unif` condition row, enter the probability as a fraction between 0 and 1 in the second position, in place of the object type. [`dtbl_lum_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_lum_read.f90#L69-L75) first reads the ordinary row structure and then rereads its first two fields to store this fraction. The value is table-wide, so a later `prob_unif` row in the same table replaces it.

On the first day of the window, SWAT+ draws a uniform random number and schedules an application when the draw is below this fraction. The single-year branch draws a day using $d=d_0+1+\lfloor U(d_1-d_0+1)\rfloor$, where $U$ is a second uniform draw and $d_0$ and $d_1$ are the entered first and last days. The implemented formula can skip the first day and select the day after the entered end. [`conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditions.f90#L485-L519)
