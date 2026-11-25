# const2

**Code reference:** `dtbl_lum(i)%act(iac)%const2` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/conditional_module.f90#L24)).

Secondary numeric action parameter. The reader raises values below 1 to 1. Some actions use the integer part as their management-action counter limit. For example, `cn_update` compares its current action count to `INT(const2)`. [`dtbl_lum_read.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/dtbl_lum_read.f90#L93-L98) · [`actions.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/actions.f90#L1246-L1264)
