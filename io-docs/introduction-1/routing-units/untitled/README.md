---
description: >-
  This file references other files specifying the elements that are part of a
  Routing Unit and its topographic and field properties.
---

# rout\_unit.rtu

| Field               | Description                                 | Type    |
| ------------------- | ------------------------------------------- | ------- |
| id                  | ID of the Routing Unit                      | integer |
| name                | Name of the Routing Unit                    | string  |
| [define](define.md) | Pointer to the Routing Unit definition file | string  |
| dlr                 | Delivery ratio                              |         |
| [topo](topo.md)     | Pointer to the topography file              | string  |
| [field](field.md)   | Pointer to the field file                   | string  |
