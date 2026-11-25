---
description: "Identifier matching this manure type against the organic/mineral constituent database entry that supplies sediment"
---

# org_min

**Code reference:** `manure_db(it)%org_min` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/fertilizer_data_module.f90#L18)).

Name of a [manure\_om.frt](../manure_om.frt/) record ([`manure_db_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/manure_db_read.f90#L52-L57)).

{% hint style="warning" %}
Suspected defect: the matched position is not used to choose the composition. The manure application reads the `manure_om.frt` row with the same number as this `manure_db.frt` row ([`pl_manure.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_manure.f90#L83-L84)). The match only gates salt and constituent additions, which require it to be row 2 or later ([`salt_fert.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_fert.f90#L29), [`cs_fert.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cs_fert.f90#L28)). This comes from source reading, not a model run.
{% endhint %}
