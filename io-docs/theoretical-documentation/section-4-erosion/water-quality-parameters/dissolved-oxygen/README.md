# Dissolved Oxygen

Rainfall is assumed to be saturated with oxygen. To determine the dissolved oxygen concentration of surface runoff, the oxygen uptake by the oxygen demanding substance in runoff is subtracted from the saturation oxygen concentration.

&#x20;          $$Ox_{surf}=Ox_{sat}-\kappa_1*cbod_{surq}*\frac{t_{ov}}{24}$$                                             4:5.3.1

where $$Ox_{surf}$$ is the dissolved oxygen concentration in surface runoff (mg $$O_2$$/L), $$Ox_{sat}$$ is the saturation oxygen concentration (mg $$O_2$$/L), $$\kappa_1$$ is the CBOD deoxygenation rate (day$$^{-1}$$), $$cbod_{surq}$$ is the CBOD concentration in surface runoff (mg CBOD/L), and $$t_{ov}$$ is the time of concentration for overland flow (hr). For loadings from HRUs, SWAT+ assumes $$\kappa_1$$ = 1.047 day$$^{-1}$$.  &#x20;
