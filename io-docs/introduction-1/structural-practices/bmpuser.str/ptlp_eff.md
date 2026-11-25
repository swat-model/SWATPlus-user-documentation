---
description: Particulate P removal by BMP
---

# ptlp\_eff

**Code reference:** `bmpuser_db(ibmpop)%bmp_pp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L63)).

Enter the fraction of particulate phosphorus removed by this BMP (`0.0–1.0`; e.g., `0.2` removes 20%). In [`smp_bmpfixed.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/smp_bmpfixed.f90#L49-L51), SWAT+ reduces sediment-bound active mineral P (`sedminpa`), stable mineral P (`sedminps`), and organic P (`sedorgp`) by:

$$L_{\text{out}} = L_{\text{in}} \cdot (1 - E_{\text{pp}})$$

where $L_{\text{in}}$ and $L_{\text{out}}$ are the respective particulate P loads before and after BMP removal, and $E_{\text{pp}}$ is `ptlp_eff`.
