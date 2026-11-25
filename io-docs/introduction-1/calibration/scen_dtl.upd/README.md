---
description: Conditional scenario decision-table update rules read from scen_dtl.upd.
---

{% hint style="info" %}
An Editor export of this format has not been verified. Field names and values in the table are based on the SWAT+ Fortran source. A dash means that a unit, recommended default, or range has not been established.
{% endhint %}

Specifies conditional scenario update tables evaluated daily during simulation, read from the working directory (`scen_dtl.upd`, not listed in `file.cio`) into `upd_cond` ([`calibration_data_module.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/calibration_data_module.f90#L52)) by [`cal_cond_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cal_cond_read.f90#L43-L62) (called from [`main.f90.in`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/main.f90.in#L86)).

# scen\_dtl.upd

## Number of rules

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [num\_dtls](num_dtls.md) | Number of scenario update rules | integer | — | — | > 0 |

## Update rules

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [max\_hits](max_hits.md) | Maximum executions limit (parsed but unused) | integer | — | 0 | — |
| [typ](typ.md) | Update table type (parsed but unused) | string | — | `""` | — |
| [dtbl](dtbl.md) | Name of the ruleset in `scen_lu.dtl` that schedules this update | string | — | `""` | — |

**Type note:** `string` means Fortran `character`; `integer` and `real` use the same names in Fortran.
