# The Supportability Operating Model

Supportability is the discipline of making a product cheaper to support and easier to succeed with — *before* the customer ever contacts support. This document describes an operating model that a program manager can run against any commercial product.

## 1. The four pillars

| Pillar | Question it answers | Primary owner |
|--------|--------------------|---------------|
| **Diagnosability** | When something breaks, can we tell why — fast? | Engineering + Support |
| **Serviceability** | Can the issue be fixed without escalation? | Engineering |
| **Self-service** | Can the customer resolve it without us? | Content + Product |
| **Feedback loop** | Do support signals change the product? | Program Management |

## 2. The lifecycle

```
 Product signal  ->  Triage & classify  ->  Root-cause driver  ->  Fix path
      ^                                                              |
      |                                                              v
 Feedback loop  <-  Measure impact  <-  Deflect / document  <-  Ship remedy
```

The program manager owns the loop, not any single box. The job is to keep signal moving toward the cheapest durable fix: product change > serviceability tooling > KB/self-service > assisted support.

## 3. Value thesis

Every supportability investment is scored on **two ledgers**:

- **Cost ledger** — case volume, handle time, escalation rate, engineering interrupt hours.
- **Revenue ledger** — renewal/retention rate on supported accounts, time-to-value, expansion (attach/upsell) enabled by a customer actually succeeding.

A change that only moves cost is worth doing. A change that moves both is a priority.

## 4. Operating cadence

- **Weekly** — top support drivers reviewed; new drivers assigned an owner and a target fix path.
- **Monthly** — deflection and escalation trends; KB coverage gaps closed.
- **Per release** — launch-readiness gate (see `playbooks/launch-readiness.md`).
- **Quarterly** — ROI review against the model in `roi-model/`.

## 5. Anti-patterns this model avoids

- Treating support purely as a cost line to be squeezed.
- Optimising handle time while escalation and repeat-contact quietly rise.
- Shipping features with no diagnosability, then paying for it in cases forever.
- Measuring activity (articles written) instead of outcome (cases deflected).
