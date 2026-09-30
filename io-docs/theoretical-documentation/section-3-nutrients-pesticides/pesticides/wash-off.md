# Wash-off

A portion of the pesticide on plant foliage may be washed off during rain events. The fraction washed off is a function of plant morphology, pesticide solubility, and the timing and intensity of the rainfall event. Wash-off will occur when the amount of precipitation on a given day exceeds 2.54 mm.

&#x20;              The amount of pesticide washing off plant foliage during a precipitation event on a given day is calculated:

$$pst_{f,wsh}=fr_{wsh}*pst_f$$                                                     3:3.1.1

where $$pst_{f,wsh}$$ is the amount of pesticide on foliage that is washed off the plant and onto the soil surface on a given day (kg pst/ha), $$fr_{wsh}$$ is the wash-off fraction for the pesticide, and $$pst_f$$ is the amount of pesticide on the foliage (kg pst/ha). The wash-off fraction represents the portion of the pesticide on the foliage that is dislodgable.

Table 3:3-1: SWAT+ input variables that pertain to pesticide wash-off.

| Variable Name | Definition                                        | Input File |
| ------------- | ------------------------------------------------- | ---------- |
| WOF           | $$fr_{wsh}$$: Wash-off fraction for the pesticide | pest.dat   |
