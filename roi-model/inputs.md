# ROI Model — Inputs & Assumptions

Every figure in the model is derived from the assumptions below. Change them here (or in `build_roi_model.py`) and every downstream number updates. All currency AUD.

## Operational baseline

| Input | Value | Note |
|-------|-------|------|
| Annual case volume | 10,000 | Assisted-support cases/year |
| Cost per case | 85 | Fully loaded |
| Escalation rate (baseline) | 20% | Cases reaching engineering |
| Escalation cost premium | 160 | Extra cost of an escalated vs. normal case |
| Mean handle time (baseline) | 55 min | Per case |
| Loaded hourly rate | 75 | Support labour |

## Revenue baseline

| Input | Value | Note |
|-------|-------|------|
| Supported ARR | 28,000,000 | Annual recurring revenue on supported accounts |
| Renewal rate (baseline) | 89% | On supported accounts |
| Accounts reaching success milestone | 600 | Per year |
| Avg expansion value | 5,000 | Upsell/attach per expanding account |
| Expansion rate | 6% | Of milestone accounts that expand |

## Improvement levers (targets)

| Lever | Target | Applies to |
|-------|--------|-----------|
| Deflection | 18% of case volume | Cost |
| Escalation reduction | −30% relative | Cost |
| Handle-time reduction | −15% relative | Cost |
| Renewal lift | +1.5 pts | Revenue |
| Expansion enablement | +2 pts expansion rate | Revenue |

> These are deliberately conservative, defensible mid-market assumptions. The point of the model is the *structure*; plug in your own sanitised numbers.
