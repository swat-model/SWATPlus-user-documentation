---
description: Intended salt-initialization pointer (read but not used in initial.cha in main 6f515368)
---

# salt

**Code reference:** `ch_init(ich)%salt` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L45)).

Intended salt-initialization pointer. SWAT+ main (6f515368) reads this `initial.cha` field but does not use its value afterward. Active channel salt initialization uses the salt pointer in `initial.cha_cs`.
