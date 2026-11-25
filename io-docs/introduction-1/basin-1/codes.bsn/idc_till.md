---
description: Tillage method used when carbon = 2
---

# idc\_till

**Code reference:** `bsn_cc%idc_till` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L71), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_cc.f90#L24)).

Selects the tillage mixing formulation in [`cbn_zhang2.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_zhang2.f90#L359). It is evaluated only when [carbon](carbon.md) = `2` (struct default `3`).

| Value | Tillage method |
| ----- | -------------- |
| 1 | DSSAT |
| 2 | EPIC |
| 3 | Kemanian (default) |
| 4 | DNDC |
