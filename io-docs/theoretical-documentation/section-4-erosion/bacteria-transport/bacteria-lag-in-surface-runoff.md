# Bacteria Lag in Surface Runoff

In large subbasins with a time of concentration greater than 1 day, only a portion of the surface runoff will reach the main channel on the day it is generated. SWAT+ incorporates a storage feature to lag a portion of the surface runoff release to the main channel. Bacteria in the surface runoff are lagged as well.&#x20;

&#x20;            Once the bacteria load in surface runoff is determined, the amount of bacteria released to the main channel is calculated:

$$bact_{lp,surf}=(bact'_{lp,surf}+bact_{lp,surstor,i-1})*(1-exp[\frac{-surlag}{t_{conc}}])$$                4:4.3.1

$$bact_{p,surf}=(bact'_{p,surf}+bact_{p,surstor,i-1})*(1-exp[\frac{-surlag}{t_{conc}}])$$                   4:4.3.2

$$bact_{lp,sed}=(bact'_{lp,sed}+bact_{lp,sedstor,i-1})*(1-exp[\frac{-surlag}{t_{conc}}])$$                    4:4.3.3

$$bact_{p,sed}=(bact'_{p,sed}+bact_{p,sedstor,i-1})*(1-exp[\frac{-surlag}{t_{conc}}])$$                       4:4.3.4

where $$bact_{lp,surf}$$ is the amount of less persistent bacteria discharged to the main channel in surface runoff on a given day (#cfu/m$$^2$$),$$bact'_{lp,surf}$$ is the amount of surface runoff less persistent bacteria generated in the HRU on a given day (#cfu/m$$^2$$), $$bact_{lp,surstor,i-1}$$ is the surface runoff less persistent bacteria stored or lagged from the previous day (#cfu/m$$^2$$), $$bact_{p,surf}$$ is the amount of persistent bacteria discharged to the main channel in surface runoff on a given day (#cfu/m2), $$bact'_{p,surf}$$ is the amount of surface runoff persistent bacteria generated in the HRU on a given day (#cfu/m$$^2$$), $$bact_{p,surstor,i-1}$$ is the surface runoff persistent bacteria stored or lagged from the previous day (#cfu/m$$^2$$), $$bact_{lp,sed}$$ is the amount of sediment-attached less persistent bacteria discharged to the main channel in surface runoff on a given day (#cfu/m$$^2$$),$$bact'_{lp,sed}$$ is the amount of sediment-attached less persistent bacteria generated in the HRU on a given day (#cfu/m$$^2$$), $$bact_{lp,sedstor,i-1}$$ is the sediment-attached less persistent bacteria stored or lagged from the previous day (#cfu/m$$^2$$), $$bact_{p,sed}$$ is the amount of sediment-attached persistent bacteria discharged to the main channel in surface runoff on a given day (#cfu/m$$^2$$), $$bact'_{p,sed}$$ is the amount of sediment-attached persistent bacteria generated in the HRU on a given day (#cfu/m$$^2$$), $$bact_{p,sedstor,i-1}$$ is the sediment-attached persistent bacteria stored or lagged from the previous day (#cfu/m$$^2$$), $$surlag$$ is the surface runoff lag coefficient, and $$t_{conc}$$ is the time of concentration for the HRU (hrs).

Table 4:4-3: SWAT+ input variables that pertain to bacteria lag calculations.

| Variable Name | Definition                                 | Input File |
| ------------- | ------------------------------------------ | ---------- |
| SURLAG        | $$surlag$$: surface runoff lag coefficient | .bsn       |
