# Routing Units

Routing Units are the spatial units in SWAT+ that allow us to lump outputs and route them to any other spatial object. Routing Units do not have a lot of properties as they mostly serve the purpose of collecting hydrographs. The simulation of the processes generating those hydrographs is controlled by the properties of the individual elements within a routing unit.

* [**rout\_unit.rtu**](untitled/) references other files specifying the elements that are part of a Routing Unit and its topographic and field properties.
* [**rout\_unit.def**](untitled-1/) specifies which elements a Routing Unit contains.
* [**rout\_unit.ele**](untitled-2/) lists all elements that are part of a Routing Unit.
* [**delratio.del**](delratio.del/) links named delivery-ratio sets to organic/mineral and constituent delivery-ratio records.
* [**dr\_om.del**](dr_om.del/) supplies organic/mineral delivery ratios for water, sediment, nutrients, and oxygen/temperature fields.
* [**dr\_pest.del**](dr_pest.del/), [**dr\_path.del**](dr_path.del/), [**dr\_hmet.del**](dr_hmet.del/), and [**dr\_salt.del**](dr_salt.del/) supply constituent delivery ratios for pesticides, pathogens, heavy metals, and salt ions used by standalone delivery-ratio (`dr`) objects.
