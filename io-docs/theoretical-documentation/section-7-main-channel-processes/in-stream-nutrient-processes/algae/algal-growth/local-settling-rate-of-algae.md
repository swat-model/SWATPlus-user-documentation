# Local Settling Rate of Algae

The local settling rate of algae represents the net removal of algae due to settling. The user defines the local settling rate of algae at 20$$\degree$$C. The settling rate is adjusted to the local water temperature using the relationship:

&#x20;         $$\sigma_1=\sigma_{1,20}*1.024^{(T_{water}-20)}$$                                                                               7:3.1.18

where $$\sigma_1$$ is the local settling rate of algae (m/day or m/hr), $$\sigma_{1,20}$$ is the local algal settling rate at 20$$\degree$$C (m/day or m/hr), and $$T_{water}$$ is the average water temperature for the day or hour ($$\degree$$C).

Table 7:3-1: SWAT+ input variables used in algae calculations.

| Variable Name | Definition                                                                                                 | File Name |
| ------------- | ---------------------------------------------------------------------------------------------------------- | --------- |
| AI0           | $$\alpha_0$$: Ratio of chlorophyll _a_ to algal biomass ($$\mu g$$ chla/mg alg)                            | .wwq      |
| IGROPT        | Algal specific growth rate option                                                                          | .wwq      |
| MUMAX         | $$\mu_{max}$$: Maximum specific algal growth rate (day$$^{-1}$$)                                           | .wwq      |
| K\_L          | $$K_L$$: Half-saturation coefficient for light (MJ/m$$^2$$-hr)                                             | .wwq      |
| TFACT         | $$fr_{phosyn}$$: Fraction of solar radiation that is photosynthetically active                             | .wwq      |
| LAMBDA0       | $$k_{l,0}$$: Non-algal portion of the light extinction coefficient (m$$^{-1}$$)                            | .wwq      |
| LAMBDA1       | $$k_{l,1}$$: Linear algal self shading coefficient            (m$$^{-1}$$ ($$\mu g$$-chla/L)$$^{-1}$$)     | .wwq      |
| LAMBDA2       | $$k_{l,2}$$: Nonlinear algal self shading coefficient            (m$$^{-1}$$($$\mu g$$-chla/L)$$^{-2/3}$$) | .wwq      |
| K\_N          | $$K_N$$: Michaelis-Menton half-saturation constant for nitrogen (mg N/L)                                   | .wwq      |
| K\_P          | $$K_P$$ : Michaelis-Menton half-saturation constant for phosphorus (mg P/L)                                | .wwq      |
| RHOQ          | $$\rho_{a,20}$$ : Local algal respiration rate at 20$$\degree$$C (day$$^{-1}$$)                            | .wwq      |
| RS1           | $$\sigma_{1,20}$$: Local algal settling rate at 20$$\degree$$C (m/day)                                     | .swq      |
