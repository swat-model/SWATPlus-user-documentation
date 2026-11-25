---
description: Harvest efficiency
---

# harv\_eff

**Code reference:** `harvop_db(iharvop)%eff` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_operations_module.f90#L114), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_read_harvops.f90#L44)).

Dimensionless harvest efficiency (`fraction`; default `0.0`, valid range `0.0–1.0`) controlling the fraction of harvested material exported from the HRU (`0.0` exports no yield; `1.0` exports all harvested yield). Its application depends on `harv_typ`:

* **Biomass (`biomass`, `tree`, `stripper`):** Used in [`mgt_harvbiomass.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_harvbiomass.f90#L39-L42) to compute $HI_{\text{tot}} = HI_{\text{ovr}} \cdot E_{\text{harv}}$, while $(1 - E_{\text{harv}}) \cdot Y$ is added to surface plant residue ([`mgt_harvbiomass.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_harvbiomass.f90#L112-L114)).
* **Grain (`grain`, `picker`):** In [`mgt_harvgrain.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_harvgrain.f90#L40-L57), exports $Y = E_{\text{harv}} \cdot M_{\text{seed}}$ (before pest-stress scaling at line 51) and transfers $(1 - E_{\text{harv}}) \cdot M_{\text{seed}}$ into active soil humus `soil1(j)%hact(1)`.
* **Tuber (`tuber`, `peanuts`):** In [`mgt_harvtuber.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_harvtuber.f90#L43-L46), exports $Y = E_{\text{harv}} \cdot M_{\text{root}}$ (before pest-stress scaling at line 61).
* **Residue (`residue`):** In [`mgt_harvresidue.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/mgt_harvresidue.f90#L36-L43), if the scheduled efficiency argument `harveff < 0.00001`, SWAT+ substitutes `harvop_db(iharvop)%eff` and multiplies it by `harv_idx`.
