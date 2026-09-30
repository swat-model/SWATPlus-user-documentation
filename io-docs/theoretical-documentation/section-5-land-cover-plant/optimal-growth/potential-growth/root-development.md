# Root Development

The amount of total plant biomass partitioned to the root system is 30-50% in seedlings and decreases to 5-20% in mature plants (Jones, 1985). SWAT+ varies the fraction of total biomass in roots from 0.40 at emergence to 0.20 at maturity. The daily root biomass fraction is calculated with the equation:

&#x20;         $$fr_{root}=0.40-0.20*fr_{PHU}$$                                                                   5:2.1.21

where $$fr_{root}$$ is the fraction of total biomass partitioned to roots on a given day in the growing season, and $$fr_{PHU}$$ is the fraction of potential heat units accumulated for the plant on a given day in the growing season.

&#x20;       Calculation of root depth varies according to plant type. SWAT+ assumes perennials and trees have roots down to the maximum rooting depth defined for the soil throughout the growing season:

&#x20;            $$z_{root}=z_{root,mx}$$                                                                                         5:2.1.22

where $$z_{root}$$ is the depth of root development in the soil on a given day (mm), and $$z_{root,mx}$$ is the maximum depth for root development in the soil (mm). The simulated root depth for annuals varies linearly from 10.0 mm at the beginning of the growing season to the maximum rooting depth at $$fr_{PHU}$$= 0.40 using the equation:

&#x20;       $$z_{root}=2.5*fr_{PHU}*z_{root,mx}$$   if  $$fr_{PHU}  \le 0.40$$                                 5:2.1.23

&#x20;       $$z_{root}=z_{root,mx}$$                             if $$fr_{PHU} > 0.40$$                                  5:2.1.24

where $$z_{root}$$ is the depth of root development in the soil on a given day (mm), $$fr_{PHU}$$ is the fraction of potential heat units accumulated for the plant on a given day in the growing season, and $$z_{root,mx}$$ is the maximum depth for root development in the soil (mm). The maximum rooting depth is defined by comparing the maximum potential rooting depth for the plant from the plant growth database (RDMX in crop.dat), and the maximum potential rooting depth for the soil from the soil input file (SOL\_ZMX in .sol—if no value is provided for this variable the model will set it to the deepest depth specified for the soil profile). The shallower of these two depths is the value used for $$z_{root,mx}$$.
