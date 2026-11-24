---
description: "Record name"
---

# name

**Code reference:** `dr_db(ii)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dr_module.f90#L17), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dr_db_read.f90#L47)).

Name identifying a delivery-ratio record (16-character string). It is matched against [dlr](../untitled-2/dlr-rout_unit.ele.md) in [**rout\_unit.ele**](../untitled-2/) during [`ru_read_elements.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_read_elements.f90#L77) and [`hru_fr_change.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_fr_change.f90#L54). The row index of each record is also referenced via `ob(iob)%props` for standalone delivery-ratio (`dr`) spatial objects.
