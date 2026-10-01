#!/usr/bin/env python3
"""Deterministic PCP-01 Run A sample draw.

The algorithm implements the frozen protocol in DETERMINISTIC-SAMPLING-PROTOCOL.md.
"""

import hashlib
import json

SEED = "PCP01-FV01"

CLASSES = {
    "FR-SET": [
        "CPS-ADA","CPS-ALGO","CPS-APT","CPS-ARB","CPS-AVAX",
        "CPS-BNB","CPS-HBAR","CPS-OP","CPS-PLUME","CPS-POL",
        "CPS-SOL","CPS-SUI","CPS-TRX","CPS-XLM","CPS-ZK",
    ],
    "FR-MID": ["CPS-LINK","CPS-QNT"],
    "FR-ISS": ["CPS-ONDO","CPS-RSR"],
    "FR-MKT": ["CPS-HYPE","CPS-INJ","CPS-SYRUP"],
}

ALLOCATION = {
    "FR-SET": 5,
    "FR-MID": 2,
    "FR-ISS": 2,
    "FR-MKT": 3,
}

def digest(class_code: str, asset_id: str) -> str:
    raw = f"{SEED}|{class_code}|{asset_id}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

def main() -> None:
    output = {
        "seed": SEED,
        "algorithm": "sha256-ascending",
        "allocation": ALLOCATION,
        "classes": {},
        "selected": [],
    }

    for class_code, assets in CLASSES.items():
        ranked = sorted(
            (
                {
                    "asset_id": asset_id,
                    "sha256": digest(class_code, asset_id),
                }
                for asset_id in assets
            ),
            key=lambda x: x["sha256"],
        )

        n = ALLOCATION[class_code]
        for index, row in enumerate(ranked, start=1):
            row["class_rank"] = index
            row["selected"] = index <= n

        output["classes"][class_code] = ranked
        output["selected"].extend(
            row["asset_id"] for row in ranked if row["selected"]
        )

    print(json.dumps(output, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
