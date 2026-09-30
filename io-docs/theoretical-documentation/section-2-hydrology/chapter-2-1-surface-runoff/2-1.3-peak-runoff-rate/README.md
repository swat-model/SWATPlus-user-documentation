# 2:1.3 Peak Runoff Rate

The peak runoff rate is the maximum runoff flow rate that occurs with a given rainfall event. The peak runoff rate is an indicator of the erosive power of a storm and is used to predict sediment loss. SWAT+ calculates the peak runoff rate with a modified rational method.

The rational method is widely used in the design of ditches, channels and storm water control systems. The rational method is based on the assumption that if a rainfall of intensity $$i$$ begins at time $$t=0$$ and continues indefinitely, the rate of runoff will increase until the time of concentration, $$t=t_{conc}$$, when the entire subbasin area\* is contributing to flow at the outlet. The rational formula is:

$$q_{peak}=\frac{C*i*Area}{3.6}$$                                                                                                                                                     2:1.3.1

where $$q_{peak}$$ is the peak runoff rate ($$m^3 s^{-1}$$), $$C$$ is the runoff coefficient, $$i$$ is the rainfall intensity (mm/hr), $$Area$$ is the subbasin area (km$$^2$$) and 3.6 is a unit conversion factor.       &#x20;



_\* The equations in section 2:1.3 use the subbasin area rather than the HRU area. Unlike HRUs, subbasins are geographically contiguous areas. Using the subbasin area makes the equations for time of concentration and peak runoff rate easier to conceptualize. In the model, these calculations are performed at the HRU level. Two modifications are made to adapt the equations to HRUs. First, the area of the subbasin is replaced by the area of the HRU. Second, the channel length term, L, used in the channel flow time of concentration calculation is multiplied by the fraction of the subbasin area with the HRU of interest._              &#x20;
