---
description: Sediment removal by BMP
---

# sed\_eff

**Code reference:** `bmpuser_db(ibmpop)%bmp_sed` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L62)).

Enter the fraction of sediment load removed by this BMP (`0.0–1.0`; e.g., `0.2` removes 20%). In `smp_bmpfixed.f90`, SWAT+ reduces the HRU sediment yield (`sedyld`) by:

$$Y_{\text{out}} = Y_{\text{in}} \cdot (1 - E_{\text{sed}})$$

where $Y_{\text{in}}$ and $Y_{\text{out}}$ are HRU sediment yield before and after BMP removal, and $E_{\text{sed}}$ is `sed_eff`.
