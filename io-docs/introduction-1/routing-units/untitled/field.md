---
description: Pointer to the field file
---

# field

**Code reference:** `ru(i)%dbsc%field_db` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_module.f90#L15)).

The pointer to the field file is a foreign key referencing [name](../../hydrology/field.fld/name.md) in [**field.fld**](../../hydrology/field.fld/). During input parsing in [`ru_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_read.f90#L241-L251), SWAT+ matches the name against `field_db(:)%name` and copies `length`, `wid`, and `ang` into `ru(i)%field` (Fortran struct defaults when unmatched: `length = 500.` `m`, `wid = 100.` `m`, and `ang = 30.` `deg` in [`ru_module.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ru_module.f90#L27-L29)).

Only `ru(iru)%field%length` ($L_{\text{fld}}$, `m`) enters routing-unit calculations: [`time_conc_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_conc_init.f90#L49-L51) converts it to kilometers ($L_{\text{ch}} = L_{\text{fld}} / 1000$) to compute the channel travel time $t_{\text{ch}}$ for Routing Unit time of concentration. The copied `wid` and `ang` fields are not used in routing-unit calculations.
