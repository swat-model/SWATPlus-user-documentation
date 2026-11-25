---
description: Plant population (read but not used in main 6f515368)
---

# plnt\_pop

**Code reference:** `pcomdb(icom)%pl(iplt)%pop` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L141), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/readpcom.f90#L70)).

Real value (default `0.0`) intended to specify initial plant population. Although [`plant_init.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_init.f90#L330-L335) checks `pcom(j)%plcur(ipl)%pop_com`, that field is never populated from `pcomdb(icom)%pl(iplt)%pop`.

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).*
