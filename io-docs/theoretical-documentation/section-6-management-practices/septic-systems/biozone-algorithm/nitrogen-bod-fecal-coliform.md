# Nitrogen, BOD, Fecal Coliform

Transformation and removal of pollutants in the biozone is directly related with the population of live bacteria biomass and bio-physical processes in the biozone layer. The fate of pollutants including Nitrogen, BOD, and Fecal Coliform is estimated by a first order reaction equation:

&#x20;                           $$C_{k,end}=C_{k,i}*e^{-K_k \Delta t}$$                                                                      (13)

where $$C_{k,end}$$ is concentration of k constituent in the biozone at the end of the day (mg/L), $$C_{k,i}$$ is concentration of $$k$$ constituent in the biozone at the beginning of the day (mg/L), and $$K_k$$ is a first order reaction rate (1/day), which is a function of the total biomass of live bacteria and a reaction rate coefficient.

&#x20;                             $$K_k=[\frac{K_{1,k}*A_d}{\theta_{si}*V_{bz}}](Bio)$$                                                                       (14)

where $$K_{1,k}$$ is the reaction rate calibration parameter for each constituent $$k$$ (m$$^3$$/kg) and $$V_{bz}$$ is the volume of the biozone (m$$^3$$). The various constituents included are meant for the primary reactions/processes that occur in the biozone layer such as nitrification, denitrification, BOD decay, and fecal coliform decay.

![](<../../../../.gitbook/assets/new2 (1).jpg>)

In Equation (14), the reaction rate is normalized with respect to the volume of bacterial biomass (pore volume,$$\theta_{si} V_{bz}$$) in the biozone layer as in the case of mortality and respiration equations. This normalization is done to avoid scaling issues in applying the algorithm to watershed scale simulations with parameters calibrated to small scale results (lab column tests).
