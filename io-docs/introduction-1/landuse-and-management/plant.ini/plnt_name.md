---
description: Plant name as in plant database
---

# plnt\_name

**Code reference:** `pcomdb(icom)%pl(iplt)%cpnm` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/plant_data_module.f90#L133), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/readpcom.f90#L68)).

Character string (`len=40`, struct default `"frsd"`) acting as a foreign key referencing the plant name in [**plants.plt**](../../databases/plants.plt/README.md). SWAT+ crosswalks `cpnm` against `pldb%plantnm` in [`readpcom.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/readpcom.f90#L73-L82) and logs unmatched names to `diagnostics.out`.
