---
description: Name of the solar radiation station
---

# slr

The name of the solar radiation station is a foreign key referencing the filenames listed in [**slr.cli**](../slr.cli-and-solar-radiation-data-files.md).&#x20;

{% hint style="info" %}
If "sim" is entered instead of a solar radiation station name, the model will generate daily solar radiation values using the weather generator station specified in column [wgn](wgn.md).
{% endhint %}
