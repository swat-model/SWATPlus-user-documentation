---
description: "Maximum soil temperature (°C) of the decomposition temperature function"
---

# tx

**Code reference:** `org_con%tx` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_module.f90#L116), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/carbon_bsn_read.f90#L76), [calibration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parm_select.f90#L506-L507)).

Upper temperature limit $T_x$ (°C) of the temperature factor below:

$$
f_T = \frac{(T - T_n)^q \, (T_x - T)}{(T_{op} - T_n)^q \, (T_x - T_{op})}, \qquad q = \frac{T_n - T_{op}}{T_{op} - T_x}
$$

[`fcgd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/fcgd.f90#L14-L27) returns 0 when $T \le T_n$ or $T \ge T_x$. The function is used for decomposition when [tmpf](tmpf.md) `= 2` and for biological mixing unless `tmpf = 3`. Keep $T_n < T_{op} < T_x$.

The SWAT+ example file (`refdata/Ames_sub1`) heads this column `t_cbn_max` and uses 50.0. The calibration parameter is `t_cbn_max`.
