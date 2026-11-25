---
description: Alternative
---

# alt

**Code reference:** `dtbl_lum(i)%alt(ic,ial)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L34)).

Enter one comparison per alternative. Numeric conditions recognize `<`, `>`, `<=`, `>=`, `=`, and `/=` (not equal). A hyphen skips the numeric comparison. Write the inequality token as `'/='` in the input file so its leading slash is read as data. [`cond_real.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cond_real.f90#L19-L52) · [`cond_integer.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cond_integer.f90#L15-L48)

Specialized conditions use their own operators. `plant_gro` and `plant_name_gro` test for growth on `=`. `plant_com` uses `=` for membership and `'/'` for nonmembership. [`conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditions.f90#L189-L220) · [`conditions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditions.f90#L690-L714)
