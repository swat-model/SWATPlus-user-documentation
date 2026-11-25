---
description: "Weighting factor that splits the organic N and P of applied fertilizer and manure between pools"
---

# rtof

**Code reference:** `man_coef%rtof` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L79), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L73), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L484-L485)).

Weighting factor for the organic nitrogen and phosphorus in applied fertilizer and manure. With carbon `= 2`, the share $1 - r$ goes to the slow humus pool: [`pl_manure.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_manure.f90#L108-L113) for manure and [`pl_fert.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_fert.f90#L107-L112) for organic fertilizer. The source comment still describes septic effluent, which does not match this use.

For organic fertilizer, [`pl_fert.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_fert.f90#L114-L121) also uses $1 - r$, not $r$, for the metabolic and structural litter pools, although the source comment says `rtof`. The amount added is then $2(1 - r)$ times the applied organic matter, which equals the applied amount only when $r = 0.5$. For manure, all of the organic nitrogen also goes to the metabolic and structural litter pools ([`pl_manure.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pl_manure.f90#L136-L141)), so $(2 - r)$ times the applied organic nitrogen is added. Both are listed in `MODEL_ISSUES.md`.

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `manure_c_frac` and uses 0.5. The calibration parameter is `manure_c_frac`.
