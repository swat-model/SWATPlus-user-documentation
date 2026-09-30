---
description: >-
  Initial soil water storage expressed as a fraction of field capacity water
  content
---

# sw\_init

All soils in the watershed will be initialized to the same fraction. If _sw\_init_ = 0.0, the model will calculate it as a function of average annual precipitation.&#x20;

{% hint style="info" %}
We recommend using a warm-up period of at least 1 year, i.e. start the simulation at least 1 year prior to the period of interest. This allows the model to get the water cycling properly before any comparisons between measured and simulated data are made. If a warm-up period is incorporated, the value for _sw\_init_ will not impact model results.
{% endhint %}
