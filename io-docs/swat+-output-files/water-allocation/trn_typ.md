---
description: "Legacy allocation heading at position 6; row-dependent values"
---

# trn_typ

**Printed header:** `trn_typ`, position 6 in the legacy 25-entry header; its printed unit is blank. The nominal label refers to transfer type. It is not a universal data-column mapping.

The active writer supplies the following values at position 6, counting scalars in the WRITE list and ignoring indentation:

| Row | Actual value at this position |
| --- | --- |
| Daily POU TXT | `"POU"` |
| Monthly/yearly/AA POU TXT | `ipou` |
| Daily POU CSV | `time%yrc` |
| Monthly/yearly/AA POU CSV | `time%yrc` |
| POD child, TXT/CSV | `hyd_output%sed` |
| POR child, TXT/CSV | `hyd_output%sedp` |

`ipou` is the place-of-use index; `ipod` and `ipor` are local indices within that POU's configured child lists. The POU name and `"POU"`/`"POD"`/`"POR"` markers are distinct values. The order varies between TXT and CSV and between daily and longer-period POU rows.

See the [actual row layouts and period limitations](allocation-transactions.md#actual-allocation-rows) before reading this heading as a physical quantity. **Code references:** [legacy header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L220); [daily rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L29), [monthly rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L85), [yearly rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L143), [average-annual rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L198).

[Back to the allocation-transactions schema](allocation-transactions.md).
