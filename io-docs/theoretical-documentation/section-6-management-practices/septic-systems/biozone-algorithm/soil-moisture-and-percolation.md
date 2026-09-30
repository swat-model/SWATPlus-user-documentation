# Soil Moisture and Percolation

Soil porosity (or saturated moisture content) is generally constant in natural soil; however, the porosity of biozone changes with time. The actual porosity of biozone decreases as the suspended solids from STE accumulate in the pore space and the mineralized biomass (dead body) increases in the biozone.

&#x20;                                                   $$\theta_s=\theta_{si}-\frac{plaque}{\rho_{bm}}$$                                                                   (8)

where $$\theta_{si}$$ is initial soil porosity with zero plaque (mm). The moisture content at each time step is estimated using the mass balance of water within the biozone.

&#x20;                                                $$\theta^t=\theta^{t-1}+\frac{Q_{STE}}{10*A_d}-I_p-ET-Q_{lat}$$                                    (9)

where $$ET$$ is evaportranspiration from biozone (mm/day) and $$Q_{lat}$$ is lateral flow (mm/day). Percolation to a subsoil layer is triggered if moisture content exceeds the field capacity in the biozone layer. Potential percolation is the maximum amount of water that can percolate during the time interval.   &#x20;

&#x20;                                                 $$I_{p,pot}=K_{bz}*\Delta t$$                                                                   (10)

where $$I_{p,pot}$$ is the potential amount of percolation (mm/day). The amount of water percolating to the sub-soil layer is calculated using storage routing methodology (Neitsch et al., 2005).

&#x20;          $$I_{p,excess}=(\theta -\theta_f)(1-exp[\frac{-\Delta t}{TT_{perc}}])$$         if      $$\theta > \theta_f$$

&#x20;           $$I_{p,excess}=0$$                                                  if      $$\theta \le \theta_f$$                                            (11)

where  $$I_{p,excess}$$ is the minimum amount of percolation (mm/day) and $$TT_{perc}$$ is travel time for percolation $$(TT_{perc}=(\theta_s-\theta_f)/K_{bz})$$ in hour. The actual percolation is the smaller of the potential and minimum percolation.

&#x20;                                                   $$I_p=min(I_{p,pot},I_{p,excess})$$                                                    (12)
