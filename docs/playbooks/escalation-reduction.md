# Playbook: Escalation Reduction

Escalations to engineering are the most expensive support path and the biggest drain on roadmap time. This playbook drives the rate down.

## Diagnose
1. Pull escalated cases for the period; tag by root-cause driver.
2. Rank drivers by (escalation count × engineering hours per escalation).
3. Separate **avoidable** (missing tool, doc, or permission) from **genuine** (real defect) escalations.

## Act
- **Avoidable** → build the serviceability tool or KB article; push the fix to first-line.
- **Genuine defect** → file with product; track until the fix ships.
- **Knowledge gap** → targeted enablement for the support tier that escalated.

## Measure
- Escalation rate (target: −30% on the top three drivers per quarter).
- Engineering interrupt hours recovered.

## Value link
Feeds the **escalation saving** and **engineering interrupt** figures in `roi-model/`. Recovered engineering hours are re-invested in roadmap — a revenue-side benefit, not just a cost cut.
