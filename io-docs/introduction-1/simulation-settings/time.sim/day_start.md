---
description: Beginning day of the simulation
---

# day\_start

SWAT+ is able to begin a simulation at any day of the year. This option can for example be useful, if the user wishes to simulate hydrological years instead of calendar years.

{% hint style="info" %}
If _day\_start_ = 0, the model will start the simulation on January 1st.

If the simulation begins before the first day of the observed climate data, SWAT+ will use simulated climate data for the time period before the start of the observed climate data.
{% endhint %}
