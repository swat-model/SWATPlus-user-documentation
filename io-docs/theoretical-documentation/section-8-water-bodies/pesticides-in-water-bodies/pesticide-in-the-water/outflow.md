# Outflow

Pesticide is removed from the water body in outflow. The amount of dissolved and particulate pesticide removed from the water body in outflow is:

&#x20;     $$pst_{sol,o}=Q*\frac{F_d*pst_{lkwtr}}{V}$$                                                           8:4.1.14

&#x20;     $$pst_{sorb,o}=Q*\frac{F_p*pst_{lkwtr}}{V}$$                                                          8:4.1.15

where $$pst_{sol,o}$$ is the amount of dissolved pesticide removed via outflow (mg pst), $$pst_{sorb,o}$$ is the amount of particulate pesticide removed via outflow (mg pst), $$Q$$ is the rate of outflow from the water body (m$$^3$$ H$$_2$$O/day), $$F_d$$ is the fraction of total pesticide in the dissolved phase, $$F_p$$ is the fraction of total pesticide in the particulate phase, $$pst_{lkwtr}$$ is the amount of pesticide in the water (mg pst), and $$V$$ is the volume of water in the water body (m$$^3$$ H$$_2$$O).

Table 8:4-1: SWAT+ input variables that pesticide partitioning.

| Variable Name | Definition                                                                               | Input File |
| ------------- | ---------------------------------------------------------------------------------------- | ---------- |
| LKPST\_KOC    | $$K_d$$: Pesticide partition coefficient (m$$^3$$/g)                                     | .lwq       |
| LKPST\_REA    | $$k_{p,aq}$$: Rate constant for degradation or removal of pesticide in the water (1/day) | .lwq       |
| LKPST\_VOL    | $$v_v$$: Volatilization mass-transfer coefficient (m/day)                                | .lwq       |
| LKPST\_STL    | $$v_s$$: Pesticide settling velocity (m/day)                                             | .lwq       |
