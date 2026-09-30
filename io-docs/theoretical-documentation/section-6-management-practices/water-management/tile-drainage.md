# Tile Drainage

&#x20;          To simulate tile drainage in an HRU, the user must specify the depth from the soil surface to the drains, the amount of time required to drain the soil to field capacity, and the amount of lag between the time water enters the tile till it exits the tile and enters the main channel.&#x20;

&#x20;              Tile drainage occurs when the perched water table rises above the depth at which the tile drains are installed. The amount of water entering the drain on a given day is calculated:

$$tile_{wtr}=\frac{h_{wtbl}-h_{drain}}{h_{wtbl}}*(SW-FC)*(1-exp[\frac{-24}{t_{drain}}])$$  if   $$h_{wtbl}>h_{drain}$$            6:2.2.1

where $$tile_{wtr}$$ is the amount of water removed from the layer on a given day by tile drainage (mm H$$_2$$O), $$h_{wtbl}$$ is the height of the water table above the impervious zone (mm), $$h_{drain}$$ is the height of the tile drain above the impervious zone (mm), $$SW$$ is the water content of the profile on a given day (mm H$$_2$$O), $$FC$$ is the field capacity water content of the profile (mm H$$_2$$O), and $$t_{drain}$$ is the time required to drain the soil to field capacity (hrs).&#x20;

&#x20;        Water entering tiles is treated like lateral flow. The flow is lagged using equations reviewed in Chapter 2:3.

Table 6:2-2: SWAT+ input variables that pertain to tile drainage.

| Variable Name | Definition                                                | Input File |
| ------------- | --------------------------------------------------------- | ---------- |
| DDRAIN        | Depth to subsurface drain (mm).                           | .mgt       |
| TDRAIN        | $$t_{drain}$$: Time to drain soil to field capacity (hrs) | .mgt       |
| GDRAIN        | $$tile_{lag}$$: Drain tile lag time (hrs)                 | .mgt       |
