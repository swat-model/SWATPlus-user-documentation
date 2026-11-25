---
description: "The list of pesticides, pathogens, heavy metals, salt ions and other constituents to simulate."
---

# Constituents

[constituents.cs](constituents.cs.md) sets which constituents a simulation carries: pesticides, pathogens, heavy metals, salt ions and other constituents. It gives a count and a list of names for each group.

The counts and the order of the names matter to many other input files. Initial values, export coefficients, delivery ratios and point-source loads list one value per constituent in the same order. A count of 0 turns the group off.
