---
description: "Legacy allocation heading at position 4; row-dependent values"
---

# yr

**Printed header:** `yr`, position 4 in the legacy 25-entry header; its printed unit is blank. The nominal label refers to calendar year. It is not a universal data-column mapping.

The active writer supplies the following values at position 4, counting scalars in the WRITE list and ignoring indentation:

| Row | Actual value at this position |
| --- | --- |
| Daily POU TXT | `time%yrc` |
| Monthly/yearly/AA POU TXT | `time%yrc` |
| Daily POU CSV | `ipou` |
| Monthly/yearly/AA POU CSV | `"POU"` |
| POD child, TXT/CSV | `delivered` |
| POR child, TXT/CSV | `hyd_output%sed` |

Dates belong to the parent POU record. POD/POR children have no date prefix; their first values are the row marker and local child index. The POU date records the reporting boundary, including the final date for average-annual output.

See the [actual row layouts and period limitations](allocation-transactions.md#actual-allocation-rows) before reading this heading as a physical quantity. **Code references:** [legacy header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L220); [daily rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L29), [monthly rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L85), [yearly rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L143), [average-annual rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L198).

[Back to the allocation-transactions schema](allocation-transactions.md).
