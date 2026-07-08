# Metrics Catalog

Every metric used in this toolkit, defined so it is reproducible and defensible. Currency is AUD; time is in hours unless noted.

## Cost-side metrics

| Metric | Definition | Why it matters |
|--------|-----------|----------------|
| **Case volume** | Count of assisted-support cases in a period | Base driver of cost |
| **Cost per case** | Fully-loaded support cost ÷ case volume | Converts volume to dollars |
| **Deflection rate** | Self-service resolutions ÷ (self-service + assisted) | Cases you never pay to handle |
| **Escalation rate** | Cases escalated to engineering ÷ total cases | Escalations are the most expensive path |
| **Mean handle time (MHT)** | Total handle hours ÷ case volume | Labour cost per case |
| **Repeat-contact rate** | Cases reopened or re-contacted within 14 days | Signals unfixed root cause |
| **Engineering interrupt hours** | Eng hours spent on escalated support | Hidden cost drawn from roadmap |

## Revenue-side metrics

| Metric | Definition | Why it matters |
|--------|-----------|----------------|
| **Supported-account renewal rate** | Renewals ÷ eligible supported accounts | Support protects the base |
| **Time-to-value (TTV)** | Days from purchase to first productive use | Faster TTV lifts retention + expansion |
| **Expansion-enabled revenue** | Upsell/attach on accounts that hit a success milestone | Support creates room to grow |
| **CSAT / effort score** | Post-case satisfaction or customer-effort score | Leading indicator of churn |

## Deriving dollars

- **Deflection saving** = deflected cases × cost per case
- **Escalation saving** = (baseline − new escalation rate) × case volume × escalation cost premium
- **Handle-time saving** = MHT reduction × case volume × loaded hourly rate
- **Protected revenue** = renewal-rate lift × supported ARR
- **Enabled revenue** = expansion rate × accounts reaching success milestone × avg expansion value

All of the above are implemented as formulas in `roi-model/build_roi_model.py`.
