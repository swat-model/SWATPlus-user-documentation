# Algal Growth

Growth and decay of algae/chlorophyll $$a$$ is calculated as a function of the growth rate, the respiration rate, the settling rate and the amount of algae present in the stream. The change in algal biomass for a given day is:

$$\Delta algae=((\mu _a*algae)-(\rho_a*algae)-(\frac{\sigma_1}{depth}*algae))*TT$$                             7:3.1.2

where $$\Delta algae$$ is the change in algal biomass concentration (mg alg/L), $$\mu_a$$ is the local specific growth rate of algae (day$$^{-1}$$ or hr$$^{-1}$$), $$\rho_a$$ is the local respiration or death rate of algae (day$$^{-1}$$ or hr$$^{-1}$$), $$\sigma_1$$ is the local settling rate for algae (m/day or m/hr), $$depth$$ is the depth of water in the channel (m), $$algae$$ is the algal biomass concentration at the beginning of the day (mg alg/L), and $$TT$$ is the flow travel time in the reach segment (day or hr). The calculation of depth and travel time are reviewed in Chapter 7:1.
