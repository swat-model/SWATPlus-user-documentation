---
description: "Comparison token for each alternative"
---

# alt(ic,ial)

**Code reference:** `dtbl_flo(i)%alt(ic,ial)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L34)).

Comparison token for condition row `ic` in alternative `ial`; enter one per alternative. Numeric conditions use `<`, `>`, `<=`, `>=`, `=`, or `'/='`, and a hyphen skips them. Category conditions behave differently; see [lum.dtl alt](../lum.dtl/alt.md). [`cond_real.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cond_real.f90#L19-L52)
