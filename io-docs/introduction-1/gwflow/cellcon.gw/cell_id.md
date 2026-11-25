---
description: "Cell number; must equal the line's position"
---

# cell_id

**Code reference:** `cell_id_in` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L190), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L515)).

Cell number. It must equal the line's position among the data lines; otherwise SWAT+ writes "row out of order" to the GWFlow record file and stops ([`gwflow_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L515-L519)).
