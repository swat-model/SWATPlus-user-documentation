---
description: This file contains water allocation tables.
---

# water\_allocation.wro

The structure of the water allocation file is different than that of most other SWAT+ input files. As usual, the first line is reserved for a title. The second line in the file specifies the total number of water allocation tables included in the file.&#x20;

Each water allocation table has three parts, which all have their own headers. First, the name of the water allocation table, the rule type, the number of source and demand objects, and whether or not one of the source objects is a channel are specified. &#x20;

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| name | Name of the water allocation table | string |  |  |  |
| [rule_typ](rule_typ.md) | Rule type to allocate water | string |  |  |  |
| src_obs | Number of source objects | integer |  |  |  |
| dmd_obs | Number of demand objects | integer |  |  |  |
| [cha_ob](cha_ob.md) | Channel as source object | string |  |  |  |

Next, the source objects and their monthly limits are defined. Source objects can be channels, reservoirs, aquifers, or an unlimited source. There needs to be one line per source object.

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| num | Source object number | integer |  |  |  |
| [ob_typ](ob_typ-source.md) | Object type of the source object | string |  |  |  |
| ob_num | ID of the source object | integer |  |  |  |
| [limit_mon](limit_mon.md) | Monthly limits | real |  |  |  |

Finally, the demand objects are defined. Demand can be irrigation demand from an HRU, municipal demand, or demand to transfer to another object.There needs to be one line per demand object.

| **Field** | **Description** | **Type** | **Unit** | **Default** | **Range** |
| --------- | --------------- | -------- | -------- | ----------- | --------- |
| num | Demand object number | integer |  |  |  |
| [ob_typ](ob_typ-demand.md) | Object type of the demand object | string |  |  |  |
| ob_num | ID of the demand object | integer |  |  |  |
| [withdr](withdr.md) | Withdrawal type | string |  |  |  |
| [amount](amount.md) | Withdrawal amount | real |  |  |  |
| [right](right.md) | Water right | string |  |  |  |
| treat_typ | Currently not functional | string |  |  |  |
| treatment | Currently not functional | string |  |  |  |
| [rcv_ob](rcv_ob.md) | Object type of the receiving object | string |  |  |  |
| [rcv_num](rcv_num.md) | ID of the receiving object | integer |  |  |  |
| rcv_dtl | Currently not used | string |  |  |  |
| [srcs](srcs.md) | Number of source objects available for the demand object | integer |  |  |  |
| [src](src.md) | Source object ID | integer |  |  |  |
| [frac](frac.md) | Fraction of demand to be met by source object | real |  |  |  |
| [comp](comp.md) | Compensation from source object | string |  |  |  |

