# Biomass Override

&#x20;         The model allows the user to specify a total biomass that the plant will produce each year. When the biomass override is set in the plant operation (.mgt), the impact of variation in growing conditions from year to year is ignored, i.e. $$\gamma_{reg}$$ is always set to 1.00 when biomass override is activated in an HRU.&#x20;

&#x20;        When a value is defined for the biomass override, the change in biomass is calculated:

&#x20;                  $$\Delta  bio_{act} = \Delta bio_i*\frac{(bio_{trg}-bio_{i-1})}{bio_{trg}}$$                                                                   5:3.2.4

where $$\Delta bio_{act}$$ is the actual increase in total plant biomass on day $$i$$ (kg/ha), $$\Delta bio_i$$ is the potential increase in total plant biomass on day $$i$$ calculated with equation 5:2.1.2 (kg/ha), $$bio_{trg}$$ is the target biomass specified by the user (kg/ha), and $$bio_{i-1}$$ is the total plant biomass accumulated on day $$i-1$$ (kg/ha).

&#x20;Table 5:3-2: SWAT+ input variables that pertain to actual plant growth.

| Variable Name | Definition                                          | Input File |
| ------------- | --------------------------------------------------- | ---------- |
| BIO\_TARG     | $$bio_{trg}/1000$$: Biomass target (metric tons/ha) | .mgt       |
