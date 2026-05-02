#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Heuristic:
    name: str
    pattern: re.Pattern[str]


HEURISTICS = [
    Heuristic("routing", re.compile(r"lead|support|android-(architecture|compose|gradle-build|testing|performance|security|code-review|debugging|release-engineering)", re.I)),
    Heuristic("constraints", re.compile(r"non-negotiable|boundary|no cyclic|no secrets|ui layer", re.I)),
    Heuristic("authority", re.compile(r"override|authority|conflict|precedence", re.I)),
    Heuristic("evidence", re.compile(r"metric|gate|baseline|measure|pass|at-risk|fail", re.I)),
    Heuristic("confidence", re.compile(r"confidence|high|medium|low|assumption", re.I)),
    Heuristic("actionability", re.compile(r"1\.|2\.|3\.|next step|phased|plan", re.I)),
    Heuristic("integration", re.compile(r"integrated|single plan|coherent|synthesis", re.I)),
    Heuristic("uncertainty", re.compile(r"missing data|unknown|need evidence|minimum data|measurement-first", re.I)),
]


def score_text(text: str) -> dict[str, int]:
    scores: dict[str, int] = {}
    for h in HEURISTICS:
        matches = len(h.pattern.findall(text))
        if matches == 0:
            scores[h.name] = 0
        elif matches == 1:
            scores[h.name] = 1
        else:
            scores[h.name] = 2
    return scores


def main() -> None:
    parser = argparse.ArgumentParser(description="Heuristic scorer for Android skill regression responses")
    parser.add_argument("--responses", default="responses", help="Directory containing Pxx.md response files")
    parser.add_argument("--output", default="regression-report.json", help="Output JSON report path")
    args = parser.parse_args()

    responses_dir = Path(args.responses)
    files = sorted(responses_dir.glob("P*.md"))
    if not files:
        print("No response files found. Add files like responses/P01.md and rerun.")
        return

    report: dict[str, Any] = {}
    total_all = 0
    for file in files:
        text = file.read_text(encoding="utf-8", errors="ignore")
        scores = score_text(text)
        total = sum(scores.values())
        total_all += total
        report[file.stem] = {**scores, "total": total}

    report["summary"] = {
        "responses": len(files),
        "average_total": round(total_all / len(files), 2),
        "max_total": 16,
    }

    Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Scored {len(files)} responses. Average total: {report['summary']['average_total']} / 16")
    print(f"Report written to: {args.output}")


if __name__ == "__main__":
    main()
