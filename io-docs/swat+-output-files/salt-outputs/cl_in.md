---
description: "Total chloride entering the channel, including groundwater"
---

# cl_in

**Code reference:** `chsalt_d(iru)%salt(isalt)%tot_in` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_salt_module.f90#L8)).

Reported chloride inlet, including groundwater from the linked-aquifer diagnostic. The controller replaces the working inlet after adding that linked load, so the printed total can differ from the input used for routing. See [daily channel calculations](channel-salt.md#daily-channel-calculations).

**Unit:** kg.

The same printed heading can appear in daily, monthly, yearly, and average-annual variants of this family. The reporting interval changes the row period; this page does not infer a total-versus-average rule beyond what the family output and source establish.

[Back to schema](channel-salt.md).
