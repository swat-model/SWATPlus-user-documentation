# Nitrite

The amount of nitrite ($$NO_2^-$$) in the stream will be increased by the conversion of $$NH_4^+$$ to $$NO_2^-$$ and decreased by the conversion of $$NO_2^-$$ to $$NO_3^-$$. The conversion of $$NO_2^-$$ to $$NO_3^-$$ occurs more rapidly than the conversion of $$NH_4^+$$ to $$NO_2^-$$, so the amount of nitrite present in the stream is usually very small. The change in nitrite for a given day is:

&#x20;          $$\Delta NO2_{str}=(\beta_{N,1}*NH4_{str}-\beta_{N,2}*NO2_{str})*TT$$                                        7:3.2.8

where $$\Delta NO2_{str}$$ is the change in nitrite concentration (mg N/L), $$\beta_{N,1}$$ is the rate constant for biological oxidation of ammonia nitrogen (day$$^{-1}$$ or hr$$^{-1}$$), $$NH4_{str}$$ is the ammonium concentration at the beginning of the day (mg N/L), $$\beta_{N,2}$$ is the rate constant for biological oxidation of nitrite to nitrate (day$$^{-1}$$ or hr$$^{-1}$$), $$NO2_{str}$$ is the nitrite concentration at the beginning of the day (mg N/L), and $$TT$$ is the flow travel time in the reach segment (day or hr). The local rate constant for biological oxidation of ammonia nitrogen is calculated with equation 7:3.2.5. The calculation of travel time is reviewed in Chapter 7:1.

The rate constant for biological oxidation of nitrite to nitrate will vary as a function of in-stream oxygen concentration and temperature. The rate constant is calculated:

&#x20;   $$\beta_{N,2}=\beta_{N,2,20}*(1-exp[-0.6*Ox_{str}])*1.047^{(T_{water}-20)}$$                                  7:3.2.9

where $$\beta_{N,2}$$ is the rate constant for biological oxidation of nitrite to nitrate (day$$^{-1}$$ or hr$$^{-1}$$), $$\beta_{N,2,20}$$  is the rate constant for biological oxidation of nitrite to nitrate at 20$$\degree$$C (day$$^{-1}$$ or hr$$^{-1}$$),$$Ox_{str}$$ is the dissolved oxygen concentration in the stream (mg O$$_2$$/L), and $$T_{water}$$ is the average water temperature for the day or hour ($$\degree$$C). The second term on the right side of equation 7:3.2.9, $$(1-exp[-0.6*Ox_{str}])$$, is a nitrification inhibition correction factor. This factor inhibits nitrification at low dissolved oxygen concentrations.
