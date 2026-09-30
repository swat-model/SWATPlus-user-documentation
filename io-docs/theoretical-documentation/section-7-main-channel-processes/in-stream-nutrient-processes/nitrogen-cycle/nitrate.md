# Nitrate

The amount of nitrate ($$NO_3^-$$) in the stream may be increased by the oxidation of $$NO_2^-$$. The nitrate concentration in the stream may be decreased by the uptake of $$NO_3^-$$ by algae. The change in nitrate for a given day is:

$$\Delta NO3_{str}=(\beta_{N,2}*NO2_{str}-(1-fr_{NH4})*\alpha_1*\mu_a*algae)*TT$$                      7:3.2.10

where $$\Delta NO3_{str}$$ is the change in nitrate concentration (mg N/L), $$\beta_{N,2}$$ is the rate constant for biological oxidation of nitrite to nitrate (day$$^{-1}$$ or hr$$^{-1}$$), $$NO2_{str}$$ is the nitrite concentration at the beginning of the day (mg N/L), $$fr_{NH4}$$ is the fraction of algal nitrogen uptake from ammonium pool, $$\alpha_1$$ is the fraction of algal biomass that is nitrogen (mg N/mg alg biomass), $$\mu _a$$ is the local growth rate of algae (day$$^{-1}$$ or hr$$^{-1}$$), $$algae$$ is the algal biomass concentration at the beginning of the day (mg alg/L), and $$TT$$ is the flow travel time in the reach segment (day or hr). The local rate constant for biological oxidation of nitrite to nitrate is calculated with equation 7:3.2.9 while the fraction of algal nitrogen uptake from ammonium pool is calculated with equation 7:3.2.7. Section 7:3.1.2.1 describes the calculation of the local growth rate of algae. The calculation of travel time is reviewed in Chapter 7:1.

Table 7:3-2: SWAT+ input variables used in in-stream nitrogen calculations.

| Variable Name | Definition                                                                                                                                                 | File Name |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| AI1           | $$\alpha_1$$: Fraction of algal biomass that is nitrogen (mg N/mg alg biomass)                                                                             | .wwq      |
| RHOQ          | $$\rho_{a,20}$$: Local algal respiration rate at 20$$\degree$$C (day$$^{-1}$$)                                                                             | .wwq      |
| BC3           | $$\beta_{N,3,20}$$: Local rate constant for hydrolysis of organic nitrogen to NH$$^+_4$$ at 20$$\degree$$C (day$$^{-1}$$ or hr$$^{-1}$$)                   | .swq      |
| RS4           | $$\sigma_{4,20}$$: Local settling rate for organic nitrogen at 20$$\degree$$C (day$$^{-1}$$)                                                               | .swq      |
| BC1           | $$\beta_{N,1,20}$$: Rate constant for biological oxidation of ammonia nitrogen at 20$$\degree$$C (day$$^{-1}$$)                                            | .swq      |
| RS3           | $$\sigma_{3,20}$$: Benthos (sediment) source rate for ammonium nitrogen at 20$$\degree$$C               (mg N/m$$^2$$-day or              mg N/m$$^2$$-hr) | .swq      |
| P\_N          | $$f_{NH4}$$: Preference factor for ammonia nitrogen                                                                                                        | .wwq      |
| BC2           | $$\beta_{N,2,20}$$: Rate constant for biological oxidation of nitrite to nitrate at 20$$\degree$$C (day$$^{-1}$$ or hr$$^{-1}$$)                           | .swq      |
