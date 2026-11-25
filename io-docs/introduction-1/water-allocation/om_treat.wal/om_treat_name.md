---
description: "Name identifying this component-value record"
---

# om_treat_name

**Code reference:** `om_treat_name(iom_tr)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L216), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/om_treat_read.f90#L43)).

16-character name identifying a treatment organic/mineral record. Matched against `org_min_name` in [water_treat.wal](../water_treat.wal/README.md) when `org_min_typ == "const"` ([`water_treatment_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_treatment_read.f90#L65)), and printed in treatment output files ([`wallo_treat_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_treat_output.f90#L19,L22,L35,L38,L52,L55,L70,L73)).
