---
description: Print interval within the period
---

# interval

**Code reference:** `pco%int_day` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L163)).

This parameter specifies the interval in days within the daily printing period (Fortran struct default: `1`). In [`basin_print_codes_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_print_codes_read.f90#L789-L790), any value `<= 0` is reset to `1` and `pco%int_day_cur` is initialized to `pco%int_day`. During simulation, [`time_control.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L212-L213) increments `pco%int_day_cur` each day and wraps it back to `1` when it exceeds `interval`.

{% hint style="info" %}
Example: If _interval_ = 2, output will be printed for every other day.
{% endhint %}
