---
description: "Cumulative custom soil-layer depth used to construct layer boundaries"
---

# csld

**Code reference:** `csld` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L28)).

Cumulative custom soil-layer depth from the soil surface (`mm`), supplied as one integer value per line in increasing order ([`soils_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L175), [layer pass](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L212)).

SWAT+ always creates a 10 mm surface layer first ([`soils_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L219)); any `csld <= 10` is ignored ([`soils_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L180), [layer pass](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L213)), and any `csld` exceeding the total profile depth $D_{\text{tot}}$ from `soils.sol` is clamped to $D_{\text{tot}}$ ([`soils_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L198), [clamp](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L224)). Properties for each custom layer spanning millimeter indices $j \in [z_{\text{prev}}, z_i]$ ($n = z_i - z_{\text{prev}} + 1$) are thickness-weighted averages of the 1 mm discretized `soils.sol` profile ([`soils_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/soils_init.f90#L243-L271)):

$$\bar{x}_i = \frac{1}{n} \sum_{j = z_{\text{prev}}}^{z_i} x(j)$$

where $\bar{x}_i$ is the averaged property assigned to custom layer $i$ and $x(j)$ is the property value at millimeter depth $j$.
