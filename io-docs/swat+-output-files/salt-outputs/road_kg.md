---
description: "Salt from road-salt applications"
---

# road_kg

**Code reference:** `salt_basin(15)` ([calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/salt_balance.f90#L189-L197)).

Salt from road-salt applications. The daily basin calculation sets totals below 0.000001 kg to zero.

**Unit:** kg for daily, monthly, and yearly output. The average-annual value is kg/yr.

See [reporting periods](basin-salt-balance.md#reporting-periods) for aggregation.

[Back to schema](basin-salt-balance.md).
