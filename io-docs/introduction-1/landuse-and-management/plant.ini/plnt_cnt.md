---
description: Number of plants in the community
---

# plnt\_cnt

**Code reference:** `pcomdb(icom)%plants_com` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L148), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/readpcom.f90#L62)).

Integer count (struct default `1`) of plant entries belonging to this plant community. It controls allocation and reading of the subsequent plant rows in [`readpcom.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/readpcom.f90#L65-L67) and sets `pcom(j)%npl` during HRU initialization in [`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L87). This number must match the number of plant lines listed beneath the community header.
