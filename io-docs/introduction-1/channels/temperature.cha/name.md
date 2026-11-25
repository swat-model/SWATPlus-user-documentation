---
description: "Record name"
---

# name

**Code reference:** `w_temp(ich_temp)%name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/channel_data_module.f90#L170)).

Record name (`character(len=13)`), read into `w_temp(1:)` by [`ch_read_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_read_temp.f90#L54). Because [`ch_temp.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_temp.f90#L170-L181) reads only `w_temp(0)`, no channel lookup uses `name`.
