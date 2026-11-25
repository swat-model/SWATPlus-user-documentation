---
description: "Name identifying this initial pathogen set"
---

# path\_init\_name(ipathi)

**Code reference:** `path_init_name(ipathi)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L6)).

Name identifying this water/benthic pathogen initialization set, read in [`path_cha_res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/path_cha_res_read.f90#L61). It is matched against [path](../initial.aqu_cs/path.md) in [**initial.aqu\_cs**](../initial.aqu_cs/) ([`aqu_read_init_cs.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_read_init_cs.f90#L101)), [path](../../reservoirs/initial.res/path.md) in [**initial.res**](../../reservoirs/initial.res/) ([`res_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/res_read.f90#L102); [`wet_initial.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wet_initial.f90#L68)), and [path](../initial.cha_cs/path.md) in [**initial.cha\_cs**](../initial.cha_cs/) ([`sd_channel_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_read.f90#L246)).
