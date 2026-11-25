---
description: "Unheaded pathogen wash-off from foliage to surface soil"
---

# wash (unheaded data position 18)

**Code reference:** `hpath_bal(j)%path(ipath)%wash` ([source](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_ls_process.f90#L36)).

There is no printed heading for data position 18. `wash` is the source component name, not a label present in the output header.

The process routine resets this daily value, then sums material transferred from foliage to surface soil when precipitation is at least 2.54 mm. The transfer is capped to the available foliage pool. It is an internal transfer, not export from the HRU. The addition operator omits `wash`, so it is not even accumulated before the averaging operator discards non-state values.

**Unit:** unresolved. The balance declaration says kg/ha while the constituent pathogen state is annotated cfu; no consistent conversion was established. The neighboring printed kg/h suffix does not establish a physical unit for this unheaded value.

The period-averaging operator assigns only `plant` and `soil`; all other result components retain their zero defaults. Thus the monthly, yearly, and average-annual versions do not preserve this component as a process total. See the [family table](README.md) for the 18-value/15-heading mismatch and average-annual CSV format warning.

[Back to the output table](README.md).
