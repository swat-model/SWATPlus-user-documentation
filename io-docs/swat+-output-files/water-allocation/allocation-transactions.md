# Allocation Transactions

The `water_allo_day`, `water_allo_mon`, `water_allo_yr`, and `water_allo_aa` TXT and CSV files interleave POU, POD, and POR records. See the [Water Allocation index](README.md#how-to-produce-these-files) for the shared `water_allo` print setting.

{% hint style="warning" %}
The printed 25-entry header is stale relative to the active POU/POD/POR writer. It cannot be used as a rectangular data schema. POU, POD, and POR records have different widths; TXT and CSV POU prefixes also differ. The writer has no three-source limit and prints no separate unmet-demand scalar.
{% endhint %}

The following table preserves the literal **legacy header order**, including the three `demand` labels. Its units describe the printed header, not a validated positional mapping to every row. Each linked page lists the actual values at that position.

| Field | Description | Unit |
| --- | --- | --- |
| [jday](jday-allocation-transactions.md) | POU day of year; children have no date prefix | blank |
| [mon](mon-allocation-transactions.md) | POU month; children have no date prefix | blank |
| [day](day-allocation-transactions.md) | POU day of month; children have no date prefix | blank |
| [yr](yr-allocation-transactions.md) | POU year is position 4 in TXT, 6 in CSV | blank |
| [unit](unit.md) | Legacy identifier heading; row-dependent value | blank |
| [trn_typ](trn_typ.md) | Legacy transfer-type heading; row-dependent value | blank |
| [trn_num](trn_num.md) | Legacy transfer-number heading; POU TXT contains name | blank |
| [drcv_typ](drcv_typ.md) | Legacy receiver-type heading; POU TXT contains duty | blank |
| [rcv_num](rcv_num.md) | Legacy receiver-number heading; POU TXT contains delivered amount | blank |
| [src1_obj](src1_obj.md) | Legacy src1 obj heading; use actual row layout | blank |
| [src1_typ](src1_typ.md) | Legacy src1 typ heading; use actual row layout | blank |
| [src1_num](src1_num.md) | Legacy src1 num heading; use actual row layout | blank |
| [demand](demand-allocation-transactions.md) | Legacy demand heading; use actual row layout | m3 |
| [src1_withdraw](src1_withdraw.md) | Legacy src1 withdraw heading; use actual row layout | m3 |
| [src1_unmet](src1_unmet.md) | Legacy src1 unmet heading; use actual row layout | m3 |
| [src2_typ](src2_typ.md) | Legacy src2 typ heading; use actual row layout | blank |
| [src2_num](src2_num.md) | Legacy src2 num heading; use actual row layout | blank |
| [demand](demand-allocation-transactions-2.md) | Legacy demand heading; use actual row layout | m3 |
| [src2_withdraw](src2_withdraw.md) | Legacy src2 withdraw heading; use actual row layout | m3 |
| [src2_unmet](src2_unmet.md) | Legacy src2 unmet heading; use actual row layout | m3 |
| [src3_typ](src3_typ.md) | Legacy src3 typ heading; use actual row layout | blank |
| [src3_num](src3_num.md) | Legacy src3 num heading; use actual row layout | blank |
| [demand](demand-allocation-transactions-3.md) | Legacy demand heading; use actual row layout | m3 |
| [src3_withdraw](src3_withdraw.md) | Legacy src3 withdraw heading; use actual row layout | m3 |
| [src3_unmet](src3_unmet.md) | Legacy src3 unmet heading; use actual row layout | m3 |

## Actual allocation rows

POU means place of use, POD point of diversion, and POR the receiving/return point. The configured counts `pou(ipou)%pods` and `%pors` determine child-row counts. Child indices are local to that POU. The [writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L29) emits these ordered scalar values; indentation is not a column:

| Record | Actual values in WRITE order | Count |
| --- | --- | ---: |
| Daily POU TXT | jday, mon, day, yr, ipou, "POU", name, duty, delivered | 9 |
| Monthly/yearly/AA POU TXT | jday, mon, day, yr, "POU", ipou, name, duty, delivered | 9 |
| Daily POU CSV | jday, mon, day, ipou, "POU", yr, ipou, name, duty, delivered | 10 |
| Monthly/yearly/AA POU CSV | jday, mon, day, "POU", ipou, yr, ipou, name, duty, delivered | 10 |
| POD child, all intervals/formats | "POD", ipod, duty, delivered, 18-component hydrograph | 22 |
| POR child, all intervals/formats | "POR", ipor, 18-component hydrograph | 20 |

Children inherit the parent POU reporting date; they do not repeat dates, receiver/source types, or global object numbers. The hydrograph tail is `flo, sed, orgn, sedp, no3, solp, chla, nh3, no2, cbod, dox, san, sil, cla, sag, lag, grv, temp`. Water is m3, sediment/size classes tons, N/P masses kg N/kg P, other masses kg, and temperature deg C. Temperature is numeric even though the legacy transaction headings do not describe it.

POU and POD duty use m³ of allocation demand. The parent `delivered` scalar uses m³ withdrawn. Each POD delivery assignment adds the current withdrawal to a separate `pou%pod%deliv` field. That field defaults to zero and has no input assignment or active producer on this revision. The daily POD scalar therefore stores the most recent withdrawal assigned to that POD, while the POD hydrograph adds withdrawals across calls. The declaration's m³/s comment for `pou%pod%deliv` does not describe the printed delivery scalar. [POD declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L14-L34), [POD inputs](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L91-L97), [Duty setup](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L149-L184), [Delivery assignments](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L130-L143)

## Daily duty and reported delivery

The start-of-day routine computes an irrigation demand subtotal, then unconditionally replaces it with `rate_max × 86400`. If a maximum-demand decision table is configured, the routine takes the result from `dmd_m3` and caps it at that same maximum. A constant action can set the result directly, while fill actions can calculate a storage deficit. The irrigation-demand action reads the POU demand currently in memory. When it targets the POU being initialized, it reads the replaced value. The printed `duty` is the resulting allocation target. [Demand assignments in order](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L128-L164), [Decision-table actions](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L189-L238)

Each POD duty is the POU duty multiplied by its configured or decision-table fraction. The routine multiplies by those fractions directly, so their sum controls how the POD duties add up. The decision-table path reads a shared array of six fractions. Its actions update one entry at a time, and the start-of-day routine does not clear that array between tables. A table that leaves a fraction unset can therefore reuse a value from an earlier table call. This six-entry limit applies to the decision-table fractions. The report writer still iterates the configured child count. [POD and POR fraction assignments](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L166-L202), [Shared fraction array](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_module.f90#L7-L10), [Fraction actions](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L811-L836)

The POU `delivered` value sums the withdrawal volumes recorded by the allocator. The receiving routines run separately, so this value does not measure water actually applied at an irrigation HRU or received by a particular POR. At the start of the day, outside sources, water towers, and unlimited sources run before the routine sets new duties. The later duty setup resets the parent and POD delivery scalars but retains daily withdrawal hydrographs. A child hydrograph can therefore contain a startup withdrawal that no longer appears in the parent's delivery scalar. [Startup processing](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L33-L48), [Source calls before duty setup](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L87-L164), [POD scalar reset](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L166-L186), [Withdrawal records](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L130-L143), [Receiving calls](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_control.f90#L56-L64)

## Withdrawal limits and compensation

The controller checks the accumulated withdrawal against `wdraw_max × 86400` before making a call. The withdrawal routine starts from the duty or the compensation request and does not reduce that request to the remaining allowance. For PODs without a withdrawal decision table, the accumulated counter resets at year end. A withdrawal-limit action can replace the maximum and reset the counter. [Withdrawal gate](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_control.f90#L18-L26), [Withdrawal request and counter](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L25-L40), [Counter update](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L130-L138), [Decision-table reset](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L182-L187), [Year-end reset](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/time_control.f90#L380-L388)

Compensation is considered when a POU is marked finished and its total delivery is below its duty. The withdrawal routine requests the selected POD's duty minus its delivery diagnostic. The controller and withdrawal routine mix global object numbers with positions inside the POD and POU lists. For example, the completion loop uses the linked-POU count to index the global POU array directly. The compensation call passes the local POD position where the callee expects a global POD index. If those indices differ, the routine can inspect or withdraw against a different record than the one associated with the reported POU. A printed duty–delivery difference is therefore a difference between two diagnostics. The writer has no separate unmet-demand value. [Completion check and compensation call](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_control.f90#L18-L54), [Local and global index lookups](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L13-L43), [Printed values](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L27-L49)

## What each POD source contributes

The allocation reader loads the place-of-use records and their local POD and POR lists from `place_of_use.wro`. The global POD source type and source object number come from `point_of_diver.wro`. In each local record, positions 2 and 5 are both read into `num`, so position 5 replaces position 2. The POR dispatcher uses that resulting `num` for the receiver. [Local list reads](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L91-L105), [Global POD reads](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L209-L245), [Receiver lookup](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_return.f90#L16-L19)

The POD hydrograph adds the withdrawal records from all calls for that source. The adjacent POD `delivered` scalar is a separate assignment that can differ from the hydrograph's accumulated `flo`. The source branches populate the hydrograph as follows. [POD hydrograph and diagnostic assignments](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L130-L143)

| Source | Water and constituents in the POD hydrograph |
| --- | --- |
| Unlimited (`unl`) | Water only. For an ordinary withdrawal, the source fraction is applied once to set POD duty and again to calculate the withdrawal from that duty. |
| Outside source (`osrc`) | Water only. The withdrawal resets the scratch hydrograph, then uses the source fraction times `osrc_om(j)%flo`, indexed by the source object number. It runs the mass conversion on the otherwise empty record. The concentration or Recall record prepared at startup is overwritten on entry to the withdrawal routine. |
| Water tower (`wtow`), canal (`can`), reservoir (`res`) | Withdraws a proportional share of the stored water and constituent masses and reduces the stored hydrograph. The minimum is checked before withdrawal. The withdrawal fraction is capped at one, so a successful withdrawal can take storage below that minimum. Tower and canal thresholds use current storage, while the reservoir uses principal volume. |
| Channel (`cha`) | Copies a proportional share of water and masses from the channel outflow. The downstream hydrograph loses only water in this branch, so the mass copied to the POD also remains in the channel outflow. The minimum is compared directly to daily volume without converting the threshold. The channel skips compensation withdrawals. |
| Standard aquifer (`aqu`) | Only water, nitrate, and soluble phosphorus are assigned. The routine reduces storage first, then calculates the withdrawal from the reduced state, so the POD receives less than the amount removed for a positive withdrawal fraction and receives zero at a fraction of one. |
| GWFlow source (`gwf`) | The branch has no withdrawal assignment. This branch of the POU allocator leaves the POD hydrograph at its zero defaults. |

[Unlimited, outside, and tower sources](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L35-L69), [Outside source preparation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L50-L91), [Channel, canal, and reservoir sources](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L71-L108), [Aquifer and GWFlow branches](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L110-L128), [Aquifer initialization and allocation](../aquifer/README.md#initialization-and-water-allocation)

## Configuration values used by the allocator

| Input | How the source uses it |
| --- | --- |
| POU `rate_max` | Rate in m³/s multiplied by 86,400 to set the daily maximum volume. It also caps the result of the POU demand table. |
| POD and POR `frac` | Dimensionless multiplier on a volume or hydrograph. |
| POD `const_min` for a channel | Compared directly to daily outflow volume in m³. The routine applies no rate conversion. |
| POD `const_min` for an aquifer | Compared directly to water-table depth in metres. |
| POD `const_min` for a reservoir, canal, or water tower | Fraction of principal reservoir volume or of current canal or tower volume. |
| POD `ann_max` | Initializes `wdraw_max`. The controller multiplies it by 86,400 before comparing it to the accumulated withdrawal volume. |

The reader stores the POD minimum-table name, and the withdrawal routine uses the constant minimum directly. The reader resolves the withdrawal-table name to an index, but the allocation controller never evaluates that index. A decision table evaluated elsewhere can change the maximum through `duty_reset`. The POR maximum table, constant, and annual limit are read but never applied in the return routine. The conveyance call is commented out, so conveyance settings have no effect on these return hydrographs through that path. [Input reads](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L91-L105), [Withdrawal-table lookup](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L160-L176), [Duty and fractions](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_start_day.f90#L149-L202), [Withdrawal gate](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_control.f90#L18-L26), [Minimum comparisons](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_withdraw.f90#L60-L123), [Water-table depth units](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L37-L40), [Decision-table reset action](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L182-L187), [Return dispatcher](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_return.f90#L16-L30)

## What the POR rows report

For ordinary POUs the return routine multiplies the current return hydrograph by each POR's fraction. Water-use POUs first replace that hydrograph with calculated effluent. Treatment POUs write treated hydrographs directly to the POR records, which the return routine passes through unchanged. The treatment loop reuses its working hydrograph after converting and capping it for the previous POR, so POR order can affect the computed flows and masses. The return routine can add water to a receiver's storage or queue it for a channel. Its HRU branch applies no water. Irrigation runs separately, with an availability check before the current HRU is selected. A reported POR volume therefore cannot establish how much irrigation reached an HRU. [Return and receiver dispatch](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_return.f90#L16-L66), [Water-use effluent](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_use.f90#L55-L68), [Treatment outflow](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_treatment.f90#L60-L85), [Irrigation delivery](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_deliv.f90#L30-L47)

Each allocation-controller call revisits POUs already marked finished. For a receiver whose branch adds the current POR hydrograph, later calls can apply it again before the next daily reset. The POR writer records the current hydrograph for that receiver, regardless of how many times it was applied. [Repeated delivery calls](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_control.f90#L56-L65), [Assignment and dispatch](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_return.f90#L16-L66), [Daily POR write](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L31-L49)

## Temperature in POD and POR rows

Scaling a hydrograph changes volume and masses and preserves its temperature. Combining hydrographs weights temperature by volume and returns zero when total volume is at most `1.e-6` m³. The ordinary return split therefore preserves the mixed temperature. Treatment and use take their temperature from the selected treatment or effluent record. The treatment cap applies to flow and masses. The average-annual writer divides volume and masses by the reporting-year count and leaves temperature as the weighted value already accumulated. [Hydrograph addition](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1334-L1360), [Scaling and division](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1437-L1484), [Treatment cap](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hydrograph_module.f90#L1258-L1279), [Average-annual writer](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L182-L195)

## Reporting periods

Monthly arrays accumulate daily records. The yearly writer adds the running monthly arrays on every writer call before checking for month end. This includes a final partial month and counts earlier daily values repeatedly. For example, if daily POU demand is 10 m3 on each of the last three days and those are the first three days of the month, the yearly demand increases by `10 + 20 + 30 = 60 m3`. Those daily demands total 30 m3. A monthly row requires calendar month end. [Daily and yearly accumulation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L13-L83)

In a Baltschieder test on this revision, the 2006 daily demand for `niwaerch_tunnel` summed to 5,676,480 m³. The monthly rows matched their respective daily sums. The yearly row reported 89,237,384 m³, within 8 m³ of the 89,237,376 m³ obtained by adding the running monthly totals. The test used an Intel ifx build without bounds checking. The bounds-checked build stopped before reporting on a separate channel-temperature array error. The fixture exercised channel-source POD rows and had no POR rows.

The year-end writer adds the yearly diagnostics to the average-annual accumulators before checking the yearly print flag. It clears the yearly records only when yearly output is enabled, and the per-POD delivery reset clears the monthly array instead of the yearly one. Turning off yearly output can therefore change the average-annual values in a multi-year run by retaining more prior-year values. The average-annual result divides those accumulated values by `time%yrs_prt` when positive. [Year-end transfer and reset](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L125-L180) · [Average-annual scaling](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/wallo_pou_output.f90#L182-L195)

[Back to the Water Allocation index](README.md).
