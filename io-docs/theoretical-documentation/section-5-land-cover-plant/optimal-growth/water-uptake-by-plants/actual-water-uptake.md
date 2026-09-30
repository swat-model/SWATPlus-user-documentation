# Actual Water Uptake

Once the potential water uptake has been modified for soil water conditions, the actual amount of water uptake from the soil layer is calculated:

&#x20;        $$w_{actualup,ly}=min\lfloor w''_{up,ly},(SW_{ly}-WP_{ly})\rfloor$$                                          5:2.2.7

where $$w_{actualup,ly}$$ is the actual water uptake for layer $$ly$$ (mm H$$_2$$O), $$SW_{ly}$$ is the amount of water in the soil layer on a given day (mm H$$_2$$O), and $$WP_{ly}$$ is the water content of layer $$ly$$ at wilting point (mm H$$_2$$O). The total water uptake for the day is calculated:

&#x20;       $$w_{actualup}=\sum^n_{ly=1} w_{actualup,ly}$$                                                                   5:2.2.8

where $$w_{actualup}$$ is the total plant water uptake for the day (mm H$$_2$$O), $$w_{actualup,ly}$$ is the actual water uptake for layer $$ly$$ (mm H$$_2$$O), and n is the number of layers in the soil profile. The total plant water uptake for the day calculated with equation 5:2.2.8 is also the actual amount of transpiration that occurs on the day.

&#x20;          $$E_{t,act}=w_{actualup}$$                                                                                     5:2.2.9

where $$E_{t,act}$$ is the actual amount of transpiration on a given day (mm H$$_2$$O) and $$w_{actualup}$$ is the total plant water uptake for the day (mm H$$_2$$O).

Table 5:2-2: SWAT+ input variables that pertain to plant water uptake.

| Variable Name | Definition                                 | Input File |
| ------------- | ------------------------------------------ | ---------- |
| EPCO          | $$epco$$: Plant uptake compensation factor | .bsn, .hru |
