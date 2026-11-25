---
description: "Retardation factor"
---

# gwsol_sorb

**Code reference:** `gwsol_sorb(s)` ([declaration](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_module.f90#L512), [read](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_read.f90#L1657)).

Retardation factor $R$ of the solute: each transport step's mass change is divided by it ([`gwflow_solute.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_solute.f90#L100-L104)):

$$\Delta m = (m_{\text{adv}} + m_{\text{disp}} + m_{\text{rct}} + m_{\text{ss}}) \, \frac{\Delta t_{s}}{R}$$

where:
- $\Delta m$ is the net solute mass change in the cell over the transport sub-step (g),
- $m_{\text{adv}}$ is the advective mass flux (`g/day`),
- $m_{\text{disp}}$ is the dispersive mass flux (`g/day`),
- $m_{\text{rct}}$ is the reaction mass rate (`g/day`),
- $m_{\text{ss}}$ is the source/sink mass rate (`g/day`),
- $\Delta t_{s}$ is the transport sub-step length (`days`), and
- $R$ is `gwsol_sorb` (dimensionless).

The mass not added is reported as sorbed ([`gwflow_solute.f90`](https://github.com/swat-model/swatplus/blob/6f515368525e7d84089ae0f9d33f4c9115de5679/src/gwflow_solute.f90#L107-L111)). Enter 1 for no sorption; values above 1 slow the solute. 0 makes the division fail. Although the name suggests a sorption coefficient, it is used as a retardation factor; this is listed in `EDITOR_RENAME_CANDIDATES.md`.
