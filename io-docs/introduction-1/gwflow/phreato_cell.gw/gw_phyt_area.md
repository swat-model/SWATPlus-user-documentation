---
description: "Phreatophyte area in the cell, m²"
---

# gw_phyt_area

**Code reference:** `gw_phyt_area(i)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L431), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1450)).

Area covered by phreatophytes in the cell, in m². Daily uptake is $Q = r \, A$, where $r$ is the rate from [phreato.gw](../phreato.gw/gw_phyt_rate.md) for the current water-table depth ([`gwflow_phreatophyte.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_phreatophyte.f90#L36)).
