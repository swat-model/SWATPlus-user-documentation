# Mineralization & Decomposition  / Immobilization

Decomposition is the breakdown of fresh organic residue into simpler organic components. Mineralization is the microbial conversion of organic, plant-unavailable phosphorus to inorganic, plant-available phosphorus. Immobilization is the microbial conversion of plant-available inorganic soil phosphorus to plant-unavailable organic phosphorus.

&#x20;          The phosphorus mineralization algorithms in SWAT+ are net mineralization algorithms which incorporate immobilization into the equations. The phosphorus mineralization algorithms developed by Jones et al. (1984) are similar in structure to the nitrogen mineralization algorithms. Two sources are considered for mineralization: the fresh organic P pool associated with crop residue and microbial biomass and the active organic P pool associated with soil humus. Mineralization and decomposition are allowed to occur only if the temperature of the soil layer is above 0°C.

&#x20;               Mineralization and decomposition are dependent on water availability and temperature. Two factors are used in the mineralization and decomposition equations to account for the impact of temperature and water on these processes.

The nutrient cycling temperature factor is calculated:

$$\gamma_{tmp,ly}=0.9*\frac{T_{soil,ly}}{T_{soil,ly}+exp[9.93-0.312*T_{soil,ly}]}+0.1$$                       3:2.2.1

where $$\gamma_{tmp,ly}$$ is the nutrient cycling temperature factor for layer $$ly$$, and $$T_{soil,ly}$$ is the temperature of layer $$ly$$ (°C). The nutrient cycling temperature factor is never allowed to fall below 0.1.&#x20;

The nutrient cycling water factor is calculated:

$$\gamma_{sw,ly}=\frac{SW_{ly}}{FC_{ly}}$$                                                                               3:2.2.2

where $$\gamma_{sw,ly}$$ is the nutrient cycling water factor for layer $$ly$$, $$SW_{ly}$$ is the water content of layer $$ly$$ on a given day (mm H$$_2$$O), and $$FC_{ly}$$ is the water content of layer $$ly$$ at field capacity (mm H$$_2$$O). ). The nutrient cycling water factor is never allowed to fall below 0.05.

&#x20;             &#x20;
