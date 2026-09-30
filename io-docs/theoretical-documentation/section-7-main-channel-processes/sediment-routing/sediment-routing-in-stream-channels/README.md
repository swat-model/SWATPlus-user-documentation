# Sediment Routing In Stream Channels

&#x20;           Each subbasin has a main routing reach where sediment from upland subbasins is routed and then added to downstream reaches.  In SWAT+, a simplified version of Bagnold (1977) stream power equation was used to calculate the maximum amount of sediment that can be transported in a stream segment.  It does not keep track of sediment pools in various particle sizes.

&#x20;           In the current version, four additional stream power equations with more physically based approach have been incorporated for modeling sediment transport, bank and bed erosions in channel containing various bed materials and sediment deposition.  If one among these four physically based approach is selected, then the sediment pool in six particle sizes are tracked by the model.    &#x20;
