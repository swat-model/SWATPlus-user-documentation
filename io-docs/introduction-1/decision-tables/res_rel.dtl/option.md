---
description: "Release equation"
---

# option

**Code reference:** `dtbl_res(i)%act(iac)%option` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L21)).

Selects the release equation. Eligible rows are processed in order. $c_1$ is [const](const.md), $c_2$ is [const2](const2.md), $S$ is current storage, $V_p$ and $V_e$ are principal and emergency storage, and $I$ is the day's inflow, all in m³. An unrecognized option releases nothing and gives no warning. [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L101-L106)

| Option | Daily release | Source |
| ------ | ------------- | ------ |
| `rate` | $86400c_1$ ($c_1$ in m³/s) | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L104-L106) |
| `rate_pct` | $c_1V_p/100$ | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L108-L110) |
| `inflo_rate` | $\max(I+86400c_2, 86400c_1)$, so $c_1$ acts as a lower bound | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L112-L114) |
| `inflo_frac` | $c_1I$ | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L116-L118) |
| `ab_emer` | $S-V_e$ when $S>V_e$ | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L120-L122) |
| `days` | $(S-b)/c_1$, with base $b$ from [file_pointer](file_pointer.md): 0, $c_2V_p$, or $c_2V_e$ | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L124-L135) |
| `dyrt` | $(S-b)/c_1 + c_2V_p/100$, with $b$ = 0, $V_p$, or $V_e$ | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L139-L152) |
| `dyrt1` | As `dyrt`, but $b$ is built from condition row 5, 4, or 3 (`con1`, `con2`, `con3`) | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L154-L180) |
| `inflo_targ` | $I + S - V_p c$, floored at 0, where $c$ is `lim_const` of condition row number $c_1$ | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L182-L188) |
| `weir` | Weir equation using the named [weir.res](../../reservoirs/weir.res/README.md) record | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L190-L227) |
| `meas` | Measured flow from the named recall record | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L229-L240) |
| `natlake` | $k\,s\,(s/(V_p-s_0))^{1.5}$, with $s_0=c_1V_p$, $s=S-s_0$, $k=c_2$ | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L242-L251) |
| `nonirr-h06` | Hanazaki scheme for non-irrigation reservoirs; $c_1$ is its alpha | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L253-L287) |
| `irr-h06` | Hanazaki scheme for irrigation reservoirs; $c_1$ is alpha, $c_2$ is beta | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L289-L328) |
| `hydrop` | Hydropower scheme; $c_1$ and $c_2$ are the seasonal amplitude and phase | [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L330-L343) |

Cautions from source reading at this commit: `natlake` takes a fractional power of a negative number when storage is below $s_0$. `hydrop` computes its seasonal factor without a sine function. `dyrt1` assumes the table has the hard-coded condition row. With more than one time step per day in [time.sim](../../simulation-settings/time.sim/README.md), only `days`, `meas`, and the percentage term of `dyrt`/`dyrt1` are divided by the number of steps, so other options can release several times their daily amount. [`res_hydro.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_hydro.f90#L85-L87)
