---
description: Hydrograph connections
---

# hydcon

**Code reference:** `pco%hydcon` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_module.f90#L179)).

Code (`"y"` or `"n"`; Fortran struct default: `"n"`) controlling hydrograph connection output. When set to `"y"`, [`header_hyd.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_hyd.f90#L9-L16) opens `hydcon.out` (and `hydcon.csv` when `csvout = "y"`), and [`hyd_connect_out.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hyd_connect_out.f90#L19-L37) writes object connectivity records.

{% hint style="warning" %}
This output file is used by the SWAT+ developers for debugging connectivity errors and infinite loops. Its usefulness for SWAT+ users is probably very limited. Accordingly, there is no description of this output file included in the [SWAT+ Output Files](https://app.gitbook.com/s/-MTFpIHUB1K63DLhLJaf/swat+-output-files) section.
{% endhint %}
