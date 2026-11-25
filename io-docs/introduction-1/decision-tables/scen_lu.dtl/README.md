---
description: "This file defines decision tables for land-use scenarios."
---

{% hint style="info" %}
An Editor export of this format has not been verified. Field names and values in the table are based on the SWAT+ Fortran source. A dash means that a unit, recommended default, or range has not been established.
{% endhint %}

This file defines decision tables for land-use scenarios.

# scen_lu.dtl

Line 1 is the title. Line 2 starts with the number of decision tables. Leave line 3 blank. For each table, enter a header and the definition row, then a condition header and exactly `conds` condition rows, then an action header and exactly `acts` action rows. Each condition row ends with `alts` comparison entries. Each action row ends with `alts` outcomes in the same order. Leave a blank line after each action block, including the last one. [`dtbl_scen_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_scen_read.f90#L38-L75)

[scen_dtl.upd](../../calibration/scen_dtl.upd/) selects the scenario tables for the daily update.

## Number of decision tables

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [mdtbl](mdtbl.md) | Number of decision tables | integer | n/a | — | — |

## Table definition

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [name](name.md) | Record name | string | n/a | — | — |
| [conds](conds.md) | Number of condition entries that follow for this table | integer | n/a | — | — |
| [alts](alts.md) | Number of alternative condition sets evaluated for each condition | integer | n/a | — | — |
| [acts](acts.md) | Number of action entries that follow for this table | integer | n/a | — | — |

## Conditions

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [var](var.md) | Condition variable tested (e.g. volume, flow, sw, time) | string | n/a | — | — |
| [ob](ob.md) | Object type the condition applies to (e.g. res, hru, canal) | string | n/a | — | — |
| [ob_num](ob_num.md) | Object index or condition-specific numeric input | integer | n/a | — | — |
| [lim_var](lim_var.md) | Limit variable compared against (e.g. evol, pvol, fc, ul) | string | n/a | — | — |
| [lim_op](lim_op.md) | Arithmetic operator for building a threshold where the condition uses one | string | n/a | — | — |
| [lim_const](lim_const.md) | Constant value used in the limit comparison | real | — | — | — |
| [alt(ic,ial)](alt_ic_ial.md) | Comparison token, repeated once per alternative | string | n/a | — | — |

## Actions

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [typ](typ.md) | Scenario action type, such as lu_change or snow_change | string | n/a | — | — |
| [ob](ob_2.md) | Object type the action applies to (e.g. res, hru, canal) | string | n/a | — | — |
| [ob_num](ob_num_2.md) | Object index or other integer input for the action | integer | n/a | — | — |
| [name](name_2.md) | Action name | string | n/a | — | — |
| [option](option.md) | Action option specific to its type (e.g. rate input, drawdown days, weir equation pointer) | string | n/a | — | — |
| [const](const.md) | Primary constant for the action (e.g. rate, days) | real | — | — | — |
| [const2](const2.md) | Secondary constant for the action (e.g. rate, days) | real | — | — | — |
| [file_pointer](file_pointer.md) | Action-specific selector or referenced record name | string | n/a | — | — |
| [act_outcomes(iac,ial)](act_outcomes_iac_ial.md) | Action outcome token, repeated once per alternative | string | n/a | — | — |

**Type note:** `string` means Fortran `character`; `integer` and `real` use the same names in Fortran.
