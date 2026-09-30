# 2:2.2.1 Penman-Monteith Method

The Penman-Monteith equation combines components that account for energy needed to sustain evaporation, the strength of the mechanism required to remove the water vapor and aerodynamic and surface resistance terms. The Penman-Monteith equation is:

$$\lambda E=\frac{\Delta*(H_{net}-G)+\rho_{air}*c_p*[e^o_z-e_z]/r_a}{\Delta+\gamma*(1+r_c/r_a)}$$                                                                                                                     2:2.2.1

where $$\lambda E$$ is the latent heat flux density (MJ m$$^{-2}$$ d$$^{-1}$$), $$E$$ is the depth rate evaporation (mm d$$^{-1}$$), $$\Delta$$ is the slope of the saturation vapor pressure-temperature curve, $$de/dT$$ (kPa ˚C$$^{-1}$$), $$H_{net}$$ is the net radiation (MJ m$$^{-2}$$ d$$^{-1}$$), $$G$$ is the heat flux density to the ground (MJ m$$^{-2}$$ d$$^{-1}$$), $$\rho_{air}$$ is the air density (kg m$$^{-3}$$), $$c_p$$ is the specific heat at constant pressure (MJ kg$$^{-1}$$ ˚C$$^{-1}$$), is the saturation vapor pressure of air at height $$z$$ (kPa), $$e_z$$ is the water vapor pressure of air at height $$z$$ (kPa), $$\gamma$$ is the psychrometric constant (kPa ˚C$$^{-1}$$), $$r_c$$ is the plant canopy resistance (s m$$^{-1}$$), and $$r_a$$ is the diffusion resistance of the air layer (aerodynamic resistance) (s m$$^{-1}$$).

For well-watered plants under neutral atmospheric stability and assuming logarithmic wind profiles, the Penman-Monteith equation may be written (Jensen et al., 1990):

$$\lambda E_t=\frac{\Delta*(H_{net}-G)+\gamma*K_1*(0.622*\gamma*\rho_{air}/P)*(e^o_z-e_z)/r_a}{\Delta+\gamma*(1+r_c/r_a)}$$                                                                                         2:2.2.2

where $$\lambda$$ is the latent heat of vaporization (MJ kg$$^{-1}$$), $$E_t$$ is the maximum transpiration rate (mm d$$^{-1}$$), $$K_1$$ is a dimension coefficient needed to ensure the two terms in the numerator have the same units (for $$u_z$$ in m s$$^{-1}$$,  $$K_1$$ = 8.64 x 104), and $$P$$ is the atmospheric pressure (kPa).

The calculation of net radiation, $$H_{net}$$, is reviewed in Chapter 1:1. The calculations for the latent heat of vaporization, $$\lambda$$, the slope of the saturation vapor pressure-temperature curve, $$\Delta$$, the psychrometric constant, $$\gamma$$, and the saturation and actual vapor pressure, $$e^o_z$$and $$e_z$$, are reviewed in Chapter 1:2. The remaining undefined terms are the soil heat flux, $$G$$, the combined term $$K_1  0.622 \lambda\rho/P$$, the aerodynamic resistance, $$r_a$$, and the canopy resistance, $$r_c$$.
