---
description: "The identifier of the weather station associated with the annual atmospheric salt deposition record"
---

# station_name

**Code reference:** `station_name` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cli_read_atmodep_salt.f90#L15)).

Station label read as text up to 15 characters at the start of every station block. SWAT+ assigns records by station order in [atmo.cli](../atmo.cli/README.md).

*(Note: In SWAT+ main (6f515368), this column is parsed into memory but is not used in simulation calculations).* See [cli_read_atmodep_salt.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cli_read_atmodep_salt.f90#L46-L93).
