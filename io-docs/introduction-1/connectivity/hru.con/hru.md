---
description: Pointer to the object data file
---

# 'obj'

The pointer to the object data file is a foreign key referencing the unique ID in the respective object data file. The header of this column is different in each connect file.

| Connect file   | Column header | Object data file                                                  |
| -------------- | ------------- | ----------------------------------------------------------------- |
| hru.con        | hru           | [**hru-data.hru**](../../hydrologic-response-units/hru-data.hru/) |
| hru-lte.con    | hlt           | [**hru-lte.hru**](../../hydrologic-response-units/hru-lte.hru/)   |
| rout\_unit.con | rtu           | [**rout\_unit.rtu**](../../routing-units/untitled/)               |
| aquifer.con    | aqu           | [**aquifer.aqu**](../../aquifers/aquifer.aqu/)                    |
| chandeg.con    | lcha          | [**channel-lte.cha**](../../channels/channel-lte.cha/)            |
| reservoir.con  | res           | [**reservoir.res**](../../reservoirs/reservoir.res/)              |
| recall.con     | rec           | [**recall.rec**](../../point-sources-and-inlets/recall.rec/)      |
| exco.con       | exc           |                                                                   |
| delratio.con   | dlr           |                                                                   |
| outlet.con     | out           | No data file                                                      |
