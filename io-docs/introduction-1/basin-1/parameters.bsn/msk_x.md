---
description: >-
  Weighting factor control relative importance of inflow rate and outflow rate
  in determining storage on reach
---

# msk\_x

The weighting factor is a function of the wedge storage. This parameter is only important if channel routing is simulated using the Muskingum routing method.

{% hint style="info" %}
For reservoir-type storage, there is no wedge and _msk\_x_ should be 0.0. For a full-wedge, _msk\_x_ should be 0.5. For rivers, _msk\_x_ will fall between 0.0 and 0.3 with a mean value near 0.2.&#x20;
{% endhint %}
