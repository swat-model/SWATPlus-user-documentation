# 1:3.3 Distribution of Rainfall Within Day

For simulations where the timing of rainfall within the day is required, the daily rainfall value must be partitioned into shorter time increments. The method used in SWAT+ to disaggregate storm data was taken from CLIGEN (Nicks et al., 1995).&#x20;

A double exponential function is used to represent the intensity patterns within a storm. With the double exponential distribution, rainfall intensity exponentially increases with time to a maximum, or peak, intensity. Once the peak intensity is reached, the rainfall intensity exponentially decreases with time until the end of the storm.&#x20;

The exponential equations governing rainfall intensity during a storm event are:

$$i(T)={i_{mx}*exp[\frac{T-T_{peak}}{\delta_{1}}], i_{mx}*exp[\frac{T_{peak}-T}{\delta_2}}]$$                                                                                             1:3.3.1

$$0\le T \le T_{peak}$$   , $$T_{peak} < T <T_{dur}$$

where $$i$$ is the rainfall intensity at time $$T$$ ($${mm}/{hr}$$), $$i_{mx}$$ is the maximum or peak rainfall intensity during the storm ($${mm}/{hr}$$), $$T$$ is the time since the beginning of the storm ($${hr}$$), $$T_{peak}$$ is the time from the beginning of the storm till the peak rainfall intensity occurs ($${hr}$$), $$T_{dur}$$ is the duration of the storm ($${hr}$$), and $$\delta_1$$ and $$\delta_2$$ are equation coefficients ($${hr}$$).

The maximum or peak rainfall intensity during the storm is calculated assuming the peak rainfall intensity is equivalent to the rainfall intensity used to calculate the peak runoff rate. The equations used to calculate the intensity are reviewed in Chapter 2:1 (section 2:1.3.3).           &#x20;
