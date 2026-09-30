# Grassed Waterways

&#x20;      Support for grass waterways was added to SWAT+. Waterways are treated as trapezoidal channels; the deposition of sediment and organic nutrients is calculated in the same manner as SWAT+ subbasin tributary channels. The primary user inputs are waterway width and length.&#x20;

&#x20;       The sediment transport capacity is defined as:

&#x20;                               $$Scap=Spcon*v^{1.5}$$                                                                     6:5.2.1

&#x20;       where $$Scap$$ is the sediment transport capacity in (mg/m$$^3$$) , $$Spcon$$ is the sediment transport coefficient and $$v$$ is flow velocity in the waterway (m/s).&#x20;

&#x20;          Unsubmerged portions of the waterway act as filter strips, and may trap both soluble and organic nutrients. These equations are simplified forms of those used by White and Arnold (2009) in the simulation of filter strips. Removal of soluble pollutants from the unsubmerged portion is calculates as:

&#x20;                    $$SolR=75.8-10.8log(SD)+25.9log(SolK)$$                               6:5.2.2

where $$SolR$$ is soluble pollutant removal (%), $$SD$$ is runoff depth over unsubmerged waterway area in (mm/day), and $$SolK$$ is the saturated hydrologic conductivity of the soil surface (mm/hr). Removal of particulate pollutant and sediment in the unsubmerged area is calculated as:

&#x20;                    $$SedR=79.0-1.04(SedL)+0.213*(SolR)$$                               6:5.2.3

where $$SedR$$ is the sediment and particulate pollutant removal (%) and $$SedL$$ is the sediment load per unit area of unsubmerged waterway in (kg/ha/day).      &#x20;
