# Surface Runoff from Urban Areas

&#x20;            In urban areas, surface runoff is calculated separately for the directly connected impervious area and the disconnected impervious/pervious area. For directly connected impervious areas, a curve number of 98 is always used. For disconnected impervious/pervious areas, a composite curve number is calculated and used in the surface runoff calculations. The equations used to calculate the composite curve number for disconnected impervious/pervious areas are (Soil Conservation Service Engineering Division, 1986):

$$CN_c=CN_p+imp_{tot}*(CN_{imp}-CN_p)*(1-\frac{imp_{dcon}}{2*imp_{tot}})$$      if          $$imp_{tot}<0.30$$       6:3.2.1

$$CN_c=CN_p+imp_{tot}*(CN_{imp}-CN_p)$$                                 if          $$imp_{tot}>0.30$$       6:3.2.2

where $$CN_c$$ is the composite moisture condition II curve number, $$CN_p$$ is the pervious moisture condition II curve number, $$CN_{imp}$$ is the impervious moisture condition II curve number, $$imp_{tot}$$ is the fraction of the HRU area that is impervious (both directly connected and disconnected), and $$imp_{dcon}$$ is the fraction of the HRU area that is impervious but not hydraulically connected to the drainage system.

&#x20;      The fraction of the HRU area that is impervious but not hydraulically connected to the drainage system, $$imp_{dcon}$$, is calculated

&#x20;           $$imp_{dcon}=imp_{tot}-imp_{con}$$                                                                                          6:3.2.3

where $$imp_{tot}$$ is the fraction of the HRU area that is impervious (both directly connected and disconnected), and $$imp_{con}$$ is the fraction of the HRU area that is impervious and hydraulically connected to the drainage system.

Table 6:3-2: SWAT+ input variables that pertain to surface runoff calculations in urban areas.

| Variable Name | Definition                                                                                                                 | File Name |
| ------------- | -------------------------------------------------------------------------------------------------------------------------- | --------- |
| CN2           | $$CN_p$$: SCS moisture condition II curve number for pervious areas                                                        | .mgt      |
| CNOP          | $$CN_p$$: SCS moisture condition II curve number for pervious areas specified in plant, harvest/kill and tillage operation | .mgt      |
| URBCN2        | $$CN_{imp}$$: SCS moisture condition II curve number for impervious areas                                                  | urban.dat |
| FIMP          | $$imp_{tot}$$: fraction of urban land type area that is impervious                                                         | urban.dat |
| FCIMP         | $$imp_{con}$$: fraction of urban land type area that is connected impervious                                               | urban.dat |
