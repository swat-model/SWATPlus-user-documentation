---
description: Target surface runoff ratio for soft calibration.
---

# srr

**Code reference:** `lscal(ireg)%lum(ilum)%meas%srr` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L89), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd.f90#L269-L342)).

Dimensionless target ratio of surface runoff to precipitation ($Q_{\text{surf}} / P$, struct default `0.`), used to calibrate `cn3_swf` in [`calsoft_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd.f90#L269-L342), [`calsoft_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd.f90#L710-L783), and [`calsoft_hyd_bfr_surq.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd_bfr_surq.f90#L44-L117), and `cn2` / `cn3_swf` for HRU-LTE in [`caltsoft_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/caltsoft_hyd.f90#L53-L134).

When `hyd_hru /= "a"` (`b` or `y` mode), [`lcu_read_softcal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L94) overwrites the input value with $f_{\text{srr}} = f_{\text{wyr}}(1 - f_{\text{bfr}})$.
