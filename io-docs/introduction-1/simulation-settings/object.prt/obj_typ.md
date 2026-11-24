---
description: Type of object to print output for
---

# obj\_typ

**Code reference:** `ob_out(ii)%obtyp` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L258)).

In [`object_read_output.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/object_read_output.f90#L56-L76), SWAT+ maps `obj_typ` and `obj_typ_no` to the global object index $i_{\text{ob}} = i_{\text{ob1}} + n_{\text{typ}} - 1$, where $i_{\text{ob1}}$ is the starting index (`sp_ob1%...`) for that object type and $n_{\text{typ}}$ is `obj_typ_no`. Output can be printed for the following types of objects:

| Object Code | Description |
| --- | --- |
| hru | HRU |
| hlt | HRU-LTE |
| ru | Routing Unit |
| res | Reservoir |
| cha | Channel |
| exc | Export Coefficient |
| dr | Delivery Ratio |
| out | Outlet |
| sdc | SWAT-DEG channel |
