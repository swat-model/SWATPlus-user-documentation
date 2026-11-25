# Channel Erosion by Channel

`ch_sedbud_*` writes one 17-column row per SWAT-DEG channel at the requested interval. The `_d`, `_m`, `_y`, and `_a` suffixes select daily, monthly, yearly, and average-annual files in TXT and optional CSV. [File creation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_sd_channel.f90#L349), [Writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_sedbud_output.f90#L12)

| Field | Description | Unit |
| --- | --- | --- |
| `jday` | Day of year | n/a |
| `mon` | Month | n/a |
| `day` | Day of month | n/a |
| `yr` | Calendar year | n/a |
| `ichan` | Index within the SWAT-DEG channel list | n/a |
| `ob` | Channel object's GIS ID | n/a |
| `name` | Channel object name | n/a |
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

The simulation clears these records at the start of each day. A channel contributes `num = 1` when it enters the sediment calculation with inflow above `1.e-6` m³. The near-zero-length channel bypass skips that calculation. A daily row can therefore have `num = 0` with zero values for width, depth, and erosion. Reporting starts after `nyskip`. [Daily reset](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L250-L254), [channel bypass](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L375-L408), [inflow gate](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L78-L84), [report calls](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L440-L450).

Daily `wid` and `dep` come from the channel's width and depth. The producer estimates floodplain area using five times channel width. It estimates `fp_mm` from deposited mass, that floodplain width, channel length, and an assumed bulk density of 1 t/m³. [Daily producer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L274-L293).

## Erosion and deposition calculations

- **Values used by the daily routine.** Setup loads `bankfull_flo`, `fp_inun_days`, `d50`, and `bed_exp` from channel parameters. Before checking inflow, the sediment routine replaces them with `1.5`, `1.0`, `1.0`, and `1.0`, respectively. Floodplain deposition uses the peak-flow test against 1.5 times the second rating-curve flow, and the active trapping calculation uses one inundation day. [Setup](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_hydsed_init.f90#L86-L116), [overrides and floodplain test](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L78-L129).
- **Bank erosion.** Bank cutting begins when the bend-adjusted velocity exceeds the critical velocity. The active mass calculation uses the computed cutting distance, channel depth, bulk density, and one quarter of the channel length. The routine computes a protected length using `arc_len_fr`, but the active mass expression uses the quarter-length directly. [Bank calculation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L168-L215).
- **Bed erosion.** Bed cutting requires slope above `1.e-6` and velocity above `0.293 * sqrt(d50)`. The routine writes gross bed erosion mass to `ebtm_t` here and in the stream-order summary. The [nutrient and sediment budget](channel-nutrient-sediment-budget.md) writes `bed_ero` after multiplying that gross mass by `wash_bed_fr`. The line that would add the calculated bed load to the routed hydrograph is commented out. [Bed calculation and reporting](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_sediment3.f90#L248-L296), [budget assignment](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_control3.f90#L414-L421).

Monthly and yearly output sums every field, including width, depth, floodplain area, and `num`. A channel contributing on 30 days can therefore print `num = 30`. The average-annual writer divides the real-valued sums by the number of printed years and keeps the accumulated `num` unchanged. [Period accumulation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_sedbud_output.f90#L15), [Addition and division](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/sd_channel_module.f90#L708)

If the run ends before the last day of the month, the yearly accumulator includes the remaining monthly values. That partial month has no separate monthly row. The [stream-order writer](channel-erosion-by-order.md) follows the same rule. [Month and year writes](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/ch_sedbud_output.f90#L33-L73).

[Back to the Channel Sediment Budgets index](README.md).
