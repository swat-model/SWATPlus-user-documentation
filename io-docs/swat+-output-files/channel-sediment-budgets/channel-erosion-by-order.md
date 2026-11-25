# Channel Erosion by Order

`chanbud_order_*` writes a 15-column row for each order from 1 through 12, including orders with no contributions. The `_d`, `_m`, `_y`, and `_a` suffixes select daily, monthly, yearly, and average-annual files in TXT and optional CSV. [File creation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_sd_channel.f90#L280), [Order loop](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/chord_sedbud_output.f90#L12)

| Field | Description | Unit |
| --- | --- | --- |
| `jday` | Day of year | n/a |
| `mon` | Month | n/a |
| `day` | Day of month | n/a |
| `yr` | Calendar year | n/a |
| `iord` | SWAT-DEG channel order | n/a |
| `num` | Count of contributing channel records | n/a |
| `wid` | Channel width contribution | m |
| `dep` | Channel depth contribution | m |
| `fp_km2` | Estimated floodplain area contribution | km2 |
| `ebank_t` | Bank erosion mass | tons |
| `ebtm_t` | Bed erosion mass | tons |
| `ebank_m` | Bank cutting distance | m |
| `ebtm_m` | Bed cutting depth | m |
| `fp_t` | Floodplain sediment deposited | tons |
| `fp_mm` | Floodplain deposition thickness contribution | mm |

The daily producer adds each channel record to its order. All fields are added across channels and over time, including `wid`, `dep`, and `fp_mm`. Read these fields as sums of the individual contributions. Monthly and yearly `num` counts channel records across days. Average annual divides the real-valued sums by the number of printed years and retains the accumulated `num`. [Order assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L65), [Order accumulation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L295), [Period writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/chord_sedbud_output.f90#L13), [Addition and division](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L708)

Only channels that run the sediment calculation with inflow above `1.e-6` m³ contribute. The producer uses the channel's current order directly as the index into the 12 bins. An order outside 1–12 is outside the array bounds. The order summaries use the same gross `ebtm_t` and daily parameter overrides as the [per-channel report](channel-erosion-by-channel.md#erosion-and-deposition-calculations). [Order initialization](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L75), [12-bin declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L112), [daily accumulation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L292-L296).

[Back to the Channel Sediment Budgets index](README.md).
