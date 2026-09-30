# Volatilization

Pesticide in the dissolved phase is available for volatilization. The amount of pesticide removed from the water via volatilization is:

&#x20;           $$pst_{vol,wtr}=\frac{v_v}{depth}*F_d*pst_{rchwtr}*TT$$                                                  7:4.1.8

where $$pst_{vol,wtr}$$ is the amount of pesticide removed via volatilization (mg pst), $$v_v$$ is the volatilization mass-transfer coefficient (m/day), $$depth$$ is the flow depth (m), $$F_d$$ is the fraction of total pesticide in the dissolved phase, $$pst_{rchwtr}$$ is the amount of pesticide in the water (mg pst), and $$TT$$ is the flow travel time (days).

&#x20;           The volatilization mass-transfer coefficient can be calculated based on Whitman’s two-film or two-resistance theory (Whitman, 1923; Lewis and Whitman, 1924 as described in Chapra, 1997). While the main body of the gas and liquid phases are assumed to be well-mixed and homogenous, the two-film theory assumes that a substance moving between the two phases encounters maximum resistance in two laminar boundary layers where transfer is a function of molecular diffusion. In this type of system the transfer coefficient or velocity is:

&#x20;               $$v_v=K_l*\frac{H_e}{H_e+R*T_K*(K_l/K_g)}$$                                                              7:4.1.9

where $$v_v$$ is the volatilization mass-transfer coefficient (m/day), $$K_l$$ is the mass-transfer velocity in the liquid laminar layer (m/day), $$K_g$$ is the mass-transfer velocity in the gaseous laminar layer (m/day), $$H_e$$ is Henry’s constant (atm m$$^3$$ mole$$^{-1}$$), $$R$$ is the universal gas constant ($$8.206*10^{-5}$$  atm m$$^3$$ (K mole)$$^{-1}$$), and $$T_K$$ is the temperature (K).

&#x20;             For rivers where liquid flow is turbulent, the transfer coefficients are estimated using the surface renewal theory (Higbie, 1935; Danckwerts, 1951; as described by Chapra, 1997). The surface renewal model visualizes the system as consisting of parcels of water that are brought to the surface for a period of time. The fluid elements are assumed to reach and leave the air/water interface randomly, i.e. the exposure of the fluid elements to air is described by a statistical distribution. The transfer velocities for the liquid and gaseous phases are calculated:

&#x20;             $$K_l=\sqrt{r_l*D_l}$$                            $$K_g=\sqrt{r_g*D_g}$$                                          7:4.1.10

where $$K_l$$ is the mass-transfer velocity in the liquid laminar layer (m/day), $$K_g$$ is the mass-transfer velocity in the gaseous laminar layer (m/day), $$D_l$$ is the liquid molecular diffusion coefficient (m$$^2$$/day), $$D_g$$ is the gas molecular diffusion coefficient (m$$^2$$/day), $$r_l$$ is the liquid surface renewal rate (1/day), and $$r_g$$ is the gaseous surface renewal rate (1/day).

&#x20;           O’Connor and Dobbins (1958) defined the surface renewal rate as the ratio of the average stream velocity to depth.

&#x20;                $$r_l=\frac{86400*v_c}{depth}$$                                                                                                  7:4.1.11

where $$r_l$$ is the liquid surface renewal rate (1/day), $$v_c$$ is the average stream velocity (m/s) and $$depth$$ is the depth of flow (m).
