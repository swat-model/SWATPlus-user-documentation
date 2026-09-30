# Surface Area

The surface area of the pond or wetland is needed to calculate the amount of precipitation falling on the water body as well as the amount of evaporation and seepage. Surface area varies with change in the volume of water stored in the impoundment. The surface area is updated daily using the equation:

&#x20;          $$SA=\beta_{sa}*V^{expsa}$$                                                                             8:1.2.2

where $$SA$$ is the surface area of the water body (ha), $$\beta_{sa}$$ is a coefficient, $$V$$ is the volume of water in the impoundment (m$$^3$$ H$$_2$$O), and $$expsa$$ is an exponent.

&#x20;           The coefficient, $$\beta_{sa}$$, and exponent, $$expsa$$, are calculated by solving equation 8:1.1.2 using two known points. For ponds, the two known points are surface area and volume information provided for the principal and emergency spillways.

&#x20;            $$expsa=\frac{log_{10}(SA_{em})-log_{10}(SA_{pr})}{log_{10}(V_{em})-log_{10}(V_{pr})}$$                                                       8:1.2.3

&#x20;             $$\beta_{sa}=(\frac{SA_{em}}{V_{em}})^{expsa}$$                                                                          8:1.2.4

where $$SA_{em}$$ is the surface area of the pond when filled to the emergency spillway (ha), $$SA_{pr}$$ is the surface area of the pond when filled to the principal spillway (ha), $$V_{em}$$ is the volume of water held in the pond when filled to the emergency spillway (m$$^3$$ H$$_2$$O), and $$V_{pr}$$ is the volume of water held in the pond when filled to the principal spillway(m$$^3$$ H$$_2$$O). For wetlands, the two known points are surface area and volume information provided for the maximum and normal water levels.

&#x20;                $$expsa=\frac{log_{10}(SA_{mx})-log_{10}(SA_{nor})}{log_{10}(V_{mx})-log_{10}(V_{nor})}$$                                              8:1.2.5

&#x20;               $$\beta_{sa}=(\frac{SA_{mx}}{V_{mx}})^{expsa}$$                                                                     8:1.2.6

where $$SA_{mx}$$ is the surface area of the wetland when filled to the maximum water level (ha), $$SA_{nor}$$ is the surface area of the wetland when filled to the normal water level (ha), $$V_{mx}$$ is the volume of water held in the wetland when filled to the maximum water level  (m$$^3$$ H$$_2$$O), and $$V_{nor}$$ is the volume of water held in the wetland when filled to the normal water level (m$$^3$$ H$$_2$$O).​
