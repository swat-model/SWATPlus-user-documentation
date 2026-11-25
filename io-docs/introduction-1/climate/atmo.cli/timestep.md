---
description: Time step of the atmospheric deposition data
---

# timestep

**Code reference:** `atmodep_cont%timestep` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/climate_module.f90#L210)).

| Option | Description    |
| ------ | -------------- |
| mo     | Monthly        |
| yr     | Yearly         |
| aa     | Average annual |

The reader treats this field as a two-character code. The same code also selects the layout in [cs_atmo.cli](../cs_atmo.cli/README.md) and [salt_atmo.cli](../salt_atmo.cli/README.md). See [cli_read_atmodep.f90](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/cli_read_atmodep.f90#L36-L37).
