# Point Sources and Inlets

Point source and inlet inputs supply external water, sediment, organic/mineral, and constituent loadings (or constant export coefficients) to SWAT+ spatial objects and water-allocation routines.

## Time-Series Recall Inputs

* [**recall.rec**](recall.rec/README.md) lists organic/mineral point-source and inlet records and their time-step types.
* [**recall\_db.rec**](recall_db.rec/README.md) maps named recall database records to constituent-group names for reservoir decision tables and water allocation.
* [**'om\_filename'.rec**](filename.rec/README.md) supplies time-series water, sediment, nutrient, oxygen, and temperature data for `type` 0–3 records in `recall.rec`.
* [**salt\_recall.rec**](salt_recall.rec/README.md) and [**'salt\_filename'.rec**](salt_filename.rec/README.md) define the salt-ion recall index and time-series format (reader not called in SWAT+ main `6f515368`).
* [**cs\_recall.rec**](cs_recall.rec/README.md) and [**'cst\_filename'.rec**](cst_filename.rec/README.md) define the general-constituent recall index and time-series format (reader not called in SWAT+ main `6f515368`).
* [**pest.com**](pest.com/README.md) and [**'pest\_filename'.rec**](pest_filename.rec.md) define the provisional pesticide recall index and time-series format.
* [**'path\_filename'.rec**](path_filename.rec.md) and [**'hmet\_filename'.rec**](hmet_filename.rec.md) document the absence of time-series recall readers for pathogens and heavy metals in SWAT+ main (`6f515368`).

## Export-Coefficient (Constant) Inputs

* [**exco.exc**](exco.exc/README.md) links named export-coefficient sets to organic/mineral and constituent export-coefficient records.
* [**exco\_om.exc**](exco_om.exc/README.md) supplies constant organic/mineral hydrograph values for standalone `exco` objects, routing-unit `exco` elements, `type = 4` recall entries, and water allocation.
* [**exco\_pest.exc**](exco_pest.exc/README.md), [**exco\_path.exc**](exco_path.exc/README.md), [**exco\_hmet.exc**](exco_hmet.exc/README.md), and [**exco\_salt.exc**](exco_salt.exc/README.md) supply constant constituent loadings for pesticides, pathogens, heavy metals, and salt ions when the corresponding counts in [`constituents.cs`](../constituents/constituents.cs.md) are positive.
