---
description: Sediment transport capacity multiplier
---

# depos

**Code reference:** `topo_db(ith)%dep_co` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/topography_data_module.f90#L11)).

Dimensionless multiplier $D$ for sediment transport capacity during surface runon across an HRU. The built-in topography record uses 1. In [`rls_routesurf.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/rls_routesurf.f90#L56-L66), the capacity is

$$T = D\,C\,Q\,S^{1.4}W^{1.4}$$

$C$ is the USLE cover factor, $Q$ is the surface runon term used in the calculation, $S$ is slope steepness, and $W$ is [field width](../field.fld/wd.md) in meters. Sediment above the capacity is deposited, so a larger coefficient allows more of the incoming sediment to pass through this step.
