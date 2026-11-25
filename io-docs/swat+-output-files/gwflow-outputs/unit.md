---
description: "Cell index"
---

# unit

**Code reference:** `i` ([cell writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_output.f90#L1225)).

The cell water-balance writer prints the GWFlow cell index. Only cells with `gw_state(i)%stat == 1` receive these rows; this is not the basin placeholder 1.

This is an identifier or label, with no physical unit.

[Back to the cell water-balance schema](cell-water-balance.md).
