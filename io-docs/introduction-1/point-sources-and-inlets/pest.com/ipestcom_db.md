---
description: "Pesticide database record identifier in pest.com"
---

# ipestcom\_db

**Code reference:** `ipestcom_db` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L32), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L225)).

Integer pesticide database identifier (`0` by default) read on its own row before each block of recall entries in `pest.com`.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
