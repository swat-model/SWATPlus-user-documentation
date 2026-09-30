---
description: Name of the relative humidity station
---

# hmd

The name of the relative humidity station is a foreign key referencing the filenames listed in [**hmd.cli**](../hmd.cli-and-humidity-data-files.md).&#x20;

{% hint style="info" %}
If "sim" is entered instead of a relative humidity station name, the model will generate daily relative humidity values using the weather generator station specified in column [wgn](wgn.md).
{% endhint %}
