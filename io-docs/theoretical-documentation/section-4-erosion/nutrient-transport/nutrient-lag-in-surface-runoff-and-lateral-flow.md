# Nutrient Lag in  Surface Runoff and Lateral Flow

&#x20;        In large subbasins with a time of concentration greater than 1 day, only a portion of the surface runoff and lateral flow will reach the main channel on the day it is generated. SWAT+ incorporates a storage feature to lag a portion of the surface runoff and lateral flow release to the main channel. Nutrients in the surface runoff and lateral flow are lagged as well.

&#x20;          Once the nutrient load in surface runoff and lateral flow is determined, the amount of nutrients released to the main channel is calculated:

$$NO3_{surf}=(NO3'_{surf}+NO3_{surstor,i-1})*(1-exp[\frac{-surlag}{t_{conc}}])$$                     4:2.5.1

$$NO3_{lat}=(NO3'_{lat}+NO3_{latstor,i-1})*(1-exp[\frac{-1}{TT_{lat}}])$$                                4:2.5.2

$$orgN_{surf}=(orgN'_{surf}+orgN_{stor,i-1})*(1-exp[\frac{-surlag}{t_{conc}}])$$                        4:2.5.3

$$P_{surf}=(P'_{surf}+P_{stor,i-1})*(1-exp[\frac{-surlag}{t_{conc}}])$$                                              4:2.5.4

$$sedP_{surf}=(sedP'_{surf}+sedP_{stor,i-1})*(1-exp[\frac{-surlag}{t_{conc}}])$$                            4:2.5.5

where $$NO3_{surf}$$ is the amount of nitrate discharged to the main channel in surface runoff on a given day (kg N/ha),$$NO3'_{surf}$$ is the amount of surface runoff nitrate generated in the HRU on a given day (kg N/ha), $$NO3_{surstor,i-1}$$ is the surface runoff nitrate stored or lagged from the previous day (kg N/ha), $$NO3_{lat}$$ is the amount of nitrate discharged to the main channel in lateral flow on a given day (kg N/ha), $$NO3'_{lat}$$ is the amount of lateral flow nitrate generated in the HRU on a given day (kg N/ha), $$NO3_{latstor,i-1}$$ is the lateral flow nitrate stored or lagged from the previous day (kg N/ha), $$orgN_{surf}$$ is the amount of organic N discharged to the main channel in surface runoff on a given day (kg N/ha),$$orgN'_{surf}$$ is the organic N loading generated in the HRU on a given day (kg N/ha), $$orgN_{stor,i-1}$$ is the organic N stored or lagged from the previous day (kg N/ha), $$P_{surf}$$ is the amount of solution P discharged to the main channel in surface runoff on a given day (kg P/ha), $$P'_{surf}$$ is the amount of solution P loading generated in the HRU on a given day (kg P/ha), $$P_{stor,i-1}$$ is the solution P loading stored or lagged from the previous day (kg P/ha), $$sedP_{surf}$$ is the amount of sediment-attached P discharged to the main channel in surface runoff on a given day (kg P/ha), $$sedP'_{surf}$$ is the amount of sediment-attached P loading generated in the HRU on a given day (kg P/ha), $$sedP_{stor,i-1}$$ is the sediment-attached P stored or lagged from the previous day (kg P/ha), $$surlag$$ is the surface runoff lag coefficient, $$t_{conc}$$ is the time of concentration for the HRU (hrs) and $$TT_{lag}$$ is the lateral flow travel time (days).

Table 4:2-5: SWAT+ input variables that pertain to nutrient lag calculations.

| Variable Name | Definition                                    | Input File |
| ------------- | --------------------------------------------- | ---------- |
| SURLAG        | $$surlag$$: surface runoff lag coefficient    | .bsn       |
| LAT\_TTIME    | $$TT_{lag}$$: Lateral flow travel time (days) | .hru       |
