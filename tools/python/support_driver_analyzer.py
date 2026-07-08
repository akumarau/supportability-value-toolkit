#!/usr/bin/env python3
"""Support Driver Analyzer.

Reads a case export and ranks the support drivers costing the most,
flags which are escalation-heavy, and highlights knowledge-base gaps.

Cost-saving lever: point remediation at the drivers that actually cost money,
not the ones that merely feel loud.

Usage:
    python support_driver_analyzer.py [path/to/cases.csv]

Only the standard library is required.
"""
from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path

LOADED_HOURLY_RATE_AUD = 75.0  # fully-loaded support cost per hour


def load(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def analyze(rows: list[dict]) -> list[dict]:
    agg: dict[str, dict] = defaultdict(
        lambda: {"count": 0, "minutes": 0, "escalated": 0, "kb": True}
    )
    for r in rows:
        d = agg[r["driver"]]
        d["count"] += 1
        d["minutes"] += int(r["handle_minutes"])
        d["escalated"] += 1 if r["escalated"].strip().lower() == "yes" else 0
        if r["has_kb_article"].strip().lower() == "no":
            d["kb"] = False

    result = []
    for driver, d in agg.items():
        hours = d["minutes"] / 60
        result.append(
            {
                "driver": driver,
                "cases": d["count"],
                "labour_hours": round(hours, 1),
                "labour_cost_aud": round(hours * LOADED_HOURLY_RATE_AUD, 2),
                "escalation_rate": round(d["escalated"] / d["count"], 2),
                "kb_gap": not d["kb"],
            }
        )
    return sorted(result, key=lambda x: x["labour_cost_aud"], reverse=True)


def main() -> None:
    default = Path(__file__).parent / "sample_data" / "cases.csv"
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else default
    rows = load(path)
    ranked = analyze(rows)

    print(f"\nAnalysed {len(rows)} cases from {path.name}\n")
    header = f"{'Driver':<26}{'Cases':>6}{'Hours':>8}{'Cost AUD':>11}{'Esc%':>7}  Flag"
    print(header)
    print("-" * len(header))
    for r in ranked:
        flag = []
        if r["escalation_rate"] >= 0.5:
            flag.append("HIGH-ESCALATION")
        if r["kb_gap"]:
            flag.append("KB-GAP")
        print(
            f"{r['driver']:<26}{r['cases']:>6}{r['labour_hours']:>8}"
            f"{r['labour_cost_aud']:>11,.0f}{int(r['escalation_rate']*100):>6}%  "
            + ", ".join(flag)
        )

    total = sum(r["labour_cost_aud"] for r in ranked)
    print(f"\nTotal modeled labour cost: AUD {total:,.0f}")
    gaps = [r["driver"] for r in ranked if r["kb_gap"]]
    if gaps:
        print("Close these KB gaps first (cost-weighted): " + ", ".join(gaps))
    print()


if __name__ == "__main__":
    main()
