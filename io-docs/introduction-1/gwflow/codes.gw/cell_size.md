---
description: "Cell size; not used by the model"
---

# cell_size

**Code reference:** `cell_size` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L70), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L238)).

Side length of a structured-grid cell. SWAT+ Editor writes it for structured grids and 0 otherwise.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).* Cell areas come from the `area` column of [cells.gw](../cells.gw/area.md).
