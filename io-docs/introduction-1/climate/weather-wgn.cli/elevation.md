# elevation

Station elevation in metres. For generated precipitation the lapse term is $L_p(z_o-z_s)/1000$. For generated temperature it is $L_t(z_s-z_o)/1000$. Here $L_p$ and $L_t$ are the basin lapse rates, and $z_o$ and $z_s$ are the object and station elevations.

See [cli_lapse.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cli_lapse.f90#L19-L34).
