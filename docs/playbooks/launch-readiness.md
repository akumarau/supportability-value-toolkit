# Playbook: Supportability Launch Readiness

A gate run before a product or feature ships, to stop shipping cost into the support queue.

## When
At the release-candidate milestone, and again 30 days post-launch.

## The gate (must pass all)

1. **Diagnosability** — every known failure mode emits an identifiable signal (log, event, error code) documented for support.
2. **Top-5 KB coverage** — the five most likely support drivers each have a published article before GA.
3. **Serviceability path** — for each top driver, there is a customer-executable or first-line fix that does not require engineering.
4. **Escalation runbook** — a defined path and owner for issues that do escalate.
5. **Telemetry baseline** — case-driver tagging is live so week-1 signal is measurable.

## Outputs
- Go / no-go recommendation with the gaps listed.
- A 30-day watch list of predicted drivers.

## Value link
Every gap caught here is cases *not* opened later. Quantify with the deflection and escalation levers in `roi-model/`.
