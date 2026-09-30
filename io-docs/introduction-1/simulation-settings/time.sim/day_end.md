---
description: Ending day of the simulation
---

# day\_end

SWAT+ is able to end a simulation at any day of the year. This option can for example be useful, if the user wishes to simulate hydrological years instead of calendar years.

{% hint style="info" %}
If _day\_end_ = 0, the model will end the simulation on December 31st.

If the simulation begins before the first day of the observed climate data, SWAT+ will use simulated climate data for the time period before the start of the observed climate data.
{% endhint %}
