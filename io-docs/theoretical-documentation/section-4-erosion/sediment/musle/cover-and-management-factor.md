# Cover and Management Factor

The USLE cover and management factor, CUSLE, is defined as the ratio of soil loss from land cropped under specified conditions to the corresponding loss from clean-tilled, continuous fallow (Wischmeier and Smith, 1978). The plant canopy affects erosion by reducing the effective rainfall energy of intercepted raindrops. Water drops falling from the canopy may regain appreciable velocity but it will be less than the terminal velocity of free-falling raindrops. The average fall height of drops from the canopy and the density of the canopy will determine the reduction in rainfall energy expended at the soil surface. A given percentage of residue on the soil surface is more effective that the same percentage of canopy cover. Residue intercepts falling raindrops so near the surface that drops regain no fall velocity. Residue also obstructs runoff flow, reducing its velocity and transport capacity.

&#x20;        Because plant cover varies during the growth cycle of the plant, SWAT+ updates $$C_{USLE}$$ daily using the equation:

$$C_{USLE}=exp([ln(0.8)-ln(C_{USLE,mn})]*exp\lfloor-0.00115*rsd_{surf}\rfloor+ln[C_{USLE,mn}])$$                                                       &#x20;

&#x20;                                                                                                                         4:1.1.10

&#x20;         where $$C_{USLE,mn}$$ is the minimum value for the cover and management factor for the land cover, and $$rsd_{surf}$$ is the amount of residue on the soil surface (kg/ha).

&#x20;     The minimum $$C$$ factor can be estimated from a known average annual $$C$$ factor using the following equation (Arnold and Williams, 1995):

&#x20;       $$C_{USLE,mn}=1.463ln[C_{USLE,aa}]+0.1034$$                                      4:1.1.11

where $$C_{USLE,mn}$$ is the minimum $$C$$ factor for the land cover and $$C_{USLE,aa}$$ is the average annual $$C$$ factor for the land cover.
