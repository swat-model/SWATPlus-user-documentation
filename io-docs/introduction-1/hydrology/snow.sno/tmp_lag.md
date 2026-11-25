---
description: Snowpack temperature lag factor
---

# tmp\_lag

**Code reference:** `snodb(isno)%timp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_module.f90#L78)).

Dimensionless coefficient $\lambda$ for estimating snowpack temperature. The built-in snow record uses 0.8. [`sq_snom.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sq_snom.f90#L45-L52) resets its snowpack temperature variable to zero on each call, so the implemented estimate is $T_{\mathrm{pack}}=\lambda T_{\mathrm{air}}$, with daily mean air temperature $T_{\mathrm{air}}$. The previous day's snowpack temperature does not carry over in this routine. This is flagged as a suspected model issue.
