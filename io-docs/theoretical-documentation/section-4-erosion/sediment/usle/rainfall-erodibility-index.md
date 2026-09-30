# Rainfall Erodibility Index

&#x20;     The value of $$EI_{USLE}$$ for a given rainstorm is the product, total storm energy times the maximum 30 minute intensity. The storm energy indicates the volume of rainfall and runoff while the 30 minute intensity indicates the prolonged peak rates of detachment and runoff.

&#x20;            $$EI_{USLE}=E_{storm}*I_{30}$$                                                                   4:1.2.2

where $$EI_{USLE}$$ is the rainfall erosion index (0.017 m-metric ton cm/(m$$^2$$ hr)), $$E_{storm}$$ is the total storm energy (0.0017 m-metric ton/m$$^2$$), and $$I_{30}$$ is the maximum 30-minute intensity (mm/hr).

&#x20;          The energy of a rainstorm is a function of the amount of rain and of all the storm’s component intensities. Because rainfall is provided to the model in daily totals, an assumption must be made about variation in rainfall intensity. The rainfall intensity variation with time is assumed to be exponentially distributed:

&#x20;          $$i_t=i_{mx}*exp(-\frac{t}{k_i})$$                                                                                  4:1.2.3

where $$i_t$$ is the rainfall intensity at time $$t$$ (mm/hr), $$i_{mx}$$ is the maximum rainfall intensity (mm/hr), $$t$$ is the time (hr), and $$k_i$$ is the decay constant for rainfall intensity (hr).&#x20;

&#x20;         The USLE energy equation is

&#x20;            $$E_{storm}=\Delta R_{day}*(12.1+8.9*log_{10}[\frac{\Delta R_{day}}{\Delta t}])$$                                       4:1.2.4

where $$\Delta R_{day}$$ is the amount of rainfall during the time interval (mm H$$_2$$O), and $$\Delta t$$ is the time interval (hr). This equation may be expressed analytically as:

&#x20;         $$E_{storm}=12.1\int_0^{\infty}i_t dt+8.9\int_0^{\infty} i_t log_{10} i_tdt$$                                              4:1.2.5

Combining equation 4:1.2.5 and 4:1.2.3 and integrating gives the equation for estimating daily rainfall energy:

&#x20;         $$E_{storm}=\frac{R_{day}}{1000}*(12.1+8.9*(log_{10}[i_{mx}]-0.434))$$                              4:1.2.6

where $$R_{day}$$ is the amount of precipitation falling on a given day (mm H$$_2$$O), and $$i_{mx}$$ is the maximum rainfall intensity (mm/hr). To compute the maximum rainfall intensity, $$i_{mx}$$, equation 4:1.2.3 is integrated to give

&#x20;             $$R_{day}=i_{mx}*k_i$$                                                                                        4:1.2.7

and

&#x20;            $$R_t=R_{day}*(1-exp[-\frac{t}{k_i}])$$                                                                   4:1.2.8

&#x20;        where $$R_{day}$$ is the amount of precipitation falling on a given day (mm H$$_2$$O), $$i_{mx}$$ is the maximum rainfall intensity (mm/hr), $$k_i$$ is the decay constant for rainfall intensity (hr), $$R_t$$ is the amount of rain falling during a time interval (mm H$$_2$$O), and $$t$$ is the time interval (hr). The maximum half-hour rainfall for the precipitation event is known:&#x20;

&#x20;           $$R_{0.5}=\alpha_{0.5}*R_{day}$$                                                                                  4:1.2.9

&#x20;    where $$R_{0.5}$$ is the maximum half-hour rainfall (mm H$$_2$$O), $$\alpha_{0.5}$$ is the maximum half-hour rainfall expressed as a fraction of daily rainfall, and $$R_{day}$$ is the amount of precipitation falling on a given day (mm H$$_2$$O). Calculation of $$\alpha_{0.5}$$ is reviewed in Chapter 1:2 and Chapter 1:3. Substituting equation 4:1.2.9 and 4:1.2.7 into 4:1.2.8 and solving for the maximum intensity gives:

&#x20;             $$i_{mx}=-2*R_{day}*1n(1-\alpha_{0.5})$$                                                         4:1.2.10

where $$i_{mx}$$ is the maximum rainfall intensity (mm/hr), $$R_{day}$$ is the amount of precipitation falling on a given day (mm H$$_2$$O), and $$\alpha_{0.5}$$ is the maximum half-hour rainfall expressed as a fraction of daily rainfall.&#x20;

&#x20;      The maximum 30 minute intensity is calculated:

&#x20;                   $$I_{30}=2*\alpha_{0.5}*R_{day}$$                                                                     4:1.2.11

where $$I_{30}$$ is the maximum 30-minute intensity (mm/hr), $$\alpha_{0.5}$$ is the maximum half-hour rainfall expressed as a fraction of daily rainfall, and $$R_{day}$$ is the amount of precipitation falling on a given day (mm H$$_2$$O).&#x20;

Table 4:1-6: SWAT+ input variables that pertain to USLE sediment yield.

| Variable Name | Definition                                                                                       | Input File |
| ------------- | ------------------------------------------------------------------------------------------------ | ---------- |
| USLE\_K       | $$K_{USLE}$$: USLE soil erodibility factor (0.013 metric ton m$$^2$$ hr/(m$$^3$$-metric ton cm)) | .sol       |
| USLE\_C       | $$C_{USLE,mn}$$: Minimum value for the cover and management factor for the land cover            | crop.dat   |
| USLE\_P       | $$P_{USLE}$$: USLE support practice factor                                                       | .mgt       |
| SLSUBBSN      | $$L_{hill}$$: Slope length (m)                                                                   | .hru       |
| SLOPE         | $$slp$$: Average slope of the subbasin (% or m/m)                                                | .hru       |
| ROCK          | $$rock$$: Percent rock in the first soil layer (%)                                               | .sol       |
