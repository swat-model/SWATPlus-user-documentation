---
description: "Groundwater flow assigned to reservoir receivers"
---

# flo_res

**Code reference:** `aqu_d(iaq)%flo_res` ([routing calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_1d_control.f90#L377)).

Groundwater flow assigned to reservoir receivers. The controller sums `aqu_d(iaq)%flo * frac_out` only for outgoing connections whose hydrograph type is `tot` and whose receiver type is `res`.

**Unit:** mm.

Monthly values sum daily exchanges; yearly values sum the monthly totals. Average-annual values divide the accumulated yearly totals by `time%yrs_prt`.

Basin output applies `aqu_prm(iaq)%area_ha / bsn%area_tot_ha`; the denominator is the full basin area, not the sum of aquifer areas. This is not necessarily a normalized mean over just the aquifers.

[Back to the output table](README.md).
