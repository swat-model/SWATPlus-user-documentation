---
description: Average slope length
---

# slp\_len

**Code reference:** `topo_db(ith)%slope_len` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/topography_data_module.f90#L8)).

Average overland slope length $L$ in meters, from the start of sheet flow to where runoff concentrates. The built-in record uses 50 m. It enters the overland travel time equation described under [slope steepness](slp.md) and the MUSLE slope-length factor:

$$LS=(L/22.128)^{m}(65.41\,\sin^2\theta+4.56\,\sin\theta+0.065)$$

Here $\theta=\arctan(S)$ and $m=0.6[1-\exp(-35.835S)]$ for slope steepness $S$. [`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L379-L385)

The initialization calculates a practice-based maximum slope length in a temporary variable, but the LS equation still uses the full HRU slope length. [`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L379-L385)
