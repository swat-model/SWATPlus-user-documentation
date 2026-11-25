---
description: "Fixed minimum level or threshold for withdrawal"
---

# const_min (POD)

**Code reference:** `pou(ipou)%pod(ipod)%const_min` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L23), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L95)).

Fixed minimum withdrawal threshold (default: `0.`). Evaluated by source type in [`wallo_withdraw.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L61-L112):

- `wtow` ([`wallo_withdraw.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L61-L63)): minimum fraction of current water-tower storage ($V_{\min} = c_{\min} \cdot V_{\text{stor}}$).
- `cha` ([`wallo_withdraw.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L75-L77)): minimum channel daily flow volume (`m^3`), compared directly against `ht2%flo` (no `86400` multiplier is applied).
- `can` ([`wallo_withdraw.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L88-L90)): minimum fraction of current canal storage ($V_{\min} = c_{\min} \cdot V_{\text{stor}}$).
- `res` ([`wallo_withdraw.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L100-L102)): minimum fraction of principal reservoir volume ($V_{\min} = c_{\min} \cdot V_{\text{pvol}}$).
- `aqu` ([`wallo_withdraw.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L112)): maximum allowable water-table depth (`m`); withdrawal proceeds only when $d_{\text{wt}} < c_{\min}$.
