---
description: Name of the temperature station
---

# tmp

The name of the temperature station is a foreign key referencing the filenames listed in [**tmp.cli**](../tmp.cli-and-temperature-data-files.md).&#x20;

{% hint style="info" %}
If "sim" is entered instead of a temperature station name, the model will generate daily temperature values using the weather generator station specified in column [wgn](wgn.md).
{% endhint %}
