---
description: "Wetland name ending in the HRU number"
---

# wet_name

**Code reference:** `wet_name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_read_hyd.f90#L21), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_read_hyd.f90#L84)).

Wetland name, up to 20 characters, such as `wet019`. Only its digits are used: SWAT+ reads the number starting at the first digit and stores the thickness for that HRU ([`wet_read_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_read_hyd.f90#L86-L92)). A name without digits is skipped.
