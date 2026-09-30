# Ammonium

The amount of ammonium (NH$$^+_4$$) in the stream may be increased by the mineralization of organic nitrogen and diffusion of ammonium from the streambed sediments. The ammonium concentration in the stream may be decreased by the conversion of NH$$^+_4$$ to NO$$^-_2$$ or the uptake of NH$$^+_4$$ by algae. The change in ammonium for a given day is:

$$\Delta NH4_{str}=(\beta_{N,3}*orgN_{str}-\beta_{N,1}*NH4_{str}+\frac{\sigma_3}{(1000*depth)}-fr_{NH4}*\alpha_1*\mu_a*algae)*TT$$&#x20;

&#x20;                                                                                                                                            7:3.2.4

where $$\Delta NH4_{str}$$ is the change in ammonium concentration (mg N/L), $$\beta_{N,3}$$ is the rate constant for hydrolysis of organic nitrogen to ammonia nitrogen (day$$^{-1}$$ or hr$$^{-1}$$), $$orgN_{str}$$ is the organic nitrogen concentration at the beginning of the day (mg N/L), $$\beta_{N,1}$$ is the rate constant for biological oxidation of ammonia nitrogen (day$$^{-1}$$ or hr$$^{-1}$$), $$NH4_{str}$$ is the ammonium concentration at the beginning of the day (mg N/L), $$\sigma_3$$ is the benthos (sediment) source rate for ammonium (mg N/m$$^2$$-day or mg N/m$$^2$$-hr), $$depth$$ is the depth of water in the channel (m), $$fr_{NH4}$$ is the fraction of algal nitrogen uptake from ammonium pool, $$\alpha_1$$ is the fraction of algal biomass that is nitrogen (mg N/mg alg biomass), $$\mu _a$$ is the local growth rate of algae (day$$^{-1}$$ or    hr$$^{-1}$$), $$algae$$ is the algal biomass concentration at the beginning of the day (mg alg/L), and $$TT$$ is the flow travel time in the reach segment (day or hr). The local rate constant for hydrolysis of organic nitrogen to NH$$^+_4$$ is calculated with equation 7:3.2.2. Section 7:3.1.2.1 describes the calculation of the local growth rate of algae. The calculation of depth and travel time is reviewed in Chapter 7:1.

&#x20;      The rate constant for biological oxidation of ammonia nitrogen will vary as a function of in-stream oxygen concentration and temperature. The rate constant is calculated:

&#x20;            $$\beta_{N,1}=\beta_{N,1,20}*(1-exp[-0.6*Ox_{str}])*1.083^{(T_{water}-20)}$$                         7:3.2.5

where $$\beta_{N,1}$$ is the rate constant for biological oxidation of ammonia nitrogen (day$$^{-1}$$ or hr$$^{-1}$$), $$\beta_{N,1,20}$$ is the rate constant for biological oxidation of ammonia nitrogen at 20$$\degree$$C (day$$^{-1}$$ or hr$$^{-1}$$), $$Ox_{str}$$ is the dissolved oxygen concentration in the stream (mg O$$_2$$/L), and $$T_{water}$$ is the average water temperature for the day or hour ($$\degree$$C). The second term on the right side of equation 7:3.2.5,$$(1-exp[-0.6*Ox_{str}])$$, is a nitrification inhibition correction factor. This factor inhibits nitrification at low dissolved oxygen concentrations.

&#x20;         The user defines the benthos source rate for ammonium at 20$$\degree$$C. The benthos source rate for ammonium nitrogen is adjusted to the local water temperature using the relationship:

&#x20;             $$\sigma_3=\sigma_{3,20}*1.074^{(T_{water}-20)}$$                                                                      7:3.2.6

where $$\sigma_3$$ is the benthos (sediment) source rate for ammonium (mg N/m$$^2$$-day or mg N/m$$^2$$2-hr), $$\sigma_{3,20}$$ is the benthos (sediment) source rate for ammonium nitrogen at 20$$\degree$$C (mg N/m$$^2$$-day or mg N/m$$^2$$-hr), and $$T_{water}$$ is the average water temperature for the day or hour ($$\degree$$C).

&#x20;          The fraction of algal nitrogen uptake from ammonium pool is calculated:

&#x20;                  $$fr_{NH4}=\frac{f_{NH4}*NH4_{str}}{(f_{NH4}*NH4_{str}+(1-f_{NH4})*NO3_{str})}$$                                              7:3.2.7

where $$fr_{NH4}$$ is the fraction of algal nitrogen uptake from ammonium pool, $$f_{NH4}$$ is the preference factor for ammonia nitrogen, $$NH4_{str}$$ is the ammonium concentration in the stream (mg N/L), and $$NO3_{str}$$ is the nitrate concentration in the stream (mg N/L).
