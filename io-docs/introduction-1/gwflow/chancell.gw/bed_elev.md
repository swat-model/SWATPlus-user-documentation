---
description: "Channel bed elevation in the cell, m"
---

# bed_elev

**Code reference:** `bed_elev` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_chan_read.f90#L27), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_chan_read.f90#L59)).

Elevation of the channel bed in this cell, in m. SWAT+ lowers it by `river_thresh` from [codes.gw](../codes.gw/river_thresh.md), adds the channel depth to get the stage, and computes the exchange with Darcy's law ([`gwflow_channel_exch.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_channel_exch.f90#L61-L87)):

$$z_{b} = z_{\text{bed}} - d_{r}, \qquad H = z_{b} + D$$

$$Q = K \, \frac{\Delta h}{b} \, W \, L$$

with the head difference $\Delta h$ taken as:

* $D$ when the head is below the bed ($h < z_{b}$): seepage driven by the full channel depth;
* $H - h$ when the head is between the bed and the stage: seepage;
* $H - h$, which is negative, when the head is above the stage: discharge to the channel.

The head exactly at $z_{b}$ or $H$ gives no exchange. Here $Q$ is the flow into the aquifer (m³/day; negative is discharge to the channel), $D$ the channel depth (the channel's `chd`, or the day's value from `chan_depth.gw`), $h$ the head, $K$ and $b$ the streambed conductivity and thickness, $W$ the channel width (`chw`) and $L$ the [chan_length](chan_length.md). Seepage is limited to the water in the channel and discharge to the water stored in the cell ([`gwflow_channel_exch.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_channel_exch.f90#L89-L100)).
