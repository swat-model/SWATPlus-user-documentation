---
description: Potential evapotranspiration filename placeholder (read but not used in main 6f515368)
---

# pet\_file

**Code reference:** `bsn_cc%petfile` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L18), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_cc.f90#L24)).

Placeholder string for a basin potential evapotranspiration filename (struct default `'pet.cli'`). When [pet](pet.md) is set to `3`, [`basin_read_cc.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_read_cc.f90#L30-L40) hardcodes opening `'pet.cli'` and [`cli_petmeas.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cli_petmeas.f90#L26-L32) reads `in_cli%pet_cli` from [**file.cio**](../../master-file-file.cio.md) rather than `bsn_cc%petfile`.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
