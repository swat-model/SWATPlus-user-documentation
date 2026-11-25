---
description: Record name
---

# name

**Code reference:** `pest_init_name(ipesti)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L5)).

Name of the water/benthic pesticide initialization set, read in [`pest_cha_res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/pest_cha_res_read.f90#L62) into the separate character array `pest_init_name` rather than `pest_water_ini%name`.

It is matched against [pest](../initial.aqu_cs/pest.md) in [**initial.aqu\_cs**](../initial.aqu_cs/) ([`aqu_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L84)), [pest](../../channels/initial.cha/ch_pest.md) in [**initial.cha**](../../channels/initial.cha/) ([`sd_channel_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_read.f90#L239)), and [pest](../../reservoirs/initial.res/res_pest.md) in [**initial.res**](../../reservoirs/initial.res/) ([`res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read.f90#L94) for reservoirs; [`wet_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_initial.f90#L61) resolves the wetland index, though `wet_water%pest` is not assigned there).
