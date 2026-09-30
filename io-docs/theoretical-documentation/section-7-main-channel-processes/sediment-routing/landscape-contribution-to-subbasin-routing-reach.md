# Landscape Contribution to Subbasin Routing Reach

&#x20;     The sediment size distribution of the detached sediment is estimated from the primary particle size distribution (Foster et al., 1980).  The values are typical of many Midwestern soils.

&#x20;          $$PSA=(SAN)(1.-CLA)^{2.4}$$                                                                     7:2.1.1

&#x20;          $$PSI=0.13SIL$$                                                                                             7:2.1.2

&#x20;         $$PCL=0.20CLA$$                                                                                           7:2.1.3

&#x20;         $$SAG=\begin{cases}2.0CLA & for &CLA < 0.25 \\  0.28(CLA -0.25)+0.5 & for &CLA 0.25 CLA 0.5 \\ 0.57 & for &CLA>0.5  \end{cases}$$              7:2.1.4

&#x20;         $$LAG=1.0-PSA-PSI-PCL-SAG$$                                               7:2.1.5

where SAN, SIL and CLA are the fractions of primary sand, silt, and clay in the original soil mass, and PSA, PSI, PCL, SAG and LAG are the fractions of sand, silt, clay, small aggregates, and large aggregates for the detached sediment before deposition.  Total sediment yield from landscape calculated by MUSLE is multiplied by these fractions to get the corresponding yield distributions of sand, silt, clay, small aggregate and large aggregate.  The particle diameters assumed are:

&#x20;         $$Sand=0.20mm \\ Silt=0.01mm \\Clay=0.002mm\\SmallAggregate=0.03mm\\LargeAggregate=0.50mm$$

&#x20;    Sediment yield from landscape is lagged (see the chapter on Erosion) and routed through grassed waterway, vegetative filter strips, and ponds, if available, before reaching the stream channel.  Thus, the sediment yield reaching the stream channel is the sum of total sediment yield calculated by MUSLE minus the lag, and the sediment trapped in grassed waterway, vegetative filter strips and/or ponds.  Please refer to the individual chapters for sediment routing through these elements.  Based on the total sediment trapping calculated in these elements, coarser sediments such as sand and large aggregate are assumed to settle/trap first followed by fine sediments such as clay.  This gives the final particle size distribution of sediment reaching the stream from landscape portion.
