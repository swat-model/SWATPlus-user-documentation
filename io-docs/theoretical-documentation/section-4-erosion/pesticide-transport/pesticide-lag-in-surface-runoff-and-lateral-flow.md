# Pesticide Lag in  Surface Runoff and Lateral Flow

In large subbasins with a time of concentration greater than 1 day, only a portion of the surface runoff and lateral flow will reach the main channel on the day it is generated. SWAT+ incorporates a storage feature to lag a portion of the surface runoff and lateral flow release to the main channel. Pesticides in the surface runoff and lateral flow are lagged as well.

&#x20;        Once the pesticide load in surface runoff and lateral flow is determined, the amount of pesticide released to the main channel is calculated:

$$pst_{surf}=(pst'_{surf}+pst_{surstor,i-1})*(1-exp[\frac{-surlag}{t_{conc}}])$$                               4:3.4.1

$$pst_{lat}=(pst'_{lat}+pst_{latstor,i-1})*(1-exp[\frac{-1}{TT_{lat}}])$$                                         4:3.4.2

$$pst_{sed}=(pst'_{sed}+pst_{sedstor,i-1})*(1-exp[\frac{-surlag}{t_{conc}}])$$                                  4:3.4.3

where $$pst_{surf}$$ is the amount of soluble pesticide discharged to the main channel in surface runoff on a given day (kg $$pst$$/ha), $$pst'_{surf}$$ is the amount of surface runoff soluble pesticide generated in HRU on a given day (kg $$pst$$/ha), $$pst_{surstor,i-1}$$ is the surface runoff soluble pesticide stored or lagged from the previous day (kg $$pst$$/ha), $$pst_{lat}$$ is the amount of soluble pesticide discharged to the main channel in lateral flow on a given day (kg $$pst$$/ha),$$pst'_{lat}$$ is the amount of lateral flow soluble pesticide generated in HRU on a given day (kg $$pst$$/ha), $$pst_{latstor,i-1}$$ is the lateral flow pesticide stored or lagged from the previous day (kg $$pst$$/ha), $$pst_{sed}$$ is the amount of sorbed pesticide discharged to the main channel in surface runoff on a given day (kg $$pst$$/ha), $$pst'_{sed}$$ is the sorbed pesticide loading generated in HRU on a given day (kg $$pst$$/ha), $$pst_{sedstor,i-1}$$ is the sorbed pesticide stored or lagged from the previous day (kg $$pst$$/ha), $$surlag$$ is the surface runoff lag coefficient, $$t_{conc}$$ is the time of concentration for the HRU (hrs) and $$TT_{lag}$$ is the lateral flow travel time (days).

Table 4:3-4: SWAT+ input variables that pertain to pesticide lag calculations.

| Variable Name | Definition                                    | Input File |
| ------------- | --------------------------------------------- | ---------- |
| SURLAG        | $$surlag$$: surface runoff lag coefficient    | .bsn       |
| LAT\_TTIME    | $$TT_{lag}$$: Lateral flow travel time (days) | .hru       |
