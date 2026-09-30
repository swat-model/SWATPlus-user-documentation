---
description: Maximum canopy storage
---

# can\_max

The maximum amount of water that can be trapped in the canopy when the canopy is fully developed.

The plant canopy can significantly affect infiltration, surface runoff and evapotranspiration. As rain falls, canopy interception reduces the erosive energy of droplets and traps a portion of the rainfall within the canopy. The influence the canopy exerts on these processes is a function of the density of plant cover and the morphology of the plant species.&#x20;

When calculating surface runoff, the SCS curve number method lumps canopy interception in the term for initial abstractions. This variable also includes surface storage and infiltration prior to runoff and is estimated as 20% of the retention parameter value for a given day. When the Green & Ampt infiltration equation is used to calculate infiltration, the interception of rainfall by the canopy must be calculated separately.&#x20;

SWAT+ allows the maximum amount of water that can be held in canopy storage to vary from day to day as a function of the leaf area index.
