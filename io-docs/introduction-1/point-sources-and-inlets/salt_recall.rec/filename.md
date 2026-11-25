---
description: "Recall input filename"
---

# filename

**Code reference:** `rec_salt(i)%filename` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L233), [open](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_salt.f90#L114)).

Name (`character(len=30)`) of the input file supplying the salt recall time series when `typ /= 4`; see [`'salt_filename'.rec`](../salt_filename.rec/README.md). Note that `recall_read_salt` is not called in SWAT+ main (`6f515368`).
