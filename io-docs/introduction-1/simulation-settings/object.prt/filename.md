---
description: User-defined name of output file
---

# filename

**Code reference:** `ob_out(ii)%filename` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L263)).

User-defined output filename (`character(len=26)`; Fortran struct default: `""`). In [`object_read_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/object_read_output.f90#L100-L103), SWAT+ opens this file directly in the simulation working directory with record length `recl = 2000` on Fortran unit `6100 + i`.

When SWIFT output is enabled (`swift_out = 1` in `codes.bsn`), [`swift_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/swift_output.f90#L283) also writes this filename alongside the average-annual object hydrograph into `SWIFT/object_prt.swf`.
