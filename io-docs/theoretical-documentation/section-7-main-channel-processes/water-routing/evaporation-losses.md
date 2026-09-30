# Evaporation Losses

Evaporation losses from the reach are calculated:

&#x20;          $$E_{ch}=coef_{ev}*E_o*L_{ch}*W*fr_{\Delta t}$$                                                              7:1.6.1

where $$E_{ch}$$ is the evaporation from the reach for the day (m$$^3$$ H$$_2$$O), $$coef_{ev}$$ is an evaporation coefficient, $$E_o$$ is potential evaporation (mm H$$_2$$O), $$L_{ch}$$ is the channel length (km), $$W$$ is the channel width at water level (m), and $$fr_{\Delta t}$$ is the fraction of the time step in which water is flowing in the channel.&#x20;

&#x20;               The evaporation coefficient is a calibration parameter for the user and is allowed to vary between 0.0 and 1.0.&#x20;

&#x20;                The fraction of the time step in which water is flowing in the channel is calculated by dividing the travel time by the length of the time step.

Table 7:1-6: SWAT+ input variables that pertain to evaporation losses.

| Variable Name | Definition                                         | File Name |
| ------------- | -------------------------------------------------- | --------- |
| EVRCH         | $$coef_{ev}$$: Reach evaporation adjustment factor | .bsn      |
| CH\_L(2)      | $$L_{ch}$$: Length of main channel (km)            | .rte      |
