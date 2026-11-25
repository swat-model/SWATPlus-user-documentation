---
description: Leading pesticide label token
---

# titldum

**Code reference:** `titldum` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_hru_aqu_read.f90#L9)).

Leading character token on each pesticide row in `pest_hru.ini` ([`pest_hru_aqu_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_hru_aqu_read.f90#L58)). SWAT+ parses this token and discards it without name matching; rows must appear in the same order as pesticides in [**constituents.cs**](../../constituents/constituents.cs.md).
