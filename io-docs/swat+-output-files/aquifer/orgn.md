---
description: "Aquifer carbon percentage under a mismatched nitrogen heading"
---

# orgn

**Code reference:** `aqu_d(iaq)%cbn` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L46); [initialization](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aqu_initial.f90#L176)).

The printed `orgn` position contains the carbon component, initialized from the aquifer's organic-carbon percentage. It does not contain organic nitrogen.

**Unit:** percent, from the carbon declaration and initialization. The printed kg/ha N label is wrong for this value.

The `cbn_init` calibration entry changes the parameter record after the live carbon value has already been copied. The reported carbon retains the initialized value. [Calibration and reported values](README.md#calibration-and-reported-values)

The period operators copy carbon without summing it or dividing by days/years. The basin multiply operator also leaves it unchanged; addition then replaces the left carbon value with the right carbon value. Consequently basin output takes the last aquifer's carbon value, not an area-weighted mean, even if that aquifer has zero area weight ([operators](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/aquifer_module.f90#L175)).

[Back to the output table](README.md).
