# Inorganic/Soluble Phosphorus

The amount of soluble, inorganic phosphorus in the stream may be increased by the mineralization of organic phosphorus and diffusion of inorganic phosphorus from the streambed sediments. The soluble phosphorus concentration in the stream may be decreased by the uptake of inorganic P by algae. The change in soluble phosphorus for a given day is:

&#x20;             $$\Delta solP_{str}=(\beta_{P,4}*orgP_{str}+\frac{\sigma_2}{(1000*depth)}-\alpha_2*\mu _a*algae)*TT$$          7:3.3.4

where $$\Delta solP_{str}$$ is the change in solution phosphorus concentration (mg P/L), $$\beta_{P,4}$$ is the rate constant for mineralization of organic phosphorus (day$$^{-1}$$ or hr$$^{-1}$$), $$orgP_{str}$$ is the organic phosphorus concentration at the beginning of the day (mg P/L), $$\sigma_2$$ is the benthos (sediment) source rate for soluble P (mg P/m$$^2$$-day or mg P/m$$^2$$-hr), $$depth$$ is the depth of water in the channel (m), $$\alpha_2$$ is the fraction of algal biomass that is phosphorus (mg P/mg alg biomass), $$\mu_a$$ is the local growth rate of algae (day$$^{-1}$$ or hr$$^{-1}$$), $$algae$$ is the algal biomass concentration at the beginning of the day (mg alg/L), and $$TT$$ is the flow travel time in the reach segment (day or hr). The local rate constant for mineralization of organic phosphorus is calculated with equation 7:3.3.2. Section 7:3.1.2.1 describes the calculation of the local growth rate of algae. The calculation of depth and travel time is reviewed in Chapter 7:1.

&#x20;     The user defines the benthos source rate for soluble P at 20$$\degree$$C. The benthos source rate for soluble phosphorus is adjusted to the local water temperature using the relationship:

&#x20;           $$\sigma _2 =\sigma_{2,20} *1.074^{(T_{water}-20)}$$                                                                     7:3.3.5

where $$\sigma_2$$ is the benthos (sediment) source rate for soluble P (mg P/m$$^2$$-day or mg P/m$$^2$$-hr),$$\sigma_{2,20}$$ is the benthos (sediment) source rate for soluble phosphorus at 20$$\degree$$C (mg P/m$$^2$$-day or mg P/m$$^2$$-hr), and $$T_{water}$$ is the average water temperature for the day or hour ($$\degree$$C).

Table 7:3-3: SWAT+ input variables used in in-stream phosphorus calculations.

| Variable Name | Definition                                                                                                     | File Name |
| ------------- | -------------------------------------------------------------------------------------------------------------- | --------- |
| AI2           | $$\alpha_2$$: Fraction of algal biomass that is phosphorus (mg P/mg alg biomass)                               | .wwq      |
| RHOQ          | $$\rho_{a,20}$$: Local algal respiration rate at 20$$\degree$$C (day$$^{-1}$$)                                 | .wwq      |
| BC4           | $$\beta_{P,4,20}$$: Local rate constant for organic phosphorus mineralization at 20$$\degree$$C (day$$^{-1}$$) | .swq      |
| RS5           | $$\sigma_{5,20}$$: Local settling rate for organic phosphorus at 20$$\degree$$C (day$$^{-1}$$)                 | .swq      |
| RS2           | $$\sigma_{2,20}$$ : Benthos (sediment) source rate for soluble phosphorus at 20$$\degree$$C (mg P/m$$^2$$-day) | .swq      |
