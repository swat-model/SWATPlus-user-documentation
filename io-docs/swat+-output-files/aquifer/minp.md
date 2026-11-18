---
description: "Calculated soluble-phosphorus load in the 1-D controller"
---

# minp

**Code reference:** `aqu_d(iaq)%minp = ob(icmd)%hin%flo * aqu_dat(iaq)%minp / 1000.` followed by `ob(icmd)%hd(1)%solp = aqu_d(iaq)%minp` ([1-D assignments](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L170)).

The controller calculates a phosphorus load using incoming hydrograph water volume and a fixed concentration, then assigns it to outgoing soluble phosphorus. It uses incoming volume, rather than the outgoing volume. This is not a stored-phosphorus balance.

**Unit:** kg P in this 1-D calculation. The volume in m3 times concentration in mg/L divided by 1000 gives kg, without division by aquifer area. The declaration and printed units row say kg/ha P; that label contradicts this assignment.

Monthly values sum daily exchanges; yearly values sum the monthly totals. Average-annual values divide the accumulated yearly totals by `time%yrs_prt`. These are accumulated daily loads, not mean storage. Basin output applies area weights to these whole-aquifer loads, producing an area-weighted load rather than either a basin total or kg/ha.

Water allocation also modifies this component: canal seepage adds soluble-P mass, while withdrawal constructs an outgoing load by multiplying it by aquifer area. These paths do not establish a consistent universal mass basis ([canal](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_canal.f90#L45); [withdrawal](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L119)).

[Back to the output table](README.md).
