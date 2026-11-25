---
description: "Alpha factor used in the bank storage recession curve"
---

# alpha_bnk

**Code reference:** `ch_hyd(ich)%alpha_bnk` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L81)).

Alpha factor used in the bank storage recession curve (`days`, struct default `0.03`). When reading `hydrology.cha`, [`ch_read_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_hyd.f90#L52) immediately transforms the value to $\exp(-\alpha_{\text{bnk}})$. In SWAT+ main (`6f515368`), `alpha_bnk` is not used downstream after being read.
