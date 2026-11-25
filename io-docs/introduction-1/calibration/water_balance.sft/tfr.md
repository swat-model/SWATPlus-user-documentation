---
description: Target tile flow ratio for soft calibration.
---

# tfr

**Code reference:** `lscal(ireg)%lum(ilum)%meas%tfr` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L89), [scale](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_control.f90#L52)).

Dimensionless target ratio of tile drainage flow to precipitation ($Q_{\text{tile}} / P$, struct default `0.`). Converted to mm (`precip_aa_sav * tfr`) in [`calsoft_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_control.f90#L52) and [`calsoft_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_control.f90#L72) for output summary reporting; no soft-calibration routine directly adjusts tile drainage parameters.
