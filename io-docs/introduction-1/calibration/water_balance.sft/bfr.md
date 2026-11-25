---
description: Target baseflow ratio for baseflow-mode soft calibration.
---

# bfr

**Code reference:** `lscal(ireg)%lum(ilum)%meas%bfr` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L89), [conversion](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L94-L96)).

Dimensionless baseflow ratio (struct default `0.`). In `b`/`y` mode (`hyd_hru /= "a"`), supply the baseflow index ($\text{BFI} = Q_{\text{base}} / Q_{\text{wyld}}$); [`lcu_read_softcal.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/lcu_read_softcal.f90#L94-L96) converts it on read to baseflow fraction of precipitation ($f_{\text{bfr}}' = f_{\text{wyr}}\,f_{\text{bfr}}$) and derives `srr` and `lfr`. [`calsoft_hyd_bfr_perc.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_hyd_bfr_perc.f90#L46-L134) then calibrates `perco` against $f_{\text{bfr}}' P$.
