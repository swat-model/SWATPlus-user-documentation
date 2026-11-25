---
description: Soil percolation coefficient
---

# perc\_co

**Code reference:** `hlt_db(i)%perco` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_module.f90#L17)).

Multiplier on the profile available water capacity that sets the soil water content above which water percolates ([`hru_lte_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_control.f90#L319-L327)):

$$w_{perc} = \max(0, \; SW - AWC \times f) \, \left( 1 - e^{-24/hk} \right)$$

where:
* $w_{perc}$ is daily soil percolation (`mm`),
* $SW$ is soil water content (`mm`),
* $AWC$ is profile available water capacity (`mm`),
* $f$ is `perc_co`, and
* $hk$ is the travel time in hours calculated from the texture properties ([`hru_lte_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_lte_read.f90#L263-L264)).

A value of 1 starts percolation above available water capacity; 0 makes all stored soil water subject to percolation.
