# Dormancy

&#x20;   SWAT+ assumes trees, perennials and cool season annuals can go dormant as the daylength nears the shortest or minimum daylength for the year. During dormancy, plants do not grow.

&#x20;      The beginning and end of dormancy are defined by a threshold daylength. The threshold daylength is calculated:   &#x20;

&#x20;       $$T_{DL,thr}=T_{DL,mn}+t_{dorm}$$                                                                        5:1.2.1

where $$T_{DL,thr}$$ is the threshold daylength to initiate dormancy (hrs), $$T_{DL,mn}$$ is the minimum daylength for the watershed during the year (hrs), and tdorm is the dormancy threshold (hrs). When the daylength becomes shorter than $$T_{DL,thr}$$ in the fall, plants other than warm season annuals that are growing in the watershed will enter dormancy. The plants come out of dormancy once the daylength exceeds $$T_{DL,thr}$$ in the spring.&#x20;

&#x20;        The dormancy threshold, $$t_{dorm}$$, varies with latitude.

$$t_{dorm}=1.0$$                  if $$\phi >$$40 º N or S                                                        5:1.2.2

$$t_{dorm}=\frac{\phi - 20}{20}$$               if 20 º N or S $$\le \phi \le$$ 40 º N or S                               5:1.2.3

$$t_{dorm}=0.0$$                  if $$\phi <$$20 º N or S                                                        5:1.2.4

where $$t_{dorm}$$ is the dormancy threshold used to compare actual daylength to minimum daylength (hrs) and $$\phi$$ is the latitude expressed as a positive value (degrees).

&#x20;         At the beginning of the dormant period for trees, a fraction of the biomass is converted to residue and the leaf area index for the tree species is set to the minimum value allowed (both the fraction of the biomass converted to residue and the minimum LAI are defined in the plant growth database). At the beginning of the dormant period for perennials, 10% of the biomass is converted to residue and the leaf area index for the species is set to the minimum value allowed. For cool season annuals, none of the biomass is converted to residue.

Table 5:1-2: SWAT+ input variables that pertain to dormancy.

| Variable Name | Definition                                                                                                                                                                                                                                        | Input File |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| SUB\_LAT      | $$\phi$$: Latitude of the subbasin (degrees).                                                                                                                                                                                                     | .sub       |
| IDC           | Land cover/plant classification:              1.warm season annual legume                      2.cold season annual legume              3.perennial legume 4.warm season annual    5.cold season annual 6.perennial                       7.trees | crop.dat   |
| ALAI\_MIN     | Minimum leaf area index for plant during dormant period (m$$^2$$/m$$^2$$)                                                                                                                                                                         | crop.dat   |
| BIO\_LEAF     | Fraction of tree biomass accumulated each year that is converted to residue during dormancy                                                                                                                                                       | crop.dat   |
