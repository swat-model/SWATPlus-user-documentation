---
description: Name of the precipitation station
---

# pcp

The name of the precipitation station is a foreign key referencing the filenames listed in [**pcp.cli**](../pcp.cli-and-precipitation-data-files.md).&#x20;

{% hint style="info" %}
If "sim" is entered instead of a precipitation station name, the model will generate daily precipitation values using the weather generator station specified in column [wgn](wgn.md).
{% endhint %}
