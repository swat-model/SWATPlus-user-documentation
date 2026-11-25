---
description: "Upper limit on residue C:P ratio in the decomposition factor"
---

# cpr\_cap

**Code reference:** `cpr_cap` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L16), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L80), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L498-L499)).

Upper limit applied to the residue C:P ratio before the phosphorus factor is computed.

[`cbn_surfrsd_decomp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cbn_surfrsd_decomp.f90#L99-L115) reduces surface residue decomposition when the residue is poor in nitrogen or phosphorus:

$$
f_{CN} = \exp\left(-0.693 \, \frac{\min(CN, CN_{cap}) - CN_{ref}}{CN_{ref}}\right), \qquad f = \min(f_{CN}, f_{CP}, 1)
$$

$f_{CP}$ uses the C:P ratio, [cpr\_cap](cpr_cap.md) and [cpr\_ref](cpr_ref.md) in the same way. A factor is 1 when the residue holds almost no N or P. Only surface residue uses these values: the call to the soil residue routine `cbn_rsd_decomp` is commented out ([`hru_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hru_control.f90#L399)).

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `cpr_cap` and uses 5000.0. The calibration parameter is `cpr_cap`.
