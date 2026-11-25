---
description: "First operation-specific value in full-prefix rows"
---

# op_var

**Code reference:** `operation-specific value` ([writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L156)).

For rows that write the full common prefix, this is the first operation-specific value. It is numeric in common irrigation and fertilizer records: the [irrigation write](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L156) supplies `irrig(j)%applied`, and the [fertilizer write](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L357) supplies `frt_kg`. The printed heading does not imply a variable-name label. There is no single value declaration for every operation.

**Unit:** operation-dependent; the printed units row uses `---`. Short rows and the expanded residue-record write can shift values relative to the nominal header; consult the [family warning](README.md) before assigning this position a meaning.

This field belongs to a fixed or event-style report rather than the standard daily/monthly/yearly/average-annual series.

[Back to the output table](README.md).
