---
description: Name of the wind speed station
---

# wnd

The name of the wind speed station is a foreign key referencing the filenames listed in [**wnd.cli**](../wnd.cli-and-wind-speed-data-files.md).&#x20;

{% hint style="info" %}
If "sim" is entered instead of a wind speed station name, the model will generate daily wind speed values using the weather generator station specified in column [wgn](wgn.md).
{% endhint %}
