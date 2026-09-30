---
description: Number of years at the beginning of the simulation to not print output
---

# nyskip

Some simulations will need a warm-up or equilibration period. The use of a warm-up period becomes more important as the simulation period of interest shortens. For 30-year simulations, a warm-up period is optional. For a simulation covering 5 years or less, a warm-up period is recommended.&#x20;

{% hint style="info" %}
Examples: If _nyskip_ = 2, the model will skip printing the first two years regardless of the starting year. If _nyskip_ = 0, output for all years of the simulation will be printed. If _nyskip_ equals the number of years in the simulation, no output will be printed. &#x20;
{% endhint %}
