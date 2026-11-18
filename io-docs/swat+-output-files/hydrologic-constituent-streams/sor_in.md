---
description: "Incoming heading over a configured constituent scalar"
---

# sor_in

The dormant incoming header places `sor_in` at position 14. At that position the write list supplies configured constituent 2 when the configured count is at least two. The tail contains one scalar per configured constituent. The source writes the scalar directly from the constituent record, so its unit follows that record. [Header fields](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/constituent_mass_module.f90#L579) · [Scalar write list](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/hcsin_output.f90#L22)

The incoming writer call is commented out in this revision. See [incoming streams](README.md#incoming-streams) for widths and the yearly metals CSV header exception. [Disabled reporting call](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/command.f90#L613)
