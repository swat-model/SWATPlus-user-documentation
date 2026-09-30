# Wetland Outflow

The wetland releases water whenever the water volume exceeds the normal storage volume, $$V_{nor}$$. Wetland outflow is calculated:

&#x20;           $$V_{flowout}=0$$               if     $$V<V_{nor}$$                                                  8:1.2.14

&#x20;           $$V_{flowout}=\frac{V-V_{nor}}{10}$$      if      $$V_{nor} \le V \le V_{mx}$$                                     8:1.2.15

&#x20;            $$V_{flowout}=V-V_{mx}$$ if       $$V>V_{mx}$$                                                8:1.2.16

where $$V_{flowout}$$ is the volume of water flowing out of the water body during the day  (m$$^3$$ H$$_2$$O), $$V$$ is the volume of water stored in the wetland (m$$^3$$ H$$_2$$O), $$V_{mx}$$ is the volume of water held in the wetland when filled to the maximum water level (m$$^3$$ H$$_2$$O), and $$V_{nor}$$ is the volume of water held in the wetland when filled to the normal water level (m$$^3$$ H$$_2$$O).

Table 8:1-2: SWAT+ input variables that pertain to ponds and wetlands.

|            |                                                                                                                |      |
| ---------- | -------------------------------------------------------------------------------------------------------------- | ---- |
| PND\_ESA   | $$SA_{em}$$: Surface area of the pond when filled to the emergency spillway (ha)                               | .pnd |
| PND\_PSA   | $$SA_{pr}$$: Surface area of the pond when filled to the principal spillway (ha)                               | .pnd |
| PND\_EVOL  | $$V_{em}$$: Volume of water held in the pond when filled to the emergency spillway (10$$^4$$ m$$^3$$ H$$_2$$O) | .pnd |
| PND\_PVOL  | $$V_{pr}$$: Volume of water held in the pond when filled to the principal spillway(10$$^4$$ m$$^3$$ H$$_2$$O)  | .pnd |
| WET\_MXSA  | $$SA_{mx}$$: Surface area of the wetland when filled to the maximum water level (ha)                           | .pnd |
| WET\_NSA   | $$SA_{nor}$$: Surface area of the wetland when filled to the normal water level (ha)                           | .pnd |
| WET\_MXVOL | $$V_{mx}$$: Volume of water held in the wetland when filled to the maximum water level (m$$^3$$ H$$_2$$O)      | .pnd |
| WET\_NVOL  | $$V_{nor}$$: Volume of water held in the wetland when filled to the normal water level (m$$^3$$ H$$_2$$O)      | .pnd |
| PND\_FR    | $$fr_{imp}$$: Fraction of the subbasin area draining into the pond                                             | .pnd |
| WET\_FR    | $$fr_{imp}$$: Fraction of the subbasin area draining into the wetland                                          | .pnd |
| PND\_K     | $$K_{sat}$$: Effective saturated hydraulic conductivity of the pond bottom (mm/hr)                             | .pnd |
| WET\_K     | $$K_{sat}$$: Effective saturated hydraulic conductivity of the wetland bottom (mm/hr)                          | .pnd |
| IFLOD1     | $$mon_{fld,beg}$$: Beginning month of the flood season                                                         | .pnd |
| IFLOD2     | $$mon_{fld,end}$$: Ending month of the flood season                                                            | .pnd |
| NDTARG     | $$ND_{targ}$$: Number of days required for the reservoir to reach target storage                               | .pnd |
