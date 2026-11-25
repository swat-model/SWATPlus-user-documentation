---
description: Average annual crop yield soft-calibration target in plant_gro.sft.
---

# yield

**Code reference:** `plcal(i)%lum(ilum)%meas%yield` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L244), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_plant.f90#L49-L516)).

Average annual dry-weight crop yield target (`t/ha`, struct default `0.`). Compared against the area-weighted simulated annual yield $\bar{Y} = \frac{1}{A_{\text{tot}}} \sum_j (Y_j A_j / 1000)$ computed by [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L558) and [`calsoft_ave_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_ave_output.f90#L68).

When the relative error $|Y_{\text{soft}} - \bar{Y}| / Y_{\text{soft}} > 0.03$, [`calsoft_plant.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calsoft_plant.f90#L49-L516) sequentially adjusts `epco`, `pest_stress`, `lai_pot`, and `harv_idx` within the bounds from `plant_parms.sft`.
