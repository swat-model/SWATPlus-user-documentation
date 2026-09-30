# Irrigation

&#x20;          Irrigation in an HRU may be scheduled by the user or automatically applied by SWAT+ in response to a water deficit in the soil. In addition to specifying the timing and application amount, the user must specify the source of irrigation water.&#x20;

&#x20;              Water applied to an HRU is obtained from one of five types of water sources: a reach, a reservoir, a shallow aquifer, a deep aquifer, or a source outside the watershed. In addition to the type of water source, the model must know the location of the water source (unless the source is outside the watershed). For the reach, shallow aquifer or deep aquifer, SWAT+ needs to know the reach number or subbasin number, respectively, in which the source is located. If a reservoir is used to supply water, SWAT+ must know the reservoir number.&#x20;

&#x20;                  If the source of the irrigation water is a reach, SWAT+ allows additional input parameters to be set. These parameters are used to prevent flow in the reach from being reduced to zero as a result of irrigation water removal. Users may define a minimum in-stream flow, a maximum irrigation water removal amount that cannot be exceeded on any given day, and/or a fraction of total flow in the reach that is available for removal on a given day.&#x20;

&#x20;                     For a given irrigation event, SWAT+ determines the amount of water available in the source. The amount of water available is compared to the amount of water specified in the irrigation operation. If the amount available is less than the amount specified, SWAT+ will only apply the available water.
