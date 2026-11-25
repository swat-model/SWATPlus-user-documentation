---
description: Object type
---

# obj

**Code reference:** `dtbl_lum(i)%act(iac)%ob` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L18)).

Object-type label for the action. Most actions act on an HRU whatever is entered, and `chan_change` acts on the current channel. [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L432-L434) · [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L1218-L1222)

`irrigate` uses it to choose the water source whose storage is reduced: `aqu`, `cha` or `sdc`, or `res`, with the source number in [obj_num](obj_num-1.md). Any other label removes water from no source. If the demand exceeds the source storage, nothing is applied. [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L263-L320)
