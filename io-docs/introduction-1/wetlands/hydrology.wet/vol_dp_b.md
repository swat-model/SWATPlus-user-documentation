---
description: Volume depth coefficient for HRU impoundment
---

# vol\_dp\_b

**Code reference:** `wet_hyddb(ires)%ccoef` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/reservoir_data_module.f90#L92)).

The quadratic curvature coefficient (default `1.0`) used alongside [`vol_dp_a`](vol_dp_a.md) to calculate water depth $h$ from the ratio of current water volume to principal volume ($V / V_{\text{pvol}}$):

$$x_1 = b^2 + 4 \cdot c \cdot \left(1 - \frac{V}{V_{\text{pvol}}}\right)$$

where $b$ is `vol_dp_a` and $c$ is `vol_dp_b`.

The resulting depth $h$ is subsequently multiplied by [`vol_area_co`](vol_area_co.md) to update the daily wetland surface area. A larger `vol_dp_b` relative to `vol_dp_a` causes the wetland to retain a wider surface area even under lower storage volumes.
