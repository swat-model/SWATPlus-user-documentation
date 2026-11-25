---
description: General-constituent mass values in a general-constituent recall file
---

# cs(ics)

**Code reference:** `rec_cs(i)%hd_cs(istep,iyrs)%cs(ics)` ([allocation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L133-L149), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L199)).

General-constituent mass load (`kg`; Fortran allocation default: `0.`) for each simulated constituent $i = 1, \dots, N_{\text{cs}}$ (`cs_db%num_cs` from [`constituents.cs`](../../constituents/constituents.cs.md)).

During simulation, [`command.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L356) calls [`recall_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_cs.f90#L50-L95) to copy `rec_cs(irec)%hd_cs` into `obcs(icmd)%hd(1)%cs(ics)` (or remove constituent mass when daily `flo < 0` in [`recall_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_cs.f90#L35-L46)). Note that [`recall_read_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read_cs.f90#L1-L247) is not called in SWAT+ main (`6f515368`).
