# Outflow

Pesticide is removed from the reach segment in outflow. The amount of dissolved and particulate pesticide removed from the reach segment in outflow is:

&#x20;          $$pst_{sol,o}=Q*\frac{F_d*pst_{rchwtr}}{V}$$                                                                      7:4.1.13

&#x20;          $$pst_{sorb,o}=Q*\frac{F_p*pst_{rchwtr}}{V}$$                                                                    7:4.1.14

where $$pst_{sol,o}$$ is the amount of dissolved pesticide removed via outflow (mg pst), $$pst_{sorb,o}$$ is the amount of particulate pesticide removed via outflow (mg pst), $$Q$$ is the rate of outflow from the reach segment (m$$^3$$ H$$_2$$O/day), $$F_d$$ is the fraction of total pesticide in the dissolved phase, $$F_p$$ is the fraction of total pesticide in the particulate phase, $$pst_{rchwtr}$$ is the amount of pesticide in the water (mg pst), and $$V$$ is the volume of water in the reach segment (m$$^3$$ H$$_2$$O).

Table 7:4-1: SWAT+ input variables that pesticide partitioning.

| Variable Name | Definition                                                                               | Input File |
| ------------- | ---------------------------------------------------------------------------------------- | ---------- |
| CHPST\_KOC    | $$K_d$$: Pesticide partition coefficient (m$$^3$$/g)                                     | .swq       |
| CHPST\_REA    | $$k_{p,aq}$$: Rate constant for degradation or removal of pesticide in the water (1/day) | .swq       |
| CHPST\_VOL    | $$v_v$$: Volatilization mass-transfer coefficient (m/day)                                | .swq       |
| CHPST\_STL    | $$v_s$$: Pesticide settling velocity (m/day)                                             | .swq       |
