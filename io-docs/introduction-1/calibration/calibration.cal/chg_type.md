---
description: Parameter change mode applied in calibration.cal.
---

# chg\_type

**Code reference:** `cal_upd(i)%chg_typ` ([read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_parmchg_read.f90#L68), [formula](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/chg_par.f90#L36-L53)).

String (up to 16 characters, struct default `""`) specifying how [`chg_par.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/chg_par.f90#L36-L53) updates the current value $p_{\text{cur}}$ using `val` ($v$):

- `absval`: $p_{\text{new}} = v$
- `abschg`: $p_{\text{new}} = p_{\text{cur}} + v$
- `pctchg`: $p_{\text{new}} = (1 + v / 100)\,p_{\text{cur}}$
- `relchg`: $p_{\text{new}} = (1 + v)\,p_{\text{cur}}$

After applying the formula, [`chg_par.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/chg_par.f90#L52-L53) clamps $p_{\text{new}}$ to $[p_{\min}, p_{\max}]$ from `abs_min` and `abs_max` in `cal_parms.cal`.
