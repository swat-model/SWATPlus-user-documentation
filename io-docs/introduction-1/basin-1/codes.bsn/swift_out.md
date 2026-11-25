---
description: SWIFT input file
---

# swift\_out

**Code reference:** `bsn_cc%swift_out` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L27), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_cc.f90#L24)).

Controls writing of SWIFT input files during routing ([`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L493)) and at the end of simulation ([`main.f90.in`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/main.f90.in#L164); struct default `0`).

| Code | Option |
| ---- | ------ |
| 0 | Do not write SWIFT input file |
| 1 | Write SWIFT input file (`swift_hru.inp`) |
