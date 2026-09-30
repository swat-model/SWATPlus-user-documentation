# Volatilization

Pesticide in the dissolved phase is available for volatilization. The amount of pesticide removed from the water via volatilization is:

&#x20;        $$pst_{vol,wtr}=v_v*SA*\frac{F_d*pst_{lkwtr}}{V}$$                                                     8:4.1.8

&#x20;    where $$pst_{vol,wtr}$$ is the amount of pesticide removed via volatilization (mg pst), $$v_v$$ is the volatilization mass-transfer coefficient (m/day), $$SA$$ is the surface area of the water body (m$$^2$$), $$F_d$$ is the fraction of total pesticide in the dissolved phase, $$pst_{lkwtr}$$ is the amount of pesticide in the water (mg pst), and _V_ is the volume of water in the water body(m$$^3$$ H$$_2$$O).

&#x20;           The volatilization mass-transfer coefficient can be calculated based on Whitman’s two-film or two-resistance theory (Whitman, 1923; Lewis and Whitman, 1924 as described in Chapra, 1997). While the main body of the gas and liquid phases are assumed to be well-mixed and homogenous, the two-film theory assumes that a substance moving between the two phases encounters maximum resistance in two laminar boundary layers where transfer is a function of molecular diffusion. In this type of system the transfer coefficient or velocity is:

&#x20;           $$v_v=K_l*\frac{H_e}{H_e+R*T_K*(K_l/K_g)}$$                                                         8:4.1.9

where $$v_v$$ is the volatilization mass-transfer coefficient (m/day), $$K_l$$ is the mass-transfer velocity in the liquid laminar layer (m/day), $$K_g$$ is the mass-transfer velocity in the gaseous laminar layer (m/day), $$H_{e}$$ is Henry’s constant (atm m$$^3$$ mole$$^{-1}$$), $$R$$ is the universal gas constant (8.206 $$*$$ 10$$^{-5}$$ atm m$$^3$$ (K mole)$$^{-1}$$), and $$T_K$$ is the temperature     ($$K$$).

For lakes, the transfer coefficients are estimated using a stagnant film approach:

&#x20;           $$K_l=\frac{D_l}{z_l}$$                                      $$K_g=\frac{D_g}{z_g}$$                              8:4.1.10

where $$K_l$$ is the mass-transfer velocity in the liquid laminar layer (m/day), $$K_g$$ is the mass-transfer velocity in the gaseous laminar layer (m/day), $$D_l$$ is the liquid molecular diffusion coefficient (m$$^2$$/day), $$D_g$$ is the gas molecular diffusion coefficient (m$$^2$$/day), $$z_l$$ is the thickness of the liquid film (m), and $$z_g$$ is the thickness of the gas film (m).

&#x20;           Alternatively, the transfer coefficients can be estimated with the equations:

&#x20;            $$K_l=K_{l,O_2}*(\frac{32}{MW})^{0.25}$$                                                        8:4.1.11

&#x20;            $$K_g =168*\mu_w*(\frac{18}{MW})^{0.25}$$                                                 8:4.1.12

where $$K_l$$ is the mass-transfer velocity in the liquid laminar layer (m/day), $$K_g$$ is the mass-transfer velocity in the gaseous laminar layer (m/day), $$K_{l,O_2}$$ is the oxygen transfer coefficient (m/day), $$MW$$ is the molecular weight of the compound, and $$\mu_w$$ is the wind speed (m/s). Chapra (1997) lists several different equations that can be used to calculate $$K_{l,O_2}$$.       &#x20;
