# Water Transfer

&#x20;        While water is most typically removed from a water body for irrigation purposes, SWAT+ also allows water to be transferred from one water body to another. This is performed with a transfer command in the watershed configuration file.&#x20;

&#x20;              The transfer command can be used to move water from any reservoir or reach in the watershed to any other reservoir or reach in the watershed. The user must input the type of water source, the location of the source, the type of water body receiving the transfer, the location of the receiving water body, and the amount of water transferred.&#x20;

&#x20;                   Three options are provided to specify the amount of water transferred: a fraction of the volume of water in the source; a volume of water left in the source; or the volume of water transferred. The transfer is performed every day of the simulation.&#x20;

&#x20;                        The transfer of water from one water body to another can be accomplished using other methods. For example, water could be removed from one water body via consumptive water use and added to another water body using point source files.

Table 6:2-3: SWAT+ input variables that pertain to water transfer.

| Variable Name | Definition                          | Input File |
| ------------- | ----------------------------------- | ---------- |
| DEP\_TYPE     | Water source type                   | .fig       |
| DEP\_NUM      | Water source location               | .fig       |
| DEST\_TYPE    | Destination type                    | .fig       |
| DEST\_NUM     | Destination location                | .fig       |
| TRANS\_AMT    | Amount of water transferred         | .fig       |
| TRANS\_CODE   | Rule code governing water transfer. | .fig       |
