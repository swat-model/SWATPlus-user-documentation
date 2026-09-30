# Seepage

The volume of water lost by seepage through the bottom of the pothole on a given day is calculated as a function of the water content of the soil profile beneath the pothole.

&#x20;    $$V_{seep}=240*K_{sat}*SA$$                                  if  $$SW<0.5*FC$$              8:1.3.7

&#x20;     $$V_{seep}=240*(1-\frac{SW}{FC})*K_{sat}*SA$$            if  $$0.5*FC \le SW <FC$$  8:1.3.8

&#x20;      $$V_{seep}=0$$                                                           if  $$SW \ge FC$$                        8:1.3.9

where $$V_{seep}$$ is the volume of water lost from the water body by seepage (m$$^3$$ H$$_2$$O), $$K_{sat}$$ is the effective saturated hydraulic conductivity of the 1st soil layer in the profile (mm/hr), $$SA$$ is the surface area of the water body (ha), $$SW$$ is the soil water content of the profile on a given day (mm H$$_2$$O), and $$FC$$ is the field capacity soil water content (mm      H$$_2$$O). Water lost from the pothole by seepage is added to the soil profile.
