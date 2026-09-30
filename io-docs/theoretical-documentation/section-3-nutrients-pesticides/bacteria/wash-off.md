# Wash-off

A portion of the bacteria on plant foliage may be washed off during rain events. The fraction washed off is a function of plant morphology, bacteria characteristics, and the timing and intensity of the rainfall event. Wash-off will occur when the amount of precipitation on a given day exceeds 2.54 mm.

&#x20;          The amount of bacteria washing off plant foliage during a precipitation event on a given day is calculated:

$$bact_{lp,wsh}=fr_{wsh,lp}*bact_{lp,fol}$$                                            3:4.1.1

$$bact_{p,wsh}=fr_{wsh,p}*bact_{p,fol}$$                                               3:4.1.2

where $$bact_{lp,wsh}$$ is the amount of less persistent bacteria on foliage that is washed off the plant and onto the soil surface on a given day (# cfu/m$$^2$$), $$bact_{p,wsh}$$ is the amount of persistent bacteria on foliage that is washed off the plant and onto the soil surface on a given day (# cfu/m$$^2$$), $$fr_{wsh,lp}$$ is the wash-off fraction for the less persistent bacteria, $$fr_{wsh,p}$$ is the wash-off fraction for the persistent bacteria, $$bact_{lp,fol}$$ is the amount of less persistent bacteria attached to the foliage (# cfu/m$$^2$$), and $$bact_{p,fol}$$ is the amount of persistent bacteria attached to the foliage (# cfu/m$$^2$$). The wash-off fraction represents the portion of the bacteria on the foliage that is dislodgable.

&#x20;         Bacteria that washes off the foliage is assumed to remain in solution in the soil surface layer.

Table 3:4-1: SWAT+ input variables that pertain to bacteria wash-off.

| Variable Name | Definition                                                      | Input File |
| ------------- | --------------------------------------------------------------- | ---------- |
| WOF\_P        | $$fr_{wsh,p}$$: Wash-off fraction for persistent bacteria       | .bsn       |
| WOF\_LP       | $$fr_{wsh,lp}$$: Wash-off fraction for less persistent bacteria | .bsn       |
