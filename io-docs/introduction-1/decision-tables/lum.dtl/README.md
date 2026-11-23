---
description: These files contain the Decision Tables.
---

# "name".dtl

The structure of the decision table files is different than that of most other SWAT+ input files. As usual, the first line is reserved for a title. The second line in the file specifies the total number of decision tables included in the file.&#x20;

Each decision table has three parts, which all have their own headers. First, the name of the decision table and the number of conditions, alternatives, and actions are specified.     &#x20;

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| name | Name of the decision table | string |  |  |  |
| conds | Number of conditions | integer |  |  |  |
| alts | Number of alternatives | integer |  |  |  |
| acts | Number of actions | integer |  |  |  |

Next, the conditions and alternatives are defined. The number of lines used for this part of the decision table depends on the number of conditions.

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [var](var.md) | Condition variable | string |  |  |  |
| [obj](obj.md) | Object type | string |  |  |  |
| [obj_num](obj_num.md) | Object ID | integer |  |  |  |
| [lim_var](lim_var.md) | Limit variable | string |  |  |  |
| [lim_op](lim_op.md) | Limit operator | string |  |  |  |
| [lim_const](lim_const.md) | Limit constant | real |  |  |  |
| [alt](alt.md) | Alternative | string |  |  |  |

Finally, the outcomes and actions are defined. The number of lines used for this part of the decision table depends on the number of actions.

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| [act\_typ](act_typ.md) | Type of action | string |  |  |  |
| [obj](obj-1.md) | Object type | string |  |  |  |
| [obj\_num](obj_num-1.md) | Object ID | integer |  |  |  |
| [name](name.md) | Name of the action | string |  |  |  |
| [option](option.md) | Action option | string |  |  |  |
| [const](const.md) | Action constant | real |  |  |  |
| [const2](const2.md) | Action constant | real |  |  |  |
| [fp](fp.md) | File pointer for action option | string |  |  |  |
| [outcome](outcome.md) | Outcome | string |  |  |  |
