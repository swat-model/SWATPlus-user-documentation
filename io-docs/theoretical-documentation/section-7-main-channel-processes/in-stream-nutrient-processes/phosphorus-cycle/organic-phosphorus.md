# Organic Phosphorus

The amount of organic phosphorus in the stream may be increased by the conversion of algal biomass phosphorus to organic phosphorus. Organic phosphorus concentration in the stream may be decreased by the conversion of organic phosphorus to soluble inorganic phosphorus or the settling of organic phosphorus with sediment. The change in organic phosphorus for a given day is:

$$\Delta orgP_{str}=(\alpha_2*\rho_a*algae-\beta_{P,4}*orgP_{str}-\sigma_5*orgP_{str})*TT$$                 7:3.3.1

where $$\Delta orgP_{str}$$ is the change in organic phosphorus concentration (mg P/L), $$\alpha_2$$ is the fraction of algal biomass that is phosphorus (mg P/mg alg biomass), $$\rho_a$$ is the local respiration or death rate of algae (day$$^{-1}$$ or hr$$^{-1}$$), $$algae$$ is the algal biomass concentration at the beginning of the day (mg alg/L), $$\beta_{P,4}$$ is the rate constant for mineralization of organic phosphorus (day$$^{-1}$$ or hr$$^{-1}$$), $$orgP_{str}$$ is the organic phosphorus concentration at the beginning of the day (mg P/L), $$\alpha_5$$ is the rate coefficient for organic phosphorus settling (day$$^{-1}$$ or hr$$^{-1}$$), and $$TT$$ is the flow travel time in the reach segment (day or hr). The fraction of algal biomass that is phosphorus is user-defined. Equation 7:3.1.17 describes the calculation of the local respiration rate of algae. The calculation of travel time is reviewed in Chapter 7:1.

&#x20;    The user defines the local rate constant for mineralization of organic phosphorus at 20$$\degree$$C. The organic phosphorus mineralization rate is adjusted to the local water temperature using the relationship:

&#x20;           $$\beta_{P,4}=\beta_{P,4,20}*1.047^{(T_{water}-20)}$$                                                                   7:3.3.2

where $$\beta_{P,4}$$ is the local rate constant for organic phosphorus mineralization (day$$^{-1}$$ or hr$$^{-1}$$), $$\beta_{P,4,20}$$ is the local rate constant for organic phosphorus mineralization at 20$$\degree$$C (day$$^{-1}$$ or hr$$^{-1}$$), and $$T_{water}$$ is the average water temperature for the day or hour ($$\degree$$C).

&#x20;      The user defines the rate coefficient for organic phosphorus settling at 20$$\degree$$C. The organic phosphorus settling rate is adjusted to the local water temperature using the relationship:

&#x20;                $$\sigma_5=\sigma_{5,20}*1.024^{(T_{water}-20)}$$                                                            7:3.3.3

where $$\sigma_5$$ is the local settling rate for organic phosphorus (day$$^{-1}$$ or hr$$^{-1}$$), $$\sigma_{5,20}$$ is the local settling rate for organic phosphorus at 20$$\degree$$C (day$$^{-1}$$ or hr$$^{-1}$$), and $$T_{water}$$ is the average water temperature for the day or hour ($$\degree$$C).
