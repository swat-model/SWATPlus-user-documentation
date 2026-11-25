---
description: "Legacy allocation heading at position 5; row-dependent values"
---

# unit

**Printed header:** `unit`, position 5 in the legacy 25-entry header; its printed unit is blank. The nominal label refers to allocation identifier. It is not a universal data-column mapping.

The active writer supplies the following values at position 5, counting scalars in the WRITE list and ignoring indentation:

| Row | Actual value at this position |
| --- | --- |
| Daily POU TXT | `ipou` |
| Monthly/yearly/AA POU TXT | `"POU"` |
| Daily POU CSV | `"POU"` |
| Monthly/yearly/AA POU CSV | `ipou` |
| POD child, TXT/CSV | `hyd_output%flo` |
| POR child, TXT/CSV | `hyd_output%orgn` |

`ipou` is the place-of-use index; `ipod` and `ipor` are local indices within that POU's configured child lists. The POU name and `"POU"`/`"POD"`/`"POR"` markers are distinct values. The order varies between TXT and CSV and between daily and longer-period POU rows.

See the [actual row layouts and period limitations](allocation-transactions.md#actual-allocation-rows) before reading this heading as a physical quantity. **Code references:** [legacy header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L220); [daily rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L29), [monthly rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L85), [yearly rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L143), [average-annual rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L198).

[Back to the allocation-transactions schema](allocation-transactions.md).
