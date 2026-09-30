# Carbonaceous  Biological Oxygen Demand

Carbonaceous biological oxygen demand (CBOD) defines the amount of oxygen required to decompose the organic matter transported in surface runoff. The SWAT+ loading function for CBOD is based on a relationship given by Thomann and Mueller (1987):

&#x20;      $$cbod_{surq}=\frac{2.7*orgC_{surq}}{Q_{surf}*area_{hru}}$$                                                                           4:5.2.1

&#x20;       where $$cbod_{surq}$$ is the CBOD concentration in surface runoff (mg CBOD/L), $$orgC_{surq}$$ is the organic carbon in surface runoff (kg $$orgC$$), $$Q_{surf}$$ is the surface runoff on a given day (mm H$$_2$$O), and $$area_{hru}$$ is the area of the HRU (km$$^2$$).&#x20;

&#x20;    The amount of organic carbon in surface runoff is calculated:

&#x20;           $$orgC_{surq}=1000*\frac{orgC_{surf}}{100}*sed*\varepsilon_{C:sed}$$                                    4:5.2.2

where $$orgC_{surq}$$ is the organic carbon in surface runoff (kg $$orgC$$), $$orgC_{surf}$$ is the percent organic carbon in the top 10 mm of soil (%), $$sed$$ is the sediment loading from the HRU (metric tons), and $$\varepsilon_{C:sed}$$ is the carbon enrichment ratio.
