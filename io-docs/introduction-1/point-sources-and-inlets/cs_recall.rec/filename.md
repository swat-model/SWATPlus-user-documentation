---
description: "Name of the input file supplying constituent recall values"
---

# filename

**Code reference:** `rec_cs(i)%filename` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L245), [open](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L113)).

Name (`character(len=30)`) of the input file supplying general-constituent recall values when `typ /= 4`; see [`'cst_filename'.rec`](../cst_filename.rec/README.md). Note that `recall_read_cs` is not called in SWAT+ main (`6f515368`).
