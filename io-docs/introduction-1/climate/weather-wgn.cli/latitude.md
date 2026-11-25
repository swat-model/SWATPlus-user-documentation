# latitude

Station latitude in decimal degrees, from −90 to 90. SWAT+ converts it to radians as $\phi=\mathrm{latitude}/57.296$ and uses its sine and cosine for solar geometry.

See [cli_initwgn.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cli_initwgn.f90#L120-L145).
