---
description: "Legacy allocation heading at position 9; row-dependent values"
---

# rcv_num

**Printed header:** `rcv_num`, position 9 in the legacy 25-entry header; its printed unit is blank. The nominal label refers to receiver number. It is not a universal data-column mapping.

The active writer supplies the following values at position 9, counting scalars in the WRITE list and ignoring indentation:

| Row | Actual value at this position |
| --- | --- |
| Daily POU TXT | `delivered` |
| Monthly/yearly/AA POU TXT | `delivered` |
| Daily POU CSV | `duty` |
| Monthly/yearly/AA POU CSV | `duty` |
| POD child, TXT/CSV | `hyd_output%no3` |
| POR child, TXT/CSV | `hyd_output%chla` |

The writer loops over the configured POD/POR counts and prints no separate unmet-demand scalar. Duty and withdrawn volume use m³. The POD delivery scalar records the most recent withdrawal assigned to that POD, while its hydrograph adds withdrawals across calls. Hydrograph components have their own units.

See the [actual row layouts and period limitations](allocation-transactions.md#actual-allocation-rows) before reading this heading as a physical quantity. **Code references:** [legacy header](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L220); [daily rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L29), [monthly rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L85), [yearly rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L143), [average-annual rows](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L198).

See [daily duty and reported delivery](allocation-transactions.md#daily-duty-and-reported-delivery) for the withdrawal-based POU total.

[Back to the allocation-transactions schema](allocation-transactions.md).
