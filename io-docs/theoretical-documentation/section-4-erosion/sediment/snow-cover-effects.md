# Snow Cover Effects

&#x20;                        The erosive power of rain and runoff will be less when snow cover is present than when there is no snow cover. During periods when snow is present in an HRU, SWAT+ modifies the sediment yield using the following relationship:

&#x20;         $$sed=\frac{sed'}{exp[\frac{3*SNO}{25.4}]}$$                                                                                           4:1.3.1

where $$sed$$ is the sediment yield on a given day (metric tons), $$sed'$$ is the sediment yield calculated with MUSLE (metric tons), and $$SNO$$ is the water content of the snow cover (mm H$$_2$$O). &#x20;
