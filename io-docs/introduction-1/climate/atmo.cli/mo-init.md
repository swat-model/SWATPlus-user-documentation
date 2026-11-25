# mo_init

First calendar month in a monthly series, from 1 to 12. Enter zero for annual layouts. When the simulation starts within a series that begins after January, the initialization can select the wrong row because its index omits the initial month offset.

See [cli_read_atmodep.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cli_read_atmodep.f90#L40-L66).
