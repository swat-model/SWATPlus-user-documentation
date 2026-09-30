---
description: Channel water routing method
---

# rte\_cha

There are two channel water routing methods available in SWAT+:

| Code | Option                  |
| ---- | ----------------------- |
| 0    | Variable Storage method |
| 1    | Muskingum method        |

{% hint style="info" %}
The user must be careful to define [msk\_co1](../parameters.bsn/msk_co1.md), [msk\_co2](../parameters.bsn/msk_co2.md) and [msk\_x](../parameters.bsn/msk_x.md) in [**parameters.bsn**](../parameters.bsn/) when the Muskingum method is chosen.
{% endhint %}
