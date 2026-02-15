#!/usr/bin/env python3
"""Validate tracking file for pre-commit hook."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from tracking_manager.utils import validate_tracking_file


def main():
    """Run validation and exit with appropriate code."""
    print("Validating tracking file...")

    is_valid, error = validate_tracking_file()

    if is_valid:
        print("✓ Tracking file is valid")
        return 0
    else:
        print(f"✗ Validation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
