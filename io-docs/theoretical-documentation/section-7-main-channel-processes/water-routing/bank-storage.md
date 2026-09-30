# Bank Storage

The amount of water entering bank storage on a given day is calculated:

&#x20;         $$bnk_{in}=tloss*(1-fr_{trns})$$                                                                            7:1.7.1

where $$bnk_{in}$$ is the amount of water entering bank storage (m$$^3$$ H$$_2$$O), $$tloss$$ are the channel transmission losses (m$$^3$$ H$$_2$$O), and $$fr_{trns}$$ is the fraction of transmission losses partitioned to the deep aquifer.

&#x20;              Bank storage contributes flow to the main channel or reach within the subbasin. Bank flow is simulated with a recession curve similar to that used for groundwater. The volume of water entering the reach from bank storage is calculated:

&#x20;                   $$V_{bnk}=bnk*(1-exp[-\alpha_{bnk}])$$                                                        7:1.7.2

where $$V_{bnk}$$ is the volume of water added to the reach via return flow from bank storage(m$$^3$$ H$$_2$$O), $$bnk$$ is the total amount of water in bank storage (m$$^3$$ H$$_2$$O), and $$\alpha_{bnk}$$ is the bank flow recession constant or constant of proportionality.

&#x20;          Water may move from bank storage into an adjacent unsaturated zone. SWAT+ models the movement of water into adjacent unsaturated areas as a function of water demand for evapotranspiration. To avoid confusion with soil evaporation and transpiration, this process has been termed ‘revap’. This process is significant in watersheds where the saturated zone is not very far below the surface or where deep-rooted plants are growing. ‘Revap’ from bank storage is governed by the groundwater revap coefficient defined for the last HRU in the subbasin.

&#x20;        The maximum amount of water than will be removed from bank storage via ‘revap’ on a given day is:

&#x20;               $$bnk_{revap,mx}=\beta_{rev}*E_o*L_{ch}*W$$                                                             7:1.7.3

where $$bnk_{revap,mx}$$ is the maximum amount of water moving into the unsaturated zone in response to water deficiencies (m$$^3$$ H$$_2$$O), $$\beta_{rev}$$ is the revap coefficient, $$E_o$$ is the potential evapotranspiration for the day (mm H$$_2$$O), $$L_{ch}$$ is the channel length (km), and $$W$$ is the width of the channel at water level (m). The actual amount of revap that will occur on a given day is calculated:&#x20;

&#x20;               $$bnk_{revap}=bnk$$                          if        $$bnk<bnk_{revap,mx}$$                                          7:1.7.4

&#x20;               $$bnk_{revap}=bnk_{revap,mx}$$             if        $$bnk \ge bnk_{revap,mx}$$                                           7:1.7.5

where $$bnk_{revap}$$ is the actual amount of water moving into the unsaturated zone in response to water deficiencies (m$$^3$$ H$$_2$$O), $$bnk_{revap,mx}$$ is the maximum amount of water moving into the unsaturated zone in response to water deficiencies (m$$^3$$ H$$_2$$O), and $$bnk$$ is the amount of water in bank storage at the beginning of day $$i$$ (m$$^3$$ H$$_2$$O).

Table 7:1-7: SWAT+ input variables that pertain to bank storage.

| Variable Name | Definition                                                                     | File Name |
| ------------- | ------------------------------------------------------------------------------ | --------- |
| TRNSRCH       | $$fr_{trns}$$: Fraction of transmission losses partitioned to the deep aquifer | .bsn      |
| ALPHA\_BNK    | $$\alpha_{bnk}$$: Bank flow recession constant or constant of proportionality  | .rte      |
| GW\_REVAP     | $$\beta_{rev}$$: Revap coefficient                                             | .gw       |
