# Fate and Transport of Bacterial Biomass

Fate and transport of biomass, including respiration, mortality, and slough-off, are estimated based on empirical relationships. Respiration and mortality rates are functions of the amount of the biomass. These values are normalized by the unit area (1/ha) so that these equations are applicable in different scales of simulations without unintended amplification due to a higher mass of biomass. For each time step, a portion of live biomass is removed during respiration and death. The reaction for bacterial respiration is calculated as follows.

&#x20;                                            $$R_{resp}=\gamma *Bio$$                                                                         (2)

where $$\gamma$$ is a respiration rate coefficient (unitless). The reaction for bacterial mortality is calculated by

&#x20;                                              $$R_{mort}=\phi*Bio$$                                                                      (3)

where $$\phi$$ is mortality rate coefficient (unitless). Bacterial biomass can be washed off to the subsoil layer by a high velocity of infiltrating water.

&#x20;                                                 $$R_{slough}=\eta*v_p^\delta$$                                                                     (4)

where $$v_p$$ is the pore velocity in the biozone layer (mm/day), $$\eta$$ is a linear coefficient (kg/ha), and $$\delta$$ is an exponential coefficient (unitless). Equations (2) to (4) are highly dependent on empirical calibration coefficients and the nature of these processes makes it difficult to validate the model equations.&#x20;

&#x20;             A portion of dead body of biomass becomes plaque. Total solids in the STE may contribute to increasing plaque accumulation in the pore space. Plaque can be sloughed off from biozone by high pore velocity of infiltrating water. As the amount of live biomass increases in the biozone, plaque also increases. The rate of change in plaque is computed by a mass balance equation.

&#x20;                                          $$\frac{d(plaque)}{dt}=R_{mort}+\frac{\sigma *\sum Q_{STE}*TS}{1000*A_d}-R_{slough}$$                                   (5)

where $$plaque$$ is the amount of dead bacteria biomass and residue (kg/ha), $$\sigma$$ is a calibration parameter to convert total solids in $$STE$$ to $$plaque$$ (unitless), $$TS$$ is the total solids contained in STE (mg/l), and $$A_d$$ is the area of drain field (ha).              &#x20;
