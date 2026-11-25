---
description: "Fraction of water lost during treatment"
---

# loss_fr

**Code reference:** `wtp(iwtp)%loss_fr` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L157), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_treatment_read.f90#L46)).

Fraction of water lost during treatment (`fraction`; uninitialized in the derived-type definition). In `6f515368`, [`wallo_treatment.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_treatment.f90#L68) instead uses `wtp_om_treat%flo` (from [om_treat.wal](../om_treat.wal/README.md)) to scale treated outflow.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
