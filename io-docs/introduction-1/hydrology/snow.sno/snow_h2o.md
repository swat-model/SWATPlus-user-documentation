---
description: Minimum snow water content that corresponds to 100% snow cover
---

# snow\_h2o

**Code reference:** `snodb(isno)%covmx` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L79)).

Snow water equivalent $W_{\max}$ in mm at which an HRU becomes fully snow covered. The built-in snow record uses 25 mm. If snow water equivalent $W$ is below this threshold, [`sq_snom.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sq_snom.f90#L69-L76) multiplies melt by the fractional coverage $r/[r+\exp(a-br)]$, where $r=W/W_{\max}$ and $a$ and $b$ are the shape coefficients calibrated by [cov50](cov50.md). At or above the threshold, the coverage is 1.
