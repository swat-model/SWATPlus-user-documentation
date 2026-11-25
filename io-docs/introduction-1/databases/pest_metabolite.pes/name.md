---
description: "Record name"
---

# name

**Code reference:** `pestcp(ip)%daughter(imeta)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pesticide_data_module.f90#L28)).

Daughter pesticide name. It must be in `pesticide.pes` and also listed as a simulated pesticide in [constituents.cs](../../constituents/constituents.cs/); otherwise it gets no position in the simulation ([`pest_metabolite_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_metabolite_read.f90#L66-L71)).
