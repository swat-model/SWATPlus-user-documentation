# Water Allocation

This page describes SWAT+ main `6f515368525e7d84089ae0f9d33f4c9115de5679`. Use the file-family index below to find the actual printed record structure and file-specific warnings. Daily, monthly, yearly, and average-annual files use `_day`, `_mon`, `_yr`, and `_aa` suffixes and have TXT and optional CSV variants.

## How to produce these files

Configure [place_of_use.wro](../../introduction-1/water-allocation/place_of_use.wro.md) and [point_of_diver.wro](../../introduction-1/water-allocation/point_of_diver.wro.md) using the filenames on the water-allocation row of `file.cio`. These are the default filenames on this revision. [Default filenames](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/input_file_module.f90#L144-L148), [Filename reader](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/readcio_read.f90#L51), [Allocation input reader](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/water_allocation_read.f90#L36-L55)

In [print.prt](../../introduction-1/simulation-settings/print.prt/README.md), set the daily, monthly, yearly, or average-annual columns of `water_allo` to `y`. For example, `water_allo y n n n` enables the daily files. Set `csvout` to `y` to also request CSV. The schema pages record file-specific CSV limitations. The POU, treatment, and use writers run after skipped years. [Print row](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/basin_print_codes_read.f90#L319), [File creation](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/header_water_allocation.f90#L11), [Reporting gate and callers](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L440-L458)

| File family | Schema |
| --- | --- |
| `water_allo_*` | [Allocation transactions](allocation-transactions.md): interleaved POU, POD, and POR records |
| `wallo_use_*` | [Water-use diagnostics](water-use.md) |
| `wallo_treat_*` | [Water-treatment diagnostics](water-treatment.md) |
