# Nitrogen Fixation

&#x20;                    If nitrate levels in the root zone are insufficient to meet the demand of a legume, SWAT+ allows the plant to obtain additional nitrogen through nitrogen fixation. Nitrogen fixation is calculated as a function of soil water, soil nitrate content and growth stage of the plant.

&#x20;               $$N_{fix}=N_{demand}*f_{gr}*min(f_{sw},f_{no3},1)$$                                                       5:2.3.9

&#x20;      where $$N_{fix}$$ is the amount of nitrogen added to the plant biomass by fixation (kg N/ha), $$N_{demand}$$ is the plant nitrogen demand not met by uptake from the soil (kg N/ha), $$f_{gr}$$ is the growth stage factor (0.0-1.0), $$f_{sw}$$ is the soil water factor (0.0-1.0), and $$f_{no3}$$ is the soil nitrate factor (0.0-1.0). The maximum amount of nitrogen that can be fixed by the plant on a given day is $$N_{demand}$$.&#x20;

&#x20;               Growth stage exerts the greatest impact on the ability of the plant to fix nitrogen. The growth stage factor is calculated:

&#x20;             $$f_{gr}=0$$                                             when  $$fr_{PHU} \le 0.15$$                               5:2.3.10

&#x20;            $$f_{gr}=6.67*fr_{PHU}-1$$                 when  $$0.15 <fr_{PHU} \le 0.30$$                  5:2.3.11

&#x20;            $$f_{gr}=1$$                                               when $$0.30 <fr_{PHU} \le 0.55$$                  5:2.3.12

&#x20;           $$f_{gr}=3.75 -5*fr_{PHU}$$                   when $$0.55 <fr_{PHU} \le 0.75$$                  5:2.3.13

&#x20;          $$f_{gr}=0$$                                                  when $$fr_{PHU} > 0.75$$                               5:2.3.14

&#x20;    where $$f_{gr}$$ is the growth stage factor and $$fr_{PHU}$$ is the fraction of potential heat units accumulated for the plant on a given day in the growing season. The growth stage factor is designed to reflect the buildup and decline of nitrogen fixing bacteria in the plant roots during the growing season.&#x20;

&#x20;         The soil nitrate factor inhibits nitrogen fixation as the presence of nitrate in the soil goes up. The soil nitrate factor is calculated:

&#x20;            $$f_{no3}=1$$                                               when $$NO3 \le 100$$                                    5:2.3.15

&#x20;           $$f_{no3}=1.5-0.0005*NO3$$               when $$100 < NO3 \le 300$$                       5:2.3.16

&#x20;           $$f_{no3}=0$$                                                  when $$NO3> 300$$                                   5:2.3.17

&#x20;         where $$f_{no3}$$ is the soil nitrate factor and $$NO3$$ is the nitrate content of the soil profile           (kg NO$$_3$$-N/ha).&#x20;

&#x20;                 The soil water factor inhibits nitrogen fixation as the soil dries out. The soil water factor is calculated:

&#x20;                    $$f_{SW}=\frac{SW}{.85*FC}$$                                                                                                      5:2.3.18

where $$f_{SW}$$ is the soil water factor, $$SW$$ is the amount of water in soil profile (mm H$$_2$$O), and $$FC$$ is the water content of soil profile at field capacity (mm H$$_2$$O).
