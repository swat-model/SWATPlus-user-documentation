---
description: Provisional pesticide time-series recall file format
---

# 'pest\_filename'.rec

Individual pesticide time-series filenames listed in [`pest.com`](pest.com/README.md) are opened on unit `108` by [`recall_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L234-L273). The reader expects a title line (`#L235`), `nbyr` (`#L237`), a header line (`#L239`), and data rows containing `iyr`, `istep`, and hydrograph values (`#L265`).

{% hint style="warning" %}
In SWAT+ main (`6f515368`), this reader is provisional/defective: [`recall_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/recall_read.f90#L265) reads into `recall(i)%hd(istep,iyrs)` (an organic/mineral `hyd_output` record) rather than populating `rec_pest(i)%hd_pest`, and `rec_pest%hd_pest` is never used in simulation calculations. For constant pesticide inputs, use [`exco_pest.exc`](exco_pest.exc/README.md).
{% endhint %}
