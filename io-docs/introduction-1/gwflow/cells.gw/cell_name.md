---
description: "Cell name for output"
---

# cell_name

**Code reference:** `cell_name(i)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L45), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L446)).

Cell name, written in the `name` column of per-cell GWFlow output ([`gwflow_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_output.f90#L1227-L1230)). SWAT+ keeps the first 16 characters. It cannot contain spaces, because fields are split on spaces. SWAT+ Editor writes names such as `cell0001`.
