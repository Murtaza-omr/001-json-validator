#!/usr/bin/env python3
"""Validate a JSON document and report its top-level structure."""

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def reject_non_json_constant(value: str) -> None:
    raise ValueError(f"Non-standard JSON constant: {value}")


def describe(value: Any) -> dict[str, Any]:
    details: dict[str, Any] = {"top_level_type": type(value).__name__}
    if isinstance(value, dict):
        details["object_keys"] = list(value.keys())
        details["key_count"] = len(value)
    elif isinstance(value, list):
        details["item_count"] = len(value)
    return details


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a JSON file or JSON text from standard input."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="-",
        help="JSON file path; use - or omit the argument to read stdin",
    )
    parser.add_argument(
        "--output",
        help="Optional path for the JSON report (the input is never modified)",
    )
    args = parser.parse_args()

    try:
        if args.input == "-":
            text = sys.stdin.read()
            source = "stdin"
        else:
            path = Path(args.input)
            text = path.read_text(encoding="utf-8")
            source = str(path)
        parsed = json.loads(text, parse_constant=reject_non_json_constant)
        report = {"valid": True, "source": source, **describe(parsed)}
        status = 0
    except json.JSONDecodeError as error:
        report = {
            "valid": False,
            "source": args.input,
            "error": error.msg,
            "line": error.lineno,
            "column": error.colno,
        }
        status = 1
    except (OSError, UnicodeError, ValueError) as error:
        report = {"valid": False, "source": args.input, "error": str(error)}
        status = 1

    rendered = json.dumps(report, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return status


if __name__ == "__main__":
    raise SystemExit(main())
