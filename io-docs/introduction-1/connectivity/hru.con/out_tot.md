---
description: Total number of outgoing hydrographs
---

# out\_tot

**Code reference:** `ob(i)%src_tot` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L357)).

The number of outgoing hydrographs determines how many spatial objects receive flow from an object. Enter 0 when the object has no outgoing hydrographs. For each outgoing hydrograph, repeat the next four columns: obj_typ, obj_id, hyd_typ, and frac.

{% hint style="warning" %}
When GWFlow is active and a record lists any `aqu` receiver, SWAT+ [drops the last connection](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hyd_read_connect.f90#L303-L314) of that record, whether or not it is the `aqu` one.
{% endhint %}
