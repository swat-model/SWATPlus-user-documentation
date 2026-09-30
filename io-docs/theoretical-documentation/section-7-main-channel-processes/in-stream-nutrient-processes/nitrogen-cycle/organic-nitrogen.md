# Organic Nitrogen

The amount of organic nitrogen in the stream may be increased by the conversion of algal biomass nitrogen to organic nitrogen. Organic nitrogen concentration in the stream may be decreased by the conversion of organic nitrogen to NH$$^+_4$$ or the settling of organic nitrogen with sediment. The change in organic nitrogen for a given day is:

&#x20;      $$\Delta orgN_{str}=(\alpha_1 * \rho_a*algae-\beta_{N,3}*orgN_{str}-\sigma_4*orgN_{str})*TT$$            7:3.2.1

where $$\Delta_{orgN_{str}}$$ is the change in organic nitrogen concentration (mg N/L), $$\alpha_1$$ is the fraction of algal biomass that is nitrogen (mg N/mg alg biomass), $$\rho_a$$ is the local respiration or death rate of algae (day$$^{-1}$$ or hr$$^{-1}$$), $$algae$$ is the algal biomass concentration at the beginning of the day (mg alg/L), $$\beta_{N,3}$$ is the rate constant for hydrolysis of organic nitrogen to ammonia nitrogen (day$$^{-1}$$ or hr$$^{-1}$$), $$orgN_{str}$$ is the organic nitrogen concentration at the beginning of the day (mg N/L), $$\sigma_4$$ is the rate coefficient for organic nitrogen settling (day$$^{-1}$$ or hr$$^{-1}$$), and $$TT$$ is the flow travel time in the reach segment (day or hr). The fraction of algal biomass that is nitrogen is user-defined. Equation 7:3.1.17 describes the calculation of the local respiration rate of algae. The calculation of travel time is reviewed in Chapter 7:1.

&#x20;       The user defines the local rate constant for hydrolysis of organic nitrogen to NH$$^+_4$$ at 20$$\degree$$C. The organic nitrogen hydrolysis rate is adjusted to the local water temperature using the relationship:

&#x20;                  $$\beta_{N,3}=\beta_{N,3,20}*1.047^{(T_{water}-20)}$$                                                                  7:3.2.2

where $$\beta_{N,3}$$ is the local rate constant for hydrolysis of organic nitrogen to NH$$^+_4$$ (day$$^{-1}$$ or hr$$^{-1}$$), $$\beta_{N,3,20}$$ is the local rate constant for hydrolysis of organic nitrogen to NH$$^+_4$$ at 20$$\degree$$C                   (day$$^{-1}$$ or hr$$^{-1}$$), and $$T_{water}$$ is the average water temperature for the day or hour ($$\degree$$C).

&#x20;        The user defines the rate coefficient for organic nitrogen settling at 20$$\degree$$C. The organic nitrogen settling rate is adjusted to the local water temperature using the relationship:

&#x20;                $$\sigma_4=\sigma_{4,20}*1.024^{(T_{water}-20)}$$                                                                        7:3.2.3

where $$\sigma_4$$ is the local settling rate for organic nitrogen (day$$^{-1}$$ or hr$$^{-1}$$), $$\sigma_{4,20}$$ is the local settling rate for organic nitrogen at 20$$\degree$$C (day$$^{-1}$$ or hr$$^{-1}$$), and $$T_{water}$$ is the average water temperature for the day or hour ($$\degree$$C).
