---
description: User-defined action name (written to management diagnostics)
---

# name

**Code reference:** `dtbl_lum(i)%act(iac)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L20)).

The action name is defined by the user. SWAT+ main (6f515368) writes it to management diagnostics when management output is enabled; it is not the action-type selector.

**Current use:** [management diagnostic output](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L163).
